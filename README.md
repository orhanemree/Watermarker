# Watermarker

💯 Watermark your images with one line of command

## 🧐 How to use:

### ⌨️ From Command Line

````bash
$ git clone https://github.com/orhanemree/Watermarker.git
$ cd Watermarker
$ pip3 install -r requirements.txt
$ python watermarker.py --help
````

#### 📎 Args
````bash
usage: watermarker.py [-h] -i INPUT_PATH -w WATERMARK_PATH [-s WATERMARK_SIZE]
                      [-t TRANSPARENCY] [-m MARGIN] [-d DOWNLOAD]

Add watermark to your images

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_PATH, --input_path INPUT_PATH
                        input image path
  -w WATERMARK_PATH, --watermark_path WATERMARK_PATH
                        output image path
  -s WATERMARK_SIZE, --watermark_size WATERMARK_SIZE
                        watermark size (default=50)
  -t TRANSPARENCY, --transparency TRANSPARENCY
                        transparency (default=150)
  -m MARGIN, --margin MARGIN
                        margin (default=5)
  -d DOWNLOAD, --download DOWNLOAD
                        download (default=False)
````

#### 🔎 Example
````bash
$ python watermarker.py -i "images/input.png" -w "images/watermark.png" -s 100 -t 200 -m 50 -d True
````

### 🌐 From Local Web Server

````bash
$ git clone https://github.com/orhanemree/Watermarker.git
$ cd Watermarker
$ pip3 install -r requirements.txt
$ python app.py
````

Now, your local Watermarker is running on http://localhost:5000/upload

## ☑️ Todo
* [x] Add transparency option.
* [ ] Get ready to production mode.
* [ ] Convert images to PNG.

## 📃 License
* This project is licensed under the [MIT License](https://github.com/orhanemree/Watermarker/blob/master/LICENSE).