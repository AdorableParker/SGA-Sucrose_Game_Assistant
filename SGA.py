# -*- coding:gbk -*-
import os
import sys,json,keyboard,time,datetime,shutil,random,pyautogui
import resource.main_window.ui.SGA_icon
import win32api, win32gui, win32print
from threading import Thread,Event
from subprocess import run
from ctypes import windll
from function import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from genshin_thread import *
from genshin_tools import *
from hxls_thread import *
from hxls_tools import *
from starrail_thread import *
from starrail_tools import *
from maa_thread import *
from maa_tools import *
# pyinstaller -D -w -i D:\Kin-project\python-SGA\resource\main_window\ui\ico\SGA.ico D:\Kin-project\python-SGA\SGA.py
#pyrcc5 -o work\SGA_icon.py work\SGA_icon.qrc
user32 = windll.user32
now_width = user32.GetSystemMetrics(0)
user32.SetProcessDPIAware()
origin_width = user32.GetSystemMetrics(0)#round(origin_width / 1920, 2)
origin_high = user32.GetSystemMetrics(1)#round(origin_high / 1080, 2)
uizoom = round(origin_width / now_width, 2)

class Main_window_function(object):
    # ���ð�ť��������ҳ��
    def button_connect(self):
        # ��������ť����
        self.rename.clicked.connect(self.rename_start)
        self.finish.clicked.connect(self.rename_finish)
        self.save.clicked.connect(self.save_config)
        self.load_button.clicked.connect(self.load_config)
        self.delete_button.clicked.connect(self.delete_config)
        self.change_config.currentIndexChanged.connect(self.create_new_config)
        self.game_box.currentIndexChanged.connect(self.change_tool_page)
        self.home_button.clicked.connect(lambda: self.change_set_page(0))
        self.history_button.clicked.connect(self.show_history)
        # ������ҳ����ť����
        self.add_button.clicked.connect(self.item_add)
        self.reduce_button.clicked.connect(self.item_reduce)
        self.save_time.clicked.connect(self.save_time_item)
        # ��ʱ����
        self.wait_key = Thread(target=self.wait_to_kill, daemon=True)
        self.wait_key.start()
        self.wait_time = Thread(target=self.wait_to_time, daemon=True)
        self.wait_time.start()
        # ������ť���Ͱ����ı�
        self.helpconfig.clicked.connect(lambda: self.sendhelp("��������"))
        self.introduce.clicked.connect(lambda: self.sendhelp("ʹ����֪"))
        self.help0.clicked.connect(lambda: self.sendhelp("��ʱ����"))

    # �����ڰ�ť���ܺ���
    def rename_start(self):
        self.rename.hide()
        self.finish.show()
        self.oldname = self.change_config.currentText()
        self.change_config.setEditable(True)
        self.showtext("��ʼ���������á������޸��������ƺ󣬵��ȷ�ϰ�ť������޸ġ�")
    def rename_finish(self):
        newname = self.change_config.currentText()
        os.rename(r"resource\main_window\config\%s.json" % (self.oldname),
                  r"resource\main_window\config\%s.json" % (newname))
        self.change_config.setEditable(False)
        index = self.change_config.currentIndex()
        self.change_config.setItemText(index, newname)
        self.finish.hide()
        self.rename.show()
        for num in range(len(self.home_config["ִ��"])):
            eval("self.cho_config%s" % (num)).setItemText(index - 1, newname)
        self.showtext("���������£�\n%s >>> %s"%(self.oldname,newname))
    def save_time_item(self):
        self.home_config["�����ļ�"] = self.change_config.currentText()
        self.home_config["Ϣ��"] = self.screen.isChecked()
        self.home_config["����"] = self.volume.isChecked()
        itemnum = len(self.home_config["ִ��"])
        dd, td, cd, wd = [], [], [], []
        vbsdir = r"%s\resource\main_window\batscr" % (self.workdir)
        vbspath = r"%s\resource\main_window\batscr\start-SAG.vbs" % (self.workdir)
        with open(r"resource\main_window\schtasks_index.json", 'r', encoding='utf-8') as x:
            self.xmldir = json.load(x)
        xmllist = self.xmldir["part1"]
        for num in range(itemnum):
            daily = eval("self.daily%s" % (num)).currentIndex()
            dd += [daily]
            pydatetime = eval("self.time%s" % (num)).dateTime().toPyDateTime()
            settime = time.mktime(pydatetime.timetuple())
            td += [settime]
            cd += [eval("self.cho_config%s" % (num)).currentText()]
            wakeup = eval("self.wakeup%s" % (num)).isChecked()
            wd += [wakeup]
            if num + 1 <= self.itemnum:
                # self.cmdrun("schtasks.exe /delete /tn %s /f" % (taskname))
                if daily == 0 or not wakeup:
                    pass
                else:
                    waketime = time.strftime("%H:%M", (pydatetime - datetime.timedelta(minutes=2)).timetuple())
                    if daily == 1:
                        time_item_list = self.xmldir["daily"]
                    else:
                        time_item_list = self.xmldir["weekly"]
                        week = ["", "", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][
                            daily]
                        time_item_list[5] = "          <" + week + " />\n"
                    time_item_list[1] = "      <StartBoundary>2023-09-20T" + waketime + "</StartBoundary>\n"
                    xmllist += time_item_list
        xmllist += self.xmldir["part2"]
        xmlpath = r"resource\main_window\SGA-wakeup.xml"
        f = open(xmlpath, 'w', encoding='utf-16')
        f.writelines(xmllist)
        f.close()
        self.cmdrun("schtasks.exe /create /tn SGA-wakeup /xml \"%s\" /f" % (xmlpath))
        self.home_config["ִ��"], self.home_config["��ʱ"] = dd, td
        self.home_config["����"], self.home_config["����"] = cd, wd
        self.home_config["��Ŀ��"] = self.itemnum
        with open("resource\main_window\home_config.json", 'w', encoding='utf-8') as c:
            json.dump(self.home_config, c, ensure_ascii=False, indent=1)
        self.showtext("SGA��ʱ�ƻ������Ѹ��¡�")
    def save_config(self):
        gamename = self.game_box.currentText()
        self.configdir = {}
        if gamename == "δѡ��":self.configdir = {"��Ϸ����": "δѡ��"}
        else:exec ("self.save_%s()"%(self.gamelist_en[self.gamelist_ch.index(gamename)]))
        configpath = r"resource\main_window\config\%s.json" % (self.change_config.currentText())
        with open(configpath, 'w', encoding='utf-8') as g:
            json.dump(self.configdir, g, ensure_ascii=False, indent=1)
        self.pixmap = QtGui.QPixmap(r"resource\main_window\ui\ico\0.png")
        self.ico.setPixmap(self.pixmap)
        self.showtext("�����Ѹ��£�"+self.change_config.currentText())
    def load_config(self):
        configname = self.change_config.currentText()
        with open("resource\main_window\config\%s.json" % (configname), 'r', encoding='utf-8') as c:
            self.configdir = json.load(c)
        gamename = self.configdir["��Ϸ����"]
        self.game_box.setCurrentText(gamename)
        if gamename == "δѡ��":pass
        else:exec ("self.load_%s()"%(self.gamelist_en[self.gamelist_ch.index(gamename)]))
        self.showtext("�������ã�"+configname)

    def delete_config(self):
        configname = self.change_config.currentText()
        configindex = self.change_config.currentIndex()
        os.remove(r"resource\main_window\config\%s.json" % (configname))
        self.change_config.removeItem(configindex)
        for num in range(len(self.home_config["ִ��"])):
            exec("self.cho_config%s.removeItem(configindex-1)" % (num))
        self.showtext("ɾ�����ã�" + configname)
    def create_new_config(self):
        if self.change_config.currentText() == "������½�����":
            newname = "Ĭ������" + str(random.randint(999, 10000))
            shutil.copyfile(r"resource\main_window\Ĭ������.json",
                            r"resource\main_window\config\%s.json" % (newname))
            self.change_config.addItem(newname)
            self.change_config.setCurrentText(newname)
            for num in range(len(self.home_config["ִ��"])):
                exec("self.cho_config%s.addItem(newname)" % (num))
            self.showtext("�������Ѵ�����" + newname)
        else:
            pass
    def show_history(self):
        from subprocess import run
        run("start "" resource\main_window\logging.txt", shell=True)
        # self.cmdrun("start "" resource\main_window\logging.txt")
    def change_tool_page(self):
        num = self.game_box.currentIndex()
        if num:
            self.start.show()
        else:
            self.stop.hide()
            self.start.hide()
        self.game_pages.setCurrentIndex(num)
    # ������ҳ����ť����
    def item_add(self):
        if self.itemnum == 12:
            pass
        else:
            newitemnum = self.itemnum + 1
            w, h = self.num_zoom([290, 80 + 30 * newitemnum])
            self.set_home_filler.setFixedSize(w, h)
            self.itemnum = newitemnum
    def item_reduce(self):
        if self.itemnum == 3:
            pass
        else:
            newitemnum = self.itemnum - 1
            w, h = self.num_zoom([290, 80 + 30 * newitemnum])
            self.set_home_filler.setFixedSize(w, h)
            self.cmdrun("schtasks.exe /delete /tn SAG-wakeup%s /f" % (newitemnum))
            self.itemnum = newitemnum
    # ʱ��-���ڼ��
    def wait_to_time(self):
        while 1:
            if self.event_pause.isSet():
                time.sleep(10)
            else:
                time.sleep(49)
            self.event_pause.wait()
            nowtime = time.localtime()
            for num in range(self.itemnum):
                execute = eval("self.daily%s" % (num)).currentIndex()
                timetuple = eval("self.time%s" % (num)).dateTime().toPyDateTime().timetuple()
                if execute in [nowtime[6], 1]:
                    if (nowtime[3:5] == timetuple[3:5]):
                        self.cg_name = eval("self.cho_config%s" % (num)).currentText()
                        self.event_pause.clear()
                        self.showtext("��ʼִ�ж�ʱ�ƻ���"+self.cg_name)
                        self.run_judge.setChecked(True)
                        break
            time.sleep(10)
    # ����������ֹ
    def wait_to_kill(self):
        while 1:
            self.event_run.wait()
            keyboard.wait("ctrl+/")
            if self.event_run.isSet(): self.pause(2)
