from PIL import Image
import argparse
import requests
import base64
from io import BytesIO

def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, "PNG")
    data = base64.b64encode(buffered.getvalue()).decode("utf-8")
    data_url = f"data:image/jpeg;base64,{data}"
    return data_url

def add_watermark(input_path:str, watermark_path:str, watermark_size:int=50, transparency:int=150, margin:int=5, download:bool=False):

    # open images
    try:
        input = Image.open(input_path)
        watermark = Image.open(watermark_path)
    except FileNotFoundError:
        response = requests.get(input_path)
        input = Image.open(BytesIO(response.content))
        response = requests.get(watermark_path)
        watermark = Image.open(BytesIO(response.content))

    # crop watermark to size
    watermark.thumbnail((watermark_size, watermark_size))
    wm = watermark.copy()
    wm.putalpha(transparency)
    watermark.paste(wm, watermark)

    # add watermark
    width, height = input.size
    position = (int(width - watermark_size - margin), int(height - watermark_size - margin))
    output = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    output.paste(input, (0, 0))
    output.paste(wm, position, mask=watermark)

    if download == True:
        output.save("images/output.png")

    return image_to_base64(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add watermark to your images")

    parser.add_argument("-i", "--input_path", required=True, help="input image path", type=str)
    parser.add_argument("-w", "--watermark_path", required=True, help="output image path", type=str)
    parser.add_argument("-s", "--watermark_size", required=False, help="watermark size (default=50)",
                        type=int, default=50)
    parser.add_argument("-t", "--transparency", required=False, help="transparency (default=150)", type=int, default=150)
    parser.add_argument("-m", "--margin", required=False, help="margin (default=5)", type=int, default=5)
    parser.add_argument("-d", "--download", required=False, help="download (default=False)", type=bool, default=False)

    args = parser.parse_args()

    add_watermark(args.input_path, args.watermark_path, watermark_size=int(args.watermark_size), transparency=args.transparency, margin=args.margin, download=args.download)
