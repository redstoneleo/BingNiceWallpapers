import os
import sys


if sys.platform == 'win32':
    import winreg
    _registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)

    def get_runonce():
        return winreg.OpenKey(_registry,
                              r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0,
                              winreg.KEY_ALL_ACCESS)

    def add(name, application):
        """add a new autostart entry"""
        key = get_runonce()
        try:
            winreg.SetValueEx(key, name, 0, winreg.REG_SZ, application)
        except WindowsError as e:
            print(e)
        winreg.CloseKey(key)

    def exists(name):
        """check if an autostart entry exists"""
        key = get_runonce()
        exists = True
        try:
            winreg.QueryValueEx(key, name)
        except WindowsError:
            exists = False
        winreg.CloseKey(key)
        return exists

    def remove(name):
        """delete an autostart entry"""
        if exists("BingNiceWallpapers"):
            key = get_runonce()
            winreg.DeleteValue(key, name)
            winreg.CloseKey(key)
else:
    _xdg_config_home = os.environ.get("XDG_CONFIG_HOME", "~/.config")
    _xdg_user_autostart = os.path.join(os.path.expanduser(_xdg_config_home),
                                       "autostart")
    if not os.path.exists(_xdg_user_autostart):
        os.makedirs(_xdg_user_autostart)

    def getfilename(name):
        """get the filename of an autostart (.desktop) file"""
        return os.path.join(_xdg_user_autostart, name + ".desktop")

    def add(name, application):
        """add a new autostart entry"""
        desktop_entry = "[Desktop Entry]\n"\
            "Name=%s\n"\
            "Exec=%s\n"\
            "Type=Application\n"\
            "Terminal=false\n" % (name, application)
        with open(getfilename(name), "w") as f:
            f.write(desktop_entry)

    def exists(name):
        """check if an autostart entry exists"""
        return os.path.exists(getfilename(name))

    def remove(name):
        """delete an autostart entry"""
        if exists("BingNiceWallpapers"):
            os.unlink(getfilename(name))


def test():
    assert not exists("test_xxx")
    try:
        add("test_xxx", "test")
        assert exists("test_xxx")
    finally:
        remove("test_xxx")
    assert not exists("test_xxx")

if __name__ == "__main__":
    test()
