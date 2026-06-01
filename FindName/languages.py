# languages.py

#Check License
LICENSE ={
    "English": {"Title": "Valid License Check",
                "Prompt": "Enter your license key:",
                "Display": "Show/Hide",
                "Button": "Check"
                },
    "Japanese": {"Title": "ライセンスキー確認",
                "Prompt": "ライセンスキーを入力下さい:",
                "Display": "表示/非表示",
                "Button": "確認"
                },
    "Vietnamese": {"Title": "Kiểm tra bản quyền",
                "Prompt": "Vui lòng nhập số bản quyền:",
                "Display": "Hiện/Ẩn",
                "Button": "Kiểm tra"
                }
}
ERRORS ={
    "English": {"Title": "Error",
                "Message": "Invalid license key!",
                "Open":"Failed to open folder!",
                },
    "Japanese": {"Title": "エラー",
                "Message": "不正なライセンスキー!",
                "Open":"フォルダを開けません!",
                },
    "Vietnamese": {"Title": "Lỗi",
                "Message": "Bản quyền không hợp lệ!",
                "Open":"Không thể truy cập thư mục!",
                }
}
#If loading data from "actions.py" bị lỗi , no need
WARNING ={
    "English" :{
        "Reset":"Warning: reset_data() failed: ",
        "Logic":"Warning: change_logic() failed: ",
        "Tooltip":"Warning: change_tooltips() failed: "
    },
    "Japanese" :{
        "Reset":"注意:データリセット不可!: ",
        "Logic":"注意:ロジック変更不可!: ",
        "Tooltip":"注意:ヒント変更不可!: "
    },
    "Vietnamese" :{
        "Reset":"Chú ý:Không khởi tạo lại được dữ liệu: ",
        "Logic":"Chú ý:Không thay đổi được logic: ",
        "Tooltip":"Chú ý:Không thay đổi được lời nhắc: "
    }
}

REG_WRITE ={
    "English":{ "WIN":"Registry failed!:",
                "MAC":"macOS plist save error:",
                "LINUX":"Linux save error:",
            },
    "Japanese":{ "WIN":"レジストリセイブエラー: ",
                "MAC":"macOS plistセイブエラー: ",
                "LINUX":"LINUX セイブエラー: ",
            },
    "Vietnamese":{ "WIN":"Register bị lỗi: ",
                "MAC":"Lỗi lưu tập tin plist: ",
                "LINUX":"LINUX bị lỗi lưu tập tin: ",
            },
}
REG_SAVE ={
    "English":{ "WIN":"Create Register error: ",
                "MAC":"macOS create plist error: ",
                "LINUX":"Linux create file error: ",
            },
    "Japanese":{ "WIN":"レジストリ登録エラー: ",
                "MAC":"macOS plist作成エラー: ",
                "LINUX":"LINUX 登録エラー: ",
            },
    "Vietnamese":{"WIN":"Tạo mới Registry bị lỗi: ",
                "MAC":"Lỗi tạo tập tin plist trên macOS: ",
                "LINUX":"LINUX bị lỗi tạo tập tin: ",
            },
}
#MENU BAR
MENU1 = {
    "Home" :{
        "English": "Home",
        "Japanese": "ホーム",
        "Vietnamese":"Nhà",
    },
    "About" :{
        "English": "About",
        "Japanese": "アプリについて",
        "Vietnamese":"Về Phần Mềm",
    },
}

MENU2 = {
    "Language" :{
        "English":"Language",
        "Japanese":"言語",
        "Vietnamese":"Ngôn ngữ"
    },
    "Theme" :{
        "English": "Theme",
        "Japanese": "テーマ",
        "Vietnamese":"Phông nền",
    },
    "Search" :{
        "English": "Change Search Folder",
        "Japanese": "検索フォルダー変更",
        "Vietnamese":"Đổi thư mục tìm",
    },
    "Exit" :{
        "English": "Exit",
        "Japanese": "終了",
        "Vietnamese":"Kết thúc",
    },
    "Author" :{
        "English": "Author",
        "Japanese": "著者",
        "Vietnamese":"Tác giả",
    },
}
THEME = {
    "Light":{
        "English":"Light",
        "Japanese":"明るい",
        "Vietnamese":"Sáng",
    },
    "Dark":{
        "English":"Dark",
        "Japanese":"ダーク",
        "Vietnamese":"Tối",
    },
    "HighContrast":{
        "English":"High Contrast",
        "Japanese":"高コントラスト",
        "Vietnamese":"Tương Phản Cao",
    },
    "LowContrast":{
        "English":"Low Contrast",
        "Japanese":"低コントラスト",
        "Vietnamese":"Tương Phản Thấp",
    },
    "CustomBackground":{
        "English":"Back Ground Color",
        "Japanese":"背景色",
        "Vietnamese":"Màu Nền",
    },
    "CustomText":{
        "English":"Text Color",
        "Japanese":"文字色",
        "Vietnamese":"Màu Chử",
    },
    "ResetCustomColor":{
        "English":"Reset Color",
        "Japanese":"リセット色",
        "Vietnamese":"Khôi phục màu",
    },
}


