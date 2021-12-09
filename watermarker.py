from PIL import Image
import argparse

def add_watermark(input_path:str, output_path:str, watermark_path:str, watermark_size:tuple=(50, 50), margin:int=5):

    # open images
    image = Image.open(input_path)
    watermark = Image.open(watermark_path)

    # crop watermark to size
    wm_size = (watermark_size[0], watermark_size[1])
    watermark.thumbnail(wm_size)

    # add watermark
    width, height = image.size
    position = (int(width - wm_size[0] - margin), int(height - wm_size[1] - margin))
    transparent = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    transparent.paste(image, (0, 0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.save(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add watermark to your images")

    parser.add_argument("-i", "--input_path", required=True, help="input image path", type=str)
    parser.add_argument("-o", "--output_path", required=True, help="output image path", type=str)
    parser.add_argument("-w", "--watermark_path", required=True, help="output image path", type=str)
    parser.add_argument("-s", "--watermark_size", required=False, help="watermark sizes (default=(50, 50))", nargs="+",
                        type=int, default=(50, 50))
    parser.add_argument("-m", "--margin", required=False, help="margin (default=5)", type=int, default=5)

    args = parser.parse_args()

    add_watermark(args.input_path, args.output_path, args.watermark_path, watermark_size=tuple(args.watermark_size), margin=args.margin)
