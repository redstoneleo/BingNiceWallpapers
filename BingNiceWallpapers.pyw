from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *
from ConfigWindow import ConfigWindow
import os
import json
import sys
import shutil
import subprocess
import icon_rc
import autorun
import random

if sys.platform.startswith('win32'):
    import win32con
    import win32gui


def open_containing_folder(folder, files=None):
    'files ---list,files=Nones是为了可以单纯地打开文件夹'
    if sys.platform.startswith('win') and files:
        def launchFileExplorer(path, files):
            from win32com.shell import shell, shellcon

            folder_pidl = shell.SHILCreateFromPath(path, 0)[0]
            desktop = shell.SHGetDesktopFolder()
            shell_folder = desktop.BindToObject(
                folder_pidl, None, shell.IID_IShellFolder)
            name_to_item_mapping = dict(
                [(desktop.GetDisplayNameOf(item, shellcon.SHGDN_FORPARSING | shellcon.SHGDN_INFOLDER), item) for item in
                 shell_folder])

            to_show = []
            for file in files:
                if file in name_to_item_mapping:
                    to_show.append(name_to_item_mapping[file])
            shell.SHOpenFolderAndSelectItems(folder_pidl, to_show, 0)

        launchFileExplorer(folder, files)
    else:
        QDesktopServices.openUrl(QUrl.fromLocalFile(folder))


class BingNiceWallpapers(QSystemTrayIcon):
    # Permissions QFile::​permissions() const

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setIcon(QIcon(':/icons/icon1px.png'))
        self.setToolTip('{}\n\n点击更换壁纸'.format(os.path.basename(os.path.splitext(self.getCurrentWallpaperPath())[0])))
        # 刚启动软件的时候不存在上一张壁纸的记录，不能=None，否则   can't specify None for path argument
        self.readSettings()
        self.lastWallpaper = ''

        self.createContextMenu()
        self.screenHeight = self.getScreenHeight()  # 会用到两次，所以不能去掉

        self.activated.connect(self.iconActivated)
        self.messageClicked.connect(lambda: open_containing_folder(self.likedWallpaperDir))
        self.replySet = set()
        self.reply2imgName = {}
        self.process = QProcess()
        self.process.start("gsettings", ['set', 'org.gnome.desktop.background', 'picture-options', "centered"])
#        self.destroyed.connect(self.closeEvent)

        self.manager = QNetworkAccessManager()

        self.getJson()

        self.timer = QTimer()
        self.timer.timeout.connect(self.changeWallpaper)
        self.timer.start(self.timeoutInterval)

        autorun.add("BingNiceWallpapers", sys.argv[0])

        self.checkUpdate()

    def getJson(self):
        if os.listdir(self.wallpaperDir):
            print(QFileInfo(self.wallpaperDir).lastModified(), QDateTime.currentDateTime())
            imageNum = min(QFileInfo(self.wallpaperDir).lastModified().daysTo(QDateTime.currentDateTime()), QDateTime.currentDateTime().date().day())  # 抉择于上次壁纸更新时间与今日的时间差和本月过了几天
        else:
            imageNum = 24  # QDateTime.currentDateTime().date().day()

        for i in range(imageNum, -1, -1):  # 倒着来是为了最后一次总可以下载到壁纸，以便后面更新今日壁纸
            queryUrl = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx={}&n=1&nc=1421741858945&pid=hp'.format(i)
            print(queryUrl)
            self.prepareReply(queryUrl)

    def prepareReply(self, url):
        reply = self.getReply(url)
        reply.finished.connect(self.readJson)

    def getReply(self, url):
        request = QNetworkRequest(QUrl(url))
        userAgent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
        request.setHeader(QNetworkRequest.UserAgentHeader, userAgent)
        reply = self.manager.get(request)
        self.replySet.add(reply)  # 保存引用，以免reply被gc
        return reply

    def readJson(self):
        reply = self.sender()
        pageSrc = reply.readAll()
        self.replySet.discard(reply)
        content = str(pageSrc.data(), 'utf-8')
        if 'null' in content:  # 链接无效的情况
            print(content)
            return

        elif "copyright" not in content:  # 获取失败，连接chinanet之类的情况
            print('reply.error()----------', reply.errorString())

            if reply.error() == 2:  # Connection closed
                self.prepareReply(reply.url())
            else:  # 随机更换壁纸，120000ms之后重新发出请求
                QTimer.singleShot(120000, lambda: self.prepareReply(reply.url()))
            return

        picInfo = json.loads(content)
        imageUrl = picInfo['images'][0]["url"]
        imageName = picInfo['images'][0]["copyright"].split('(')[0].rstrip()

        reply = self.getReply(imageUrl)
        # reply.readyRead.connect(self.__readyRead)

        reply.finished.connect(self.downloadFinished)

        self.reply2imgName[reply] = imageName


