APP_NAME = "FindName"
VERSION = "1.0.0"
YEAR = 2025
AUTHOR = {
    "English":"UEDA HATSURU",
    "Japanese":"植田発",
    "Vietnamese":"UEDA HATSURU"
}
ICON_FILE = "app.png"
GUIDE_FILE = "Guide.txt"
GUIDE_TITLE ={
    "English":"How to Use",
    "Japanese":"使い方について",
    "Vietnamese":"Về cách sử dụng"
}
COMPANY = {
    "English":"Yamazaki Engineering Ltd Co.",
    "Japanese":"山崎エンジニアリング株式会社",
    "Vietnamese":"Công ty CP Kỹ thuật Yamazaki"
}
OS_PATH ={
    "WIN" :"~/Documents",
    "MAC":"~/Library/Preferences",
    "LINUX":"~/.config"
}
DEFAULT_CONFIG = {
    "OS": "WIN",
    "Language": "English",
    "SearchPath": "~/Documents",
    "Theme": "Light",
    "Window":(-1,-1,-1),
    "Text": (-1,-1,-1),
    "Passed": False
}
DEFAULT_THEME = "Light"
REG_KEY = "FileSearch"
THEMES = {
    "Light": {
        "Window":            (245, 245, 245),
        "WindowText":        (0, 0, 0),
        "Base":              (245, 245, 245),
        "AltBase":           (235, 235, 235),
        "Text":              (0, 0, 0),
        "Button":            (245, 245, 245),
        "ButtonText":        (0, 0, 0),
        "Highlight":         (76, 163, 224),
        "HighlightText":     (255, 255, 255),
        "ToolTipBase":       (255, 255, 220),
        "ToolTipText":       (0, 0, 0),
        "PlaceholderText":   (120, 120, 120),
        "DisabledText":      (150, 150, 150),
    },

    "Dark": {
        "Window":            (30, 30, 30),
        "WindowText":        (255, 255, 255),
        "Base":              (30, 30, 30),
        "AltBase":           (35, 35, 35),
        "Text":              (255, 255, 255),
        "Button":            (45, 45, 45),
        "ButtonText":        (255, 255, 255),
        "Highlight":         (42, 130, 218),
        "HighlightText":     (0, 0, 0),
        "ToolTipBase":       (50, 50, 50),
        "ToolTipText":       (255, 255, 255),
        "PlaceholderText":   (160, 160, 160),
        "DisabledText":      (110, 110, 110),
    },

    "HighContrast": {
        "Window":            (0, 0, 0),
        "WindowText":        (255, 255, 0),
        "Base":              (0, 0, 0),
        "AltBase":           (30, 30, 30),
        "Text":              (255, 255, 0),
        "Button":            (0, 0, 0),
        "ButtonText":        (255, 255, 0),
        "Highlight":         (255, 255, 0),
        "HighlightText":     (0, 0, 0),
        "ToolTipBase":       (255, 255, 0),
        "ToolTipText":       (0, 0, 0),
        "PlaceholderText":   (200, 200, 200),
        "DisabledText":      (180, 180, 180),
    },

    "LowContrast": {
        "Window":            (240, 240, 240),
        "WindowText":        (80, 80, 80),
        "Base":              (240, 240, 240), 
        "AltBase":           (230, 230, 230),
        "Text":              (80, 80, 80),
        "Button":            (235, 235, 235),
        "ButtonText":        (80, 80, 80),
        "Highlight":         (180, 180, 180),
        "HighlightText":     (0, 0, 0),
        "ToolTipBase":       (255, 255, 240),
        "ToolTipText":       (80, 80, 80),
        "PlaceholderText":   (160, 160, 160),
        "DisabledText":      (170, 170, 170),
    },
}

MAPPING = {
    "en_US": "English",
    "en-EN": "English",
    "ja_JP": "Japanese",
    "vi_VN": "Vietnamese",
}
# Search Option
LOGICS ={
    "OR":0,
    "AND":1,
    "NOT":2
}
#File Extensions
EXTENSIONS ={
    0: [],
    1: [".vwx",".vwxp",".vwxw",".sta"],
    2: [".vwx",".sta",".mcd",".dwg", ".step", ".stp","dxf",
                ".CAT",".iges", ".igs", ".sldprt", ".sldasm", ".prt"],
    3: [".xls",".xlsx",".xlsm",".xlsb",".xltx",".xltm",".xlt",".csv",".numbers"],
    4: [".pdf"],
    5: [".dxf"],
    6: [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg","png"],
    7: [".mp4", ".avi",".flv", ".mkv", ".mov", ".wmv"],
    8: [ ".doc", ".docx", ".odt", ".rtf",".dot","docm","dotx"],
    9: [".txt", ".ini",".log" ,".csv" ,".md",".yml",".yaml",".json"],
    10: [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    11: [".py", ".java", ".js", ".c",".cpp",".php", ".rb", ".html", ".htm", ".css", ".cs",".frx","frm","bas","cls","vba"],
    12: [".exe", ".msi", ".bat", ".cmd",".pkg",".sh", ".app", ".jar",  ".pyw", ".pyc"],
    }
# Previewable Classified type
VIEW_EXT = {
    "text":[3,4,6,8,9],
    "cad" :[1,2,5],
    "prog":[11],
    "media":[7,10],
    "other":[12]
}
#Event Handlers States for media files
STATES ={
    "None":0, #init / no file/ non media file selected state
    "Selected":1, # media file selected
    "Playing":2,
    "Paused":3,
    "Stopped":4,
    "Muted":5,
    "Unmuted":6
}

CAD_EXT = ['.vwx', '.dwg', '.sldprt']