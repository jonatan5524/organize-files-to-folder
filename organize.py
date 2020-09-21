import os
import shutil
from os.path import expanduser

user_home_dir = expanduser("~")
download_dir = user_home_dir + "\\Downloads\\"

folders_names_list = [ 
    "Audio file formats" ,
    "Compressed files" ,
    "Disc and media files",
    "Data and database files",
    "E-mail files" ,
    "Executable files" ,
    "Font files",
    "Image file formats" ,
    "Internet related files" ,
    "Presentation file formats" ,
    "Programming files",
    "Spreadsheet file formats" ,
    "System related file formats" ,
    "Video file formats" ,
    "Word processor and text file formats",
    "Torrents"
]

file_extenstion_folder_kind_dict = {
    "aif": "Audio file formats",
    "cda": "Audio file formats",
    "mid": "Audio file formats",
    "midi": "Audio file formats",
    "mp3": "Audio file formats",
    "mpa": "Audio file formats",
    "ogg": "Audio file formats",
    "wav": "Audio file formats",
    "wma": "Audio file formats",
    "wpl": "Audio file formats",
    "7z": "Compressed files",
    "arj": "Compressed files", 
    "deb": "Compressed files",
    "pkg": "Compressed files",
    "rar": "Compressed files",
    "rpm": "Compressed files",
    "tar.gz": "Compressed files",
    "z": "Compressed files",
    "zip": "Compressed files",
    "bin": ["Disc and media files", "Executable files"],
    "dmg": "Disc and media files",
    "iso": "Disc and media files",
    "toast": "Disc and media files",
    "vcd": "Disc and media files",
    "csv": "Data and database files",
    "dat": "Data and database files",
    "db": "Data and database files",
    "dbf": "Data and database files",
    "log": "Data and database files",
    "mdb": "Data and database files",
    "sav": "Data and database files",
    "sql": "Data and database files",
    "tar": "Data and database files",
    "xml": "Data and database files",
    "email": "E-mail files",
    "eml": "E-mail files",
    "emlx": "E-mail files",
    "msg": "E-mail files",
    "oft": ["E-mail files", "Font files" ],
    "ost": "E-mail files",
    "pst": "E-mail files",
    "vcf": "E-mail files",
    "apk": "Executable files",
    "bat": "Executable files",
    "cgi": ["Executable files", "Internet related files", "Programming files" ],
    "gl": "Executable files",
    "com": "Executable files",
    "exe": "Executable files",
    "gadget": "Executable files",
    "jar": "Executable files",
    "msi": ["Executable files", "System related file formats" ],
    "py": ["Executable files", "Internet related files", "Programming files" ],
    "wsf": "Executable files",
    "fnt": "Font files",
    "fon": "Font files",
    "ttf": "Font files",
    "ai": "Image file formats",
    "bmap": "Image file formats",
    "gif": "Image file formats",
    "ico": ["Image file formats", "System related file formats" ],
    "jpeg": "Image file formats",
    "jpg": "Image file formats",
    "png": "Image file formats",
    "ps": "Image file formats",
    "psd": "Image file formats",
    "svg": "Image file formats",
    "tif": "Image file formats",
    "tiff": "Image file formats",
    "asp": "Internet related files",
    "aspx": "Internet related files",
    "cer": "Internet related files",
    "cfm": "Internet related files",
    "css": "Internet related files",
    "htm": "Internet related files",
    "html": "Internet related files",
    "js": "Internet related files",
    "jsp": "Internet related files",
    "part": "Internet related files",
    "rss": "Internet related files",
    "php": ["Internet related files", "Programming files"],
    "webp": "Internet related files",
    "xhtml": "Internet related files",
    "key": "Presentation file formats",
    "odp": "Presentation file formats",
    "pps": "Presentation file formats",
    "ppt": "Presentation file formats",
    "pptx": "Presentation file formats",
    "go": "Programming files",
    "c": "Programming files",
    "pl": ["Programming files", "Internet related files"],
    "class": "Programming files",
    "cpp": "Programming files",
    "cs": "Programming files",
    "h": "Programming files",
    "java": "Programming files",
    "sh": "Programming files",
    "swift": "Programming files",
    "vb": "Programming files",
    "bak": "System related file formats",
    "cab": "System related file formats",
    "cfg": "System related file formats",
    "cpl": "System related file formats",
    "cur": "System related file formats",
    "dll": "System related file formats",
    "dmp": "System related file formats",
    "drv": "System related file formats",
    "icns": "System related file formats",
    "ini": "System related file formats",
    "lnk": "System related file formats",
    "sys": "System related file formats",
    "tmp": "System related file formats",
    "ods":  "Spreadsheet file formats",
    "xls": "Spreadsheet file formats",
    "xlsm": "Spreadsheet file formats",
    "xlsx": "Spreadsheet file formats",
    "3g2": "Video file formats",
    "3gp": "Video file formats",
    "avi": "Video file formats",
    "flv": "Video file formats",
    "h264": "Video file formats",
    "m4v": "Video file formats",
    "mkv": "Video file formats",
    "mov": "Video file formats",
    "mp4": "Video file formats",
    "mpg": "Video file formats",
    "mpeg": "Video file formats",
    "rm": "Video file formats",
    "swf": "Video file formats",
    "vob": "Video file formats",
    "wmv": "Video file formats",
    "doc": "Word processor and text file formats",
    "docx": "Word processor and text file formats",
    "odt": "Word processor and text file formats",
    "pdf": "Word processor and text file formats",
    "rtf": "Word processor and text file formats",
    "tex": "Word processor and text file formats",
    "txt": "Word processor and text file formats",
    "torrent": "Torrents"
}

def create_link(position, pointing_to):
    try:
        print("lnk " + position + " --> " + pointing_to)
        os.link(pointing_to, position)
    except OSError as e:
        print("Creation of the link %s failed" % pointing_to)
        print(e)

def mv_file(src, dst):
    try:
        print("mv " + src + " --> " + dst)
        shutil.move(src, dst)
    except OSError as e:
        print("transfer of file %s failed" % src)
        print(e)

def run_on_files():
    for filename in os.listdir(download_dir):
        extenstion = filename.split(".")[-1].lower()
        if extenstion in file_extenstion_folder_kind_dict:
            folder = file_extenstion_folder_kind_dict[extenstion]
            if type(folder) is list:
                multiple_folders(filename, folder)
            else:
                transfer_file(filename, folder)

def transfer_file(filename, folder):
    src = download_dir + filename
    dst = download_dir + folder + "//" + filename
    mv_file(src, dst)

def multiple_folders(filename, folders):
    pointing_to = download_dir + folders[-1] + "//" + filename
    transfer_file(filename, folders[-1])
    for folder in folders[:-1]:
        position = download_dir + folder + "//" + filename
        create_link(position, pointing_to)
    

def create_directory(path):
    try:
        os.mkdir(path)
    except OSError as e:
        print("Creation of the directory %s failed" % path)
        print(e)
    else:
        print ("Successfully created the directory %s" % path)

def main():
    print("the user home directory %s" % user_home_dir)
    for name in folders_names_list:
        create_directory(download_dir + name)
    run_on_files()

if __name__ == "__main__":
    main()