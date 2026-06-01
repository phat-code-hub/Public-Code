# actions.py
#--------------------------------------------------------------------------------------
import os

from PySide6.QtWidgets import (QListWidgetItem,QMessageBox,QFileDialog,
                            QColorDialog,QLineEdit,
                            QTextEdit,QApplication,
                            QDialog,QPlainTextEdit,QVBoxLayout)
from PySide6.QtCore import Qt,QUrl
from PySide6.QtGui import QPalette,QColor,QFontMetrics,QDesktopServices

from FindName.view_media import reset_media_ui,main_media
from FindName.view_txt  import *
from FindName.view_cad  import *
from FindName.languages import *
from FindName.constants import *
from FindName.system_info import saved_to_registry,path_normalized
from FindName import *
#--------------------------------------------------------------------------------------
def move_to_center(self):
        # Get the screen geometry of the primary screen
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()

        # Get the geometry of the window
        window_geometry = self.frameGeometry()

        # Move center of window geometry to center of screen
        window_geometry.moveCenter(screen_geometry.center())

        # Move the top-left of the window to match the new center
        self.move(window_geometry.topLeft())

#--------------------------------------------------------------------------------------
def change_language(self,lang = "EN"):
    types= TYPES
    self.language = LANGUAGES["English"][lang]
    
    #Update changed language to registry
    saved_to_registry(self)
    #Set the LABELS and combo box items based on the selected language
    self.setWindowTitle(LABELS[self.language]["Title"])
    # Main menu
    self.menu1_home.setTitle(f'{MENU1["Home"][self.language]}(&H)')
    self.menu2_about.setTitle(f'{MENU1["About"][self.language]}(&A)')
    # Sub Menu
    self.menu11_language.setTitle(f'{MENU2["Language"][self.language]}(&L)')
    self.menu21_guide.setText(f'{GUIDE["Title"][self.language]} ')
    self.menu22_author.setText(f'{MENU2["Author"][self.language]}')
    #----------Languages-----------------
    self.menu111_language_japanese.setText( LANGUAGES[self.language]["JP"])
    self.menu111_language_english.setText(LANGUAGES[self.language]["EN"])
    self.menu111_language_vietnamese.setText( LANGUAGES[self.language]["VN"])
    #----------Theme Color-----------------
    self.menu_theme.setTitle(f'{MENU2["Theme"][self.language]}...')
    self.action_theme_light.setText(THEME["Light"][self.language])
    self.action_theme_dark.setText(THEME["Dark"][self.language])
    self.action_theme_high.setText(THEME["HighContrast"][self.language])
    self.action_theme_low.setText(THEME["LowContrast"][self.language])
    self.action_custom_bg.setText(THEME["CustomBackground"][self.language])
    self.action_custom_text.setText(THEME["CustomText"][self.language])
    self.action_reset_custom.setText(THEME["ResetCustomColor"][self.language])
    #-------------------------------------------------------------------------
    self.search_menu.setText(f'{MENU2["Search"][self.language]}...')
    self.exit.setText(MENU2["Exit"][self.language])

    self.search_folder_label.setText(LABELS[self.language]["SearchPath"])
    self.search_label.setText(LABELS[self.language]["SearchKeyword"])
    self.search_input.setPlaceholderText(PLACE_HOLDER[self.language])
    self.search_button.setText(LABELS[self.language]["SearchButton"])
    self.and_radio.setText(OPTIONS[self.language]["AND"])
    self.or_radio.setText(OPTIONS[self.language]["OR"])
    self.not_radio.setText(OPTIONS[self.language]["NOT"])
    self.file_type_label.setText(LABELS[self.language]["FileType"])
    self.folder_label.setText(LABELS[self.language]["Folders"])
    self.file_label.setText(LABELS[self.language]["Files"])
    self.cancel_button.setText(LABELS[self.language]["Cancel"])
    self.info_label.setText(LABELS[self.language]["Info"])
    self.play_button.setText(LABELS[self.language]["Play"])
    self.stop_button.setText(LABELS[self.language]["Stop"])
    self.seek.setText(LABELS[self.language]["Seek"])
    self.volume.setText(LABELS[self.language]["Volume"])
    self.mute_button.setText(LABELS[self.language]["Mute"])
    self.info.setText("")
    self.file_type_combo.clear()
    for _ in range(len(TYPES)):
        self.file_type_combo.addItem(types[_][self.language])
    change_logic(self)
    change_tooltips(self)
    init_preview(self)
#----------------------------------------------------------------   
# def change_theme(self):
    
