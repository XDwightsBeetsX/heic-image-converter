# Convert those Pesky `.HEIC` Images to Something More Useful!

i-Device images often come in `.heic` image file format, but these don't translate well to other uses...

I had a bunch of downloaded `.heic` files but wanted to convert them to `.png` or `.jpg` format so I wrote this converter!

## Next Features

- `.heic` ➡️ `.jpg` - *no suitable package found to develop on Windows for `.jpg` conversion. only png now*

## Usage

1. ***Install [required](#requirements) packages***
   1. `pip install pillow` (or use default `PIL` - legacy)
   2. `pip install pillow_heif`
2. ***Download the repo*** [**`.zip`**](https://github.com/XDwightsBeetsX/image-converter/archive/refs/heads/master.zip)
3. Obtain the ***path to the python `main.py` program***
4. Obtain the ***path to the `.heic` image folder***
5. Use desired [flags](#flags)

> *see the [Example](#example) below!*

## Flags

| Flag      | Options            | Description |
|  :-:      | :--                | :--         |
| `--to`    | `png`              | sets the desired type to convert the `.heic` files to. |
| `--dest`  | `path/to/saveDest` | choose the save location for the converted files. |
| `-del`    | `none`             | delete the original `.heic` file after successful conversions. |
### Example:

```shell
> python ./main.py test/heic --to png --dest test/png -del
[IMG CONVERTER] - running...
[IMG CONVERTER] - [SETUP] - '--to' flag set with 'png'.
[IMG CONVERTER] - [SETUP] - did not find the '--dest' directory. creating 'test/png'...
[IMG CONVERTER] - [SETUP] - created 'test/png'
[IMG CONVERTER] - [SETUP] - '--dest' flag set with 'test/png'.
[IMG CONVERTER] - [SETUP] - '-del' flag set.
[IMG CONVERTER] - [CONVERTING] - source: 'test/heic\IMG_1753.HEIC'
[IMG CONVERTER] - [CONVERTING] - new image: 'test/png\IMG_1753.png'
[IMG CONVERTER] - [CONVERTING] - '-del' flag has been set. removing 'test/heic\IMG_1753.HEIC'...
[IMG CONVERTER] - [CONVERTING] - source: 'test/heic\IMG_4499.HEIC'
[IMG CONVERTER] - [CONVERTING] - new image: 'test/png\IMG_4499.png'
[IMG CONVERTER] - [CONVERTING] - '-del' flag has been set. removing 'test/heic\IMG_4499.HEIC'...
[IMG CONVERTER] - [REPORT] - Reporting file conversions...
[IMG CONVERTER] - [REPORT] - [1/2 COMPLETE] - test/png\IMG_1753.png
[IMG CONVERTER] - [REPORT] - [2/2 COMPLETE] - test/png\IMG_4499.png
[IMG CONVERTER] - [REPORT] - report done. 2/2 complete.
[IMG CONVERTER] - finished.
```

### [Requirements](requirements.txt)

I used the `Image` module from `pillow/PIL`, and the `pillow_heif` package to help with conversions:

```python
from PIL import Image
import pillow_heif
```

> *if you have comments / suggestions / bug fixes, please make a github [issue](https://github.com/XDwightsBeetsX/heic-image-converter/issues)*
> 
> *thanks for checking this project out :)*