class Common(object):
    # �л�����ҳ��
    def change_set_page(self, num):
        self.set_pages.setCurrentIndex(num)
    # ���ָʾ�ı�������¼�ı���ʷ
    def showtext(self, msg, nowtime=None):
        txt = open("resource\main_window\logging.txt", 'a+', encoding='utf-8')
        if nowtime == None:
            nowtime = time.strftime("%H:%M:%S ", time.localtime())
        else:
            txt.write("\n")
        self.output_string.append(nowtime + msg)
        self.output_string.ensureCursorVisible()
        txt.write(nowtime + msg + "\n")
    # ���������Ϣ
    def sendhelp(self, helpstr):
        with open("resource\main_window\home_help.json", 'r', encoding='utf-8') as h:
            self.home_help = json.load(h)
        help_list = self.home_help[helpstr]
        self.output_string.moveCursor(self.output_string.textCursor().End)
        self.output_string.append("")
        for i in help_list:
            self.output_string.append(i)
            self.output_string.ensureCursorVisible()
    def helph(self):
        img = cv2.imread(r"resource\main_window\ui\hxh.png")
        img = cv2.resize(img, (int(self.uizoom * 643), int(self.uizoom * 419)))
        cv2.imshow("", img)
        cv2.moveWindow("", int(self.uizoom * 639), int(self.uizoom * 331))
        cv2.waitKey(0)
    def cmdrun(self,cmdstr):
        run(cmdstr, shell=True)
    def screenOff(self):
        HWND_BROADCAST = 0xffff
        WM_SYSCOMMAND = 0x0112
        SC_MONITORPOWER = 0xF170
        MonitorPowerOff = 2
        SW_SHOW = 5
        windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND,
                                   SC_MONITORPOWER, MonitorPowerOff)

        shell32 = windll.LoadLibrary("shell32.dll")
        shell32.ShellExecuteW(None, 'open', 'rundll32.exe',
                              'USER32', '', SW_SHOW)
    # ui��С��Ӧ
    def ui_zoom(self, x, y, w, h):
        x, y, w, h = int(self.uizoom * x), int(self.uizoom * y), int(self.uizoom * w), int(self.uizoom * h)
        return QtCore.QRect(x, y, w, h)
    # ui��С��Ӧ
    def num_zoom(self, numlist):
        for num in range(len(numlist)): numlist[num] = int(self.uizoom * numlist[num])
        return numlist
    # ������ʽ
    def comboboxstyle(self, f):
        f.setStyleSheet("QAbstractItemView::item {height: 22px;}")
        f.setView(QtWidgets.QListView())
        # font = QtGui.QFont()
        # font.setPointSize(10)  # �����С
        # f.setFont(font)
