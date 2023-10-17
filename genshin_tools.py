# -*- coding:gbk -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import json
class Genshin_ui_group(object):
    def genshin_game_tool(self):
        self.genshin_page = QtWidgets.QWidget()
        self.genshin_page.setObjectName("genshin_page")
        self.game_pages.addWidget(self.genshin_page)
        with open("resource\genshin\genshin_index.json", 'r', encoding='utf-8') as d:
            self.genshin_index = json.load(d)
        # ��ǩ
        self.genshin_choose_Label = QtWidgets.QLabel(self.genshin_page)
        self.genshin_choose_Label.setGeometry(self.ui_zoom(20, 0, 81, 25))
        self.genshin_choose_Label.setObjectName("genshin_choose_Label")
        self.genshin_choose_Label.setText(self._translate("main_window", "ѡ ��"))
        self.genshin_set_Label = QtWidgets.QLabel(self.genshin_page)
        self.genshin_set_Label.setGeometry(self.ui_zoom(110, 0, 81, 25))
        self.genshin_set_Label.setObjectName("genshin_set_Label")
        self.genshin_set_Label.setText(self._translate("main_window", "�л�ҳ��"))
        # ����ҳ��
        self.genshin_filler = QtWidgets.QWidget(self.genshin_page)
        self.trans_list = self.genshin_index["����"]
        self.genshin_filler.setMinimumSize(168, len(self.trans_list) * 30)  #######���ù������ĳߴ�
        self.genshin_scroll = QtWidgets.QScrollArea(self.genshin_page)
        self.genshin_scroll.setWidget(self.genshin_filler)
        x, y, w, h = self.num_zoom([2, 28, 168, 280])
        self.genshin_scroll.move(x, y)
        self.genshin_scroll.resize(w, h)
        self.genshin_scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        for num in range(len(self.trans_list)):
            tname = self.trans_list[num]
            fnamep = self.genshin_index[tname]
            strc, strs, strp = "self.genshin_choose_%s" % (fnamep), "self.genshin_set_%s" % (fnamep), "self.genshin_%s_page" % (fnamep)
            exec(strc + "= QtWidgets.QCheckBox(self.genshin_filler)")
            exec(strs + "= QtWidgets.QPushButton(self.genshin_filler)")
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
        self.genshin_choose_create.setEnabled(False)
        self.genshin_choose_create.setChecked(True)
        self.genshin_choose_kill_game.setEnabled(False)
        self.genshin_choose_kill_game.setChecked(True)
        self.genshin_set_create.clicked.connect(lambda: self.change_set_page(1))
        self.genshin_set_team.clicked.connect(lambda: self.change_set_page(2))
        self.genshin_set_dispatch.clicked.connect(lambda: self.change_set_page(3))
        self.genshin_set_para_trans.clicked.connect(lambda: self.change_set_page(4))
        self.genshin_set_crystalfly.clicked.connect(lambda: self.change_set_page(5))
        self.genshin_set_comp.clicked.connect(lambda: self.change_set_page(6))
        self.genshin_set_serenitea_pot.clicked.connect(lambda: self.change_set_page(7))
        self.genshin_set_cut_tree.clicked.connect(lambda: self.change_set_page(8))
        self.genshin_set_kill_game.clicked.connect(lambda: self.change_set_page(9))

        self.genshin_start_program()
        self.genshin_team_program()
        self.genshin_dispatch_program()
        self.genshin_para_trans_program()
        self.genshin_crystalfly_program()
        self.genshin_comp_program()
        self.genshin_serenitea_pot_program()
        self.genshin_cut_tree_program()
        self.genshin_kill_game_program()
        # ������ť
        self.genshin_help1.clicked.connect(lambda: self.send_genshin_help("ģ�����"))
        self.genshin_help2.clicked.connect(lambda: self.send_genshin_help("�л�����"))
        self.genshin_help3.clicked.connect(lambda: self.send_genshin_help("̽����ǲ"))
        self.genshin_help4.clicked.connect(lambda: self.send_genshin_help("�����ʱ���"))
        self.genshin_help5.clicked.connect(lambda: self.send_genshin_help("׽����"))
        self.genshin_help6.clicked.connect(lambda: self.send_genshin_help("�ϳ���֬"))
        self.genshin_help7.clicked.connect(lambda: self.send_genshin_help("�����"))
        self.genshin_help8.clicked.connect(lambda: self.send_genshin_help("����"))
        self.genshin_help9.clicked.connect(lambda: self.send_genshin_help("��������"))
    def send_genshin_help(self,helpstr):
        with open("resource\genshin\genshin_help.json", 'r', encoding='utf-8') as h:
            self.genshin_help = json.load(h)
        help_list = self.genshin_help[helpstr]
        self.output_string.moveCursor(self.output_string.textCursor().End)
        self.output_string.append("")
        for i in help_list:
            self.output_string.append(i)
            self.output_string.ensureCursorVisible()
    # ����ҳ��
    def genshin_start_program(self):
        self.genshin_game_path_Label = QtWidgets.QLabel(self.genshin_create_page)
        self.genshin_game_path_Label.setGeometry(self.ui_zoom(5, 5, 81, 25))
        self.genshin_game_path_Label.setObjectName("genshin_game_path_Label")
        self.genshin_game_path_Label.setText(self._translate("main_window", "��Ϸ����·��"))
        self.genshin_game_path = QtWidgets.QLineEdit(self.genshin_create_page)
        self.genshin_game_path.setGeometry(self.ui_zoom(5, 40, 260, 20))
        self.genshin_game_path.setObjectName("genshin_game_path")
        self.genshin_game_path.home(False)
        self.genshin_server_box = QtWidgets.QComboBox(self.genshin_create_page)
        self.genshin_server_box.setGeometry(self.ui_zoom(90, 5, 50, 25))
        self.genshin_server_box.setObjectName("genshin_server_box")
        self.comboboxstyle(self.genshin_server_box)
        self.genshin_server_box.addItems(self.genshin_index["������"])
        self.genshin_help1 = QtWidgets.QPushButton(self.genshin_create_page)
        self.genshin_help1.setGeometry(self.ui_zoom(225, 5, 40, 25))
        self.genshin_help1.setObjectName("genshin_help1")
        self.genshin_help1.setText(self._translate("main_window", "����"))
    # �л�����ҳ��
    def genshin_team_program(self):
        self.genshin_team_Label = QtWidgets.QLabel(self.genshin_team_page)
        self.genshin_team_Label.setGeometry(self.ui_zoom(60, 80, 160, 25))
        self.genshin_team_Label.setObjectName("genshin_team_Label")
        self.genshin_team_Label.setText(self._translate("main_window", "����������������ѡ��"))
        self.genshin_help2 = QtWidgets.QPushButton(self.genshin_team_page)
        self.genshin_help2.setGeometry(self.ui_zoom(225, 5, 40, 25))
        self.genshin_help2.setObjectName("genshin_help2")
        self.genshin_help2.setText(self._translate("main_window", "����"))
    # ��ǲ����ҳ��
    def genshin_dispatch_program(self):
        self.genshin_region_Label = QtWidgets.QLabel(self.genshin_dispatch_page)
        self.genshin_region_Label.setGeometry(self.ui_zoom(15, 5, 81, 25))
        self.genshin_region_Label.setObjectName("genshin_region_Label")
        self.genshin_region_Label.setText(self._translate("main_window", "����ѡ��"))
        self.genshin_material_Label = QtWidgets.QLabel(self.genshin_dispatch_page)
        self.genshin_material_Label.setGeometry(self.ui_zoom(120, 5, 81, 25))
        self.genshin_material_Label.setObjectName("genshin_material_Label")
        self.genshin_material_Label.setText(self._translate("main_window", "����ѡ��"))

        self.genshin_help3 = QtWidgets.QPushButton(self.genshin_dispatch_page)
        self.genshin_help3.setGeometry(self.ui_zoom(225, 5, 40, 25))
        self.genshin_help3.setObjectName("genshin_help3")
        self.genshin_help3.setText(self._translate("main_window", "����"))

        rlist = self.genshin_index["��ǲ����"]
        for num in range(1, 6):
            strr, strm = "genshin_region" + str(num), "genshin_material" + str(num)
            exec("self.genshin_region%s = QtWidgets.QComboBox(self.genshin_dispatch_page)" % (num))
            exec("self.genshin_material%s = QtWidgets.QComboBox(self.genshin_dispatch_page)" % (num))
            fr, fm = eval("self." + strr), eval("self." + strm)
            fr.setGeometry(self.ui_zoom(10, num * 30+10, 62, 25))
            fr.setObjectName(strr)
            self.comboboxstyle(fr)
            fr.addItems(self.genshin_index["��ǲ����"])
            fm.setGeometry(self.ui_zoom(90, num * 30+10, 128, 25))
            fm.setObjectName(strm)
            self.comboboxstyle(fm)
            fm.addItems(self.genshin_index["�ɵ���ǲ����"])
        self.genshin_region1.currentIndexChanged.connect(lambda: self.change_list(self.genshin_region1, self.genshin_material1))
        self.genshin_region2.currentIndexChanged.connect(lambda: self.change_list(self.genshin_region2, self.genshin_material2))
        self.genshin_region3.currentIndexChanged.connect(lambda: self.change_list(self.genshin_region3, self.genshin_material3))
        self.genshin_region4.currentIndexChanged.connect(lambda: self.change_list(self.genshin_region4, self.genshin_material4))
        self.genshin_region5.currentIndexChanged.connect(lambda: self.change_list(self.genshin_region5, self.genshin_material5))
    # ��ǲ����ҳ��-�л��б�
    def change_list(self, fr, fm):
        mlist = self.genshin_index[fr.currentText() + "��ǲ����"]
        fm.clear()
        fm.addItems(mlist)
    # �����ʱ�������ҳ��
    def genshin_para_trans_program(self):
        self.genshin_para_trans_Label = QtWidgets.QLabel(self.genshin_para_trans_page)
        self.genshin_para_trans_Label.setGeometry(self.ui_zoom(5, 5, 81, 25))
        self.genshin_para_trans_Label.setObjectName("genshin_para_trans_Label")
        self.genshin_para_trans_Label.setText(self._translate("main_window", "���Ĳ���Ԥ��"))
        self.genshin_para_trans_material1 = QtWidgets.QLineEdit(self.genshin_para_trans_page)
        self.genshin_para_trans_material2 = QtWidgets.QLineEdit(self.genshin_para_trans_page)
        self.genshin_para_trans_material3 = QtWidgets.QLineEdit(self.genshin_para_trans_page)
        self.genshin_para_trans_material4 = QtWidgets.QLineEdit(self.genshin_para_trans_page)
        self.genshin_para_trans_material5 = QtWidgets.QLineEdit(self.genshin_para_trans_page)
        self.genshin_help4 = QtWidgets.QPushButton(self.genshin_para_trans_page)
        self.genshin_help4.setGeometry(self.ui_zoom(225, 5, 40, 25))
        self.genshin_help4.setObjectName("genshin_help4")
        self.genshin_help4.setText(self._translate("main_window", "����"))
        for num in range(1, 6):
            strt = "genshin_para_trans_material" + str(num)
            ft = eval("self." + strt)
            ft.setGeometry(self.ui_zoom(5, 10 + num * 30, 260, 20))
            ft.setObjectName("genshin_para_trans_material" + str(num))
    # ׽��������ҳ��
    def genshin_crystalfly_program(self):
        # ��ѡ��ť��ʼ��
        self.genshin_crystalfly0 = QtWidgets.QCheckBox(self.genshin_crystalfly_page)
        self.genshin_crystalfly1 = QtWidgets.QCheckBox(self.genshin_crystalfly_page)
        self.genshin_crystalfly2 = QtWidgets.QCheckBox(self.genshin_crystalfly_page)
        self.genshin_crystalfly3 = QtWidgets.QCheckBox(self.genshin_crystalfly_page)
        self.genshin_crystalfly4 = QtWidgets.QCheckBox(self.genshin_crystalfly_page)
        self.genshin_crystalfly5 = QtWidgets.QCheckBox(self.genshin_crystalfly_page)
        self.genshin_help5 = QtWidgets.QPushButton(self.genshin_crystalfly_page)
        self.genshin_help5.setGeometry(self.ui_zoom(225, 5, 40, 25))
        self.genshin_help5.setObjectName("genshin_help5")
        self.genshin_help5.setText(self._translate("main_window", "����"))
        strlist = self.genshin_index["����"]
        for num in range(len(strlist)):
            strc = "genshin_crystalfly" + str(num)
            fc = eval("self." + strc)
            fc.setGeometry(self.ui_zoom(10, 10 + num * 30, 140, 25))
            fc.setObjectName(strc)
            fc.setText(self._translate("main_window", strlist[num]))
            # fc.setChecked(blist[num])
    # �ϳ�Ũ����֬ҳ��
    def genshin_comp_program(self):
        self.genshin_comp_Label = QtWidgets.QLabel(self.genshin_comp_page)
        self.genshin_comp_Label.setGeometry(self.ui_zoom(60, 80, 160, 25))
        self.genshin_comp_Label.setObjectName("genshin_comp_Label")
        self.genshin_comp_Label.setText(self._translate("main_window", "�ϳ�Ũ����֬��������ѡ��"))
        self.genshin_help6 = QtWidgets.QPushButton(self.genshin_comp_page)
        self.genshin_help6.setGeometry(self.ui_zoom(225, 5, 40, 25))
        self.genshin_help6.setObjectName("genshin_help6")
        self.genshin_help6.setText(self._translate("main_window", "����"))
    # ��ȡ�����ҳ��
    def genshin_serenitea_pot_program(self):
        self.genshin_serenitea_pot_Label = QtWidgets.QLabel(self.genshin_serenitea_pot_page)
        self.genshin_serenitea_pot_Label.setGeometry(self.ui_zoom(60, 80, 160, 25))
        self.genshin_serenitea_pot_Label.setObjectName("genshin_serenitea_pot_Label")
        self.genshin_serenitea_pot_Label.setText(self._translate("main_window", "��ȡ�������������ѡ��"))
        self.genshin_help7 = QtWidgets.QPushButton(self.genshin_serenitea_pot_page)
        self.genshin_help7.setGeometry(self.ui_zoom(225, 5, 40, 25))
        self.genshin_help7.setObjectName("genshin_help7")
        self.genshin_help7.setText(self._translate("main_window", "����"))
    # ��������ҳ��
    def genshin_cut_tree_program(self):  #
        woodlist1a, woodlist2a, woodlist3a = self.genshin_index["ľ������1"], self.genshin_index["ľ������2"], self.genshin_index[
            "ľ������3"]
        woodlist1b, woodlist2b, woodlist3b = self.genshin_index["tree_kind1"], self.genshin_index["tree_kind2"], \
        self.genshin_index[
            "tree_kind3"]
        self.genshin_filler_tree = QtWidgets.QWidget(self.genshin_cut_tree_page)
        w, h = self.num_zoom([290, len(woodlist1a) * 30 + 25])
        self.genshin_filler_tree.setMinimumSize(w, h)  #######���ù������ĳߴ�
        self.genshin_scroll_tree = QtWidgets.QScrollArea(self.genshin_cut_tree_page)
        self.genshin_scroll_tree.setWidget(self.genshin_filler_tree)
        [w, h] = self.num_zoom([290, 200])
        # self.genshin_scroll_tree.move(0, 10)
        self.genshin_scroll_tree.resize(w, h)
        self.genshin_scroll_tree.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.genshin_cut_circulate_Label = QtWidgets.QLabel(self.genshin_filler_tree)
        self.genshin_cut_circulate_Label.setGeometry(self.ui_zoom(10, 5, 81, 25))
        self.genshin_cut_circulate_Label.setObjectName("genshin_cut_circulate_Label")
        self.genshin_cut_circulate_Label.setText(self._translate("main_window", "ѭ������"))
        self.genshin_cut_circulate = QtWidgets.QLineEdit(self.genshin_filler_tree)
        self.genshin_cut_circulate.setGeometry(self.ui_zoom(70, 8, 40, 20))
        self.genshin_cut_circulate.setObjectName("genshin_cut_circulate")
        self.genshin_help8 = QtWidgets.QPushButton(self.genshin_filler_tree)
        self.genshin_help8.setGeometry(self.ui_zoom(225, 5, 40, 25))
        self.genshin_help8.setObjectName("genshin_help8")
        self.genshin_help8.setText(self._translate("main_window", "����"))
        intValidator = QtGui.QIntValidator()
        intValidator.setRange(1, 99)
        self.genshin_cut_circulate.setValidator(intValidator)
        for i in range(1, 4):
            la, lb = self.genshin_index["ľ������%s" % (i)], self.genshin_index["tree_kind%s" % (i)]
            for num in range(len(lb)):
                strw = "self.genshin_choose_%s" % (lb[num])
                exec(strw + "= QtWidgets.QCheckBox(self.genshin_filler_tree)")
                fw = eval(strw)
                fw.setGeometry(self.ui_zoom(-80 + i * 90, 35 + num * 30, 140, 25))
                fw.setObjectName(strw)
                fw.setText(self._translate("main_window", la[num]))
    # ����ҳ��
    def genshin_kill_game_program(self):
        self.genshin_choose_kill_game= QtWidgets.QCheckBox(self.genshin_kill_game_page)
        self.genshin_choose_kill_game.setGeometry(self.ui_zoom(5, 5, 140, 25))
        self.genshin_choose_kill_game.setObjectName("genshin_choose_kill_game")
        self.genshin_choose_kill_game.setText(self._translate("main_window", "�ر���Ϸ"))
        self.genshin_choose_kill_SGA = QtWidgets.QCheckBox(self.genshin_kill_game_page)
        self.genshin_choose_kill_SGA.setGeometry(self.ui_zoom(5, 35, 140, 25))
        self.genshin_choose_kill_SGA.setObjectName("genshin_choose_kill_SGA")
        self.genshin_choose_kill_SGA.setText(self._translate("main_window", "�ر�SGA"))
        self.genshin_choose_kill_SGA.clicked.connect(self.genshin_kill_SGA_click)
        self.genshin_choose_sleep = QtWidgets.QCheckBox(self.genshin_kill_game_page)
        self.genshin_choose_sleep.setGeometry(self.ui_zoom(5, 65, 140, 25))
        self.genshin_choose_sleep.setObjectName("genshin_choose_sleep")
        self.genshin_choose_sleep.setText(self._translate("main_window", "����˯��"))
        self.genshin_choose_sleep.clicked.connect(self.genshin_sleep_click)
        self.genshin_continue_Label = QtWidgets.QLabel(self.genshin_kill_game_page)
        self.genshin_continue_Label.setGeometry(self.ui_zoom(5, 90, 160, 25))
        self.genshin_continue_Label.setObjectName("genshin_continue_Label")
        self.genshin_continue_Label.setText(self._translate("main_window", "����ִ��"))
        self.genshin_refresh_button = QtWidgets.QPushButton(self.genshin_kill_game_page)
        self.genshin_refresh_button.setGeometry(self.ui_zoom(60, 90, 25, 25))
        self.genshin_refresh_button.setObjectName("genshin_refresh")
        self.genshin_refresh_button.setIcon(QtGui.QIcon(r"resource\main_window\ui\refresh.png"))
        self.genshin_refresh_button.setFlat(True)
        self.genshin_refresh_button.clicked.connect(self.genshin_refresh)
        self.genshin_continue_box = QtWidgets.QComboBox(self.genshin_kill_game_page)
        self.genshin_continue_box.setGeometry(self.ui_zoom(5, 120, 135, 25))
        self.genshin_continue_box.setObjectName("genshin_continue_box")
        self.comboboxstyle(self.genshin_continue_box)
        self.genshin_continue_box.addItems(["��ִ��"]+self.filelist)
        self.genshin_continue_box.currentIndexChanged.connect(self.genshin_continue_change)
        self.genshin_help9 = QtWidgets.QPushButton(self.genshin_kill_game_page)
        self.genshin_help9.setGeometry(self.ui_zoom(225, 5, 40, 25))
        self.genshin_help9.setObjectName("genshin_help9")
        self.genshin_help9.setText(self._translate("main_window", "����"))
    # ����ҳ��-������ť
    def genshin_kill_SGA_click(self):
        if self.genshin_choose_kill_SGA.isChecked():
            self.genshin_choose_kill_game.setChecked(True)
    def genshin_sleep_click(self):
        if self.genshin_choose_sleep.isChecked():
            self.genshin_choose_kill_game.setChecked(True)
    def genshin_continue_change(self):
        if self.genshin_continue_box.currentIndex() != 0:
            self.genshin_choose_kill_game.setChecked(True)
            self.genshin_choose_kill_SGA.setChecked(False)
            self.genshin_choose_sleep.setChecked(False)
    def genshin_refresh(self):
        filedir = "resource\main_window\config"
        self.filelist = []
        for file in os.listdir(filedir):
            name, suffix = os.path.splitext(file)
            if suffix == ".json": self.filelist += [name]
        self.genshin_continue_box.clear()
        self.genshin_continue_box.addItems(["��ִ��"] + self.filelist)
    # ��ԭ�񹤾߸�ʽ��������
    def load_genshin(self):
        # ���ع�������
        trans_list = self.genshin_index["����"]
        for num in range(len(trans_list)):
            fc = eval("self.genshin_choose_" + self.genshin_index[trans_list[num]])
            tname = trans_list[num]
            che = self.configdir[tname]
            fc.setChecked(che)
        # ��������
        self.genshin_game_path.setText(self.configdir["��Ϸ����·��"])
        self.genshin_server_box.setCurrentIndex(self.configdir["������"])
        # ������ǲ����
        for num in range(1, 6):
            fr, fm = eval("self.genshin_region%s"%(num)), eval("self.genshin_material%s"%(num))
            rnum = self.configdir["��ǲ����" + str(num)]
            fr.setCurrentIndex(rnum)
            fm.setCurrentIndex(self.configdir["��ǲ����" + str(num)])
        # ���ز����ʱ���ʹ�ò�������
        for num in range(1, 6):
            ft = eval("self.genshin_para_trans_material%s"%(num))
            ft.setText(self.configdir["ʹ�ò���" + str(num)])
            ft.home(False)
        # ���ؾ�������
        blist = self.configdir["����"]
        for num in range(len(blist)):
            fc = eval("self.genshin_crystalfly%s"%(num))
            fc.setChecked(blist[num])
        for i in range(1, 4):
            for num in range(len(self.genshin_index["tree_kind%s" % (i)])):
                eval("self.genshin_choose_" + self.genshin_index["tree_kind%s" % (i)][num]).setChecked(
                    self.configdir["����%s" % (i)][num])
        self.genshin_cut_circulate.setText(self.configdir["����ѭ��"])
        self.genshin_choose_kill_game.setChecked(self.configdir["�ر���Ϸ"])
        self.genshin_choose_kill_SGA.setChecked(self.configdir["�ر�SGA"])
        self.genshin_choose_sleep.setChecked(self.configdir["����˯��"])
        self.genshin_continue_box.setCurrentText(self.configdir["����ִ��"])
    # ��ԭ�񹤾߸�ʽ��������
    def save_genshin(self):
        self.configdir = {"��Ϸ����": "ԭ��"}
        self.configdir["��Ϸ����·��"] = self.genshin_game_path.text().strip("\"")
        self.configdir["������"] = self.genshin_server_box.currentIndex()

        plist = self.genshin_index["����"]
        for num in range(len(plist)):
            strc = "choose_" + self.genshin_index[plist[num]]
            fc = eval("self.genshin_" + strc)
            self.configdir[plist[num]] = fc.isChecked()
        for num in range(1, 6):
            strr, strm, strt = "" + str(num), "" + str(num), "" + str(num)
            fr = eval("self.genshin_region%s" % (num))
            fm = eval("self.genshin_material%s" % (num))
            ft = eval("self.genshin_para_trans_material%s" % (num))
            t_region = fr.currentText()
            self.configdir["��ǲ����" + str(num)] = self.genshin_index["��ǲ����"].index(t_region)
            self.configdir["��ǲ����" + str(num)] = self.genshin_index[t_region + "��ǲ����"].index(
                fm.currentText())
            self.configdir["ʹ�ò���" + str(num)] = ft.text()
        self.configdir["����"] = []
        for num in range(6): self.configdir["����"] += [eval("self.genshin_crystalfly" + str(num)).isChecked()]
        for i in range(1, 4):
            self.configdir["����%s" % (i)] = []
            for num in range(len(self.genshin_index["tree_kind%s" % (i)])):
                self.configdir["����%s" % (i)] += [eval(
                    "self.genshin_choose_" + self.genshin_index["tree_kind%s" % (i)][num]).isChecked()]
        self.configdir["����ѭ��"] = self.genshin_cut_circulate.text()
        self.configdir["�ر���Ϸ"] = self.genshin_choose_kill_game.isChecked()
        self.configdir["�ر�SGA"] = self.genshin_choose_kill_SGA.isChecked()
        self.configdir["����˯��"] = self.genshin_choose_sleep.isChecked()
        self.configdir["����ִ��"] = self.genshin_continue_box.currentText()
    # ��ԭ�񹤾߸�ʽ-�����ļ������������б�
    def create_genshin_config_runlist(self):
        choose_list, region_list, dispatchm_list, usem_list = [], [], [], []
        for name in self.genshin_index["����"]: choose_list += [self.rundir[name]]
        start_list = [self.rundir["��Ϸ����·��"],self.rundir["������"]]
        for num in range(1, 6):
            region_list += [self.rundir["��ǲ����" + str(num)]]
            dispatchm_list += [self.rundir["��ǲ����" + str(num)]]
            usem_list += [self.rundir["ʹ�ò���" + str(num)]]
        fly_list = self.rundir["����"]
        cuttree_list = [self.rundir["����ѭ��"],self.rundir["����1"],self.rundir["����2"],self.rundir["����3"]]
        finish_list = [self.rundir["�ر���Ϸ"],self.rundir["�ر�SGA"],self.rundir["����˯��"]]
        return [choose_list, start_list, region_list, dispatchm_list, usem_list, fly_list, cuttree_list, finish_list]
    # ��ԭ�񹤾߸�ʽ-��ǰҳ�棬���������б�
    def create_genshin_main_runlist(self):
        ctlist1, ctlist2, ctlist3 = [], [], []
        choose_list, region_list, dispatchm_list, usem_list, fly_list = [], [], [], [], []
        for name in self.genshin_index["����"]:
            fc = eval("self.genshin_choose_" + self.genshin_index[name])
            choose_list += [fc.isChecked()]
        start_list = [self.genshin_game_path.text(),self.genshin_server_box.currentIndex()]
        for num in range(1, 6):
            region_list += [eval("self.genshin_region%s"%(num)).currentIndex()]
            dispatchm_list += [eval("self.genshin_material%s"%(num)).currentIndex()]
            usem_list += [eval("self.genshin_para_trans_material%s"%(num)).text()]
        for num in range(len(self.genshin_index["����"])):
            fly_list += [eval("self.genshin_crystalfly%s"%(num)).isChecked()]
        for wood in self.genshin_index["tree_kind1"]: ctlist1 += [eval("self.genshin_choose_" + wood).isChecked()]
        for wood in self.genshin_index["tree_kind2"]: ctlist2 += [eval("self.genshin_choose_" + wood).isChecked()]
        for wood in self.genshin_index["tree_kind3"]: ctlist3 += [eval("self.genshin_choose_" + wood).isChecked()]
        cuttree_list = [self.genshin_cut_circulate.text(), ctlist1, ctlist2, ctlist3]
        finish_list = [self.genshin_choose_kill_game.isChecked(),
                       self.genshin_choose_kill_SGA.isChecked(),
                       self.genshin_choose_sleep.isChecked()]
        self.continue_config = self.genshin_continue_box.currentText()
        return [choose_list, start_list, region_list, dispatchm_list, usem_list, fly_list, cuttree_list, finish_list]