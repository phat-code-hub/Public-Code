from pathlib import Path
import os

#----------------------------------------------------------
#                Initial Constant
#----------------------------------------------------------

BASE_DIR = str(Path(__file__).parent.resolve())
GUIDE_DIR = os.path.join(BASE_DIR, "resources","lang")
MAX_ROW = 10 # Excel,text preview limit rows
MAX_VOL  = 100 # Max Volume
MAX_CHARS = 2000 # Max chars for text reading
# Check LibreOffice was installed paths or not
Loffice = ["C:\\Program Files\\LibreOffice\\program\\soffice.exe",
        "C:\\Program Files (x86)\\LibreOffice\\program\\soffice.exe"]
#Check FreeCAD was installed paths or not
FreeCADPath= [
    r"C:\\Program Files\\FreeCAD 1.0\\bin\\FreeCADCmd.exe",
    r"C:\\Program Files\\FreeCAD\\bin\\FreeCADCmd.exe"
]