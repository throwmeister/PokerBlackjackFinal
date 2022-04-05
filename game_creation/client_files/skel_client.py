import builtins, logging, json, pika
'''
from twisted.internet.defer import Deferred
from twisted.internet.threads import deferToThread
'''
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet.task import LoopingCall
from game_creation.shared_directory import data_format as form
from client_data import ClientInfo

decode_type = form.decode_format()


# noinspection PyArgumentList
class MainClient(Protocol):
    format = decode_type

    def __init__(self):
        self.loop: LoopingCall = LoopingCall(self.send_keep_alive)
        self.lobby_mq: MessageQueue = None

    def connectionMade(self):
        # Do we want the client to be auto logged in?
        # Do we want to save the login details if they have logged in before?
        pass

    def connectionLost(self, reason):
        print('disconnecting')

    def send_login(self, username, password):
        x = form.ClientLoginRequest()
        x.username = username
        x.password = password
        x.version = form.version_number()
        req = form.ClientRequestHeader()
        req.request_type = form.ClientRequestTypeEnum.LOGIN_REQUEST
        req.data = x.__dict__
        s = json.dumps(req.__dict__)
        ClientInfo.logger.info('Send login')
        self.transport.write(f'{s}\r'.encode(self.format))

    def send_logout(self):
        ClientInfo.logger.info('Send logout')
        self.lobby_mq.stop_consumption()
        self.format_send_data(form.ClientRequestTypeEnum.LOGOUT_REQUEST)

    def create_game(self, name, game_type, password=''):
        user_data = form.ClientCreateGame()
        user_data.game_type = game_type
        user_data.game_name = name
        user_data.password = password
        self.format_send_data(form.ClientRequestTypeEnum.CREATE_GAME, user_data)

    def join_game(self, game_id, password=''):
        user_data = form.ClientJoinGame()
        user_data.game_id = game_id
        user_data.password = password
        self.format_send_data(form.ClientRequestTypeEnum.JOIN_GAME, user_data)

    def format_send_data(self, request_type: form.ClientRequestTypeEnum, data=None):
        req = form.ClientRequestHeader()
        req.request_type = request_type
        req.session_id = ClientInfo.session_id
        if data:
            try:
                req.data = data.__dict__
            except builtins.AttributeError:
                req.data = data
        else:
            req.data = ''
        s = json.dumps(req.__dict__)
        ClientInfo.logger.info(f'{request_type.name}')
        self.transport.write(f'{s}\r'.encode(self.format))

    def dataReceived(self, data: bytes):
        listed_data = self.decode_data(data)
        for json_data in listed_data:
            ClientInfo.logger.debug(f'{json_data}')
            message = form.ServerRequestHeader(json_data)
            match message.request_type:
                case form.ServerRequestTypeEnum.LOGIN_RESPONSE:
                    ClientInfo.logger.info('Handling login')
                    self.handle_login_response(message.data)
                case form.ServerRequestTypeEnum.INVALID_SESSION:
                    # Stop keep alive function
                    ClientInfo.logger.error('Invalid session. Log in')
                    self.loop.stop()
                case form.ServerRequestTypeEnum.CREATE_GAME_RESPONSE:
                    self.handle_create_game_response(message.data)
                case form.ServerRequestTypeEnum.JOIN_GAME_RESPONSE:
                    self.handle_join_game_response(message.data)
                case form.ServerRequestTypeEnum.UPDATE_EVERY_GAME_LIST:
                    ClientInfo.main_gui.set_game_list(message.data)
                case _:
                    # Invalid command
                    pass

    def decode_data(self, data):
        sp_data = data.decode(self.format).split('\r')
        return [x for x in sp_data if x]

    def handle_login_response(self, data):
        response_data = form.ServerLoginResponse(data)
        ClientInfo.logger.info(response_data.message)
        if response_data.response_code == form.LoginResponseEnum.SUCCESS:
            ClientInfo.set_login_values(response_data.username, response_data.keep_alive,
                                        response_data.session_id)
            ClientInfo.valid_session = True
            self.loop.start(response_data.keep_alive)
            # reactor.callFromThread(self.start_keep_alive, response_data.keep_alive)
            ClientInfo.logger.info('Running message queue')
            self.lobby_mq = MessageQueue(queue_name=f'gameserver.{response_data.username}.{response_data.session_id}',
                                         exchange=form.exchange_name())
            self.lobby_mq.set_consume(self.dataReceived)
            reactor.callInThread(self.lobby_mq.start_consumption)
            ClientInfo.logger.info('Message queue has successfully been added to the thread')
            ClientInfo.login_gui.login_response_success()
            ClientInfo.main_gui.change_to_games_screen()
            # self.create_game()
        elif response_data.response_code == form.LoginResponseEnum.ERROR:
            # User must re-input
            # self.send_login()
            ClientInfo.login_gui.login_response_failed()
            pass
        else:
            raise RuntimeError

    def send_keep_alive(self):
        self.format_send_data(form.ClientRequestTypeEnum.KEEP_ALIVE, ClientInfo.username)

    def handle_create_game_response(self, data):
        response_data = form.ServerCreateGame(data)
        if response_data.response_code == form.CreateGameEnum.SUCCESS:
            ClientInfo.logger.info(f'Game creation: {form.CreateGameEnum.SUCCESS.name}')
            ClientInfo.game_joined = response_data.game_id
            ClientInfo.game_owner = True
        elif response_data.response_code == form.CreateGameEnum.NAME_ERROR:
            # Popup
            ClientInfo.logger.info(f'Game creation: {form.CreateGameEnum.NAME_ERROR.name}')
        elif response_data.response_code == form.CreateGameEnum.ALREADY_CREATED_GAME:
            ClientInfo.logger.info(f'Game creation: {form.CreateGameEnum.ALREADY_CREATED_GAME.name}')
        else:
            raise RuntimeError

    def handle_join_game_response(self, data):
        response_data = form.ServerJoinGame(data)
        log_join = lambda response: ClientInfo.logger.info(f'Game join: {response}')
        if response_data.response_code == form.JoinGameEnum.SUCCESS:
            log_join(form.JoinGameEnum.SUCCESS.name)
            ClientInfo.game_joined = response_data.game_id
        elif response_data.response_code == form.JoinGameEnum.WRONG_PASSWORD:
            log_join(form.JoinGameEnum.WRONG_PASSWORD.name)

    def lose_connection(self):
        self.transport.loseConnection()


