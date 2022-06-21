import sys
import os

from PIL import Image
import pillow_heif


EXPECTED_ARGS = 1  # > python [path/to/convert.py](0) [path/to/img_dir](1)
SAMPLE_CMD = "> python [path/to/convert.py] [path/to/img_dir]"
pre		= "[IMG CONVERTER] - "
conv	= "[CONVERTING] - "
rep		= "[REPORT] - "
err		= "[ERROR] - "


# temporarily only do '.heic' -> '.png'
def convert_files(dir_str, i_from=".heic", i_to=".png"):
	"""
	Converts files in `dir_str` from `i_from` to `i_to`
	
	returns lists of `complete, incomplete` filepaths
	"""
	# store a list of files that did not convert
	complete = []
	incomplete = []

	# go through files, check if have i_from extension, convert to i_to w/ same name
	dir_bytes = os.fsencode(dir_str)
	for file_bytes in os.listdir(dir_bytes):
		# obtain strings for path and filename
		filename = os.fsdecode(file_bytes)
		filepath = os.path.join(dir_str, filename)

		new_filename = filename.split(".")[0] + i_to
		new_filepath = os.path.join(dir_str, new_filename)
		
		# if file already exists in destination filetype, skip
		if os.path.isfile(new_filename):
			pass

		# file is desired source format, like '.heic', convert to desired format
		if filename.lower().endswith(i_from):
			try:
				# convert file and save
				heif_file = pillow_heif.read_heif(filepath)
				image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw")
				saveAs = i_to.split(".")[1]  # get format like '.png' -> 'png'
				image.save(new_filepath, format(saveAs))
				
				# console output
				print(f"{pre}{conv}source:    '{filepath}'")
				print(f"{pre}{conv}new image: '{new_filepath}'")
				complete.append(new_filepath)
			
			# there was an issue converting this file, note and continue
			except Exception:
				incomplete.append(filepath)
	
	# lists of complete and incomplete filepath strings
	return complete, incomplete


def report(complete, incomplete):
	"""Displays the completed and incomplete file conversions."""
	
	lc = len(complete)
	li = len(incomplete)

	print(f"{pre}{rep}reporting file conversions...")
	for i, inc in enumerate(incomplete):
		print(f"{pre}{rep}[{i+1}/{li} INCOMPLETE] - {inc}")
	for i, com in enumerate(complete):
		print(f"{pre}{rep}[{i+1}/{lc} COMPLETE] - {com}")
	print(f"{pre}{rep}report done. {lc}/{(lc + li)} complete.")


# (ENTRY)
if __name__ == "__main__":
	print(f"{pre}running...")

	try:
		# read and clean arg(s)
		if len(sys.argv) < EXPECTED_ARGS + 1:
			print(f"{pre}must supply image directory. EX: {SAMPLE_CMD}")
			print(f"{pre}quitting...")
			quit()
		path = sys.argv[1].strip()

		# check arg validity
		if not os.path.isdir(path):
			print(f"{err}image directory not found: '{path}'")
			print(f"{pre}quitting...")
			quit()
		
		# convert files
		print(f"{pre}image directory found: '{path}'")
		complete, incomplete = convert_files(path)

		# show report
		report(complete, incomplete)
		
		# done
		print(f"{pre}finished.")
		quit()
	
	# issue reading arguments
	except Exception as e:
		print(f"{err}an error occurred. message:")
		print(e)
		print(f"{pre}quitting...")
		quit()
