# txt_view.py
import os,csv
import pandas as pd
import subprocess
import mammoth
import xlrd,openpyxl
#-----------------------------------
from PySide6.QtGui import QPixmap,QImageReader
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidget,QTableWidgetItem,QLabel,QWidget,QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView
#-----------------------------------
from FindName.languages import *
from FindName.actions import *
from FindName.system_info import path_normalized
from FindName import MAX_CHARS,MAX_ROW
#----------------------------------------------------------------------
def main_text(self, filepath,ext,ord):
    self.current_image = None
    supported_ext = [b"." + fmt for fmt in QImageReader.supportedImageFormats()]
    #Supported_ext includes : images , plaintext, Excel , Word
    if ext.lower() == ".pdf":
        preview_pdf(self, filepath)
    elif ord == 9: # Plain text
        preview_text(self,filepath)
    elif ext.lower() in [".docx",".doc"]:
        preview_word(self,filepath,ext)
    elif ext.lower() in [ ".xlsx" ,".xls"]:
        preview_excel(self,filepath)
    elif ext.lower() in [".csv",".CSV"]:
        preview_csv(self,filepath)
    elif ext.encode() in supported_ext: # Image files
        self.current_image = filepath
        preview_image(self, filepath)    
    else:
        message(self,"Support","View",source="main text")
#----------------------------------------------------------------------
def preview_pdf(self, filepath):
    # Show the PDF viewer
    from PySide6.QtPdf import QPdfDocument
    try:
        status = self.pdf_doc.load(filepath)
        if status != QPdfDocument.Error.None_:
            message(self,"PDF","Load",source="preview PDF")
            return
        self.preview_top.addWidget(self.pdf_view)
        self.preview_top.setCurrentWidget(self.pdf_view)
    except Exception as e:
        message(self,"PDF","View",source="preview PDF",error_code=e)
