import shared_directory.data_format as form
import session
from uuid import uuid4


class Participant:
    def __init__(self, session_id):
        self.session_id = session_id
        session_object: session.Session = session.Session.sessions[session_id]
        self.username = session_object.player_name


class Game:
    Games = {}

    def __init__(self, name, game_type, password, owner_id):
        self.present = []
        self.players = []
        self.owner_id = owner_id
        self.lobby_name = name
        self.game_type = game_type
        self.password = password
        self.in_progress = False
        self.game_status = form.GameStatus.INVALID
        self.game_id = self.create_game_id()
        self.add_game()

    @staticmethod
    def create_game_id():
        return str(uuid4())

    def add_game(self):
        self.Games[self.game_id] = self

    @classmethod
    def game_exists(cls, session_id):
        if session_id in cls.Games:
            return True
        else:
            return False

    @classmethod
    def game_name_exists(cls, name, session_id):
        for game in cls.Games.values():
            game: Game
            if game.lobby_name == name:
                return True
        return False

    def add_participant(self, participant: Participant):
        self.present.append(participant)

    def remove_participant(self, participant: Participant):
        if participant in self.players:
            self.players.remove(participant)
        self.present.remove(participant)

    def remove_game(self):
        del self.Games[self.owner_id]


