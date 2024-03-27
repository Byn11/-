# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import connection

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "ゆうちょ内為ツールシステム（IBM）"
        description = "PyDracula APP - Theme with colors based on Dracula for Python."
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_new1.clicked.connect(self.buttonClick)
        #widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.pushButton.clicked.connect(self.buttonClick)
        widgets.pushButton_2.clicked.connect(self.buttonClick)
        widgets.pushButton_3.clicked.connect(self.buttonClick)
        widgets.pushButton_5.clicked.connect(self.buttonClick)
        widgets.pushButton_6.clicked.connect(self.buttonClick)
        widgets.pushButton_7.clicked.connect(self.buttonClick)
        widgets.pushButton_8.clicked.connect(self.buttonClick)
        widgets.pushButton_9.clicked.connect(self.buttonClick)
        widgets.pushButton_10.clicked.connect(self.buttonClick)
        widgets.checkBox_2.clicked.connect(self.buttonClick)
        widgets.checkBox_9.clicked.connect(self.buttonClick)
        widgets.lineEdit_2.textChanged.connect(self.text_change)
        widgets.lineEdit_3.textChanged.connect(self.text_change)
        widgets.lineEdit_4.textChanged.connect(self.text_change)
        widgets.lineEdit_5.textChanged.connect(self.text_change)
        widgets.pushButton_4.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)



        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "Modern_GUI_PyDracula_PySide6_or_PyQt6-master/themes/py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def admit_generate(self):
        if widgets.lineEdit_3.text()!='' and widgets.lineEdit_2.text()!='' and widgets.lineEdit_4.text()!='':
            flag=True
        else:
            flag=False

        if flag:
            widgets.pushButton_4.show()
        else:
            widgets.pushButton_4.hide()
    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            print(btn.styleSheet())
            #btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.keyword)
            UIFunctions.resetStyle(self, btnName)
            #btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))


        if btnName == "btn_new1":
            widgets.stackedWidget.setCurrentWidget(widgets.print)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE


            widgets.pushButton_4.hide()
            widgets.lineEdit_4.hide()
            widgets.pushButton_5.hide()
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            print(btn.styleSheet())
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
        
        if btnName=="pushButton_3":
                directory1 = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "./")  # 起始路径
                widgets.lineEdit_3.setText(directory1)
                self.admit_generate()

        if btnName=="pushButton_6":
                directory1 = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "./")  # 起始路径
                widgets.lineEdit_5.setText(directory1)  

        if btnName=="pushButton_8":
                directory1 = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "./")  # 起始路径
                widgets.lineEdit_7.setText(directory1)

        if btnName=="pushButton_9":
                directory1 = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "./")  # 起始路径
                widgets.lineEdit_6.setText(directory1)  
        if btnName=="pushButton_7":
            msg=connection.printconnect(widgets.lineEdit_5.text())
            widgets.plainTextEdit_2. setPlainText('\n'.join(msg))

        if btnName=="pushButton_10":
            msg=connection.gen_keywordfile(widgets.lineEdit_6.text(),widgets.lineEdit_7.text())
            widgets.plainTextEdit_4.setPlainText('\n'.join(msg))

        if btnName == "pushButton_2":
            directory1 = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "./")  # 起始路径
            widgets.lineEdit_2.setText(directory1)
            isexist=connection.showfile(directory1)
            if not isexist['GDPS']:
                widgets.checkBox_4.hide()
            else:
                widgets.checkBox_4.show()
            if not isexist['MCDS']:
                widgets.checkBox_3.hide()
            else:
                widgets.checkBox_3.show()
            if not isexist['CGFAIL']:
                widgets.checkBox_5.hide()
            else:
                widgets.checkBox_5.show()
            if not isexist['DSPL']:
                widgets.checkBox_6.hide()
            else:
                widgets.checkBox_6.show()
            if not isexist['SMSSGCHK']:
                widgets.checkBox_7.hide()
            else:
                widgets.checkBox_7.show()
            if not isexist['STORAGE']:
                widgets.checkBox_8.hide()
            else:
                widgets.checkBox_8.show()
            if not isexist['RMFSUM']:
                widgets.checkBox_9.hide()
            else:
                widgets.checkBox_9.show()
            if sum(list(isexist.values()))<=1:
                widgets.checkBox_2.hide()
            else:
                widgets.checkBox_2.show()

            self.admit_generate()
            
        if btnName=='checkBox_2':
            if widgets.checkBox_2.isChecked():
                widgets.checkBox_4.setCheckState(Qt.Checked)
                widgets.checkBox_3.setCheckState(Qt.Checked)
                widgets.checkBox_5.setCheckState(Qt.Checked)
                widgets.checkBox_6.setCheckState(Qt.Checked)
                widgets.checkBox_7.setCheckState(Qt.Checked)
                widgets.checkBox_8.setCheckState(Qt.Checked)
                widgets.checkBox_9.setCheckState(Qt.Checked)
                widgets.lineEdit_4.show()
                widgets.pushButton_5.show()
            else:
                widgets.checkBox_4.setCheckState(Qt.Unchecked)
                widgets.checkBox_3.setCheckState(Qt.Unchecked)
                widgets.checkBox_5.setCheckState(Qt.Unchecked)
                widgets.checkBox_6.setCheckState(Qt.Unchecked)
                widgets.checkBox_7.setCheckState(Qt.Unchecked)
                widgets.checkBox_8.setCheckState(Qt.Unchecked)
                widgets.checkBox_9.setCheckState(Qt.Unchecked)
                widgets.lineEdit_4.hide()
                widgets.pushButton_5.hide()
        if btnName=='pushButton_5':
            directory1,_ = QFileDialog.getOpenFileName(self,
                                                      "选取文件",
                                                      "./")  # 起始路径
            widgets.lineEdit_4.setText(directory1)
        self.admit_generate()

        if btnName=='checkBox_9':
            if widgets.checkBox_9.isChecked():
                widgets.lineEdit_4.show()
                widgets.pushButton_5.show()
            else:
                widgets.lineEdit_4.hide()
                widgets.pushButton_5.hide()
        if btnName == "btn_save":
            print("Save BTN clicked!")

        if btnName=='pushButton_4':
            gener_list={}
            gener_list['GDPS']=widgets.checkBox_4.isChecked()
            gener_list['MCDS']=widgets.checkBox_3.isChecked()
            gener_list['CGFAIL']=widgets.checkBox_5.isChecked()
            gener_list['DSPL']=widgets.checkBox_6.isChecked()
            gener_list['SMSSGCHK']=widgets.checkBox_7.isChecked()
            gener_list['STORAGE']=widgets.checkBox_8.isChecked()
            gener_list['RMFSUM']=widgets.checkBox_9.isChecked()
            print(gener_list)
            msg=connection.generator(gener_list,widgets.lineEdit_2.text(),widgets.lineEdit_3.text(),widgets.lineEdit_4.text())
            print(msg)
            widgets.label_4.setText('\n'.join(msg))
        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)
        #print('resizeEvent')

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
    
    def text_change(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName=='lineEdit_4' or btnName=='lineEdit_2' or btnName=='lineEdit_3':
            self.admit_generate()
        if btnName=='lineEdit_5':
            file_list=connection.browser(widgets.lineEdit_5.text())
            print(file_list)
            widgets.plainTextEdit_3.setPlainText(file_list)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
