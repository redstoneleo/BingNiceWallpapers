<<<<<<< HEAD
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ConfigWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(790, 488)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon1px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.storePathEdit = QtWidgets.QLineEdit(self.tab)
        self.storePathEdit.setReadOnly(True)
        self.storePathEdit.setObjectName("storePathEdit")
        self.horizontalLayout_4.addWidget(self.storePathEdit)
        self.browseButton = QtWidgets.QPushButton(self.tab)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout_4.addWidget(self.browseButton)
        self.open = QtWidgets.QPushButton(self.tab)
        self.open.setObjectName("open")
        self.horizontalLayout_4.addWidget(self.open)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.storePathEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.storePathEdit_2.setReadOnly(True)
        self.storePathEdit_2.setObjectName("storePathEdit_2")
        self.horizontalLayout.addWidget(self.storePathEdit_2)
        self.browseButton_2 = QtWidgets.QPushButton(self.tab)
        self.browseButton_2.setObjectName("browseButton_2")
        self.horizontalLayout.addWidget(self.browseButton_2)
        self.open_2 = QtWidgets.QPushButton(self.tab)
        self.open_2.setObjectName("open_2")
        self.horizontalLayout.addWidget(self.open_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.timeEdit = QtWidgets.QTimeEdit(self.tab)
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeEdit.setTime(QtCore.QTime(0, 10, 0))
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout_3.addWidget(self.timeEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.autoRun = QtWidgets.QCheckBox(self.tab)
        self.autoRun.setChecked(True)
        self.autoRun.setObjectName("autoRun")
        self.verticalLayout.addWidget(self.autoRun)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(71, 31, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setDefault(True)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_2.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.okButton.clicked.connect(Dialog.accept)
        self.cancelButton.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "设置 - 必应好壁纸"))
        self.label_4.setText(_translate("Dialog", "壁纸所在位置"))
        self.browseButton.setText(_translate("Dialog", "更改"))
        self.open.setText(_translate("Dialog", "打开"))
        self.label_5.setText(_translate("Dialog", "收藏的壁纸所在位置"))
        self.browseButton_2.setText(_translate("Dialog", "更改"))
        self.open_2.setText(_translate("Dialog", "打开"))
        self.label_3.setText(_translate("Dialog", "自动更换壁纸的时间间隔（时：分：秒）"))
        self.timeEdit.setDisplayFormat(_translate("Dialog", "HH:mm:ss"))
        self.autoRun.setText(_translate("Dialog", "开机启动"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "设置"))
        self.groupBox.setTitle(_translate("Dialog", "本软件"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>必应好壁纸：每一张令人心旷神怡的壁纸后面都有一个真实的故事让你心动，让必应壁纸带你环球旅行吧，换一张壁纸，换一种心情！</p><p>必应好壁纸每天都会为你更新来自微软<a href=\"http://cn.bing.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">必应搜索</span></a>的壁纸！</p><p><span style=\" color:#0000ff;\">鼠标左击本软件的图标可以更换壁纸，右击显示功能菜单，此外本软件也会在指定的时间间隔自动更换壁纸。</span></p><p><span style=\" color:#0000ff;\">如果你有收藏了的壁纸，那么当你把它们放到本软件的壁纸库后，本软件就会使用它们来作为更换的壁纸。</span></p><p><span style=\" color:#0000ff;\">本软件会自动提示你更新到最新版。</span></p><p>将壁纸作为电脑壁纸外的其它用途将可能导致微软找你聊聊，壁纸版权请联系微软或必应。</p><p><span style=\" font-size:10pt;\">软件主页：</span><a href=\"http://mathjoy.lofter.com/post/42208d_7cabcf7\"><span style=\" text-decoration: underline; color:#0000ff;\">http://mathjoy.lofter.com/post/42208d_7cabcf7</span></a></p><p>问题反馈：redstone-cold@163.com</p><p><span style=\" font-size:10pt;\">用户QQ群（iMath软件）：</span><a href=\"http://shang.qq.com/wpa/qunwpa?idkey=2bde057aaff9c01f5b898cc197fe442925c773cc3e3b637fc79eaa1e600d2470\"><span style=\" text-decoration: underline; color:#0000ff;\">272830154</span></a> （点击群号即可加群）</p></body></html>"))
        self.groupBox_3.setTitle(_translate("Dialog", "我"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>你好！我喜欢数学、物理、编程（专Python、PyQt）、国语动画、国语布袋戏、看书、看杂志、音乐、乒乓球、羽毛球。</p><p>如果你在软件方面有比较具有创意的点子，但你又不会写软件，那么不妨和我谈谈，我可能帮你把它给做出来哟！</p><p>欢迎光临我的专页：<a href=\"http://mathjoy.lofter.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">http://mathjoy.lofter.com/</span></a></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "关于"))
        self.okButton.setText(_translate("Dialog", "确认"))
        self.cancelButton.setText(_translate("Dialog", "取消"))


import icon_rc
=======
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfigWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(790, 488)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon1px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.storePathEdit = QtWidgets.QLineEdit(self.tab)
        self.storePathEdit.setReadOnly(True)
        self.storePathEdit.setObjectName("storePathEdit")
        self.horizontalLayout_4.addWidget(self.storePathEdit)
        self.browseButton = QtWidgets.QPushButton(self.tab)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout_4.addWidget(self.browseButton)
        self.open = QtWidgets.QPushButton(self.tab)
        self.open.setObjectName("open")
        self.horizontalLayout_4.addWidget(self.open)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.storePathEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.storePathEdit_2.setReadOnly(True)
        self.storePathEdit_2.setObjectName("storePathEdit_2")
        self.horizontalLayout.addWidget(self.storePathEdit_2)
        self.browseButton_2 = QtWidgets.QPushButton(self.tab)
        self.browseButton_2.setObjectName("browseButton_2")
        self.horizontalLayout.addWidget(self.browseButton_2)
        self.open_2 = QtWidgets.QPushButton(self.tab)
        self.open_2.setObjectName("open_2")
        self.horizontalLayout.addWidget(self.open_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.timeEdit = QtWidgets.QTimeEdit(self.tab)
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.timeEdit.setTime(QtCore.QTime(0, 10, 0))
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout_3.addWidget(self.timeEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.autoRun = QtWidgets.QCheckBox(self.tab)
        self.autoRun.setChecked(True)
        self.autoRun.setObjectName("autoRun")
        self.verticalLayout.addWidget(self.autoRun)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(71, 31, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_2.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.okButton.clicked.connect(Dialog.accept)
        self.cancelButton.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "设置 - 必应好壁纸"))
        self.label_4.setText(_translate("Dialog", "壁纸所在位置"))
        self.browseButton.setText(_translate("Dialog", "更改"))
        self.open.setText(_translate("Dialog", "打开"))
        self.label_5.setText(_translate("Dialog", "收藏的壁纸所在位置"))
        self.browseButton_2.setText(_translate("Dialog", "更改"))
        self.open_2.setText(_translate("Dialog", "打开"))
        self.label_3.setText(_translate("Dialog", "自动更换壁纸的时间间隔（时：分：秒）"))
        self.timeEdit.setDisplayFormat(_translate("Dialog", "HH:mm:ss"))
        self.autoRun.setText(_translate("Dialog", "开机启动"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "设置"))
        self.groupBox.setTitle(_translate("Dialog", "本软件"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>必应好壁纸：每一张令人心旷神怡的壁纸后面都有一个真实的故事让你心动，让必应壁纸带你环球旅行吧，换一张壁纸，换一种心情！</p><p>必应好壁纸每天都会为你更新来自微软<a href=\"http://cn.bing.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">必应搜索</span></a>的壁纸！</p><p><span style=\" color:#0000ff;\">鼠标左击本软件的图标可以更换壁纸，右击显示功能菜单，此外本软件也会在指定的时间间隔自动更换壁纸。</span></p><p><span style=\" color:#0000ff;\">如果你有收藏了的壁纸，那么当你把它们放到本软件的壁纸库后，本软件就会使用它们来作为更换的壁纸。</span></p><p><span style=\" color:#0000ff;\">本软件会自动提示你更新到最新版。</span></p><p>将壁纸作为电脑壁纸外的其它用途将可能导致微软找你聊聊，壁纸版权请联系微软或必应。</p><p><span style=\" font-size:10pt;\">软件主页：</span><a href=\"http://mathjoy.lofter.com/post/42208d_7cabcf7\"><span style=\" text-decoration: underline; color:#0000ff;\">http://mathjoy.lofter.com/post/42208d_7cabcf7</span></a></p><p>问题反馈：redstone-cold@163.com</p><p><span style=\" font-size:10pt;\">用户QQ群（iMath软件）：</span><a href=\"http://shang.qq.com/wpa/qunwpa?idkey=2bde057aaff9c01f5b898cc197fe442925c773cc3e3b637fc79eaa1e600d2470\"><span style=\" text-decoration: underline; color:#0000ff;\">272830154</span></a> （点击群号即可加群）</p></body></html>"))
        self.groupBox_3.setTitle(_translate("Dialog", "我"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>你好！我喜欢数学、物理、编程（专Python、PyQt）、国语动画、国语布袋戏、看书、看杂志、音乐、乒乓球、羽毛球。</p><p>如果你在软件方面有比较具有创意的点子，但你又不会写软件，那么不妨和我谈谈，我可能帮你把它给做出来哟！</p><p>欢迎光临我的专页：<a href=\"http://mathjoy.lofter.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">http://mathjoy.lofter.com/</span></a></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "关于"))
        self.okButton.setText(_translate("Dialog", "确认"))
        self.cancelButton.setText(_translate("Dialog", "取消"))

import icon_rc
>>>>>>> a9d19b1694df63504960fefae1aba696ea5de373
