# ui_main.py
import os
import sys
# ---------------------------
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput,QMediaDevices
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtGui import QAction,QIcon,QActionGroup
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView
# ---------------------------
from FindName.actions import *
from FindName.languages import *
from FindName.view_media import *
from FindName.constants import *
from FindName.system_info import (resource_path,saved_to_registry,
                        check_license,toggle_password_visibility)
from FindName.system_info import (check_installed_app,apply_theme,choose_custom_background,
                                    choose_custom_text,reset_custom_colors)
# ---------------------------
# Valid Confirmation
# ---------------------------
class CheckForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(LICENSE[DEFAULT_CONFIG["Language"]]["Title"])
        self.setGeometry(100, 100, 300, 150)
        self.setup_ui()
        move_to_center(self)
    def setup_ui(self):
        layout = QVBoxLayout()
        self.prompt = QLabel(LICENSE[DEFAULT_CONFIG["Language"]]["Prompt"])
        layout.addWidget(self.prompt)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.show_hide_checkbox = QCheckBox(LICENSE[DEFAULT_CONFIG["Language"]]["Display"])
        layout.addWidget(self.show_hide_checkbox)
        
        self.check_button = QPushButton(LICENSE[DEFAULT_CONFIG["Language"]]["Button"])
        layout.addWidget(self.check_button)

        self.setLayout(layout)
        # Connect the button to the check_license function
        self.check_button.clicked.connect(lambda pw:check_license(self,self.password_input.text().strip().lower()))
        self.password_input.returnPressed.connect(lambda pw:check_license(self,self.password_input.text().strip().lower()))
        self.show_hide_checkbox.stateChanged.connect(lambda state:toggle_password_visibility(self,self.show_hide_checkbox.checkState()))