class ClientCreator(ClientFactory):
    @staticmethod
    def start_connection():
        import colouredlogs
        '''
        logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                            datefmt='%d-%m-%Y:%H:%M:%S',
                            level=logging.INFO,

                            )
        '''
        ClientInfo.logger = logging.getLogger('Main')
        colouredlogs.format('[%(hostname)s] %(asctime)s %(message)s')

        colouredlogs.install(logger=ClientInfo.logger)
        endpoint = TCP4ClientEndpoint(reactor, 'localhost', 8007)
        endpoint.connect(ClientCreator())
        reactor.run()

    @staticmethod
    def stop_reactor():
        print('reactor stopped')
        reactor.stop()
        raise RuntimeError

    def buildProtocol(self, addr):
        ClientInfo.tcpHandler = MainClient()
        return ClientInfo.tcpHandler


class MessageQueue:
    def __init__(self, queue_name, exchange, routing_key=''):
        self.queue_name = queue_name
        self.exchange = exchange
        self.routing_key = routing_key
        my_url = form.message_url()

        self.connection = pika.BlockingConnection(pika.URLParameters(url=my_url))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue=queue_name, durable=False, exclusive=False, auto_delete=True)
        self.channel.queue_bind(queue=queue_name, exchange=exchange, routing_key=routing_key)

    def start_consumption(self):
        self.channel.start_consuming()

    def set_consume(self, func):
        self.channel.basic_consume(queue=self.queue_name, auto_ack=True, on_message_callback=mq_data_received)

    def stop_consumption(self):
        self.channel.stop_consuming()


def mq_data_received(ch, method, properties, body):
    json_data = body.decode()
    ClientInfo.logger.debug(f'{json_data}')
    message = form.ServerRequestHeader(json_data)
    match message.request_type:
        case form.ServerRequestTypeEnum.UPDATE_EVERY_GAME_LIST:
            pass

'''

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%d-%m-%Y:%H:%M:%S',
                        level=logging.INFO)

    logger = logging.getLogger('Main')
    endpoint = TCP4ClientEndpoint(reactor, 'localhost', 8007)
    endpoint.connect(ClientCreator())
    reactor.run()

'''