from PIL import Image
import argparse

def add_watermark(input_path:str, output_path:str, watermark_path:str, watermark_size:int=50, transparency:int=150, margin:int=5):

    # open images
    input = Image.open(input_path)
    watermark = Image.open(watermark_path)

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
    output.save(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add watermark to your images")

    parser.add_argument("-i", "--input_path", required=True, help="input image path", type=str)
    parser.add_argument("-o", "--output_path", required=True, help="output image path", type=str)
    parser.add_argument("-w", "--watermark_path", required=True, help="output image path", type=str)
    parser.add_argument("-s", "--watermark_size", required=False, help="watermark size (default=50)",
                        type=int, default=50)
    parser.add_argument("-t", "--transparency", required=False, help="transparency (default=150)", type=int, default=150)
    parser.add_argument("-m", "--margin", required=False, help="margin (default=5)", type=int, default=5)

    args = parser.parse_args()

    add_watermark(args.input_path, args.output_path, args.watermark_path, watermark_size=int(args.watermark_size), transparency=args.transparency, margin=args.margin)
