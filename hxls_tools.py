# -*- coding:gbk -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import json,os,webbrowser
class Hxls_ui_group(object):
    def hxls_game_tool(self):
        self.hxls_page = QtWidgets.QWidget()
        self.hxls_page.setObjectName("hxls_page")
        self.game_pages.addWidget(self.hxls_page)
        with open("resource\hxls\hxls_index.json", 'r', encoding='utf-8') as d:
            self.hxls_index = json.load(d)
        # ��ǩ
        self.hxls_choose_Label = QtWidgets.QLabel(self.hxls_page)
        self.hxls_choose_Label.setGeometry(self.ui_zoom(20, 0, 81, 25))
        self.hxls_choose_Label.setObjectName("hxls_choose_Label")
        self.hxls_choose_Label.setText(self._translate("main_window", "ѡ ��"))
        self.hxls_set_Label = QtWidgets.QLabel(self.hxls_page)
        self.hxls_set_Label.setGeometry(self.ui_zoom(110, 0, 81, 25))
        self.hxls_set_Label.setObjectName("hxls_set_Label")
        self.hxls_set_Label.setText(self._translate("main_window", "�л�ҳ��"))
        # ����ҳ��
        self.hxls_filler = QtWidgets.QWidget(self.hxls_page)
        self.trans_list = self.hxls_index["����"]
        self.hxls_filler.setMinimumSize(168, len(self.trans_list) * 30)  #######���ù������ĳߴ�
        self.hxls_scroll = QtWidgets.QScrollArea(self.hxls_page)
        self.hxls_scroll.setWidget(self.hxls_filler)
        x, y, w, h = self.num_zoom([2, 28, 168, 280])
        self.hxls_scroll.move(x, y)
        self.hxls_scroll.resize(w, h)
        self.hxls_scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        for num in range(len(self.trans_list)):
            tname = self.trans_list[num]
            fnamep = self.hxls_index[tname]
            strc, strs, strp = "self.hxls_choose_%s" % (fnamep), "self.hxls_set_%s" % (fnamep), "self.hxls_%s_page" % (fnamep)
            exec(strc + "= QtWidgets.QCheckBox(self.hxls_filler)")
            exec(strs + "= QtWidgets.QPushButton(self.hxls_filler)")
            exec(strp + "= QtWidgets.QWidget()")
            fc, fs, fp = eval(strc), eval(strs), eval(strp)
            fc.setGeometry(self.ui_zoom(5, 5 + 30 * num, 110, 16))
            fc.setObjectName(strc)
            fc.setText(self._translate("main_window", tname))
            fs.setGeometry(self.ui_zoom(125, 3 + (30 * num), 20, 20))
            fs.setObjectName(strs)
            fs.setIcon(QtGui.QIcon(r"resource\main_window\ui\set.png"))
            fs.setFlat(True)
            fp.setObjectName(strp)
            self.set_pages.addWidget(fp)
        self.hxls_choose_create.setEnabled(False)
        self.hxls_choose_create.setChecked(True)
        self.hxls_choose_kill_game.setEnabled(False)
        self.hxls_choose_kill_game.setChecked(True)
        self.hxls_set_create.clicked.connect(lambda: self.change_set_page(10))
        self.hxls_set_fight.clicked.connect(lambda: self.change_set_page(11))
        self.hxls_set_dispatch.clicked.connect(lambda: self.change_set_page(12))
        self.hxls_set_review.clicked.connect(lambda: self.change_set_page(13))
        self.hxls_set_market.clicked.connect(lambda: self.change_set_page(14))
        self.hxls_set_recruit.clicked.connect(lambda: self.change_set_page(15))
        self.hxls_set_reward.clicked.connect(lambda: self.change_set_page(16))
        self.hxls_set_market_network.clicked.connect(lambda: self.change_set_page(17))
        self.hxls_set_random_gift.clicked.connect(lambda: self.change_set_page(18))
        self.hxls_set_kill_game.clicked.connect(lambda: self.change_set_page(19))

        self.hxls_start_program()
        self.hxls_fight_program()
        self.hxls_dispatch_program()
        self.hxls_review_program()
        self.hxls_market_program()
        self.hxls_recruit_program()
        self.hxls_reward_program()
        self.hxls_market_network_program()
        self.hxls_random_gift_program()
        self.hxls_kill_game_program()
        # ������ť
        self.hxls_help1.clicked.connect(lambda: self.send_hxls_help("ģ�����"))
        self.hxls_help2.clicked.connect(lambda: self.send_hxls_help("��ս"))
        self.hxls_help3.clicked.connect(lambda: self.send_hxls_help("���²ɹ�"))
        self.hxls_help4.clicked.connect(lambda: self.send_hxls_help("ս���ع�"))
        self.hxls_help5.clicked.connect(lambda: self.send_hxls_help("����"))
        self.hxls_help6.clicked.connect(lambda: self.send_hxls_help("���ѷ�ļ"))
        self.hxls_help7.clicked.connect(lambda: self.send_hxls_help("���չ���"))
        self.hxls_help8.clicked.connect(lambda: self.send_hxls_help("��������"))
        self.hxls_help9.clicked.connect(lambda: self.send_hxls_help("�����"))
        self.hxls_help10.clicked.connect(lambda: self.send_hxls_help("��������"))

    def send_hxls_help(self, helpstr):
        with open("resource\hxls\hxls_help.json", 'r', encoding='utf-8') as h:
            self.hxls_help = json.load(h)
        help_list = self.hxls_help[helpstr]
        self.output_string.moveCursor(self.output_string.textCursor().End)
        self.output_string.append("")
        for i in help_list:
            self.output_string.append(i)
            self.output_string.ensureCursorVisible()
    # ����ҳ��
    def hxls_start_program(self):
        self.hxls_game_path_Label = QtWidgets.QLabel(self.hxls_create_page)
        self.hxls_game_path_Label.setGeometry(self.ui_zoom(5, 5, 81, 25))
        self.hxls_game_path_Label.setObjectName("hxls_game_path_Label")
        self.hxls_game_path_Label.setText(self._translate("main_window", "��Ϸ����·��"))
        self.hxls_game_path = QtWidgets.QLineEdit(self.hxls_create_page)
        self.hxls_game_path.setGeometry(self.ui_zoom(5, 40, 260, 20))
        self.hxls_game_path.setObjectName("hxls_game_path")
        self.hxls_game_path.home(False)
        self.hxls_server_box = QtWidgets.QComboBox(self.hxls_create_page)
        self.hxls_server_box.setGeometry(self.ui_zoom(90, 5, 50, 25))
        self.hxls_server_box.setObjectName("hxls_server_box")
        self.comboboxstyle(self.hxls_server_box)
        self.hxls_server_box.addItems(self.hxls_index["������"])
        self.hxls_help1 = QtWidgets.QPushButton(self.hxls_create_page)
        self.hxls_help1.setGeometry(self.ui_zoom(225, 5, 40, 25))
        self.hxls_help1.setObjectName("hxls_help1")
        self.hxls_help1.setText(self._translate("main_window", "����"))
        # ʵ�ù�����
        self.hxls_gift_Label = QtWidgets.QLabel(self.hxls_create_page)
        self.hxls_gift_Label.setGeometry(self.ui_zoom(5, 70, 81, 25))
        self.hxls_gift_Label.setObjectName("hxls_game_path_Label")
        self.hxls_gift_Label.setText(self._translate("main_window", "ʵ�ù���"))
        self.hxls_gift_choose = QtWidgets.QPushButton(self.hxls_create_page)
        self.hxls_gift_choose.setGeometry(self.ui_zoom(5, 100, 60, 25))
        self.hxls_gift_choose.setObjectName("gift_choose")
        self.hxls_gift_choose.setText(self._translate("main_window", "����ѡ��"))
        self.hxls_gift_choose.clicked.connect(self.opengiftweb)
    # ��ս/��������ҳ��
    def hxls_fight_program(self):
        self.hxls_help2 = QtWidgets.QPushButton(self.hxls_fight_page)
        self.hxls_help2.setGeometry(self.ui_zoom(225, 10, 40, 25))
        self.hxls_help2.setObjectName("hxls_help2")
        self.hxls_help2.setText(self._translate("main_window", "����"))
        self.hxls_retour_Label = QtWidgets.QLabel(self.hxls_fight_page)
        self.hxls_retour_Label.setGeometry(self.ui_zoom(5, 10, 81, 25))
        self.hxls_retour_Label.setObjectName("retour_Label")
        self.hxls_retour_Label.setText(self._translate("main_window", "�ٴ�����"))
        self.hxls_fight_Label = QtWidgets.QLabel(self.hxls_fight_page)
        self.hxls_fight_Label.setGeometry(self.ui_zoom(70, 10, 81, 25))
        self.hxls_fight_Label.setObjectName("fight_Label")
        self.hxls_fight_Label.setText(self._translate("main_window", "����ѡ��"))
        self.hxls_refight = QtWidgets.QCheckBox(self.hxls_fight_page)
        self.hxls_refight.setGeometry(self.ui_zoom(20, 35, 58, 25))
        self.hxls_refight.setObjectName("refight")
        self.hxls_fight_box = QtWidgets.QComboBox(self.hxls_fight_page)
        self.hxls_fight_box.setGeometry(self.ui_zoom(65, 35, 60, 25))
        self.hxls_fight_box.setObjectName("fight_box")
        self.comboboxstyle(self.hxls_fight_box)
        self.hxls_fight_box.addItems(self.hxls_index["��ս�ؿ�"])
    # ���²ɹ�����ҳ��
    def hxls_dispatch_program(self):
        self.hxls_top_dispatch = QtWidgets.QWidget(self.hxls_dispatch_page)
        self.hxls_trans_list = self.hxls_index["����"]
        x, y = self.num_zoom([290, 250])
        self.hxls_top_dispatch.setMinimumSize(x, y)  #######���ù������ĳߴ�
        self.hxls_scroll_dispatch = QtWidgets.QScrollArea(self.hxls_dispatch_page)
        self.hxls_scroll_dispatch.setWidget(self.hxls_top_dispatch)
        x, y, w, h = self.num_zoom([0, 0, 290, 200])
        self.hxls_scroll_dispatch.move(x, y)
        self.hxls_scroll_dispatch.resize(w, h)
        self.hxls_scroll_dispatch.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # ѡ���ǩ
        self.hxls_material_Label = QtWidgets.QLabel(self.hxls_top_dispatch)
        self.hxls_material_Label.setGeometry(self.ui_zoom(25, 35, 81, 25))
        self.hxls_material_Label.setObjectName("material")
        self.hxls_material_Label.setText(self._translate("main_window", "����ѡ��"))
        self.hxls_fund_Label = QtWidgets.QLabel(self.hxls_top_dispatch)
        self.hxls_fund_Label.setGeometry(self.ui_zoom(105, 35, 81, 25))
        self.hxls_fund_Label.setObjectName("fund")
        self.hxls_fund_Label.setText(self._translate("main_window", "�ʽ�ѡ��"))
        self.hxls_plan_Label = QtWidgets.QLabel(self.hxls_top_dispatch)
        self.hxls_plan_Label.setGeometry(self.ui_zoom(190, 35, 81, 25))
        self.hxls_plan_Label.setObjectName("plan")
        self.hxls_plan_Label.setText(self._translate("main_window", "����ѡ��"))
        # �ٴβɹ�
        self.hxls_re_dispatch = QtWidgets.QCheckBox(self.hxls_top_dispatch)
        self.hxls_re_dispatch.setGeometry(self.ui_zoom(5, 5, 81, 25))
        self.hxls_re_dispatch.setObjectName("re_dispatch")
        self.hxls_re_dispatch.setText(self._translate("main_window", "�ٴβɹ�"))
        for num in range(6):
            exec("self.hxls_material%s = QtWidgets.QComboBox(self.hxls_top_dispatch)" % (num + 1))
            exec("self.hxls_fund%s = QtWidgets.QComboBox(self.hxls_top_dispatch)" % (num + 1))
            exec("self.hxls_plan%s = QtWidgets.QComboBox(self.hxls_top_dispatch)" % (num + 1))
            exec("self.hxls_material%s.addItems(self.hxls_index[\"���²ɹ�����\"])" % (num + 1))
            exec("self.hxls_fund%s.addItems(self.hxls_index[\"Я���ʽ�\"])" % (num + 1))
            exec("self.hxls_plan%s.addItems(self.hxls_index[\"�ɹ�����\"])" % (num + 1))

        self.hxls_help3 = QtWidgets.QPushButton(self.hxls_top_dispatch)
        self.hxls_help3.setGeometry(self.ui_zoom(225, 5, 40, 25))
        self.hxls_help3.setObjectName("hxls_help3")
        self.hxls_help3.setText(self._translate("main_window", "����"))

        for num in range(1, 7):
            strm,strd,strp = "hxls_material%s"%(num),"hxls_fund%s"%(num),"hxls_plan%s"%(num)
            fm, fd, fp = eval("self."+strm), eval("self."+strd), eval("self."+strp)
            fm.setGeometry(self.ui_zoom(5, 35 + num * 30, 85, 25))
            fm.setObjectName(strm)
            self.comboboxstyle(fm)
            fd.setGeometry(self.ui_zoom(95, 35 + num * 30, 75, 25))
            fd.setObjectName(strd)
            self.comboboxstyle(fd)
            fp.setGeometry(self.ui_zoom(175, 35 + num * 30, 90, 25))
            fp.setObjectName(strp)
            self.comboboxstyle(fp)
    # ս���ع�����ҳ��
    def hxls_review_program(self):
        self.hxls_help4 = QtWidgets.QPushButton(self.hxls_review_page)
        self.hxls_help4.setGeometry(self.ui_zoom(225, 5, 40, 25))
        self.hxls_help4.setObjectName("hxls_help4")
        self.hxls_help4.setText(self._translate("main_window", "����"))
        self.hxls_review_Label = QtWidgets.QLabel(self.hxls_review_page)
        self.hxls_review_Label.setGeometry(self.ui_zoom(10, 5, 80, 25))
        self.hxls_review_Label.setObjectName("review_Label")
        self.hxls_review_Label.setText(self._translate("main_window", "ս���ع�ѡ��"))

        self.hxls_review0 = QtWidgets.QComboBox(self.hxls_review_page)
        self.hxls_review0.setGeometry(self.ui_zoom(20, 35, 50, 25))
        self.hxls_review0.setObjectName("review0")
        self.comboboxstyle(self.hxls_review0)
        self.hxls_review0.addItems(self.hxls_index["ս���ع�ѡ��"])
    # ��ȡ����ҳ��
    def hxls_market_program(self):
        self.hxls_market_Label = QtWidgets.QLabel(self.hxls_market_page)
        self.hxls_market_Label.setGeometry(self.ui_zoom(60, 80, 160, 25))
        self.hxls_market_Label.setObjectName("hxls_market_Label")
        self.hxls_market_Label.setText(self._translate("main_window", "��ȡ������������ѡ��"))
        self.hxls_help5 = QtWidgets.QPushButton(self.hxls_market_page)
        self.hxls_help5.setGeometry(self.ui_zoom(225, 5, 40, 25))
        self.hxls_help5.setObjectName("hxls_help5")
        self.hxls_help5.setText(self._translate("main_window", "����"))
    # ���ѷ�ļ����ҳ��
    def hxls_recruit_program(self):
        self.hxls_help6 = QtWidgets.QPushButton(self.hxls_recruit_page)
        self.hxls_help6.setGeometry(self.ui_zoom(225, 5, 40, 25))
        self.hxls_help6.setObjectName("hxls_help6")
        self.hxls_help6.setText(self._translate("main_window", "����"))

        self.hxls_expedite_Label = QtWidgets.QLabel(self.hxls_recruit_page)
        self.hxls_expedite_Label.setGeometry(self.ui_zoom(5, 5, 81, 25))
        self.hxls_expedite_Label.setObjectName("expedite_Label")
        self.hxls_expedite_Label.setText(self._translate("main_window", "����"))
        self.hxls_recruit_Label = QtWidgets.QLabel(self.hxls_recruit_page)
        self.hxls_recruit_Label.setGeometry(self.ui_zoom(45, 5, 81, 25))
        self.hxls_recruit_Label.setObjectName("recruit_Label")
        self.hxls_recruit_Label.setText(self._translate("main_window", "��ļ�ƻ�"))

        self.hxls_expedite = QtWidgets.QCheckBox(self.hxls_recruit_page)
        self.hxls_expedite.setGeometry(self.ui_zoom(10, 35, 58, 22))
        self.hxls_expedite.setObjectName("expedite")

        self.hxls_recruit0 = QtWidgets.QComboBox(self.hxls_recruit_page)
        self.hxls_recruit0.setGeometry(self.ui_zoom(40, 35, 60, 22))
        self.hxls_recruit0.setObjectName("recruit0")
        self.comboboxstyle(self.hxls_recruit0)
        numlist = ["0��", "100��", "200��", "300��", "400��", "500��", "600��", "700��"]
        self.hxls_recruit0.addItems(numlist)
        # �鿨��ʷ
        self.recruit_history = QtWidgets.QPushButton(self.hxls_recruit_page)
        self.recruit_history.setGeometry(self.ui_zoom(245, 35, 25, 25))
        self.recruit_history.setObjectName("recruit_history")
        self.recruit_history.setIcon(QtGui.QIcon(r"resource\main_window\ui\history.png"))
        self.recruit_history.setFlat(True)
        self.recruit_history.clicked.connect(self.open_history)
    def open_history(self):
        self.cmdrun("start "" resource\hxls\screenshot")
    # ��ȡÿ��ҳ��
    def hxls_reward_program(self):
        self.hxls_reward_Label = QtWidgets.QLabel(self.hxls_reward_page)
        self.hxls_reward_Label.setGeometry(self.ui_zoom(60, 80, 160, 25))
        self.hxls_reward_Label.setObjectName("hxls_reward_Label")
        self.hxls_reward_Label.setText(self._translate("main_window", "��ȡÿ����������ѡ��"))
        self.hxls_help7 = QtWidgets.QPushButton(self.hxls_reward_page)
        self.hxls_help7.setGeometry(self.ui_zoom(225, 5, 40, 25))
        self.hxls_help7.setObjectName("hxls_help7")
        self.hxls_help7.setText(self._translate("main_window", "����"))
    # ��������ҳ��
    def hxls_market_network_program(self):
        self.hxls_market_network_Label = QtWidgets.QLabel(self.hxls_market_network_page)
        self.hxls_market_network_Label.setGeometry(self.ui_zoom(60, 80, 160, 25))
        self.hxls_market_network_Label.setObjectName("hxls_market_network_Label")
        self.hxls_market_network_Label.setText(self._translate("main_window", "����������������ѡ��"))
        self.hxls_help8 = QtWidgets.QPushButton(self.hxls_market_network_page)
        self.hxls_help8.setGeometry(self.ui_zoom(225, 5, 40, 25))
        self.hxls_help8.setObjectName("hxls_help8")
        self.hxls_help8.setText(self._translate("main_window", "����"))
    # ʹ�������ҳ��
    def hxls_random_gift_program(self):
        self.hxls_random_gift_Label = QtWidgets.QLabel(self.hxls_random_gift_page)
        self.hxls_random_gift_Label.setGeometry(self.ui_zoom(60, 80, 160, 25))
        self.hxls_random_gift_Label.setObjectName("hxls_random_gift_Label")
        self.hxls_random_gift_Label.setText(self._translate("main_window", "ʹ���������������ѡ��"))
        self.hxls_help9 = QtWidgets.QPushButton(self.hxls_random_gift_page)
        self.hxls_help9.setGeometry(self.ui_zoom(225, 5, 40, 25))
        self.hxls_help9.setObjectName("hxls_help9")
        self.hxls_help9.setText(self._translate("main_window", "����"))
    # ����ҳ��
    def hxls_kill_game_program(self):
        self.hxls_choose_kill_game = QtWidgets.QCheckBox(self.hxls_kill_game_page)
        self.hxls_choose_kill_game.setGeometry(self.ui_zoom(5, 5, 140, 25))
        self.hxls_choose_kill_game.setObjectName("hxls_choose_kill_game")
        self.hxls_choose_kill_game.setText(self._translate("main_window", "�ر���Ϸ"))
        self.hxls_choose_kill_SGA = QtWidgets.QCheckBox(self.hxls_kill_game_page)
        self.hxls_choose_kill_SGA.setGeometry(self.ui_zoom(5, 35, 140, 25))
        self.hxls_choose_kill_SGA.setObjectName("hxls_choose_kill_SGA")
        self.hxls_choose_kill_SGA.setText(self._translate("main_window", "�ر�SGA"))
        self.hxls_choose_kill_SGA.clicked.connect(self.hxls_kill_SGA_click)
        self.hxls_choose_sleep = QtWidgets.QCheckBox(self.hxls_kill_game_page)
        self.hxls_choose_sleep.setGeometry(self.ui_zoom(5, 65, 140, 25))
        self.hxls_choose_sleep.setObjectName("hxls_choose_sleep")
        self.hxls_choose_sleep.setText(self._translate("main_window", "����˯��"))
        self.hxls_choose_sleep.clicked.connect(self.hxls_sleep_click)
        self.hxls_continue_Label = QtWidgets.QLabel(self.hxls_kill_game_page)
        self.hxls_continue_Label.setGeometry(self.ui_zoom(5, 90, 160, 25))
        self.hxls_continue_Label.setObjectName("hxls_continue_Label")
        self.hxls_continue_Label.setText(self._translate("main_window", "����ִ��"))
        self.hxls_refresh_button = QtWidgets.QPushButton(self.hxls_kill_game_page)
        self.hxls_refresh_button.setGeometry(self.ui_zoom(60, 90, 25, 25))
        self.hxls_refresh_button.setObjectName("hxls_refresh")
        self.hxls_refresh_button.setIcon(QtGui.QIcon(r"resource\main_window\ui\refresh.png"))
        self.hxls_refresh_button.setFlat(True)
        self.hxls_refresh_button.clicked.connect(self.hxls_refresh)
        self.hxls_continue_box = QtWidgets.QComboBox(self.hxls_kill_game_page)
        self.hxls_continue_box.setGeometry(self.ui_zoom(5, 120, 135, 25))
        self.hxls_continue_box.setObjectName("hxls_continue_box")
        self.comboboxstyle(self.hxls_continue_box)
        self.hxls_continue_box.addItems(["��ִ��"] + self.filelist)
        self.hxls_continue_box.currentIndexChanged.connect(self.hxls_continue_change)
        self.hxls_help10 = QtWidgets.QPushButton(self.hxls_kill_game_page)
        self.hxls_help10.setGeometry(self.ui_zoom(225, 5, 40, 25))
        self.hxls_help10.setObjectName("hxls_help10")
        self.hxls_help10.setText(self._translate("main_window", "����"))
    # ����ҳ��-������ť
    def hxls_kill_SGA_click(self):
        if self.hxls_choose_kill_SGA.isChecked():
            self.hxls_choose_kill_game.setChecked(True)
    def hxls_sleep_click(self):
        if self.hxls_choose_sleep.isChecked():
            self.hxls_choose_kill_game.setChecked(True)
    def hxls_continue_change(self):
        if self.hxls_continue_box.currentIndex() != 0:
            self.hxls_choose_kill_game.setChecked(True)
            self.hxls_choose_kill_SGA.setChecked(False)
            self.hxls_choose_sleep.setChecked(False)
    def hxls_refresh(self):
        filedir = "resource\main_window\config"
        self.filelist = []
        for file in os.listdir(filedir):
            name, suffix = os.path.splitext(file)
            if suffix == ".json": self.filelist += [name]
        self.hxls_continue_box.clear()
        self.hxls_continue_box.addItems(["��ִ��"] +self.filelist)
    def opengiftweb(self):
        webbrowser.open("https://www.bilibili.com/read/cv24639360/?from=search&spm_id_from=333.337.0.0", new=0,
                        autoraise=True)
    # �Ի������Ṥ�߸�ʽ��������
    def load_hxls(self):
        # ���ع�������
        trans_list = self.hxls_index["����"]
        for num in range(len(trans_list)):
            fc = eval("self.hxls_choose_" + self.hxls_index[trans_list[num]])
            fc.setChecked(self.configdir[trans_list[num]])
        # ��������
        self.hxls_game_path.setText(self.configdir["��Ϸ����·��"])
        self.hxls_server_box.setCurrentIndex(self.configdir["������"])
        # ������ս����
        self.hxls_refight.setChecked(self.configdir["��ս����"][0])
        self.hxls_fight_box.setCurrentIndex(self.configdir["��ս����"][1])
        # ������ǲ����
        for num in range(1, 7):
            fm, fd, fp = eval("self.hxls_material%s"%(num)), eval("self.hxls_fund%s"%(num)), eval("self.hxls_plan%s"%(num))
            fm.setCurrentIndex(self.configdir["���²ɹ�%s"%(num)][0])
            fd.setCurrentIndex(self.configdir["���²ɹ�%s"%(num)][1])
            fp.setCurrentIndex(self.configdir["���²ɹ�%s"%(num)][2])
        self.hxls_re_dispatch.setChecked(self.configdir["�ٴβɹ�"])
        # ����ս���ع�����
        self.hxls_review0.setCurrentIndex(self.configdir["ս���ع�����"])
        # �������ѷ�ļ����
        self.hxls_expedite.setChecked(self.configdir["���ѷ�ļ����"][0])
        self.hxls_recruit0.setCurrentIndex(self.configdir["���ѷ�ļ����"][1])
        self.hxls_choose_kill_game.setChecked(self.configdir["�ر���Ϸ"])
        self.hxls_choose_kill_SGA.setChecked(self.configdir["�ر�SGA"])
        self.hxls_choose_sleep.setChecked(self.configdir["����˯��"])
        self.hxls_continue_box.setCurrentText(self.configdir["����ִ��"])
    # �Ի������Ṥ�߸�ʽ��������
    def save_hxls(self):
        self.configdir = {"��Ϸ����": "��������"}
        self.configdir["��Ϸ����·��"] = self.hxls_game_path.text().strip("\"")
        self.configdir["������"] = self.hxls_server_box.currentIndex()
        plist = self.hxls_index["����"]
        for num in range(len(plist)):
            strc = "choose_" + self.hxls_index[plist[num]]
            fc = eval("self.hxls_" + strc)
            self.configdir[plist[num]] = fc.isChecked()
        for num in range(1, 7):
            fm, fd, fp = eval("self.hxls_material%s"%(num)), eval("self.hxls_fund%s"%(num)), eval("self.hxls_plan%s"%(num))
            self.configdir["���²ɹ�" + str(num)] = [fm.currentIndex(),fd.currentIndex(),fp.currentIndex()]
        self.configdir["�ٴβɹ�"]  = self.hxls_re_dispatch.isChecked()
        self.configdir["ս���ع�����"] = self.hxls_review0.currentIndex()
        self.configdir["��ս����"] = [self.hxls_refight.isChecked() ,self.hxls_fight_box.currentIndex()]
        self.configdir["���ѷ�ļ����"] = [self.hxls_expedite.isChecked() ,self.hxls_recruit0.currentIndex()]
        self.configdir["�ر���Ϸ"] = self.hxls_choose_kill_game.isChecked()
        self.configdir["�ر�SGA"] = self.hxls_choose_kill_SGA.isChecked()
        self.configdir["����˯��"] = self.hxls_choose_sleep.isChecked()
        self.configdir["����ִ��"] = self.hxls_continue_box.currentText()
    # �Ի������Ṥ�߸�ʽ-�����ļ������������б�
    def create_hxls_config_runlist(self):
        choose_list, dispatch_list = [], []
        for name in self.hxls_index["����"]: choose_list += [self.rundir[name]]
        start_list = [self.rundir["��Ϸ����·��"],self.rundir["������"]]
        for num in range(1, 7):
            dispatch_list += [self.rundir["���²ɹ�" + str(num)]]
        dispatch_list += [self.rundir["�ٴβɹ�"]]
        review_list = self.rundir["ս���ع�����"]
        fight_list = self.rundir["��ս����"]
        recruit_list = self.rundir["���ѷ�ļ����"]
        finish_list = [self.rundir["�ر���Ϸ"],self.rundir["�ر�SGA"],self.rundir["����˯��"]]
        return [choose_list, start_list, fight_list,dispatch_list, review_list,  recruit_list, finish_list]
    # �Ի������Ṥ�߸�ʽ-��ǰҳ�棬���������б�
    def create_hxls_main_runlist(self):
        choose_list, dispatch_list = [], []
        for name in self.hxls_index["����"]:
            fc = eval("self.hxls_choose_" + self.hxls_index[name])
            choose_list += [fc.isChecked()]
        start_list = [self.hxls_game_path.text(),self.hxls_server_box.currentIndex()]
        for num in range(1, 7):
            dispatch_list += [[eval("self.hxls_material" + str(num)).currentIndex(),
                           eval("self.hxls_fund" + str(num)).currentIndex(),
                           eval("self.hxls_plan" + str(num)).currentIndex()]]
        dispatch_list += [self.hxls_re_dispatch.isChecked()]
        review_list = self.hxls_review0.currentIndex()
        fight_list = [self.hxls_refight.isChecked(), self.hxls_fight_box.currentIndex()]
        recruit_list = [self.hxls_expedite.isChecked(), self.hxls_recruit0.currentIndex()]
        finish_list = [self.hxls_choose_kill_game.isChecked(),
                       self.hxls_choose_kill_SGA.isChecked(),
                       self.hxls_choose_sleep.isChecked()]
        self.continue_config = self.hxls_continue_box.currentText()
        return [choose_list, start_list, fight_list,dispatch_list, review_list,  recruit_list, finish_list]