#     """Pick background + text colors using QColorDialog."""
#     color = QColorDialog.getColor(self.palette().color(QPalette.Window), self, make_word(self,0)) #Background
#     if color.isValid():
#         palette = self.palette()
#         palette.setColor(QPalette.Window, color)
#         self.setPalette(palette)

#     text_color = QColorDialog.getColor(Qt.black, self, make_word(self,1))
#     if text_color.isValid():
#         p = self.palette()
#         p.setColor(QPalette.WindowText, text_color)
#         self.setPalette(p)
# #----------------------------------------------------------------
# def make_word(self,kind=0):
#     if self.language =="English":
#         word = f"Select {THEME[self.language][kind]} color"
#     elif self.language == "Japanese":
#         word = f"{THEME[self.language][kind]}の色を選んでください。"
#     else:
#         word = f"Xin chọn màu của {THEME[self.language][kind]}"
#     return word
#----------------------------------------------------------------  
def open_file_dialog(self):
    select_folder = LABELS[self.language]["SelectFolder"]
    folder_path = QFileDialog.getExistingDirectory(self, select_folder,self.search_path)
    if folder_path:
        self.search_path = folder_path
        self.search_folder_path.setText(folder_path)
        searchFiles(self)
    else:
        show_empty(self)
#----------------------------------------------------------------
def show_author(self):
    COPYRIGHT= f"{COMPANY[self.language]}\n © All rights reserved by {AUTHOR[self.language]} {YEAR}\nVersion: {VERSION}\n"
    QMessageBox.information(self, MENU2["Author"][self.language], COPYRIGHT)
#----------------------------------------------------------------
def read_content(file_path,tag= None):
    lines = []
    if (tag):
        start_tag = f"[{tag}]"
        end_tag = f"[/{tag}]"
        inside = False
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if stripped == start_tag:
                    inside = True
                    continue
                if stripped == end_tag:
                    break
                if inside:
                    lines.append(line.rstrip("\n"))
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [line.rstrip("\n") for line in f]
            
    return "\n".join(lines)
#----------------------------------------------------------------

def resource_path(relative_path):
    
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)
#----------------------------------------------------------------
def show_guide(self):
    from pathlib import Path
    # guide_path = os.path.join(os.path.dirname(__file__),"resources","lang", GUIDE_PATH)
    # guide_path = resource_path(
    #     os.path.join("resources", "lang", GUIDE_PATH)
    # )
    # guide_path = path_normalized(guide_path)
    guide_path = Path(resource_path("resources")) / "lang" / GUIDE_PATH
    # Read guidance content based on language tag
    tag = (self.language[0].upper() if self.language else "E")
    content = read_content(guide_path,tag)
    # Preview content in a dialog
    dialog = QDialog()
    dialog.setWindowTitle(GUIDE_TITLE[self.language])
    dialog.resize(600, 400)

    layout = QVBoxLayout(dialog)

    text_edit = QPlainTextEdit()
    text_edit.setPlainText(content)
    text_edit.setReadOnly(True)

    layout.addWidget(text_edit)

    dialog.exec()
    print("GUIDE PATH:", guide_path)
    print("EXISTS:", os.path.exists(guide_path))
#----------------------------------------------------------------
#Search from search pattern
def change_search_source(self,source =1):
    if self.search_input.text().strip() :
        if source == 2:
            if self.folder_list.currentItem() is None:
                return
            else:
                self.search_path = os.path.join(self.search_path,self.folder_list.selectedItems()[0].text())
        self.search_folder_path.setText(self.search_path)
        if self.init:
            self.init = False
        if not self.init:
            self.info.setText(LABELS[self.language]["message"])
        searchFiles(self,source = source)
    else:
        if not self.init:
            show_empty(self)
            init_preview(self)
#----------------------------------------------------------------
def change_type(self):
    if self.file_type_combo.currentIndex() == -1:
        self.type_index =0
    else:
        self.type_index =self.file_type_combo.currentIndex()
    self.search_type =EXTENSIONS[self.type_index]
    searchFiles(self)
#----------------------------------------------------------------
def change_logic(self):
    if self.and_radio.isChecked():
        self.logic_index = LOGICS["AND"]
    elif self.or_radio.isChecked():
        self.logic_index = LOGICS["OR"]
    else:
        self.logic_index = LOGICS["NOT"]
    searchFiles(self)

