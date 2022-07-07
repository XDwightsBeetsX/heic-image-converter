import sys
from heic_image_converter.globals import *
from heic_image_converter.Converter import Converter


# (ENTRY)
# EX: > python [path/to/convert.py](0) [path/to/sourceDir](1) --to(2) [saveAs](3) --dest(4) [path/to/saveDir](5) --del
if __name__ == "__main__":
	print(f"{PRE}running...")
	
	ImgConverter = Converter(sys.argv[1:])
	ImgConverter.convert_files()

	print(f"{PRE}finished.")
