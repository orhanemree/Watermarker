from flask import Flask, request, render_template
from os import path
from watermarker import add_watermark

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static"

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/download", methods=["GET", "POST"])
def download():
    if request.method == "POST":

        # input image
        input = request.files["input"]

        # watermark image
        watermark = request.files["watermark"]

        filename = add_watermark(input, watermark, watermark_size=int(request.form["size"]), transparency=int(request.form["transparency"]), margin=int(request.form["margin"]))

        return render_template("download.html", filename=filename)

if __name__ == '__main__':
    app.run(debug=True)