#----------------------------------------------------------------
def show_file_info(self,current):
    self.info.setTextInteractionFlags(self.info.textInteractionFlags() | Qt.TextSelectableByMouse)
    fm = QFontMetrics(self.info.font())
    try:
        if current is None:
            self.info.setText("")
            return
        file_index = self.file_list.currentRow()
        filename = current.data(Qt.UserRole) or current.text()
        if not filename:
            filename = current.text()
        #Get file full path
        file_path = os.path.dirname(self.found_files[file_index]).lower()
        file_path = file_path.removeprefix(self.search_path).removeprefix(os.path.sep)
        foundfolders =[i.text().lower() for i in self.folder_list.findItems("",Qt.MatchContains)]
        index = list(filter(lambda i:foundfolders[i] in file_path,range(len(foundfolders))))
        if index:
            self.folder_list.setCurrentRow(index[0])
        self.full_path =self.found_files[self.file_list.row(current)]
        #Get file name
        short_path =fm.elidedText(self.found_files[self.file_list.row(current)],Qt.ElideMiddle,500)
        self.info.setText(short_path)
        preview_file(self,self.full_path)
    except Exception as e:
        message(self,"None","Read",source="Show file Info",error_code=e)
#-----------------------------------------------------------------------   
def open_file_location(self,item):
    import subprocess
    filepath = os.path.dirname(self.found_files[self.file_list.row(item)])
    try:
        if DEFAULT_CONFIG["OS"] == "WIN":
            QDesktopServices.openUrl(QUrl.fromLocalFile(filepath))
        elif DEFAULT_CONFIG["OS"] == "MAC":
            subprocess.run(["open", filepath])
        else:  # Linux and others
            subprocess.run(["xdg-open", filepath])
    except Exception as e:
        QMessageBox.critical(self,ERRORS[self.language]["Title"], f'{ERRORS[self.language]["Open"]}:\n{e}')
#-----------------------------------------------------------------------
def change_tooltips(self):
    self.search_folder_change.setToolTip(HINT["Dialog"][self.language])
    self.file_type_combo.setToolTip(HINT["Type"][self.language])
    self.folder_list.setToolTip(HINT["Folder"][self.language])
    self.file_list.setToolTip(HINT["File"][self.language])
    self.search_input.setToolTip(HINT["Search"][self.language])
    logic = HINT["Logic"][self.language] 
    self.or_radio.setToolTip(logic[0])
    self.and_radio.setToolTip(logic[1])
    self.not_radio.setToolTip(logic[2])
#----------------------------------------------------------------
def reset_data(self):
    self.keywords = ""
    self.condition = None
    self.found_files = []
    self.found_folders = set()
    self.found_files_short = []
    self.found_folders_short = set()
#-----------------------------------------------------------------------
def show_empty(self):
    reset_data(self)
    for root, dirs, _ in os.walk(self.search_path):
        if dirs:
            for dir in dirs:
                self.found_folders.add(os.path.join(root, dir))
    if self.found_folders:
        for folder in self.found_folders:
            partial_path = folder.removeprefix(self.search_path)
            if partial_path.startswith(os.path.sep):
                partial_path = partial_path[1:]
            self.found_folders_short.add(partial_path)
    showdata(self)
#-----------------------------------------------------------------------
def showdata(self,source=1):
    self.file_list.clear()
    self.folder_list.clear()
    if source == 1:
        if self.found_folders or self.found_files:
            self.info.setText(LABELS[self.language]["finish"])
        else:
            self.info.setText("")
        if self.found_folders:
            folders = list(self.found_folders)
            for folder in folders:
                partial_path = folder.removeprefix(self.search_path)
                if partial_path.startswith(os.path.sep):
                    partial_path = partial_path[1:]
                self.found_folders_short.add(partial_path)
        if self.found_files:
            for file in self.found_files:
                filename = os.path.basename(file)
                self.found_files_short.append(filename)
    else:
        if self.found_files:
            for file in self.found_files:
                filename = os.path.basename(file)
                self.found_files_short.append(filename)
    #----------------------------------------------------------------------
    if len(self.found_files)>0:
        for file in self.found_files_short:
            item = QListWidgetItem(file)
            item.setData(Qt.UserRole, file)
            self.file_list.addItem(item)
    self.file_label.setText(LABELS[self.language]["Files"]+" "+ str(self.file_list.count()))
    if len(self.found_folders)>0:
        for folder in self.found_folders_short:
            self.folder_list.addItem(folder)
    self.folder_label.setText(LABELS[self.language]["Folders"]+" "+ str(self.folder_list.count()))
