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

        basedir = path.abspath(path.dirname(__file__))
        static = path.join(basedir, app.config["UPLOAD_FOLDER"])

        # input image
        input = request.files["input"]
        i_filename = f"upload.{input.filename.split('.')[1]}"
        input_path = path.join(static, i_filename)
        input.save(input_path)

        # watermark image
        watermark = request.files["watermark"]
        w_filename = f"watermark.{watermark.filename.split('.')[1]}"
        watermark_path = path.join(static, w_filename)
        watermark.save(watermark_path)

        add_watermark(input_path, input_path, watermark_path, watermark_size=(int(request.form["size"]), int(request.form["size"])), margin=int(request.form["margin"]))

        return render_template("download.html", filename=path.join("static/", i_filename))

if __name__ == '__main__':
    app.run(debug=True)