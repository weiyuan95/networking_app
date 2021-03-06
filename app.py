from flask import Flask, url_for, g, render_template, make_response
from flask_cors import CORS
from helpers import headers
import time

app = Flask(__name__)
CORS(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/image")
def load_image():
    # assume a square image is used the original
    # and that each box is 50px * 50px
    IMAGE_DIMENSION = 1000
    IMAGE_EXT = ".png"
    BOX_SIZE = 50
    IMAGES_PER_COL = IMAGE_DIMENSION // BOX_SIZE

    table_contents = []

    last_col_num = (IMAGES_PER_COL * (IMAGES_PER_COL - 1)) + 1
    first_row_box_filenums = range(1, last_col_num+1, IMAGES_PER_COL)

    for increment in range(IMAGES_PER_COL):
        table_contents.append("<tr>")

        for start_col_num in first_row_box_filenums:
            box_num = start_col_num + increment

            image_path = f"cropped_images/subpic_{box_num}{IMAGE_EXT}"
            image_tag = f"<img src='{url_for('static', filename=image_path)}'/>"
            table_contents.append(f"<td>{image_tag}</td>")

        table_contents.append("</tr>")

    table_string = "".join(table_contents)

    return render_template("image.html",
                            table_contents=table_string)

@app.route("/hpack")
def hpack():
    resp = make_response("SSS was a hard mod")
    resp.headers.update(headers.generate_headers(26))
    return resp

@app.route("/oneimage")
def load_one_image():
    table_string = ""
    image_tag = f"<img height='50px' width='50px' src='{url_for('static', filename='original.jpg')}'/>"

    NUM_ROWS = 50
    NUM_COLS = 50

    for row_num in range(NUM_ROWS):
        table_string += "<tr>"

        for col_num in range(NUM_COLS):
            table_string += f"<td>{image_tag}</td>"

        table_string += "</tr>"

    return render_template("image.html",
                        table_contents=table_string)


if __name__ == "__main__":
    app.run(debug=True)