#     def __readyRead(self):
#         reply = self.sender()
# #        print(self.reply2imgName[reply])
#         # self.reply2imgName[reply].write(reply.readAll())

    def downloadFinished(self):

        reply = self.sender()
        print(reply.error(), reply.errorString())
        imgPath = os.path.join(self.wallpaperDir, self.reply2imgName.pop(reply) + '.bmp')
        if not reply.error():
            # If format is 0, QImage will attempt to guess the format by
            # looking at fileName's suffix.   后面这个bmp旨在加快判断速度
            QImage.fromData(reply.readAll()).scaledToHeight(self.screenHeight, Qt.SmoothTransformation).save(imgPath, 'bmp')
            print(imgPath)
            self.setWallpaper(imgPath)
            self.showMessage('今日壁纸已经更新', '快看看你的桌面吧！')
            self.wallpapers = list(map(lambda file: os.path.join(self.wallpaperDir, file), os.listdir(self.wallpaperDir)))
        self.replySet.discard(reply)

    def getScreenHeight(self):
        desktop = QApplication.desktop()
        # 不能用availableGeometry，因为任务栏可能透明，并且关机画面的时候任务栏会消失，如果用availableGeometry的话那么就会缺脚了
        screenHeight = desktop.screenGeometry().height()
        return screenHeight

    def createContextMenu(self):
        trayIconMenu = QMenu()
        self.likeCurrentWallpaperAction = QAction("收藏当前壁纸", self, icon=QIcon(':/icons/emblem-favorite.png'), triggered=self.likeCurrentWallpaper)  # 因为要全局引用，所以加self
        self.lastWallpaperAction = QAction("上一张", self, icon=QIcon(':/icons/edit-undo.png'), triggered=lambda: self.setWallpaper(self.lastWallpaper))
        setAction = QAction("设置", self, icon=QIcon(':/icons/emblem-system.png'), triggered=self.on_options_triggered)
        quitAction = QAction("退出", self, icon=QIcon(':/icons/emblem-unreadable.png'), triggered=qApp.quit)

        trayIconMenu.addAction(self.likeCurrentWallpaperAction)
        trayIconMenu.addAction(self.lastWallpaperAction)
        trayIconMenu.addAction(setAction)
        trayIconMenu.addAction(quitAction)

        self.setContextMenu(trayIconMenu)

    def likeCurrentWallpaper(self):
        if os.path.exists(self.getCurrentWallpaperPath()):  # 还是要检查的，有时候根本没有当前壁纸，一片漆黑
            shutil.copy2(self.getCurrentWallpaperPath(), self.likedWallpaperDir)
            self.showMessage('收藏成功！', '点击本信息打开存放的位置')

    def getCurrentWallpaperPath(self):

        if sys.platform.startswith('win'):
            currentWallpaperPath = win32gui.SystemParametersInfo(Action=win32con.SPI_GETDESKWALLPAPER)
        elif sys.platform.startswith('linux'):
            currentWallpaperPath = subprocess.check_output(["gsettings", 'get', 'org.gnome.desktop.background', 'picture-uri']).decode('utf-8')[8:-2]  # .rstrip('file://')

        # print('currentWallpaperPath--------------',currentWallpaperPath,self.likedWallpaperDir)

        return currentWallpaperPath

    # def openWallpaperFolder(self):
    #     if sys.platform.startswith('win'):
    #         currentWallpaperPath=win32gui.SystemParametersInfo(Action=win32con.SPI_GETDESKWALLPAPER)
    #         if os.path.exists(currentWallpaperPath):
    #             folder,baseName=os.path.split(currentWallpaperPath)
    #             open_containing_folder(folder,[baseName])
    #     elif sys.platform.startswith('linux'):
    #         QDesktopServices.openUrl(QUrl.fromLocalFile(self.wallpaperDir))

    @pyqtSlot()
    def on_options_triggered(self):

        # 如果none→self，那么TypeError: QDialog(QWidget parent=None, Qt.WindowFlags
        # flags=0): argument 1 has unexpected type 'BingNiceWallpapers'
        settingsDialog = ConfigWindow(None, self.settings)

        if settingsDialog.exec() == QDialog.Accepted:
            # 如果目的地存在wallpaperDir同名文件夹会出错
            if not os.path.exists(settingsDialog.storePathEdit.text()):
                self.pathToWallpaperDir = settingsDialog.pathToWallpaperDir
                shutil.move(self.wallpaperDir, self.pathToWallpaperDir)
                self.wallpaperDir = settingsDialog.storePathEdit.text()

            if not os.path.exists(settingsDialog.storePathEdit_2.text()):
                self.pathToLikedWallpaperDir = settingsDialog.pathToLikedWallpaperDir
                shutil.move(self.likedWallpaperDir, self.pathToLikedWallpaperDir)
                self.likedWallpaperDir = settingsDialog.storePathEdit_2.text()

            self.timeoutInterval = settingsDialog.timeEdit.time().minute() * 60 * 1000
            print('self.timeoutInterval------------', self.timeoutInterval)
            self.timer.start(self.timeoutInterval)

            print('exists("test_xxx")---------',
                  autorun.exists("BingNiceWallpapers"), sys.argv[0])
            if settingsDialog.autoRun.isChecked():
                autorun.add("BingNiceWallpapers", sys.argv[0])
            else:
                autorun.remove("BingNiceWallpapers")
            print('exists("test_xxx")---------',
                  autorun.exists("BingNiceWallpapers"))

            self.writeSettings()

    def readSettings(self):
        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, "iMath", "BingNiceWallpapers")
        appDataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        self.pathToWallpaperDir = self.settings.value("pathToWallpaperDir", appDataLocation)  # 当第一次在U盘里运行，关闭后，然后copy到电脑上运行，就会得出invalid路径
        self.pathToLikedWallpaperDir = self.settings.value("pathToLikedWallpaperDir", appDataLocation)  # 当第一次在U盘里运行，关闭后，然后copy到电脑上运行，就会得出invalid路径

        self.timeoutInterval = int(self.settings.value("timeoutInterval", 600000))

        self.wallpaperDir = os.path.join(self.pathToWallpaperDir, '必应好壁纸壁纸库')
        self.likedWallpaperDir = os.path.join(self.pathToLikedWallpaperDir, '收藏的壁纸')
        #print('before--------------', self.wallpaperDir)
        if os.path.exists(self.wallpaperDir) == False:  # 用户可能删除Wallpapers这个文件夹
            self.pathToWallpaperDir = appDataLocation
            self.wallpaperDir = os.path.join(self.pathToWallpaperDir, '必应好壁纸壁纸库')
            #  print('after--------------', self.wallpaperDir)
            try:  # 当pathToWallpaperDir不存在，但当前文件夹下存在'必应好壁纸壁纸库'文件夹时会出错
                os.makedirs(self.wallpaperDir)
            except FileExistsError:
                pass

        if not os.path.exists(self.likedWallpaperDir):
            self.pathToLikedWallpaperDir = appDataLocation
            self.likedWallpaperDir = os.path.join(self.pathToLikedWallpaperDir, '收藏的壁纸')
            try:
                os.makedirs(self.likedWallpaperDir)
            except FileExistsError:
                pass

        self.writeSettings()  # 上面两个路径不存在的话，要立即更新settings，以便于configwindow读取到存在的路径

    def writeSettings(self):
        self.settings.setValue("pathToWallpaperDir", self.pathToWallpaperDir)
        self.settings.setValue("timeoutInterval", self.timeoutInterval)
        self.settings.setValue("pathToLikedWallpaperDir", self.pathToLikedWallpaperDir)

