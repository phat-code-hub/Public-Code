import os,sys
import platform,locale

from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor,QGuiApplication
from PySide6.QtWidgets import (
                            QListWidgetItem,QMessageBox,QFileDialog,
                            QLineEdit,QApplication,QColorDialog
                        )
#----------------------------------------------------------
from FindName import *
from FindName.constants import MAPPING,THEMES,DEFAULT_CONFIG,OS_PATH,DEFAULT_THEME,REG_KEY
from FindName.languages import ERRORS,REG_WRITE,REG_SAVE
import FindName.ui_main

# ---------------------------
# Ensure Error of main path
# ---------------------------
def resource_path(relative_path):
    """Get absolute path to resource (works for dev and PyInstaller)."""
    if hasattr(sys, "_MEIPASS"):
        # When running as a bundled EXE
        base_path = sys._MEIPASS
    else:
        # When running as a normal Python script
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)
#----------------------------------------------------------
def path_normalized(path0):
    # Convert REAL yen sign → backslash
    path0 = path0.replace("\u00A5", "\\")
    # Normalize slashes
    path0 = path0.replace("/", "\\")
    # Use absolute path
    path0 = os.path.abspath(path0)
    return path0
#----------------------------------------------------------
#              Confirm PC Info
#----------------------------------------------------------
def pc_info():
    # Detect OS
    if platform.system() == "Windows":
        os_name = "WIN"
        lang, _ = locale.getdefaultlocale()
        lang_code = lang or "en_US"
    elif platform.system() == "Darwin":  # macOS
        os_name = "MAC"
        lang_code = os.environ.get("LANG", "")
        lang_code = lang_code.split(".")[0] if "." in lang_code else lang_code

        if not lang_code:
            lang_code, _ = locale.getdefaultlocale()

    elif platform.system() == "Linux":
        os_name = "LINUX"
        lang_code = os.environ.get("LANG", "")
        lang_code = lang_code.split(".")[0] if "." in lang_code else lang_code

        if not lang_code:
            lang_code, _ = locale.getdefaultlocale()
    else:
        os_name = "UNKNOWN"
        lang_code = "en_US"

    return os_name, MAPPING.get(lang_code, "English")
#----------------------------------------------------------
def init_theme():
    # Use consistent cross-platform style
    # High DPI settings
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    # Recommended additional DPI policy
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
#----------------------------------------------------------
def check_registration():
    init_theme()
    config =DEFAULT_CONFIG
    config["OS"],config["Language"] = pc_info()
    config["SearchPath"] = path_normalized(os.path.expanduser(OS_PATH["WIN"]))
    config["Theme"] = DEFAULT_THEME
    # Windows
    if config["OS"] == "WIN":
        config_win(config)
    # MAC
    elif config["OS"] == "MAC":
        config_mac()

    # Linux
    elif config["OS"] == "LINUX":
        config_linux()
    else:
        config = DEFAULT_CONFIG
    DEFAULT_CONFIG.update(config)
#--------------------------------------------------------------------------------------
def config_win(config=None):
    import winreg
    registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    try:
        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        ) as theme_key:
            # AppsUseLightTheme = 0 → Dark mode , 1-> Light mode
            value, _ = winreg.QueryValueEx(theme_key, "AppsUseLightTheme")
            theme = "Dark" if value == 0 else "Light"
    except Exception:
        theme = "Light"   # fallback if theme key missing
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, fr"Software\\{REG_KEY}")
        passed = winreg.QueryValueEx(reg_key, "Passed")[0]
        if passed.lower() == "true":
            config["Language"] = winreg.QueryValueEx(reg_key, "Language")[0]
            config["SearchPath"] = winreg.QueryValueEx(reg_key, "SearchPath")[0]
            window = winreg.QueryValueEx(reg_key, "Window")[0]
            text = winreg.QueryValueEx(reg_key, "Text")[0]
            config["Window"], config["Text"] = config_color(theme, window, text)
            config["Passed"] = True

        winreg.CloseKey(reg_key)

    except FileNotFoundError:
        config["Passed"] = False
#--------------------------------------------------------------------
def config_mac(config=None):
    from pathlib import Path
    import plistlib
    plist_path = Path(OS_PATH["MAC"]).expanduser() / f"{REG_KEY}.plist"
    if  plist_path.exists():
        with open(plist_path, "rb") as f:
                data = plistlib.load(f)
                if data.get("Passed") == "True":
                    config["Language"] = data.get("Language",OS_PATH["MAC"])
                    config["SearchPath"] =path_normalized( data.get("SearchPath",os.path.expanduser("~")))
                    config["Theme"] = DEFAULT_THEME
                    config["Window"],config["Text"] = config_color(
                        DEFAULT_THEME,
                        data.get("Window"),
                        data.get("Text")
                    )
                    config["Passed"] = True
    else:
        config["Passed"] = False
