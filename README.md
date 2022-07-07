# Convert those Pesky `.HEIC` Images to Something More Useful!

i-Device images often come in `.heic` image file format, but these don't translate well to other uses...

I had a bunch of downloaded `.heic` files but wanted to convert them to `.png` format so I wrote this converter!

## Notes

- no suitable package was found to convert `.heic` ➡️ `.jpg` on Windows.
- panoramic or stretched images may not convert properly.
- skips already-converted files to prevent redundancy

## Usage

You can use this code by **[installing the PYPI package](#package-install)** ***OR*** **[manually installing](#manual-install)**.

### Package Install

1. Download from [PYPI](https://pypi.org/project/heic-image-converter/) via command line

	```shell
	shell> pip install heic-image-converter
	```

2. Use the [`heic_image_converter/Converter.py`](heic_image_converter/Converter.py)

	```python
	import sys
	from heic_image_converter.Converter import Converter

	# EX: > python [path/to/convert.py](0) [path/to/sourceDir](1) --to(2) [saveAs](3) --dest(4) [path/to/saveDir](5) -del
	if __name__ == "__main__":
		ImgConverter = Converter(sys.argv[1:])
		ImgConverter.convert_files()
	```

### Manual Install

1. ***Download the repo*** [**`.zip`**](https://github.com/XDwightsBeetsX/image-converter/archive/refs/heads/master.zip)
2. ***Install required packages***
	```shell
	shell> pip install pillow_heif
	shell> pip install pillow # (optional): can use default `PIL` (legacy)
	``` 
3. Obtain the ***path to the python `main.py` program***
4. Obtain the ***path to the `.heic` image folder***
5. Run the python script with the desired [flags](#flags)

> *if you run into [usage](#usage) issues, check that you have installed the [requirements](./requirements.txt)*

## Examples

- Set the destination folder with `--dest`

	<img src="docs/img/sample_run1.png" style="width:800px; height:auto;" alt="set custom destination folder" title="set custom destination folder">

- Automatically delete converted files with `-del`

	<img src="docs/img/sample_run2.png" style="width:800px; height:auto;" alt="set delete flag" title="set delete flag">

## Flags

- double-hyphen '`--`' flags take arguments
- single-hyphen '`-`' flags are booleans

| Flag      | Options            | Description |
|  :-:      | :--                | :--         |
| `--to`    | `png`              | sets the desired type to convert the `.heic` files to. |
| `--dest`  | `path/to/saveDest` | choose the save location for the converted files. |
| `-del`    | `none`             | delete the original `.heic` file after successful conversions. |

> *if you have comments / suggestions / bug fixes, please make a github issue [here](https://github.com/XDwightsBeetsX/heic-image-converter/issues)*
> 
> *thanks for checking this project out :)*
