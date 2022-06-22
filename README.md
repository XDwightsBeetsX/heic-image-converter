# Convert those Pesky `.HEIC` Images to Something More Useful!

i-Device images often come in `.heic` image file format, but these don't translate well to other uses...

I had a bunch of downloaded `.heic` files but wanted to convert them to `.png` or `.jpg` format so I wrote this converter!

## Next Features

- `.heic` ➡️ `.jpg`
- `--dest` flag for custom save folder destination

## Usage

1. ***Install [required](#requirements) packages***
   1. `pip install pillow` (or use default `PIL` - legacy)
   2. `pip install pillow_heif`
2. ***Download the repo*** [**`.zip`**](https://github.com/XDwightsBeetsX/image-converter/archive/refs/heads/master.zip)
3. Obtain the ***path to the python `convert.py` program***
4. Obtain the ***path to the `.heic` image folder***

### Example:

```shell
> python .\src\convert.py .\test\heic
[IMG CONVERTER] - running...
[IMG CONVERTER] - image directory found: '.\test\heic'
[IMG CONVERTER] - [CONVERTING] - source:    '.\test\heic\IMG_1753.HEIC'
[IMG CONVERTER] - [CONVERTING] - new image: '.\test\heic\IMG_1753.png'
[IMG CONVERTER] - [CONVERTING] - source:    '.\test\heic\IMG_4499.HEIC'
[IMG CONVERTER] - [CONVERTING] - new image: '.\test\heic\IMG_4499.png'
[IMG CONVERTER] - [REPORT] - reporting file conversions...
[IMG CONVERTER] - [REPORT] - [1/2 COMPLETE] - .\test\heic\IMG_1753.png
[IMG CONVERTER] - [REPORT] - [2/2 COMPLETE] - .\test\heic\IMG_4499.png
[IMG CONVERTER] - [REPORT] - report done. 2/2 complete.
[IMG CONVERTER] - finished.
```

### [Requirements](requirements.txt)

I used the `Image` module from `pillow/PIL`, and the `pillow_heif` package to help with conversions:

```python
from PIL import Image
import pillow_heif
```