#--------------------------------------------------------------------
def config_linux(config=None):
    import json
    file = Path(OS_PATH["LINUX"]).expanduser() / REG_KEY / "settings.json"
    if file.exists():
        with open(file, "r") as f:
            data = json.load(f)
            if data.get("Passed") == "True":
                config["Language"] = data.get("Language",OS_PATH["LINUX"])
                config["SearchPath"] = path_normalized(data.get("SearchPath",os.path.expanduser("~")))
                config["Theme"] = DEFAULT_THEME
                config["Window"],config["Text"] = config_color(
                        DEFAULT_THEME,
                        data.get("Window"),
                        data.get("Text")
                    )
                config["Passed"] = True
    else:
        config["Passed"] = False
#--------------------------------------------------------------------
def config_color(color_theme,win_colors,text_colors) :
    color_win =(int(n) for n in win_colors.split(','))
    color_text = (int(n) for n in text_colors.split(','))
    if any(n<0 for n in color_win):
        color_win  = THEMES[color_theme]["Window"]
        color_text = THEMES[color_theme]["Text"]
        
    return color_win, color_text
#--------------------------------------------------------------------
#User can define color by many ways
def to_qcolor(value):
    if isinstance(value, QColor):
        return value
    if isinstance(value, str):
        return QColor(value)
    if isinstance(value, (tuple, list)):
        return QColor(*value)
    raise ValueError(f"Unsupported color format: {value}")
#--------------------------------------------------------------------------------------
def apply_custom_colors(palette: QPalette, custom: dict):
    if "Window" in custom:
        palette.setColor(QPalette.Window, to_qcolor(custom["Window"]))
        palette.setColor(QPalette.Base, to_qcolor(custom["Window"]))

    if "Text" in custom:
        palette.setColor(QPalette.Text, to_qcolor(custom["Text"]))
        palette.setColor(QPalette.WindowText, to_qcolor(custom["Text"]))
        palette.setColor(QPalette.ButtonText, to_qcolor(custom["Text"]))
#--------------------------------------------------------------------------------------
def apply_theme(self, theme_name):
    if theme_name not in THEMES:
        return
    self.current_theme = theme_name
    #Save to custom_colors dict
    self.custom_colors["Window"] = THEMES[theme_name]["Window"]
    self.custom_colors["Text"] = THEMES[theme_name]["Text"]
    set_theme(QApplication.instance(), theme_name)
#--------------------------------------------------------------------------------------
def set_theme(app: QApplication, app_theme: str, customcolor: dict | None = None):
    app.setStyle("Fusion")

    # 1. Always create a base palette
    palette = create_pallet(app_theme)

    # 2. Apply user overrides (if any)
    if customcolor:
        apply_custom_colors(palette, customcolor)

    # 3. Apply palette to app
    app.setPalette(palette)
#--------------------------------------------------------------------------------------
def create_pallet(theme :str = "Light")->QPalette:
    colors = THEMES[theme]
    pallet = QPalette()
    pallet.setColor(QPalette.Window, to_qcolor(colors["Window"]))
    pallet.setColor(QPalette.WindowText, to_qcolor(colors["WindowText"]))
    pallet.setColor(QPalette.Base, to_qcolor(colors["Base"]))
    pallet.setColor(QPalette.AlternateBase, to_qcolor(colors["AltBase"]))
    pallet.setColor(QPalette.Text, to_qcolor(colors["Text"]))
    pallet.setColor(QPalette.Button, to_qcolor(colors["Button"]))
    pallet.setColor(QPalette.ButtonText, to_qcolor(colors["ButtonText"]))
    pallet.setColor(QPalette.Highlight, to_qcolor(colors["Highlight"]))
    pallet.setColor(QPalette.HighlightedText, to_qcolor(colors["HighlightText"]))
    pallet.setColor(QPalette.ToolTipBase, to_qcolor(colors["ToolTipBase"]))
    pallet.setColor(QPalette.ToolTipText, to_qcolor(colors["ToolTipText"]))
    pallet.setColor(QPalette.PlaceholderText, to_qcolor(colors["PlaceholderText"]))

    pallet.setColor(QPalette.Disabled, QPalette.Text, to_qcolor(colors["DisabledText"]))
    pallet.setColor(QPalette.Disabled, QPalette.ButtonText, to_qcolor(colors["DisabledText"]))

    return pallet
#--------------------------------------------------------------------------------------
# User's background color
#--------------------------------------------------------------------------------------
def choose_custom_background(self):
    color = QColorDialog.getColor(
        parent=QApplication.activeWindow()
    )
    if not color.isValid():
        return
    self.custom_colors["Window"] = (color.red(), color.green(), color.blue())
    set_theme(QApplication.instance(), self.current_theme, self.custom_colors)
#--------------------------------------------------------------------------------------
# User's text color
#--------------------------------------------------------------------------------------
def choose_custom_text(self):
    color = QColorDialog.getColor(
        parent=QApplication.activeWindow()
    )
    if not color.isValid():
        return
    self.custom_colors["Text"] = (color.red(), color.green(), color.blue())
    set_theme(QApplication.instance(), self.current_theme, self.custom_colors)