#
#    @pyqtSlot()
#    def closeEvent(self):

#        self.writeSettings()
#
#        print('close???????')

    def iconActivated(self, reason):  # 点击托盘图标随即更换壁纸
        if reason == QSystemTrayIcon.Context:
            currentWallpaperPath = self.getCurrentWallpaperPath()
            isLiked = os.path.exists(os.path.join(self.likedWallpaperDir, os.path.basename(currentWallpaperPath)))
            if isLiked:
                self.likeCurrentWallpaperAction.setText('当前壁纸已经收藏')
            else:
                self.likeCurrentWallpaperAction.setText('收藏当前壁纸')
            self.likeCurrentWallpaperAction.setEnabled(os.path.exists(currentWallpaperPath) and not isLiked)

            self.lastWallpaperAction.setEnabled(os.path.exists(self.lastWallpaper))
        else:
            self.changeWallpaper()

    def changeWallpaper(self):
        try:
            l = random.choice(self.wallpapers)
        except Exception as e:
            print(e)
            self.wallpapers = list(map(lambda file: os.path.join(self.wallpaperDir, file), os.listdir(self.wallpaperDir)))
            l = random.choice(self.wallpapers)
        finally:
            self.wallpapers.remove(l)
            self.setWallpaper(l)

    def setOEMBackground(self, imagePath):  # 待查看win10是否有此特性
        import winreg
        winreg.SetValue(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\Background", winreg.REG_SZ, "0")

    def setWallpaper(self, imagePath):
        self.lastWallpaper = self.getCurrentWallpaperPath()
        if os.path.exists(imagePath):  # 改变存储文件夹，然后再点击上一张的时候，上一张壁纸不存在
            # imagePath=r'E:\360云盘\编程\Python\Project\BingNiceWallpapers\Wallpapers\金色琴弦.png'
            self.setToolTip('{}\n\n点击更换壁纸'.format(os.path.basename(os.path.splitext(imagePath)[0])))
            if sys.platform.startswith('win32'):

                import winreg  # 避免跨平台module出现问题
                winreg.SetValue(winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop\\WallpaperStyle", winreg.REG_SZ, "0")
                # winreg.DeleteKey(key, sub_key)去除快捷方式小箭头，有待实现

                # with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control
                # Panel\\Desktop",access=winreg.KEY_WRITE ) as key:

                # regSettings=QSettings("HKEY_CURRENT_USER\\Control Panel\\Desktop",QSettings.NativeFormat)
                # regSettings.setValue("WallpaperStyle","0")

                try:
                    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, imagePath, win32con.SPIF_UPDATEINIFILE |
                                                  win32con.SPIF_SENDCHANGE | win32con.SPIF_SENDWININICHANGE)  # 1+2 有啊
                except win32gui.error:  # 用户塞了别的非bmp图片

                    newName = os.path.splitext(imagePath)[0] + '.bmp'
                    # If format is 0, QImage will attempt to guess the format
                    # by looking at fileName's suffix.   后面这个bmp旨在加快判断速度
                    QImage(imagePath).scaledToHeight(self.screenHeight, Qt.SmoothTransformation).save(newName, 'bmp')
                    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, newName, win32con.SPIF_UPDATEINIFILE |
                                                  win32con.SPIF_SENDCHANGE | win32con.SPIF_SENDWININICHANGE)  # 1+2 有啊
                    os.remove(imagePath)

            elif sys.platform.startswith('linux'):
                self.process.start("gsettings", ['set', 'org.gnome.desktop.background', 'picture-uri', QUrl.fromLocalFile(imagePath).toString()])

    def checkUpdate(self):
        reply = self.getReply('http://mathjoy.lofter.com/post/42208d_7cabcf7')
        reply.finished.connect(self.checkNewVersion)

    def checkNewVersion(self):
        reply = self.sender()
        pageSrc = reply.readAll()
        content = str(pageSrc.data(), 'utf-8')

        if '必应好壁纸' in content:
            if '2016-10-15' in content:
                print('no NewVersion')

            else:
                print('has NewVersion')
                standardButton = QMessageBox.information(
                    None, '发现新版本', '确认后将前往官网下载最新版 <strong>必应好壁纸</strong>')
                if standardButton == QMessageBox.Ok:
                    QDesktopServices.openUrl(reply.url())

        else:
            print('无法访问主页')
            QTimer.singleShot(120000, self.checkUpdate)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    QApplication.setQuitOnLastWindowClosed(False)

    trayIcon = BingNiceWallpapers()
    trayIcon.show()
    sys.exit(app.exec_())