#----------------------------------------------------------------------
def preview_image(self, filepath):
    self.current_image = filepath
    pixmap = QPixmap(filepath)
    if pixmap.isNull():
        message(self,"Image","Load",source="Preview image")
        return
    available_size = self.preview_top.size()
    scaled = pixmap.scaled(
            # self.image_view.size(),
            available_size,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
    self.image_view.setPixmap(scaled)
    self.image_view.setAlignment(Qt.AlignCenter)
    self.preview_top.setCurrentWidget(self.image_view)
    return
#----------------------------------------------------------------------
def resizeEvent(self, event):
    super().resizeEvent(event)
    if self.current_image is not None:
        pixmap = QPixmap(self.current_image)
        available_size = self.preview_top.size()
        scaled = pixmap.scaled(
            # self.image_view.size(),
            available_size,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.image_view.setPixmap(scaled)
#----------------------------------------------------------------------
def preview_text(self, filepath):
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            # Read only up to limit chars to avoid memory explosion
            content = f.read(MAX_CHARS)
            if not content.strip():
                message(self,"Text","Empty",source="preview text")
                return
            content = content.strip()
            # Split and limit number of lines
            lines = content.splitlines()
            truncated = False
            if len(lines) > MAX_ROW:
                lines = lines[:MAX_ROW]
                truncated = True
            final_text = "\n".join(lines)
            if truncated:
                w1,w2,w3 = PREVIEW["Text"]["Truncate"][self.language]
                final_text += f"\n\n[{w1} {MAX_ROW} {w2}/{MAX_CHARS} {w3}]"
            if not final_text.strip():
                message(self,"Text","Empty",source="preview text")
            else:
                self.text_view.setText(final_text)
                self.text_view.setAlignment(Qt.AlignCenter)
                self.preview_top.setCurrentWidget(self.text_view)
    except Exception as e:
        message(self,"Text","Read",source="preview text",error_code=e)
    return
#----------------------------------------------------------------------
def preview_csv(self,filepath):
    encodings = ["utf-8", "cp932"]
    data = []
    encoding_used = None
    # Try multiple encodings
    for enc in encodings:
        try:
            with open(filepath, newline='', encoding=enc, errors="ignore") as f:
                reader = csv.reader(f)

                for i, row in enumerate(reader):
                    if i >= MAX_ROW:
                        break
                    data.append(row)
            encoding_used = enc
            break
        except Exception:
            data = []
    if not data:
        message(self,"CSV","Read",source="preview CSV")
        return

    # Build table
    table = QTableWidget()
    table.setRowCount(len(data))
    table.setColumnCount(len(data[0]))
    table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    
    for r, row in enumerate(data):
        for c, value in enumerate(row):
            table.setItem(r, c, QTableWidgetItem(value))
    # Add footer message if truncated
    if len(data) == MAX_ROW:
        w1,w2 =  PREVIEW["CSV"]["Truncate"][self.language]
        if encoding_used:
            label_name =f"{w1} {MAX_ROW} {w2} (encoding: {encoding_used})"
            label = QLabel(label_name)
            label.setStyleSheet("color: gray; padding: 4px; font-size: 12px;")
            container = QWidget()
            vbox = QVBoxLayout(container)
            vbox.addWidget(table)
            vbox.addWidget(label)
            self.preview_top.addWidget(container)
            self.preview_top.setCurrentWidget(container)
        else:
            message(self,"CSV","Read",source="preview CSV")
    else:
        self.preview_top.addWidget(table)
        self.preview_top.setCurrentWidget(table)
#----------------------------------------------------------------------
def preview_word(self, filepath, ext):
    from .actions import message
    # 1) If .doc → convert to .docx using LibreOffice
    if ext == ".doc":
        try:
            filepath = convert_doc_to_docx(filepath)
            if filepath:
                ext = ".docx"
            else:
                message(self,"Doc","Convert",source="preview Word")
                return
        except Exception as e:
            message(self,"Doc","Convert",source="preview Word",error_code=e)
            return
    # 2) Try DOCX → HTML
    if ext == ".docx":
        from docx import Document
        try:
            doc = Document(filepath)
            text = []
            for paragraph in doc.paragraphs:
                text.append(paragraph.text)
                if len(text) >= MAX_ROW:
                    text.append(f'... {PREVIEW["Doc"]["Truncate"][self.language]}')
                    break
            text = "\n".join(text)
            if text.strip():
                self.text_view.setText(text)
                self.preview_top.setCurrentWidget(self.text_view)
            else:
                message(self,"Doc","Empty",source="preview Word")
        except Exception as e:
            message(self,"Doc","Read",source="preview Word",error_code=e)
            return
        try:
            with open(filepath, "rb") as f:
                html = mammoth.convert_to_html(f).value
            if html.strip():
                self.web.setHtml(html)
                self.preview_top.setCurrentWidget(self.web)
                return

        except Exception as e:
            message(self,"Doc","File",source="preview Word",error_code=e)
            return
#----------------------------------------------------------------------
def convert_doc_to_docx(self,filepath):
    import os, subprocess, tempfile
    from pathlib import Path
    new_file=None
    # Check te valid of Libre Office
    LO = Path(Loffice[0]).expanduser() or Path(Loffice[1]).expanduser()
    if LO.exists():
        LO = LO.resolve()
        out_dir = tempfile.gettempdir()   # Always safe
        #Create runnable file in  temp folder  to read/write without permission
        cmd = f'"{LO}" --headless --convert-to docx --outdir "{out_dir}" "{filepath}"'

        result = subprocess.run(
            cmd,
            shell=True,          # Need to run in cmd 
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        base = os.path.splitext(os.path.basename(filepath))[0]
        new_file = os.path.join(out_dir, base + ".docx")

        if not os.path.exists(new_file):
            msg = f'{PREVIEW["Doc"]["Allow"][self.language][0]} {self.OS} {PREVIEW["Doc"]["Allow"][self.language][1]}]'
            raise PermissionError(msg)
    else:
        # not found LibreOffice, not installed 
        pass
    return new_file
#----------------------------------------------------------------------    

def preview_excel(self, filepath):
    try:
        # Load Excel file depending on extension
        if filepath.endswith(".xls"):
            try:
                df=pd.read_excel(filepath,header=0, engine="xlrd")
                # df.columns = df.columns.fillna("").astype(str)
            except Exception as e:
                self.image_view.setText(f'{PREVIEW["Excel"]["Read"][self.language]} {e}')
                self.image_view.setAlignment(Qt.AlignCenter)
                self.preview_top.setCurrentWidget(self.image_view)
                return
        else:
            df = pd.read_excel(filepath, header=0, engine="openpyxl")
        df.columns = df.columns.fillna("").astype(str)
        df.columns = ["" if col.startswith("Unnamed") else col for col in df.columns]
        # Limit preview rows
        total_rows = len(df)
        if total_rows > MAX_ROW:
            df_preview  = df.head(MAX_ROW)
            footer = f"<p style='color:#666;font-size:12px;'>Showing first {MAX_ROW} rows (Total rows: {total_rows})</p>"
        else:
            df_preview = df
            footer =""
        html = df_preprocessor(self,df_preview)
        # Add styling to make it look like Windows preview
        styled_html = f"""
        <html>
            <head>
                <style>
                    body {{
                        font-family: Segoe UI, Arial;
                        font-size: 13px;
                        padding: 8px;
                    }}
                    table.excel-table {{
                        border-collapse: collapse;
                        width: 100%;
                    }}
                    table.excel-table th {{
                        background: #f0f0f0;
                        border: 1px solid #d0d0d0;
                        color: #252525
                        padding: 4px;
                        text-align: left;
                        font-weight: 600;
                    }}
                    table.excel-table td {{
                        border: 1px solid #d0d0d0;
                        padding: 4px;
                    }}
                    # table.excel-table tr:nth-child(even) td {{
                    #     background: #fafafa;
                    # }}
                </style>
            </head>
            <body>
                {html }
                {footer}
            </body>
        </html>
        """
        self.text_view.setHtml(styled_html)
        self.preview_top.setCurrentWidget(self.text_view)
    except Exception as e:
        self.image_view.setText(f'{PREVIEW["Excel"]["View"][self.language]} {e}')
        self.image_view.setAlignment(Qt.AlignCenter)
        self.preview_top.setCurrentWidget(self.image_view)
        return
    return
#--------------------------------------------------
#  Clean raw old format  data
def df_preprocessor(self,df:pd.DataFrame) ->str:
    import re
    # Replace NaN with empty string
    df = df.fillna("")

    # Convert all to string
    df = df.astype(str)

    # Remove illegal control characters
    def clean_text(v):
        # Remove ASCII control chars except tab/newline
        return re.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F]", "", v)

    df = df.map(clean_text)

    # Now convert to HTML safely
    return df.to_html(
        index=False,
        border=0,
        classes="excel-table",
        justify="left",
        escape=True
    )
    
def message(self,kind,error_type,source ="preview file",error_code =None):
    text =f"Source: {source}\n"
    text  += PREVIEW.get(kind,{}).get(error_type).get(self.language,"English")
    text += f"\n{str(error_code)}" if error_code else ""
    self.image_view.setText(text)
    #Pull image_view on top
    self.preview_top.setCurrentWidget(self.image_view)