#--------------------------------------------------------------------------------------
# Reset color
#--------------------------------------------------------------------------------------
def reset_custom_colors(self):
    self.custom_colors.clear()
    set_theme(QApplication.instance(), self.current_theme)
#--------------------------------------------------------------------------------------
def toggle_password_visibility(self,state):
    if state == Qt.Checked:
        self.password_input.setEchoMode(QLineEdit.Normal)
    else:
        self.password_input.setEchoMode(QLineEdit.Password)
#--------------------------------------------------------------------------------------
def check_license(self,password):
    import re
    # if re.match(r"^0\w*",password):
    if "0" in password:
        DEFAULT_CONFIG["Passed"] = True
        create_registry(self)
        self.close()
        self =FindName.ui_main.FileSearchHandler()
        self.show()
    else:
        QMessageBox.critical(None, ERRORS[DEFAULT_CONFIG["Language"]]["Title"], ERRORS[DEFAULT_CONFIG["Language"]]["Message"])
        self.close()
#--------------------------------------------------------------------------------------
def check_installed_app(self):
    hasOffice = hasCAD = False
    for path in Loffice:
        if os.path.exists(path):
            hasOffice = True
            break
    for path in FreeCADPath:
        if os.path.exists(path):
            hasCAD = True
            if  path not in sys.path:
                sys.path.append(path)
            break
    return hasOffice, hasCAD
#--------------------------------------------------------------------------------------
def create_registry(self):
    # Windows
    if DEFAULT_CONFIG["OS"] == "WIN":
        import winreg
        try:
            reg_key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, f"Software\\{REG_KEY}")
            winreg.SetValueEx(reg_key, "Language", 0, winreg.REG_SZ,DEFAULT_CONFIG["Language"])
            winreg.SetValueEx(reg_key, "SearchPath", 0, winreg.REG_SZ, os.path.expanduser("~")+"\\Documents")
            winreg.SetValueEx(reg_key, "Passed", 0, winreg.REG_SZ, str(DEFAULT_CONFIG["Passed"]))
            winreg.CloseKey(reg_key)
        except Exception as e:
            print(REG_WRITE[DEFAULT_CONFIG["Language"]]["WIN"],e)
    # MAC
    elif DEFAULT_CONFIG["OS"] == "MAC":
        # macOS: use plist
        from pathlib import Path
        import plistlib
        plist_path = Path("~/Library/Preferences").expanduser() / f"{REG_KEY.lower()}.plist"
        try:
            with open(plist_path, "wb") as f:
                # plistlib.dump(data, f)
                plistlib.dump(DEFAULT_CONFIG, f)
        except Exception as e:
            print(REG_WRITE[DEFAULT_CONFIG["Language"]]["MAC"],e)
    # Linux
    else:
        import json
        config_dir = Path(OS_PATH["LINUX"]).expanduser() / REG_KEY
        config_dir.mkdir(parents=True, exist_ok=True)
        
        file = Path(OS_PATH["LINUX"]).expanduser() / f"{REG_KEY} / settings.json"
        try:
            with file.open("w", encoding="utf-8") as f:
                json.dump(DEFAULT_CONFIG, f)
        except Exception as e:
                print(REG_WRITE[DEFAULT_CONFIG["Language"]]["LINUX"],e)
#----------------------------------------------------------------   
def saved_to_registry(self):
        # Windows
        if DEFAULT_CONFIG["OS"] == "WIN":
            import winreg
            try:
                reg_key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, f"Software\\{REG_KEY}")
                winreg.SetValueEx(reg_key, "Language", 0, winreg.REG_SZ, self.language)
                winreg.SetValueEx(reg_key, "SearchPath", 0, winreg.REG_SZ, self.search_path)
                winreg.SetValueEx(reg_key, "Passed", 0, winreg.REG_SZ, "True")
                winreg.CloseKey(reg_key)
            except Exception as e:
                print(REG_SAVE[self.language]["WIN"],e)
        # MAC
        elif DEFAULT_CONFIG["OS"] == "MAC":
            from pathlib import Path
            import plistlib
            plist_path = Path("~/Library/Preferences").expanduser() / f"{REG_KEY}.plist"
            try:
                with open(plist_path, "wb") as f:
                    plistlib.dump(DEFAULT_CONFIG, f)
            except Exception as e:
                print(REG_SAVE[self.language]["MAC"],e)
        # MAC
        # Linux
        else:
            import json
            file = Path(OS_PATH["LINUX"]).expanduser() / f"{REG_KEY} / settings.json"
            try:
                with file.open("w", encoding="utf-8") as f:
                    json.dump(DEFAULT_CONFIG, f)
            except Exception as e:
                print(REG_SAVE[self.language]["LINUX"],e)
#----------------------------------------------------------------