#Title
TITLE = {
    "English":"Search File",
    "Japanese": "ファイル検索",
    "Vietnamese": "Tìm Tập Tin"
}
# Language Radio Button
LANGUAGES ={"English":{"EN":"English","JP":"Japanese","VN"  :"Vietnamese"},
            "Japanese":{"EN":"英語","JP":"日本語","VN"  :"ベトナム語"},
            "Vietnamese":{"EN":"Tiếng Anh","JP":"Tiếng Nhật","VN"  :"Tiếng Việt"}}
LABELS = {
    "English": {
        "Title": "File Search",
        "SearchPath": "Search Path:",
        "SearchKeyword": "Search keyword:",
        "FileType": "File Type:",
        "Folders": "Folders:",
        "Files": "Files:",
        "SearchButton": "Search",
        "SelectFolder": "Select Folder",
        "Info": "File Information:",
        "message": "Searching, please wait...",
        "finish": "Search finished!",
        "Cancel": "Cancel",
        "Play": "Play",
        "Paused":"Paused",
        "Stop":"Stop",
        "Seek":"Seek",
        "Volume":"Volume",
        "Mute":"Mute",
        "Unmute":"Unmute"
    },
    "Japanese": {
        "Title": "ファイル検索",
        "SearchPath": "検索パス:",
        "SearchKeyword": "検索キーワード:",
        "FileType": "ファイルタイプ:",
        "Folders": "フォルダ:",
        "Files": "ファイル:",
        "SearchButton": "検索",
        "SelectFolder": "フォルダを選択",
        "Info": "ファイル情報:",
        "message": "検索中、お待ちください...",
        "finish": "検索完了!",
        "Cancel": "キャンセル",
        "Play": "プレイ",
        "Paused":"一時停止",
        "Stop":"停止",
        "Seek":"探し",
        "Volume":"音声",
        "Mute":"ミュート",
        "Unmute":"ミュート解除"
    },
    "Vietnamese": {
        "Title": "Tìm kiếm tập tin",
        "SearchPath": "Đường dẫn:",
        "SearchKeyword": "Từ Khóa:",
        "FileType": "Kiểu tập tin:",
        "Folders": "Thư mục:",
        "Files": "Tập tin:",
        "SearchButton": "Tìm kiếm",
        "SelectFolder": "Chọn thư mục",
        "Info": "Chi tiết tập tin:",
        "message": "Đang tìm, vui lòng đợi...",
        "finish": "Hoàn Thành tìm kiếm!",
        "Cancel": "Hủy",
        "Play": "Chơi",
        "Paused":"Tạm Dừng",
        "Stop":"Dừng",
        "Seek":"Tìm",
        "Volume":"Âm Lượng",
        "Mute":"Tắt Tiếng",
        "Unmute":"Mở Tiếng"
    }
}

#File Type
TYPES ={
    0:{"English": 'All', 'Japanese': '全て',"Vietnamese": "Tất cả"},
    1:{"English": 'VectorWorks Files', 'Japanese': 'VectorWorks ファイル',  "Vietnamese": "Tập tin VectorWorks"},
    2:{"English": 'CAD Files', 'Japanese': 'CAD ファイル',  "Vietnamese": "Tập tin CAD"},
    3:{"English": 'Excel Files', 'Japanese': 'Excel ファイル',  "Vietnamese": "Tập tin Excel"},
    4:{"English": 'PDF Files', 'Japanese': 'PDF ファイル',  "Vietnamese": "Tập tin PDF"},
    5:{"English": 'DXF Files', 'Japanese': 'DXF ファイル',  "Vietnamese": "Tập tin DXF"},
    6:{"English": 'Image Files', 'Japanese': '画像 ファイル',"Vietnamese": "Tập tin hình ảnh"},
    7:{"English": 'Video Files', 'Japanese': '動画 ファイル',"Vietnamese": "Tập tin video"},
    8:{"English": 'Word Files', 'Japanese': 'Word ファイル',  "Vietnamese": "Tập tin Word"},
    9:{"English": 'Text Files', 'Japanese': 'テキスト ファイル',"Vietnamese": "Tập tin text"},
    10:{"English": 'Audio Files', 'Japanese': '音声 ファイル',"Vietnamese": "Tập tin âm thanh"},
    11:{"English": 'Program Files', 'Japanese': 'プログラム ファイル', "Vietnamese": "Tập tin chương trình"},
    12:{"English": 'Executable Files', 'Japanese': '実行可能 ファイル', "Vietnamese": "Tập tin thực thi"}
    }