# -----------------------------------------------------------------------------------
# View Info Dialog
# -----------------------------------------------------------------------------------
class Viewer(QWidget):
    def __init__(self,content = None,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Text Viewer")
        self.resize(500, 400)
        layout = QVBoxLayout()

        self.textbox = QPlainTextEdit()
        self.textbox.setReadOnly(True)

        layout.addWidget(self.textbox)
        self.setContent(content)

    def setContent(self,content):
        if content:
            self.textbox.setPlainText(content)
        # else:
        #     self.textbox.setPlainText("No content to display.")
# -----------------------------------------------------------------------------------
# UI-only class 
# -----------------------------------------------------------------------------------
class FileSearch(QWidget):
    def __init__(self):
        super().__init__()
        self.default_values()
        self._build_ui()
        self._build_menu()
        self._build_layout()
    #---------------------------------------------
    def default_values(self):
        self.language,self.search_path= DEFAULT_CONFIG["Language"],DEFAULT_CONFIG["SearchPath"]
        # Other default values 
        self.init =True
        self.is_seeking = False
        self.viewer = None
        self.custom_colors = {} # Store user customize color
        self.current_theme = DEFAULT_CONFIG.get("Theme","Light")
    #---------------------------------------------
    def _build_menu(self):
        """Build main menu bar (Home, About)."""
        #================================================
        # Create MenuBar
        #================================================
        bar = QMenuBar(self)
        # ----------------------------
        # Menu 1 : Home
        # ----------------------------
        self.menu1_home = bar.addMenu(f'{MENU1["Home"][self.language]}(&H)')
        # SubMenu 1-1 :Language 
        self.menu11_language = self.menu1_home.addMenu(f'{MENU2["Language"][self.language]} (&L)')
        
        self.menu111_language_japanese =QAction( LANGUAGES[self.language]["JP"],self)
        self.menu111_language_english =QAction(LANGUAGES[self.language]["EN"],self)
        self.menu111_language_vietnamese =QAction( LANGUAGES[self.language]["VN"],self)
        
        self.menu111_language_japanese.setShortcut("Ctrl+J")
        self.menu111_language_english.setShortcut("Ctrl+E")
        self.menu111_language_vietnamese.setShortcut("Ctrl+V")
        
        
        self.menu11_language.addAction(self.menu111_language_japanese)
        self.menu11_language.addAction(self.menu111_language_english)
        self.menu11_language.addAction(self.menu111_language_vietnamese)
        
        # SubMenu 1-2 : Theme (background , font) change
        #Set Theme as a menu 
        self.menu_theme = self.menu1_home.addMenu(MENU2["Theme"][self.language])

        self.theme_group = QActionGroup(self)
        self.theme_group.setExclusive(True)

        self.action_theme_light = QAction(THEME["Light"][self.language], self, checkable=True)
        self.action_theme_dark = QAction(THEME["Dark"][self.language], self, checkable=True)
        self.action_theme_high = QAction(THEME["HighContrast"][self.language], self, checkable=True)
        self.action_theme_low = QAction(THEME["LowContrast"][self.language], self, checkable=True)
        
        self.action_theme_dark.setShortcut("Ctrl+Alt+D")
        self.action_theme_light.setShortcut("Ctrl+Alt+L")

        
        for act in (
            self.action_theme_light,
            self.action_theme_dark,
            self.action_theme_high,
            self.action_theme_low,
        ):
            self.theme_group.addAction(act)
            self.menu_theme.addAction(act)

        self.action_theme_light.setChecked(True)

        self.menu_theme.addSeparator()
        
        self.action_custom_bg = QAction(THEME["CustomBackground"][self.language], self)
        self.action_custom_text = QAction(THEME["CustomText"][self.language], self)
        self.action_reset_custom = QAction(THEME["ResetCustomColor"][self.language], self)

        self.menu_theme.addAction(self.action_custom_bg)
        self.menu_theme.addAction(self.action_custom_text)
        self.menu_theme.addAction(self.action_reset_custom)


        # SubMenu 1-3 : Change Search Folder
        self.search_menu = QAction(f'{MENU2["Search"][self.language]}...',self)
        self.search_menu.setShortcut("Ctrl+S")
        self.menu1_home.addAction(self.search_menu)
        #------------------------------
        self.menu1_home.addSeparator()
        #Submenu 1-4: Exit
        self.exit = QAction(MENU2["Exit"][self.language], self)
        self.exit.setShortcuts(["Alt+X","Esc","Alt+F4"])
        self.menu1_home.addAction(self.exit)

        # ----------------------------
        # Menu2: About
        # ----------------------------
        self.menu2_about = bar.addMenu(f'{MENU1["About"][self.language]}(&A)')
        self.menu21_guide = QAction(GUIDE["Title"][self.language], self)
        self.menu22_author = QAction(MENU2["Author"][self.language], self)
        
        self.menu21_guide.setShortcut("Ctrl+G")
        self.menu22_author.setShortcut("Ctrl+W")
        
        self.menu2_about.addAction(self.menu21_guide)
        self.menu2_about.addAction(self.menu22_author)

        # Finally, attach menubar to layout
        self.main_layout.setMenuBar(bar)
#-------------------------------------------------------------
    def _build_ui(self):
        self.main_layout = QVBoxLayout()
        # Hold basic Info
        #================================================
        #      LEFT PANEL (file controls)
        #================================================
        self.layoutL = QVBoxLayout()
        #----------------------------------
        # Search folder row
        self.search_folder_label = QLabel("Search Path")
        self.search_folder_path = QLabel("")
        self.search_folder_change = QPushButton("...")

        # Keyword row
        self.search_label = QLabel("Keyword")
        self.search_input = QLineEdit()
        self.search_button = QPushButton("Search")

        # Search logic radios
        self.search_radio = QButtonGroup()
        self.or_radio = QRadioButton(OPTIONS[self.language]["OR"])
        self.and_radio = QRadioButton(OPTIONS[self.language]["AND"])
        self.not_radio = QRadioButton(OPTIONS[self.language]["NOT"])
        self.search_radio.addButton(self.or_radio, 0)
        self.search_radio.addButton(self.and_radio, 1)
        self.search_radio.addButton(self.not_radio, 2)

        # File type combo
        self.file_type_label = QLabel("File Type")
        self.file_type_combo = QComboBox()

        # Folders and files list widgets
        # Folders
        self.folder_label = QLabel("Folders")
        self.folder_list = QListWidget()
        # Files
        self.file_label = QLabel("Files")
        self.file_list = QListWidget()

        # Info & Cancel
        self.info_label = QLabel("Info")
        self.info = QLabel()
        self.cancel_button = QPushButton("Cancel")

        #================================================
        #      RIGHT PANEL (file Preview)
        #       (Divide 2 panels: top and bottom)
        #================================================
        
        #-----------------------------------------------
        # Top Preview QStackedWidget (image, text, CAD placeholder)
        #-----------------------------------------------
        self.preview_top = QStackedWidget()
        # Index 0: image view
        self.image_view = QLabel("No preview")
        self.current_image = None
        # Index 1: text view
        self.text_view = QTextEdit()
        # Index 2: CAD / placeholder
        self.cad_view = QLabel("CAD preview not implemented")
        # Index 3: Web view for word document
        self.web = QWebEngineView()
        # Index 4 : PDF Preview
        self.pdf_doc = QPdfDocument(self)
        self.pdf_view = QPdfView(self)
        self.pdf_view.setDocument(self.pdf_doc)
        #-----------------------------------------------
        #          Bottom Preview (Media related)
        #-----------------------------------------------
        self.preview_bottom = QWidget()
        # Media Player
        self.player = QMediaPlayer()
        self.layoutR = QHBoxLayout()
        #Audio Component
        self.audio_output = QAudioOutput(self)
        
        self.play_button = QPushButton("Play")
        self.stop_button = QPushButton("Stop")
        self.seek = QLabel("Seek:")
        self.seek_slider = QSlider(Qt.Horizontal)
        self.timer = QLabel("00:00 / 00:00")
        self.volume =QLabel("Volume:")
        self.volume_slider = QSlider(Qt.Horizontal)
        
        
        self.mute_button = QPushButton("Mute")
        
        # Video widget
        self.video_widget = QVideoWidget()
        # Set Controls Size
        self.setGeometry(100, 100, 1000, 600)
        self.search_folder_change.setFixedSize(50, 30)
        self.layoutR.setContentsMargins(6, 6, 6, 6)
        #-------------Top Panel----------------------
        self.preview_top.setMinimumSize(200, 100)
        self.preview_top.setMinimumHeight(200)
        self.image_view.setWordWrap(True)
        self.image_view.setStyleSheet("border: 1px solid lightgray;")
        self.image_view.setAlignment(Qt.AlignCenter)
        self.text_view.setReadOnly(True) 
        self.text_view.setAlignment(Qt.AlignCenter)
        self.cad_view.setAlignment(Qt.AlignCenter)
        self.cad_view.setStyleSheet("border: 1px dashed gray;")
        self.pdf_view.setZoomMode(QPdfView.ZoomMode.FitInView)
        #-------------Bottom Panel-------------------
        self.seek.setMinimumWidth(60)
        self.volume.setMinimumWidth(60)
        self.timer.setMinimumWidth(100)
        self.mute_button.setMinimumWidth(100)
        self.video_widget.setMinimumSize(200, 100)
        self.preview_bottom.setMinimumHeight(200) # ensure minimum height
        #---------- Other settings--------------------
        self.audio_output.setDevice(QMediaDevices.defaultAudioOutput())
        self.audio_output.setVolume(0.1) # 10%
        self.volume_slider.setRange(0,250)
        self.volume_slider.setValue(50)
        self.seek_slider.setRange(0, 100)
        self.timer.setAlignment(Qt.AlignCenter)
    #----------------------------------------------------------------
    def _build_layout(self):
        
        #======================================
        #          LEFT SIDE PANEL
        #======================================
        self.layoutL = QVBoxLayout()
        self.layoutR = QVBoxLayout()
        
        # L1: Search Row
        search_folder_layout = QHBoxLayout()
        search_folder_layout.addWidget(self.search_folder_label)
        search_folder_layout.addWidget(self.search_folder_path)
        search_folder_layout.addWidget(self.search_folder_change)
        # L2: Search Keyword Row
        keyword_layout = QHBoxLayout()
        keyword_layout.addWidget(self.search_label)
        keyword_layout.addWidget(self.search_input)
        keyword_layout.addWidget(self.search_button)
        # L3: Search Logic Row
        search_logic_layout = QHBoxLayout()
        search_logic_layout.addWidget(self.or_radio)
        search_logic_layout.addWidget(self.and_radio)
        search_logic_layout.addWidget(self.not_radio)
        # L4: File Type Row
        file_type_layout = QHBoxLayout()
        file_type_layout.addWidget(self.file_type_label)
        file_type_layout.addWidget(self.file_type_combo)
        
        #L5 List Layout include list and Folder list box layout
        folder_layout = QVBoxLayout()
        folder_layout.addWidget(self.folder_label)
        folder_layout.addWidget(self.folder_list)
        
        file_layout = QVBoxLayout()
        file_layout.addWidget(self.file_label)
        file_layout.addWidget(self.file_list)
        #------------O-------------------
        list_layout = QHBoxLayout()
        list_layout.addLayout(folder_layout)
        list_layout.addLayout(file_layout)
        
        # L6 Selected file Information
        info_layout = QHBoxLayout()
        info_layout.addWidget(self.info_label)
        info_layout.addWidget(self.info)
        # L8: Cancel Button
        self.cancel_button.setMaximumWidth(80)
        #-----------------------------------------
        # Add all left layout to self.layoutL
        #-----------------------------------------
        # self.layoutL.addLayout(lang_layout)
        self.layoutL.addLayout(search_folder_layout)
        self.layoutL.addLayout(keyword_layout)
        self.layoutL.addLayout(search_logic_layout)
        self.layoutL.addLayout(file_type_layout)
        self.layoutL.addLayout(list_layout)
        self.layoutL.addLayout(info_layout)
        self.layoutL.addWidget(self.cancel_button, alignment=Qt.AlignCenter)
        #-----------------------------------------
        self.preview_top = QStackedWidget()
        #-----------------------------------------
        # Add all top layouts to self.preview_top
        #-----------------------------------------
        self.preview_top.addWidget(self.text_view)
        self.preview_top.addWidget(self.image_view)
        self.preview_top.addWidget(self.web)
        self.preview_top.addWidget(self.pdf_view)
        self.preview_top.addWidget(self.cad_view)
        #======================================
        #          RIGHT SIDE PANEL
        #======================================
        #-----------------------------------------
        # Add all right layout to self.layoutR
        #-----------------------------------------
        controls_layout = QVBoxLayout()
        controls_row1 = QHBoxLayout()
        controls_row2 = QHBoxLayout()
        controls_row3 = QHBoxLayout()
        
        controls_row1.addWidget(self.play_button)
        controls_row1.addWidget(self.stop_button)
        
        controls_row2.addWidget(self.seek)
        controls_row2.addWidget(self.seek_slider)
        controls_row2.addWidget(self.timer)
        
        controls_row3.addWidget(self.volume)
        controls_row3.addWidget(self.volume_slider)
        controls_row3.addWidget(self.mute_button)
        
        controls_layout.addLayout(controls_row1)
        controls_layout.addLayout(controls_row2)
        controls_layout.addLayout(controls_row3)
        
        controls_layout.addStretch()
        
        self.layoutR.addWidget(self.video_widget, stretch=5)
        self.layoutR.addLayout(controls_layout, stretch=2)
        
        #-----------------------------------------
        # Add all bottom layouts to self.preview_bottom
        #-----------------------------------------
        self.preview_bottom.setLayout(self.layoutR)
        
        self.player.setAudioOutput(self.audio_output)
        try:
            self.player.setVideoOutput(self.video_widget)
        except BaseException:
            pass

        # Create Left and Right panels
        left_panel = QWidget()
        left_panel.setLayout(self.layoutL)
        
        right_splitter = QSplitter(Qt.Vertical)
        right_splitter.addWidget(self.preview_top)
        right_splitter.addWidget(self.preview_bottom)
        # Split equal height 
        right_splitter.setStretchFactor(0, 7)  # preview_top
        right_splitter.setStretchFactor(1, 3)  # preview_bottom
        #lock splitter to prevent resizing
        right_splitter.setChildrenCollapsible(False)
        
        right_panel = QWidget()
        right_panel_layout = QVBoxLayout()
        right_panel_layout.addWidget(right_splitter)
        right_panel.setLayout(right_panel_layout)
        # Create splitter and add panels
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([400, 600])
        # Add splitter to main layout
        self.main_layout.addWidget(splitter)
        self.setLayout(self.main_layout)
        #--------------------------------------------
        self.preview_top.setSizePolicy(
            QSizePolicy.Expanding,      # horizontal OK
            QSizePolicy.Preferred       # vertical shrink allowed
        )
        
        self.video_widget.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        self.image_view.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        #Interaction
        self.image_view.setScaledContents(False)
        self.mute_button.setCheckable(True)
        self.seek_slider.setEnabled(False)
        self.player.pause()
        #-----------------------------------------------
        #          Initialize Setting
        #-----------------------------------------------
        self.setWindowTitle(TITLE[self.language])
        self.icon = resource_path("app.ico")
        self.setWindowIcon(QIcon(self.icon))
        self.isOffice,self.isCAD = check_installed_app(self)
    #------------------------------------------------
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            QApplication.quit()
        super().keyPressEvent(event)
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    def resizeEvent(self, event):
        # Ensure PDF adjusts to new size automatically
        if hasattr(self, "pdf_view"):
            self.pdf_view.update()  # redraw
        super().resizeEvent(event)
    #----------------------------------------------------------
# ---------------------------
# Logic-heavy subclass
# ---------------------------
class FileSearchHandler(FileSearch):
    """
    Full application handler: sets defaults, hooks signals, and implements behavior.
    """
    def __init__(self):
        # Build UI first (from parent)
        super().__init__()
        self._restore_defaults()
        
        # Ensure correct radios are checked
        self.file_type_combo.setCurrentIndex(self.type_index if hasattr(self, "type_index") else 0)
        self.logic_index = LOGICS.get("OR", 0) if isinstance(LOGICS, dict) else 0
        try:
            btn = self.search_radio.button(self.logic_index)
            if btn:
                btn.setChecked(True)
        except Exception:
            pass
        # Set initial UI values (safe)
        self.search_folder_path.setText(self.search_path or "")
        self.search_type = EXTENSIONS[self.type_index]
        # Apply initial state: reset data, change logic/tooltips (these are project-specific)
        reset_data(self)
        change_logic(self)
        change_tooltips(self)
        # try:
        #     reset_data(self)
        # except Exception as e: #"actions.py" file missed
        #     print(WARNING[self.language]["Reset"], e)
        # try:
        #     change_logic(self)
        # except Exception as e: #"actions.py" file missed
        #     print(WARNING[self.language]["Logic"], e)
        
        # try:
        #     change_tooltips(self)
        # except Exception as e:#"actions.py" file missed
        #     print(WARNING[self.language]["Tooltip"], e)

        # Wire all signals here (exactly once)
        self._connect_signals()
        
        #Init Main Form
        init_preview(self)
        
    # -- default/state restoration -------------------
    def _restore_defaults(self):
        self.type_index = 0
        try:
            self.file_type_combo.clear()
            for _ in range(len(TYPES)):
                self.file_type_combo.addItem(TYPES[_][self.language])
            self.file_type_combo.setCurrentIndex(self.type_index)
        except Exception:
            pass
        
        # Fill UI label texts 
        try:
            apply_theme(self,self.current_theme)
            # Search labels
            self.search_folder_label.setText(LABELS[self.language]["SearchPath"])
            self.search_label.setText(LABELS[self.language]["SearchKeyword"])
            self.search_button.setText(LABELS[self.language]["SearchButton"])
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
            # placeholder
            self.search_input.setPlaceholderText(PLACE_HOLDER[self.language])
        except Exception:
            pass

# -- connect all event handlers here ----------------
    def _connect_signals(self):
        # # Language selection
        self.menu111_language_english.triggered.connect(lambda: change_language(self,"EN"))
        self.menu111_language_japanese.triggered.connect(lambda: change_language(self,"JP"))
        self.menu111_language_vietnamese.triggered.connect(lambda: change_language(self,"VN"))
        # self.theme_color.triggered.connect(lambda : change_theme(self))
        
        self.action_theme_light.triggered.connect(
            lambda: apply_theme(self,"Light")
        )
        self.action_theme_dark.triggered.connect(
            lambda: apply_theme(self,"Dark")
        )
        self.action_theme_high.triggered.connect(
            lambda: apply_theme(self,"HighContrast")
        )
        self.action_theme_low.triggered.connect(
            lambda: apply_theme(self,"LowContrast")
        )
        #Custom color
        self.action_custom_bg.triggered.connect(lambda: choose_custom_background(self))
        self.action_custom_text.triggered.connect(lambda:choose_custom_text(self))
        self.action_reset_custom.triggered.connect(lambda:reset_custom_colors(self))
        
        self.exit.triggered.connect(self.close)
        
        self.menu21_guide.triggered.connect(lambda : show_guide(self))
        self.menu22_author.triggered.connect(lambda : show_author(self))
        # Folder chooser
        self.search_folder_change.clicked.connect(lambda: open_file_dialog(self))
        self.search_menu.triggered.connect(lambda: open_file_dialog(self))
        # Search actions
        self.search_input.returnPressed.connect(lambda: change_search_source(self, source=1))
        self.search_button.clicked.connect(lambda: change_search_source(self, source=1))

        # File type selection
        self.file_type_combo.currentIndexChanged.connect(lambda: change_type(self))

        # Search logic radios
        self.search_radio.buttonClicked.connect(lambda: change_logic(self))

        # Folder double-click triggers search into folder
        self.folder_list.itemDoubleClicked.connect(lambda: change_search_source(self, source=2))

        # File list selection & double-click
        # Route selection through our handler that decides which preview to show
        self.file_list.currentItemChanged.connect(lambda current:show_file_info(self,current))
        self.file_list.itemDoubleClicked.connect(lambda item: open_file_location(self, item))
    
        #Volume Slider
        self.volume_slider.valueChanged.connect(
            lambda value:  on_volume_changed(self,value)
            )
        self.mute_button.clicked.connect(
            lambda checked: toggle_mute(self,checked)
            )
        #Player
        self.player.durationChanged.connect(
            lambda duration :on_duration_changed(self,duration)
            )
        self.player.positionChanged.connect(
            lambda pos: on_position_changed(self, pos)
            )
        #Elapsed time Slider
        self.seek_slider.sliderPressed.connect(
            lambda : on_slider_pressed(self)
            )
        self.seek_slider.sliderReleased.connect(
            lambda : on_slider_released(self)
            )
        self.seek_slider.sliderMoved.connect(
            lambda value: self.player.setPosition(value)
            )
        
        #Buttons
        self.play_button.clicked.connect(lambda :media_play_or_pause(self))
        self.stop_button.clicked.connect(lambda : media_state(self,STATES["Stopped"]))
    # Cancel / quit
        self.cancel_button.clicked.connect(QApplication.quit)

    #--------------------------------------------------------
    # override to ensure proper cleanup
    def closeEvent(self, event):
        # Save to Windows Registry before closing
        try:
            saved_to_registry(self)
        except Exception as e:
            print(f'{REG_SAVE[self.language][DEFAULT_CONFIG["OS"]]} {e}')

        super().closeEvent(event)  # Call the default close event handler event.accept()  # Allow the window to close

# End of ui_main.py