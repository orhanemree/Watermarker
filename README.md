# Watermarker

💯 Watermark your images with one line of command

## 🧐 How to use:

````bash
$ git clone https://github.com/orhanemree/Watermarker.git
$ pip3 install -r requirements.txt
$ python watermarker.py --help
````

## 📎 Args
````bash
usage: watermarker.py [-h] -i INPUT_PATH -o OUTPUT_PATH -w WATERMARK_PATH [-s WATERMARK_SIZE [WATERMARK_SIZE ...]] [-m MARGIN]

Add watermark to your images

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_PATH, --input_path INPUT_PATH
                        input image path
  -o OUTPUT_PATH, --output_path OUTPUT_PATH
                        output image path
  -w WATERMARK_PATH, --watermark_path WATERMARK_PATH
                        output image path
  -s WATERMARK_SIZE [WATERMARK_SIZE ...], --watermark_size WATERMARK_SIZE [WATERMARK_SIZE ...]
                        watermark sizes (default=(50, 50))
  -m MARGIN, --margin MARGIN
                        margin (default=5)
````

## 🔎 Example
````bash
$ python watermarker.py -i "watermarker.png" -o "watermarked.png" -w "python-logo.png" -m 2
````

## 📃 License
* This project is licensed under the [MIT License](https://github.com/orhanemree/Watermarker/blob/master/LICENSE).