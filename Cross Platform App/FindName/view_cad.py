import os,sys
# import olefile
import zipfile
from PIL import Image
import win32com.client
import shutil
import subprocess
#------------------------------------------------------------------
def main_cad( self,filepath, ext, ord):
   cache_path = "C:\MyData\VectorWork\cache"
   # Approach 1: Get Windows Thumbnail
   win_icon = window_nail(self,filepath,ord)
   print("Windows Thumbnail:", win_icon)
   # Approach 2: Extract Thumbnail from OLE file
   ole_thumb = extract_thumbnail(filepath, cache_path)  
   print("OLE Thumbnail:", ole_thumb)
   # Approach 3: Use freecad to render thumbnail (if applicable)
   print(render_with_freecad(self,filepath, cache_path))

   # ext = ext.lower()
   # if ext in ['.sldprt','.sldasm',"slddrw"]:
   #    solid_thumpnail(self,filepath,cache_path)
   # elif ext in ['.vwx','.mcd']:
   #    vector_thumpnail(self,filepath,cache_path)
#------------------------------------------------------------------
def window_nail(self,filepath,cache_path):
   try:
        shell = win32com.client.Dispatch("Shell.Application")

        folder = shell.NameSpace(os.path.dirname(filepath))
        item = folder.ParseName(os.path.basename(filepath))

        if item is None:
            return None

        # This retrieves the icon/thumbnail Windows uses
        icon = item.GetIconLocation(0)

        return icon

   except Exception as e:
        print("Windows thumbnail error:", e)

   return None

#------------------------------------------------------------------
def extract_thumbnail(filepath, cache_dir):

    try:

        if not olefile.isOleFile(filepath):
            return None

        ole = olefile.OleFileIO(filepath)

        if ole.exists("Preview"):

            data = ole.openstream("Preview").read()

            img = Image.open(io.BytesIO(data))

            out = os.path.join(cache_dir, "preview.png")

            img.save(out)

            return out

    except Exception as e:
        print("Thumbnail extraction error:", e)

    return None
#------------------------------------------------------------------
def render_with_freecad(self,filepath, cache_dir):
   freecad = r"C:\\Program Files\\FreeCAD 1.0\\bin\\FreeCADCmd.exe"
   output = os.path.join(cache_dir, "render.png")

   script = os.path.join(
      os.path.dirname(__file__),
   #   "engine",
      "cad_render.py"
   )

   try:
      filepath = filepath.encode('utf-8',"ignore").decode()
      output = output.encode('utf-8',"ignore").decode()
      script = script.encode('utf-8',"ignore").decode()
      subprocess.run(
         [freecad, 
         script, 
         filepath, 
         output],
         check=True
      )

      if os.path.exists(output):
         return output

   except Exception as e:
      print("FreeCAD render error:", e)

   return None
#------------------------------------------------------------------
# def solid_thumpnail(self,path,cahe_path):
#    try:
#       if not olefile.isOleFile(path):
#             print("Not an OLE file:", path)
#             return None
#       ole = olefile.OleFileIO(path)
#       if ole.exists("Preview"):

#             data = ole.openstream("Preview").read()

#             img = Image.open(io.BytesIO(data))

#             out = os.path.join(cache_dir, "preview_sw.png")
#             img.save(out)

#             return out
#       if ole.exists('Thumbnail'):
#          thumb = ole.openstream('Thumbnail')
#          img = Image.open(thumb)
#          img.save(os.path.join(cahe_path,os.path.basename(path)+".jpg"))
#          return os.path.join(cahe_path,os.path.basename(path)+".jpg")
#    except Exception as e:
#       print("Error in solid_thumpnail:", e)  
# #------------------------------------------------------------------
# def vector_thumpnail(self,path,cahe_path):
#    print("Vector Thumbnail")