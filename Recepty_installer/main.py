from pathlib import Path
import shutil
import ctypes, sys
import os, winshell
from win32com.client import Dispatch


def copy_directory_to_C(source_path: str):
    dest_path = Path("C:/Recepty")
    src_path = Path(source_path)

    shutil.copytree(src_path,dest_path,dirs_exist_ok=True)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def make_shortcut_on_desktop():
    desktop = winshell.desktop()
    path = os.path.join(desktop, "Automatyczne wypełnianie recept.lnk")
    target = r"C:\Recepty\runProgram.bat"
    wDir = r"C:\Recepty"
    icon = r"C:\Recepty\src\resources\prescription_icon_with_background.ico"
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()


if __name__ == "__main__":
    print("Trwa instalowanie programu proszę czekać")
    if is_admin():
        try:
            copy_directory_to_C("Recepty")
            make_shortcut_on_desktop()
            print("Program został pomyślnie zainstalowany")
            print("Skrót został utworzony na pulpicie")
            print()
        except:
            print()
            print("\033[91m!!! Błąd przy instalacji, skontatkuj się z deweloperem !!!\033[00m")
        finally:
            input("Klinij enter aby zakończyć")
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)