#-----------------------------------------------------------------------
def filter_type(self):
    filtered_files = []
    filtered_folders =  set()
    if self.search_type or len(self.search_type)>0:
        for file in self.found_files:
            if any(file.lower().endswith(ext) for ext in self.search_type):
                filtered_files.append(file)
                dirname= os.path.dirname(file)
                if dirname.startswith(os.path.sep) and DEFAULT_CONFIG["OS"] != "MAC":
                    partial_path = partial_path[1:]
                    dirname = dirname[1:]
                filtered_folders.add(dirname)
    return filtered_files, filtered_folders
#-----------------------------------------------------------------------
def searchFiles(self,source = 1):
    import re
    reset_data(self)
    keyword = self.search_input.text().strip()
    self.info.setText(LABELS[self.language]["message"])
    if keyword :
        self.init = False
        self.keywords = re.split(r'[ ,;:/|]+', self.search_input.text().strip().lower())
        if  len(self.keywords)==1 and self.keywords[0] in ["*","*.*","."]:
            for root, dirs, files in os.walk(self.search_path):
                for name in files + dirs:
                    if os.path.isfile(os.path.join(root, name)):
                                self.found_files.append(os.path.join(root, name))
                                self.found_folders.add(os.path.dirname(os.path.join(root, name)))
                    elif os.path.isdir(os.path.join(root, name)):
                        self.found_folders.add(os.path.join(root, name))
        else:
            for root, dirs, files in os.walk(self.search_path):
                # Check if any file or folder name matches any part of the search pattern
                for name in files + dirs:
                    if self.logic_index == 0: #OR
                        self.condition =any(part in name.lower() for part in self.keywords)
                    elif self.logic_index == 1:#AND
                        self.condition =all(part in name.lower() for part in self.keywords)
                    else:#NOT
                        self.condition =not all(part in name.lower() for part in self.keywords)
                    if self.condition:
                        if os.path.isfile(os.path.join(root, name)):
                            self.found_files.append(os.path.join(root, name))
                            self.found_folders.add(os.path.dirname(os.path.join(root, name)))
        # Filter by file type
        if self.search_type or len(self.search_type)>0:
            self.found_files,folders = filter_type(self)
            self.found_folders = folders.intersection(self.found_folders)
        self.filtered_files, self.filtered_folders = self.found_files, self.found_folders
        showdata(self,source)
    else:#Nothing selected
        reset_data(self)
        if not self.init:
            show_empty(self)
        init_preview(self)
#----------------------------------------------------------------------
def resizeEvent(self, event):
    if hasattr(self, "original_pixmap") and self.original_pixmap:
        self.update_scaled_image()
    super().resizeEvent(event)
#----------------------------------------------------------------------
def preview_file(self,path):
    ext = os.path.splitext(path)[1].lower()
    ord_list =[ i  for i,(k,v) in enumerate(EXTENSIONS.items()) if ext in v] or [0]# Index of file in EXTENSIONS
    if ord_list[0] == 0 :
        message(self,"Support","View",source="previewFile")
        return
    else:
        ord = ord_list[0]
    filetype = [k.lower() for k,v in VIEW_EXT.items() if ord in v][0]#Type to choose Preview code 
    reset_media_ui(self,enabled=False)
    path = path_normalized(path)
    if filetype == "text": #Include image types
        main_text(self,path,ext,ord) # type: ignore
    if filetype == "cad":
        pass
        # main_cad(self,path,ext,ord) # type: ignore
    # if filetype == "prog":
    #     main_txt(self,path,ext,ord) # type: ignore
    elif filetype == "media":
        main_media(self,path,ext,ord)
    else:
        message(self,"Support","File",source="previewFile")
#--------------------------------------------------------
#      Remove , changed conflict separator of path
#--------------------------------------------------------
# Init starting , no select state of preview window
def init_preview(self):
    if self.init:
        self.image_view.setText(PREVIEW["Select"]["First"][self.language])
    else:
        if len(self.found_files)>0:
            self.image_view.setText(PREVIEW["Select"]["None"][self.language])
        else:
            self.image_view.setText(PREVIEW["Select"]["Empty"][self.language])
    self.image_view.setAlignment(Qt.AlignCenter)
    self.preview_top.setCurrentWidget(self.image_view)
#----------------------------------------------------------------------
def message(self,kind,error_type,source ="preview file",error_code =None):
    pass
    # text =f"Source: {source}\n"
    # text  += PREVIEW.get(kind,{}).get(error_type).get(self.language,"English")
    # text += f"\n{str(error_code)}" if error_code else ""
    # self.image_view.setText(text)
    # #Pull image_view on top
    # self.preview_top.setCurrentWidget(self.image_view)