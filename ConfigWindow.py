<<<<<<< HEAD
# -*- coding: utf-8 -*-

"""
Module implementing ConfigWindow.
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog, QFileDialog
import os
import sys
import autorun
from Ui_ConfigWindow import Ui_Dialog


class ConfigWindow(QDialog, Ui_Dialog):

    """
    Class documentation goes here.
    """

    def __init__(self, parent=None, settings=None):
        """
        Constructor

        @param parent reference to the parent widget (QWidget)
        """
        super().__init__(parent)
        self.setupUi(self)

        self.autoRun.setChecked(autorun.exists('BingNiceWallpapers'))
        self.storePathEdit.setText(
            os.path.join(settings.value("pathToWallpaperDir"), '必应好壁纸壁纸库'))
        self.storePathEdit_2.setText(
            os.path.join(settings.value("pathToLikedWallpaperDir"), '收藏的必应壁纸'))

        self.timeEdit.setTime(QTime.fromMSecsSinceStartOfDay(int(settings.value("timeoutInterval"))))

    @pyqtSlot()
    def on_browseButton_clicked(self):

        pathToWallpaperDir = os.path.normpath(
            QFileDialog.getExistingDirectory(self))

        print('pathToWallpaperDir--------', pathToWallpaperDir)  # 取消后 返回  点 .   bugggggg

        # 如果取消QFileDialog.getExistingDirectory的话，那么得到的就是  ‘’
        # 如果目的地存在wallpaperDir同名文件夹会出错
        if pathToWallpaperDir != '':
            self.storePathEdit.setText(
                os.path.join(pathToWallpaperDir, '必应好壁纸壁纸库'))
            self.pathToWallpaperDir = pathToWallpaperDir

        # else:
        #     self.tipsLabel.setText(
        #         '{}   已经存在，请选择别的位置'.format(pathToWallpaperDir))

    @pyqtSlot()
    def on_browseButton_2_clicked(self):

        pathToLikedWallpaperDir = os.path.normpath(
            QFileDialog.getExistingDirectory(self))

        # 如果取消QFileDialog.getExistingDirectory的话，那么得到的就是  ‘’    and if
        if pathToLikedWallpaperDir != '':
            self.storePathEdit_2.setText(
                os.path.join(pathToLikedWallpaperDir, '收藏的必应壁纸'))
            self.pathToLikedWallpaperDir = pathToLikedWallpaperDir

        # else:
        #     self.tipsLabel.setText(
        #         '{}   已经存在，请选择别的位置'.format(pathToWallpaperDir))

    @pyqtSlot()
    def on_open_clicked(self):
        # 壁纸库
        if os.path.exists(self.storePathEdit.text()):  # 更改路径后，新路径还未存在
            QDesktopServices.openUrl(QUrl.fromLocalFile(self.storePathEdit.text()))

    @pyqtSlot()
    def on_open_2_clicked(self):
        # 收藏的必应壁纸
        if os.path.exists(self.storePathEdit_2.text()):
            QDesktopServices.openUrl(QUrl.fromLocalFile(self.storePathEdit_2.text()))

    @pyqtSlot()
    def closeEvent(self, event):
        pass
    # @pyqtSlot(bool)
    # def on_autoRun_clicked(self, checked):
    #     regSettings = QSettings(
    #         r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run", QSettings.NativeFormat)
#        print('on_autoRun_clicked-------', regSettings.allKeys())
#        if checked:
#            regSettings.setValue("BingNiceWallpapers",sys.executable)
#        else:
#            regSettings.remove("BingNiceWallpapers")
=======
# -*- coding: utf-8 -*-

"""
Module implementing ConfigWindow.
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog, QFileDialog
import os
import sys
import autorun
from Ui_ConfigWindow import Ui_Dialog


class ConfigWindow(QDialog, Ui_Dialog):

    """
    Class documentation goes here.
    """

    def __init__(self, parent=None, settings=None):
        """
        Constructor

        @param parent reference to the parent widget (QWidget)
        """
        super().__init__(parent)
        self.setupUi(self)

        self.autoRun.setChecked(autorun.exists('BingNiceWallpapers'))
        self.storePathEdit.setText(
            os.path.join(settings.value("pathToWallpaperDir"), '必应好壁纸壁纸库'))
        self.storePathEdit_2.setText(
            os.path.join(settings.value("pathToLikedWallpaperDir"), '收藏的必应壁纸'))

        self.timeEdit.setTime(QTime.fromMSecsSinceStartOfDay(int(settings.value("timeoutInterval"))))

    @pyqtSlot()
    def on_browseButton_clicked(self):

        pathToWallpaperDir = os.path.normpath(
            QFileDialog.getExistingDirectory(self))

        print('pathToWallpaperDir--------', pathToWallpaperDir)  # 取消后 返回  点 .   bugggggg

        # 如果取消QFileDialog.getExistingDirectory的话，那么得到的就是  ‘’
        # 如果目的地存在wallpaperDir同名文件夹会出错
        if pathToWallpaperDir != '':
            self.storePathEdit.setText(
                os.path.join(pathToWallpaperDir, '必应好壁纸壁纸库'))
            self.pathToWallpaperDir = pathToWallpaperDir

        # else:
        #     self.tipsLabel.setText(
        #         '{}   已经存在，请选择别的位置'.format(pathToWallpaperDir))

    @pyqtSlot()
    def on_browseButton_2_clicked(self):

        pathToLikedWallpaperDir = os.path.normpath(
            QFileDialog.getExistingDirectory(self))

        # 如果取消QFileDialog.getExistingDirectory的话，那么得到的就是  ‘’    and if
        if pathToLikedWallpaperDir != '':
            self.storePathEdit_2.setText(
                os.path.join(pathToLikedWallpaperDir, '收藏的必应壁纸'))
            self.pathToLikedWallpaperDir = pathToLikedWallpaperDir

        # else:
        #     self.tipsLabel.setText(
        #         '{}   已经存在，请选择别的位置'.format(pathToWallpaperDir))

    @pyqtSlot()
    def on_open_clicked(self):
        # 壁纸库
        if os.path.exists(self.storePathEdit.text()):  # 更改路径后，新路径还未存在
            QDesktopServices.openUrl(QUrl.fromLocalFile(self.storePathEdit.text()))

    @pyqtSlot()
    def on_open_2_clicked(self):
        # 收藏的必应壁纸
        if os.path.exists(self.storePathEdit_2.text()):
            QDesktopServices.openUrl(QUrl.fromLocalFile(self.storePathEdit_2.text()))

    @pyqtSlot()
    def closeEvent(self, event):
        pass
    # @pyqtSlot(bool)
    # def on_autoRun_clicked(self, checked):
    #     regSettings = QSettings(
    #         r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run", QSettings.NativeFormat)
#        print('on_autoRun_clicked-------', regSettings.allKeys())
#        if checked:
#            regSettings.setValue("BingNiceWallpapers",sys.executable)
#        else:
#            regSettings.remove("BingNiceWallpapers")
>>>>>>> a9d19b1694df63504960fefae1aba696ea5de373