OPTIONS ={"English":{"AND":"All matched (AND)","OR":"Contain(OR)","NOT"  :"Not contain(NOT)"},
        "Japanese":{"AND":"全て一致(AND)","OR":"いずれか(OR)","NOT"  :"いずれか除外(NOT)"},
        "Vietnamese":{"AND":"Tất cả(AND)","OR":"Bao hàm(OR)","NOT"  :"Không bao hàm(NOT)"}}

#Search Text Placeholder
PLACE_HOLDER={"English":"Input search keywords",
            "Japanese":"検索キーワードを入力",
            "Vietnamese":"Nhập từ khóa tìm kiếm"}
#Form Hints
HINT ={
    "Dialog" :{"English":"Click to change search folder",
            "Japanese":"クリックして検索フォルダを変更",
            "Vietnamese":"Click để thay đổi đường dẫn tìm kiếm"},
    "Search":{"English":"Multiple keywords are separated by ',:;' or spaces, '*' for show all",
                "Japanese":"複数のキーワードは半角で英字、数字、記号とし',:;'または空白で区切って入力,'*'は全て表示",
                "Vietnamese":"Các từ khóa cách nhau bởi ',:;' hoặc khoảng trắng,'*' để hiển thị tất cả"},
    "Logic" : {"English":
                {
                0: "Any of the keywords matches",
                1: "All of the keywords matches, ignore order",
                2: "Not contain all keywords"
                },
            "Japanese":{
                0: "いずれかのキーワードに一致",
                1: "順番問わず、全てのキーワードに一致",
                2: "全てのキーワードに一致しない"
                },
            "Vietnamese":{
                0: "Có ít nhất một từ khóa ",
                1: "Tất cả đều tìm thấy , không cần thứ tự",
                2: "Không chứa tất cả các từ khóa này"
                }
            },
    
    "Type" : {"English":"Select file type",
            "Japanese":"ファイルタイプを選択",
            "Vietnamese":"Chọn Lodi tập tin"},

    "Folder" : {"English":"Double Click to change search folder",
                "Japanese":"ダブルクリックしてフォルダを選択、再検索",
                "Vietnamese":"Click đúp để chọn đường dẫn tìm kiếm, tìm kiếm lại"},

    "File" : {"English":"Double Click to go file location",
            "Japanese":"ダブルクリックしてファイルの場所を開く",
            "Vietnamese":"Click đúp để đi tới vị trí tập tin"}

}
#-------------PREVIEW MESSAGE---------------------------------
PREVIEW ={
    # File Selected state
    "Select":{
        "First":{
            "English":"No File selected!\nDrag vertical and horizontal splitter to shrink ,expand window",
            "Japanese":"選択ファイルがありません!\n横、縦のスプリッターのドラッグにより、窓を拡大と縮小します。",
            "Vietnamese":"Chưa chọn tập tin nào!\nDi chuyển đường phân cách lên xuống , trái phải để điểu chỉnh cửa sổ",
        },
        "None": {
            "English":"No File selected!",
            "Japanese":"選択ファイルがありません!",
            "Vietnamese":"Chưa chọn tập tin nào!",
        },
        "Empty": {
            "English":"No file available!",
            "Japanese":"ファイルがありません!",
            "Vietnamese":"Không có tập tin nào!",
        },
    },
    #Show file
    "None":{
        "Read":{
            "English":"No thing Preview!",
            "Japanese":"プリビュー無し!",
            "Vietnamese":"Không có gì để xem!",
            },
    },
    #Preview file
    "Support":{
        "View":{
                "English":"[Unsupported file type!]",
                "Japanese":"[ファイル形式非対応!]",
                "Vietnamese":"[Không hỗ trợ loại file này!]",
            },
        "File":{
            "English":"Cannot Preview File!",
            "Japanese":"ファイルプリビュー出来ません!",
            "Vietnamese":"Không xem file được!",
            }
        },
    "PDF" :{"Load" :{
                "English" :"[Cannot load PDF file]",
                "Japanese":"[PDFファイルをロード不可]",
                "Vietnamese":"[Không thể đọc được file PDF]",
                },
            "View":{
                "English" :"[PDF preview failed]",
                "Japanese":"[PDFプレビューが失敗しました]",
                "Vietnamese":"Không thể xem được file PDF",
            }},
    "Image":{
        "Load":{
            "English" :"[Cannot load image file : ]",
            "Japanese":"[画像ファイルを読み込み不可 : ]",
            "Vietnamese":"[Không thể đọc được file ảnh : ]",
        }
        
    },
    "Text": {
        "Truncate":{
            "English":["Showing first","lines","chars"],
            "Japanese":["最初の","ライン","文字"],
            "Vietnamese":["Hiện ","dòng đầu"," từ "],
        },
        "Empty":{
            "English" :"[Empty file]",
            "Japanese":"[空ファイル]",
            "Vietnamese":"[Tập tin rỗng]",
        },
        "Read":{
            "English" :"[Cannot read plain text file! : ]",
            "Japanese":"[プレインテキストファイルを読み込み不可! : ]",
            "Vietnamese":"[Không thể đọc được file văn bản]! : ",
        },
    },
    "CSV": {
        "Read":{
            "English" :"[Cannot read CSV file! : ]",
            "Japanese":"[CSVファイルを読み込み不可! : ]",
            "Vietnamese":"[Không thể đọc được file CSV]! : ",
        },
        "Truncate":{
            "English":["Showing first","lines"],
            "Japanese":["最初の","ライン"],
            "Vietnamese":["Hiện ","dòng đầu"],
        },
    },
    "Doc": {
        "Convert":{
            "English":"[Failed to convert doc to docx!]\n Need to be install LibreOffice",
            "Japanese":"[docからdocxの形式へ変換失敗!]\n'Libre Office'のアプリをインストールしてください。",
            "Vietnamese":"[Đổi định dạng doc sang docx thất bại]\n Bạn cần cài đặt thêm bộ Libre Office",
        },
        "Truncate":{
            "English":"[Truncate]",
            "Japanese":"[中略]",
            "Vietnamese":"[Lược bỏ]",
        },
        "Empty":{
            "English" :"[Empty file]",
            "Japanese":"[空ファイル]",
            "Vietnamese":"[Tập tin rỗng]",
        },
        "Read":{
            "English" :"[Cannot read plain text file! : ]",
            "Japanese":"[プレインテキストファイルを読み込み不可! : ]",
            "Vietnamese":"[Không thể đọc được file văn bản]! : ",
        },
        "File":{
            "English" :"[Import Mammoth module failed!]",
            "Japanese":"[Mammothのモジュールの読込失敗!]",
            "Vietnamese":"[Không thể đọc module Mammoth!]",
        },
        "Allow":{
                "English" :["Cannot find converted file — Likely,","blocked the write operation"],
                "Japanese":["ファイルの変換不可です。恐らく","が書込みを禁止するようです。"],
                "Vietnamese":["Chuyển đổi tập tin thất bại.Có thể ","cấm cho ghi!]"],
                },
    },
    "Excel" :{
        "Read":{
            "English" :"[Cannot read xls file!]",
            "Japanese":"[xlsファイルの読込失敗!]",
            "Vietnamese":"[Không thể đọc được file xls!]",
        },
        "View":{
            "English" :"[Cannot preview excel file!]",
            "Japanese":"[Excelファイルのプリビュー失敗!]",
            "Vietnamese":"[Không thể xem được file Excel!]",
        }
    },
    "Media": {
        "FLV" :{
            "English" :"[Converting FLV… Please wait]",
            "Japanese":"[FVLを変換中、少々お待ちください]",
            "Vietnamese":"[Xin đợi một chút, đang chuyển đổi file FLV!]",
        },
        "Convert" :{
            "English" :"[Failed to convert FLV]",
            "Japanese":"[FVLの変換失敗!]",
            "Vietnamese":"[Chuyển đổi FLV thất bại!]",
        },
        "Prepare" :{
            "English" :"[Preparing media]",
            "Japanese":"[メディア待機中]",
            "Vietnamese":"[Tập tin Media đang chuẩn bị!]",
        },
        "Failed":{
            "English" :"[Cannot prepare media]",
            "Japanese":"[メディア再生不可!]",
            "Vietnamese":"[Chuyển đổi FLV thất bại!]",
        }
    }
}
GUIDE = {
    "Title" :{
        "English" :"Guidance",
        "Japanese":"案内",
        "Vietnamese":"Hướng dẫn sử dụng",
    },
    
    
}