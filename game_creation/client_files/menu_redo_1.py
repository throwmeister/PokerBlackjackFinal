from PyQt5 import QtCore, QtGui, QtWidgets
from create_game_screen import CreateGame
from login_screen import Login
from join_game_screen import JoinGame
from client_data import ClientInfo
from game_creation.shared_directory import data_format as form


class Menu(object):
    def setupUi(self, Form):
        Form.setObjectName("Poker and Blackjack")
        Form.closeEvent = self.closed_event
        Form.resize(1054, 860)
        Form.setStyleSheet("QWidget{\n"
"    background-color: rgb(15, 102, 72);\n"
"    \n"
"}\n"
"\n"
"QLabel{\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"    font-family: MS Shell Dlg 2;\n"
"    font-size: 30px;\n"
"                \n"
"    color: rgb(0, 85, 0);\n"
"                \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 132, 93, 255), stop:1 rgba(97, 192, 164, 255));\n"
"                border-radius: 3px;\n"
"                border: 2px groove rgb(0, 0, 0)\n"
"            }\n"
"            QPushButton:hover{\n"
"            background-color: #e3c086;\n"
"            outline: none\n"
"            }"
"QHeaderView::section {\n"
"    background-color: #ebc17a;\n"
"    border-style: none;\n"
"    font-size: 14pt;\n"
"    border-right: 1px solid #d9a143;\n"
"border-bottom: 1px solid #d9a143;\n"
"border-left: 1px solid #d9a143;\n"
"padding: 6px\n"
"}\n"
"QTableCornerButton::section{\n"
"background-color: #ebc17a;\n"
"    padding: 4px;\n"
"    border: 1px solid #ebc17a;\n"
"    font-size: 14pt;\n"
"}\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.main_stack = QtWidgets.QStackedWidget(Form)
        self.main_stack.setObjectName("main_stack")
        self.main_menu = QtWidgets.QWidget()
        self.main_menu.setObjectName("main_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.play_button = QtWidgets.QPushButton(self.main_menu)
        self.play_button.setMinimumSize(QtCore.QSize(450, 100))
        self.play_button.setMaximumSize(QtCore.QSize(450, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        self.play_button.setFont(font)
        self.play_button.setObjectName("play_button")
        self.verticalLayout_2.addWidget(self.play_button, 0, QtCore.Qt.AlignHCenter)
        self.settings_button = QtWidgets.QPushButton(self.main_menu)
        self.settings_button.setMinimumSize(QtCore.QSize(450, 100))
        self.settings_button.setMaximumSize(QtCore.QSize(450, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        self.settings_button.setFont(font)
        self.settings_button.setObjectName("settings_button")
        self.verticalLayout_2.addWidget(self.settings_button, 0, QtCore.Qt.AlignHCenter)
        self.exit_button = QtWidgets.QPushButton(self.main_menu)
        self.exit_button.setMinimumSize(QtCore.QSize(450, 100))
        self.exit_button.setMaximumSize(QtCore.QSize(450, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout_2.addWidget(self.exit_button, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.main_stack.addWidget(self.main_menu)
        self.lobby = QtWidgets.QWidget()
        self.lobby.setObjectName("lobby")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.lobby)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.games_list = QtWidgets.QTreeWidget(self.lobby)
        self.games_list.setStyleSheet("background-color: #ebc17a;\n"
                                      "                border: 6px groove #d9a143;\n"
                                      "font-size: 22px;\n"
                                      "QHeaderView::section\n"
                                      "{\n"
                                      "    border-top: 1px solid #fffff8;\n"
                                      "}\n"
                                      "\n"
                                      "QHeaderView::vertical\n"
                                      "{\n"
                                      "    border-left: 1px solid #fffff8;\n"
                                      "}")
        self.games_list.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.games_list)
        self.verticalLayout_5.addWidget(self.games_list)
        self.join_game_button = QtWidgets.QPushButton(self.lobby)
        self.join_game_button.setMinimumSize(QtCore.QSize(0, 50))
        self.join_game_button.setObjectName("pushButton_5")
        self.verticalLayout_5.addWidget(self.join_game_button)
        self.create_game_button = QtWidgets.QPushButton(self.lobby)
        self.create_game_button.setMinimumSize(QtCore.QSize(0, 50))
        self.create_game_button.setObjectName("pushButton_4")
        self.verticalLayout_5.addWidget(self.create_game_button)
        self.back_button_game_list = QtWidgets.QPushButton(self.lobby)
        self.back_button_game_list.setMinimumSize(QtCore.QSize(0, 50))
        self.back_button_game_list.setObjectName("pushButton_3")
        self.verticalLayout_5.addWidget(self.back_button_game_list)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.main_stack.addWidget(self.lobby)
        self.game_player_list = QtWidgets.QWidget()
        self.player_list_screen = QtWidgets.QWidget()
        self.player_list_screen.setObjectName("p_or_b")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.player_list_screen)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.player_list = QtWidgets.QListWidget(self.player_list_screen)
        self.player_list.setStyleSheet("background-color: #ebc17a;\n"
                                       "                border: 6px groove #d9a143;\n"
                                       "font-size: 22px;")
        self.player_list.setObjectName("player_list")
        self.verticalLayout_6.addWidget(self.player_list)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_game_button = QtWidgets.QPushButton(self.player_list_screen)
        self.start_game_button.setEnabled(False)
        self.start_game_button.setObjectName("start_game_button")
        self.horizontalLayout.addWidget(self.start_game_button)
        self.playing_checkbox = QtWidgets.QCheckBox(self.player_list_screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playing_checkbox.sizePolicy().hasHeightForWidth())
        self.playing_checkbox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.playing_checkbox.setFont(font)
        self.playing_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.playing_checkbox.setStyleSheet("font-family: MS Shell Dlg 2;\n"
                                            "    font-size: 30px;\n"
                                            "                \n"
                                            "    color: rgb(0, 85, 0);\n"
                                            "                \n"
                                            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 132, 93, 255), stop:1 rgba(97, 192, 164, 255));\n"
                                            "                border-radius: 3px;\n"
                                            "                border: 2px groove rgb(0, 0, 0)")
        self.playing_checkbox.setObjectName("playing_checkbox")
        self.horizontalLayout.addWidget(self.playing_checkbox)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.leave_game_button = QtWidgets.QPushButton(self.player_list_screen)
        self.leave_game_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.leave_game_button.setObjectName("leave_game_button")
        self.verticalLayout_6.addWidget(self.leave_game_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.main_stack.addWidget(self.player_list_screen)
        self.verticalLayout.addWidget(self.main_stack)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)


        self.retranslateUi(Form)
        self.main_stack.setCurrentIndex(0)
        self.exit_button.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.play_button.clicked.connect(self.open_login_window)
        ClientInfo.main_gui = self
        self.settings_button.clicked.connect(self.tester_button)
        self.games_list.itemClicked.connect(self.game_clicked)
        self.join_game_button.clicked.connect(self.join_game_pressed)
        self.create_game_button.clicked.connect(self.create_game_pressed)
        self.back_button_game_list.clicked.connect(lambda _: self.main_stack.setCurrentIndex(0))
        self.playing_checkbox.clicked.connect(self.playing_checkbox_clicked)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Poker and Blackjack", "Poker and Blackjack"))
        self.title.setText(_translate("Poker and Blackjack", "🅿🅾🅺🅴🆁 🅰🅽🅳 🅱🅻🅰🅲🅺🅹🅰🅲🅺"))
        self.play_button.setText(_translate("Poker and Blackjack", "Play"))
        self.settings_button.setText(_translate("Poker and Blackjack", "Settings"))
        self.exit_button.setText(_translate("Poker and Blackjack", "Exit"))
        self.games_list.headerItem().setText(0, _translate("Form", "Name"))
        self.games_list.headerItem().setText(1, _translate("Form", "Type"))
        self.games_list.headerItem().setText(2, _translate("Form", "Owner"))
        self.games_list.headerItem().setText(3, _translate("Form", "Players"))
        self.games_list.headerItem().setText(4, _translate("Form", "In progress"))
        __sortingEnabled = self.games_list.isSortingEnabled()
        self.games_list.setSortingEnabled(False)
        self.games_list.setSortingEnabled(__sortingEnabled)
        self.join_game_button.setText(_translate("Form", "Join game"))
        self.create_game_button.setText(_translate("Form", "Create game"))
        self.back_button_game_list.setText(_translate("Form", "Back"))
        self.start_game_button.setText(_translate("Form", "Start"))
        self.playing_checkbox.setText(_translate("Form", "Playing"))
        self.leave_game_button.setText(_translate("Form", "Leave"))

    def tester_button(self):
        self.main_stack.setCurrentIndex(2)
    def game_clicked(self, items):
        '''
        print(self.games_list.topLevelItem(0).data(5, 0))
        print(self.games_list.selectedItems()[0])
        print(items.treeWidget().currentIndex().row())'''
        self.selected_game = items.data(5, 0)
        print(self.selected_game)

    def change_screens(self, num):
        self.main_stack.setCurrentIndex(int(num))

    def open_login_window(self):
        if ClientInfo.valid_session:
            self.change_screens(form.MenuScreenEnums.GAME_LIST)
        else:
            self.lwindow = QtWidgets.QDialog()
            self.lui = Login()
            self.lui.setupUi(self.lwindow)
            self.lui.username_line.setText('Alex')
            self.lui.password_line.setText('alex')
            self.lwindow.show()
            print('This ran!')

    def set_game_list(self, data):
        self.games_list.clear()
        ClientInfo.logger.info(data)
        try:
            for game_id, game_vars in data.items():
                ClientInfo.logger.info(f'Game from game_id: {game_id} and values: {game_vars}')
                d = form.UpdateGameListVariables(game_vars)
                items = [d.game_name, d.game_type, d.owner, str(d.num_players), str(d.in_progress), game_id]
                QtWidgets.QTreeWidgetItem(self.games_list, items)
        except AttributeError:
            pass

    def set_player_list(self, data):
        self.player_list.clear()
        ClientInfo.logger.info('Setting game player list')
        ClientInfo.logger.info(data)
        for player in data:
            d = form.UpdatePlayerList(player)
            ready = '✅'
            if d.ready == form.PlayerReadyEnum.FALSE:
                ready = '❌'
            self.player_list.addItem(f'{d.player_name} {ready}')

    def join_game_pressed(self):
        if self.selected_game:
            self.jwindow = QtWidgets.QDialog()
            self.jui = JoinGame()
            self.jui.setupUi(self.jwindow)
            self.jui.game_id = self.selected_game
            self.jui.password_edit.setText('ILOVEPOKER')
            self.jwindow.show()
        else:
            print('please select a game')

    def create_game_pressed(self):
        self.create_window = QtWidgets.QDialog()
        self.create_ui = CreateGame()
        self.create_ui.setupUi(self.create_window)
        self.create_window.show()

    def set_owner_command(self):
        self.start_game_button.setEnabled(True)

    def playing_checkbox_clicked(self):
        self.playing_checkbox.setEnabled(False)
        if self.playing_checkbox.isChecked():
            ClientInfo.tcpHandler.ready_game(game_id=ClientInfo.game_joined, ready_type=form.ReadyTypeEnum.READY)
        else:
            ClientInfo.tcpHandler.ready_game(game_id=ClientInfo.game_joined, ready_type=form.ReadyTypeEnum.UNREADY)

    def ready_success(self):
        ClientInfo.logger.info('Ready: success')
        self.playing_checkbox.setEnabled(True)

    def ready_error(self, reverse_action: bool):
        self.playing_checkbox.setEnabled(True)
        self.playing_checkbox.setChecked(reverse_action)
        ClientInfo.logger.info('Ready failed')

    def closed_event(self, event):
        ClientInfo.tcpHandler.lose_connection()
        raise RuntimeError




if __name__ == '__main__':
    import sys
    import qt5reactor
    app = QtWidgets.QApplication(sys.argv)

    qt5reactor.install()

    main = QtWidgets.QWidget()
    ui = Menu()
    ui.setupUi(main)

    # create_login = Login()
    # create_game = CreateGame()
    import skel_client as tcp_client

    main.show()


    # Start TCP Client
    tcp_client.ClientCreator.start_connection()

    sys.exit(app.exec_())