class Ui_main_window(Main_window_function,Common,Genshin_ui_group,Hxls_ui_group,Maa_ui_group):
    def __init__(self):
        self.event_run = Event()
        self.event_pause = Event()
        self.event_pause.set()
        self.cg_name = ""
        self.continue_config = ""
        self.uizoom = uizoom
        self.workdir = os.getcwd()
    def setupUi(self, main_window):
        # ���崰�ڳ�ʼ��
        self.set_main_window()
        self.config_group()
        self.load_set_home()
        self.button_connect()
        # ����ҳ���ʼ��
        self.genshin_game_tool()
        self.hxls_game_tool()
        self.maa_game_tool()

    # ��ʼ����ҳ
    def set_main_window(self):
        # ���ڳ�ʼ��
        main_window.setObjectName("main_window")
        main_window.resize(int(self.uizoom * 730), int(self.uizoom * 365))
        self._translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(self._translate("main_window", "ɰ�Ǵ���"))
        main_window.setWindowIcon(QtGui.QIcon(":/SGA.ico"))
        main_window.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint |
                                   QtCore.Qt.WindowCloseButtonHint)
        main_window.setFixedSize(main_window.width(), main_window.height())

        # ��ʾͼ��
        self.ico = QtWidgets.QLabel(main_window)
        self.ico.setGeometry(self.ui_zoom(310, 220, 140, 140))
        self.pixmap = QtGui.QPixmap(r"resource\main_window\ui\SGA.png")
        self.ico.setPixmap(self.pixmap)
        self.ico.setScaledContents(True)
        # �����ж�
        self.run_judge = QtWidgets.QCheckBox(main_window)
        self.run_judge.setGeometry(self.ui_zoom(0, 0, 110, 16))
        self.run_judge.setObjectName("run_judge")
        self.run_judge.setChecked(False)
        self.run_judge.stateChanged.connect(self.run)
        self.run_judge.hide()
        # �ı������
        self.output_string = QtWidgets.QTextBrowser(main_window)
        self.output_string.setGeometry(self.ui_zoom(470, 10, 256, 350))
        self.output_string.setObjectName("output_string")
        self.output_string.moveCursor(self.output_string.textCursor().Start)
        notify = "ʹ����֪��\n" \
                 "1������Ŀ�����³�SGA����ѡ���Դ����������ѹ����˸ù��ߣ��������˿�ٱ���������ÿһ�ε�������ʹ��Դ�������ѡ�\n" \
                 "2��SGA��������������ģ�飬���е��������߶�����֤û�з�ŷ��գ��±��ã����Ϸ���\n" \
                 "3��SGA������Ե������άȨ�����ⷴ����SGA���£��������飬���עBվ�˺ţ����Ǻۡ�\n" \
                 "4��ģ�������ڼ䣬�ɵ�������ϡ�ֹͣ����ť�������ϼ���ctrl+/��������ֹ���С�\n" \
                 "5������SGAʹ�÷�������Ŀ���飬�ɲ鿴SGA�ļ����е�˵���ļ�����ϸ˵������SGA���ӽ���İ�����ť�ľ�����ʾ����ο�Bվ�˺ţ����Ǻ� ��SGA���ܺ���ʾ��Ƶ��"
        self.output_string.append(notify)
        self.history_button = QtWidgets.QPushButton(main_window)
        self.history_button.setGeometry(self.ui_zoom(700, 10, 25, 25))
        self.history_button.setObjectName("history_button")
        self.history_button.setIcon(QtGui.QIcon(r"resource\main_window\ui\history.png"))
        self.history_button.setFlat(True)
        # ���öѵ������ʼ��
        self.set_pages = QtWidgets.QStackedWidget(main_window)
        self.set_pages.setGeometry(self.ui_zoom(175, 10, 290, 210))
        self.set_pages.setObjectName("set_pages")
        self.set_home_page = QtWidgets.QWidget()
        self.set_home_page.setObjectName("set_home_page")
        self.set_pages.addWidget(self.set_home_page)
        # ��Ϸ�ѵ������ʼ��
        self.game_pages = QtWidgets.QStackedWidget(main_window)
        self.game_pages.setGeometry(self.ui_zoom(0, 10, 170, 350))
        self.game_pages.setObjectName("game_pages")
        self.game_home_page = QtWidgets.QWidget()
        self.game_home_page.setObjectName("game_home_page")
        self.game_pages.addWidget(self.game_home_page)
        # ��������
        self.home_back = QtWidgets.QLabel(self.game_home_page)
        self.home_back.setGeometry(self.ui_zoom(5, 0, 174, 350))
        self.pixmap = QtGui.QPixmap(r"resource\main_window\ui\back\game_home.png")
        self.home_back.setPixmap(self.pixmap)
        self.home_back.setScaledContents(True)
        # ֹͣ��ť
        self.stop = QtWidgets.QPushButton(main_window)
        self.stop.setGeometry(self.ui_zoom(30, 330, 65, 25))
        self.stop.setObjectName("stop")
        self.stop.setText(self._translate("main_window", "ֹͣ"))
        self.stop.clicked.connect(lambda: self.pause(2))  # ֹͣ��ť���ӹ�����ֹ
        self.stop.hide()
        # ��ʼ��ť
        self.start = QtWidgets.QPushButton(main_window)
        self.start.setGeometry(self.ui_zoom(30, 330, 90, 25))
        self.start.setObjectName("start")
        self.start.setText(self._translate("main_window", "����"))
        self.start.clicked.connect(lambda: self.run_judge.setChecked(True))  # ��ʼ��ť���ӿ�ʼ����
        self.start.hide()
        # ����
        self.helpm = QtWidgets.QPushButton(main_window)
        self.helpm.setGeometry(self.ui_zoom(445, 338, 25, 25))
        self.helpm.setObjectName("helpm")
        self.helpm.setIcon(QtGui.QIcon(r"resource\main_window\ui\support.png"))
        self.helpm.setFlat(True)
        self.helpm.clicked.connect(self.helph)

    def config_group(self):
        # ��ȡ�����ļ��б�
        filedir = "resource\main_window\config"
        self.filelist = []
        for file in os.listdir(filedir):
            name, suffix = os.path.splitext(file)
            if suffix == ".json": self.filelist += [name]
        # ������Ŀ��ǩ
        self.change_config_Label = QtWidgets.QLabel(main_window)
        self.change_config_Label.setGeometry(self.ui_zoom(177, 215, 60, 23))
        self.change_config_Label.setObjectName("change_config_Label")
        self.change_config_Label.setText(self._translate("main_window", "����"))
        # �����л�
        self.change_config = QtWidgets.QComboBox(main_window)
        self.change_config.setGeometry(self.ui_zoom(175, 245, 140, 25))
        self.change_config.setObjectName("change_config")
        self.comboboxstyle(self.change_config)
        self.change_config.addItems(["������½�����"] + self.filelist)
        self.change_config.setCurrentIndex(1)
        # ������������ð�ť
        self.finish = QtWidgets.QPushButton(main_window)
        self.finish.setGeometry(self.ui_zoom(205, 215, 25, 25))
        self.finish.setObjectName("finish")
        self.finish.setIcon(QtGui.QIcon(r"resource\main_window\ui\finish.png"))
        self.finish.setFlat(True)
        self.finish.hide()
        # ���������ð�ť
        self.rename = QtWidgets.QPushButton(main_window)
        self.rename.setGeometry(self.ui_zoom(205, 215, 25, 25))
        self.rename.setObjectName("rename")
        self.rename.setIcon(QtGui.QIcon(r"resource\main_window\ui\rename.png"))
        self.rename.setFlat(True)
        # �������ð�ť
        self.save = QtWidgets.QPushButton(main_window)
        self.save.setGeometry(self.ui_zoom(230, 215, 25, 25))
        self.save.setObjectName("save")
        self.save.setIcon(QtGui.QIcon(r"resource\main_window\ui\save.png"))
        self.save.setFlat(True)
        # �������ð�ť
        self.load_button = QtWidgets.QPushButton(main_window)
        self.load_button.setGeometry(self.ui_zoom(255, 215, 25, 25))
        self.load_button.setObjectName("load_button")
        self.load_button.setIcon(QtGui.QIcon(r"resource\main_window\ui\load.png"))
        self.load_button.setFlat(True)
        # ɾ�����ð�ť
        self.delete_button = QtWidgets.QPushButton(main_window)
        self.delete_button.setGeometry(self.ui_zoom(290, 215, 25, 25))
        self.delete_button.setObjectName("delete_button")
        self.delete_button.setIcon(QtGui.QIcon(r"resource\main_window\ui\delete.png"))
        self.delete_button.setFlat(True)
        # ��Ϸ����ѡ�������б��ǩ
        self.game_box_Label = QtWidgets.QLabel(main_window)
        self.game_box_Label.setGeometry(self.ui_zoom(175, 275, 81, 20))
        self.game_box_Label.setObjectName("game_box_Label")
        self.game_box_Label.setText(self._translate("main_window", "�� Ϸ ѡ ��"))
        # ��ҳ���ð�����ť
        self.helpconfig = QtWidgets.QPushButton(main_window)
        self.helpconfig.setGeometry(self.ui_zoom(276, 273, 40, 25))
        self.helpconfig.setObjectName("helpconfig")
        self.helpconfig.setText(self._translate("main_window", "����"))

        # ��Ϸ����ѡ�������б�
        self.game_box = QtWidgets.QComboBox(main_window)
        self.game_box.setGeometry(self.ui_zoom(175, 300, 140, 25))
        self.game_box.setObjectName("game_box")
        self.comboboxstyle(self.game_box)
        self.gamelist_en = os.listdir("resource")
        self.gamelist_en.remove("main_window")
        self.gamelist_ch = []
        for folder in self.gamelist_en:
            with open("resource\%s\%s_index.json" % (folder, folder), 'r', encoding='utf-8') as tem:
                self.temdir = json.load(tem)
            self.gamelist_ch += [self.temdir["��Ϸ����"]]
        self.game_box.addItems(["δѡ��"]+self.gamelist_ch)
        # ��ҳ��ť
        self.home_button = QtWidgets.QPushButton(main_window)
        self.home_button.setGeometry(self.ui_zoom(246, 330, 70, 25))
        self.home_button.setObjectName("home_button")
        self.home_button.setText(self._translate("main_window", "������ҳ"))

        # ʹ����֪
        self.introduce = QtWidgets.QPushButton(main_window)
        self.introduce.setGeometry(self.ui_zoom(174, 330, 70, 25))
        self.introduce.setObjectName("introduce")
        self.introduce.setText(self._translate("main_window", "ʹ��˵��"))

    def load_set_home(self):
        with open(r"resource\main_window\home_config.json", 'r', encoding='utf-8') as c:
            self.home_config = json.load(c)
        self.itemnum = self.home_config["��Ŀ��"]
        # ���ع���������
        self.set_home_filler = QtWidgets.QWidget(self.set_home_page)
        w, h = self.num_zoom([290, 85 + 30 * self.itemnum])
        self.set_home_filler.setFixedSize(w, h)
        self.set_home_scroll = QtWidgets.QScrollArea(self.set_home_page)
        self.set_home_scroll.setWidget(self.set_home_filler)
        [w, h] = self.num_zoom([290, 200])
        self.set_home_scroll.resize(w, h)
        self.set_home_scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # ��ʱִ����Ŀ����
        self.time_item_Label = QtWidgets.QLabel(self.set_home_filler)
        self.time_item_Label.setGeometry(self.ui_zoom(10, 5, 90, 23))
        self.time_item_Label.setObjectName("time_item_Label")
        self.time_item_Label.setText(self._translate("main_window", "��ʱ��Ŀ����"))
        self.add_button = QtWidgets.QPushButton(self.set_home_filler)
        self.add_button.setGeometry(self.ui_zoom(90, 5, 25, 25))
        self.add_button.setObjectName("add_button")
        self.add_button.setIcon(QtGui.QIcon(r"resource\main_window\ui\add.png"))
        self.add_button.setFlat(True)
        self.reduce_button = QtWidgets.QPushButton(self.set_home_filler)
        self.reduce_button.setGeometry(self.ui_zoom(120, 5, 25, 25))
        self.reduce_button.setObjectName("reduce_button")
        self.reduce_button.setIcon(QtGui.QIcon(r"resource\main_window\ui\reduce.png"))
        self.reduce_button.setFlat(True)
        # �������ð�ť
        self.save_time = QtWidgets.QPushButton(self.set_home_filler)
        self.save_time.setGeometry(self.ui_zoom(180, 5, 40, 25))
        self.save_time.setObjectName("save_time")
        self.save_time.setIcon(QtGui.QIcon(r"resource\main_window\ui\save.png"))
        self.save_time.setFlat(True)
        # ��ҳ�����
        self.help0 = QtWidgets.QPushButton(self.set_home_filler)
        self.help0.setGeometry(self.ui_zoom(225, 5, 40, 25))
        self.help0.setObjectName("help0")
        self.help0.setText(self._translate("main_window", "����"))
        # ����״̬�趨
        self.screen = QtWidgets.QCheckBox(self.set_home_filler)
        self.screen.setGeometry(self.ui_zoom(5, 35, 140, 25))
        self.screen.setObjectName("screen")
        self.screen.setText(self._translate("main_window", "������Ϣ��"))
        self.volume = QtWidgets.QCheckBox(self.set_home_filler)
        self.volume.setGeometry(self.ui_zoom(100, 35, 140, 25))
        self.volume.setObjectName("volume")
        self.volume.setText(self._translate("main_window", "��������"))
        self.screen.setChecked(self.home_config["Ϣ��"])
        self.volume.setChecked(self.home_config["����"])
        # ��ʱ�������ñ�ǩ
        self.week_Label = QtWidgets.QLabel(self.set_home_filler)
        self.week_Label.setGeometry(self.ui_zoom(15, 65, 81, 16))
        self.week_Label.setObjectName("week_Label")
        self.week_Label.setText(self._translate("main_window", "ִ ��"))
        self.time_Label = QtWidgets.QLabel(self.set_home_filler)
        self.time_Label.setGeometry(self.ui_zoom(70, 65, 81, 16))
        self.time_Label.setObjectName("time_Label")
        self.time_Label.setText(self._translate("main_window", "�� ʱ"))
        self.cho_config_Label = QtWidgets.QLabel(self.set_home_filler)
        self.cho_config_Label.setGeometry(self.ui_zoom(150, 65, 81, 16))
        self.cho_config_Label.setObjectName("cho_config_Label")
        self.cho_config_Label.setText(self._translate("main_window", "�� �� �� ��"))
        self.wakeup_Label = QtWidgets.QLabel(self.set_home_filler)
        self.wakeup_Label.setGeometry(self.ui_zoom(235, 65, 81, 16))
        self.wakeup_Label.setObjectName("wakeup_Label")
        self.wakeup_Label.setText(self._translate("main_window", "�� ��"))
        # ����ʱ����Ŀ
        self.timeindex = ["����", "ÿ��", "��һ", "�ܶ�", "����", "����", "����", "����", "����"]
        for num in range(12):
            exec("self.daily%s = QtWidgets.QComboBox(self.set_home_filler)" % (num))
            exec("self.time%s = QtWidgets.QDateTimeEdit(self.set_home_filler)" % (num))
            exec("self.cho_config%s = QtWidgets.QComboBox(self.set_home_filler)" % (num))
            exec("self.wakeup%s = QtWidgets.QCheckBox(self.set_home_filler)" % (num))
            strw, strd = "wakeup%s" % (num), "daily%s" % (num)
            strt, strc = "time%s" % (num), "cho_config%s" % (num)
            fw, fd, ft = eval("self." + strw), eval("self." + strd), eval("self." + strt)
            fc = eval("self." + strc)
            fw.setGeometry(self.ui_zoom(245, 85 + num * 30, 58, 25))
            fw.setObjectName(strw)
            fd.setGeometry(self.ui_zoom(5, 85 + num * 30, 50, 25))
            fd.setObjectName(strd)
            self.comboboxstyle(fd)
            fd.addItems(self.timeindex)
            ft.setGeometry(self.ui_zoom(60, 85 + num * 30, 55, 25))
            ft.setObjectName(strt)
            ft.setDisplayFormat("hh:mm")
            fc.setGeometry(self.ui_zoom(120, 85 + num * 30, 115, 25))
            fc.setObjectName(strt)
            self.comboboxstyle(fc)
            fc.addItems(self.filelist)
            exec("self.daily%s.setCurrentIndex(%s)" % (num, self.home_config["ִ��"][num]))
            exec("self.time%s.setDateTime(datetime.datetime.fromtimestamp(%s))" % (
            num, self.home_config["��ʱ"][num]))
            exec("self.cho_config%s.setCurrentText(\"%s\")" % (num, self.home_config["����"][num]))
            exec("self.wakeup%s.setChecked(%s)" % (num, self.home_config["����"][num]))
        self.change_config.setCurrentText(self.home_config["�����ļ�"])
        # ��ʼ��xml,bat�ļ�
        if self.home_config["����·��"] != self.workdir:
            self.home_config["����·��"] = self.workdir
            with open(r"resource\main_window\home_config.json", 'w', encoding='utf-8') as c:
                json.dump(self.home_config, c, ensure_ascii=False, indent=1)
            vbsdir = r"%s\resource\main_window\batscr" % (self.workdir)
            vbspath = r"%s\resource\main_window\batscr\start-SGA.vbs" % (self.workdir)
            with open(r"resource\main_window\schtasks_index.json", 'r', encoding='utf-8') as m:
                self.xmldir = json.load(m)
            xmllist = self.xmldir["part2"]
            xmllist[32] = "      <Command>" + vbspath + "</Command>\n"
            xmllist[34] = "      <WorkingDirectory>" + vbsdir + "</WorkingDirectory>\n"
            self.xmldir["part2"] = xmllist
            with open(r"resource\main_window\schtasks_index.json", 'w', encoding='utf-8') as x:
                json.dump(self.xmldir, x, ensure_ascii=False, indent=1)
            f = open(r"resource\main_window\batscr\start-SGA.bat", 'r', encoding='utf-8')
            start_SGA_list = f.readlines()
            f.close()
            start_SGA_list[5]="start /d \"%s\" SGA.exe\n"%(self.workdir)
            f = open(r"resource\main_window\batscr\start-SGA.bat", 'w', encoding='utf-8')
            f.writelines(start_SGA_list)
            f.close()
            if os.path.exists(r"resource\maa"):
                f = open(r"resource\maa\batscr\once_sleep.bat", 'r', encoding='ansi')
                batlist = f.readlines()
                f.close()
                batlist[2] = self.workdir[:2]+"\n"
                batlist[3] = "cd %s\n"%(self.workdir)
                f = open(r"resource\maa\batscr\once_sleep.bat", 'w', encoding='ansi')
                f.writelines(batlist)
                f.close()

    # �ű����к���
    def run(self):
        if not self.run_judge.isChecked():
            pass
        else:
            self.event_run.set()
            self.event_pause.clear()
            self.start.hide()
            self.stop.show()
            if self.continue_config == "":
                self.output_string.clear()
                self.ico.setPixmap(QtGui.QPixmap(r"resource\main_window\ui\ico\0.png"))
                self.showtext("", nowtime=time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()))
            else:self.showtext("",nowtime="")
            if self.cg_name != "":
                self.showtext("�������ã�" + self.cg_name)
                with open(r"resource\main_window\config\%s.json" % (self.cg_name), 'r', encoding='utf-8') as r:
                    self.rundir = json.load(r)
                self.cg_name = ""
                gamename = self.rundir["��Ϸ����"]
                exec("self.runlist = self.create_%s_config_runlist()" % (
                    self.gamelist_en[self.gamelist_ch.index(gamename)]))
                try:self.continue_config = self.rundir["����ִ��"]
                except:self.continue_config = ""
            else:
                gamename = self.game_box.currentText()
                exec("self.runlist = self.create_%s_main_runlist()" % (
                    self.gamelist_en[self.gamelist_ch.index(gamename)]))
                self.showtext("���е�ǰ����")
            self.showtext("����ģ�飺"+gamename)
            if self.volume.isChecked(): pyautogui.press('volumemute')
            if self.continue_config == "��ִ��": self.continue_config = ""
            exec("self.thready = Thread_%s(self.runlist)" % (self.gamelist_en[self.gamelist_ch.index(gamename)]))
            self.thready.start()
            self.thready.testsignal.connect(self.showtext)
            self.thready.accomplish.connect(self.pause)
    # ������ֹ
    def pause(self, num):  # 1�������� 2����ֹͣ,��ťֹͣ 3����ֹͣ
        self.event_run.clear()
        self.event_pause.set()
        self.run_judge.setChecked(False)
        if num == 1:
            self.pixmap = QtGui.QPixmap(r"resource\main_window\ui\ico\1.png")
        else:
            self.thready.terminate()
            if num == 2:
                self.showtext("���ֶ�ֹͣ��")
                self.pixmap = QtGui.QPixmap(r"resource\main_window\ui\ico\2.png")
            elif num == 3:
                self.pixmap = QtGui.QPixmap(r"resource\main_window\ui\ico\3.png")
        self.stop.hide()
        self.start.show()
        self.ico.setPixmap(self.pixmap)
        main_window.activateWindow()
        if self.continue_config != "" and num == 1:
            self.cg_name = self.continue_config
            self.run_judge.setChecked(True)
        else:
            if self.volume.isChecked(): pyautogui.press('volumemute')
            if self.screen.isChecked():self.screenOff()
if __name__ == '__main__':
    if windll.shell32.IsUserAnAdmin():
        a=QtWidgets.QApplication(sys.argv)
        main_window=QtWidgets.QWidget()
        b=Ui_main_window()
        b.setupUi(main_window)
        main_window.show()
        sys.exit(a.exec_())
    else:run("mshta vbscript:msgbox(\"��ʹ�ù���ԱȨ������SGA\",64,\"��ʾ\")(window.close)", shell=True)