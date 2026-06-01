# main.py
import sys
from PySide6.QtWidgets import QApplication
from FindName.ui_main import CheckForm,FileSearchHandler
from FindName.constants import DEFAULT_CONFIG
from FindName.system_info import check_registration
#-----------------------------------------------------------------
def main():
    check_registration()
    app = QApplication(sys.argv)
    form = FileSearchHandler() if DEFAULT_CONFIG.get("Passed") else CheckForm() 
    form.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()
#-----------------------------------------------------------------