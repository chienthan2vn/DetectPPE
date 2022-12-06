import os
from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS, cross_origin
import cv2
import numpy as np
from dt import img, video, mode
app = Flask(__name__)

# Apply Flask CORS
CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = "static"

@app.route("/", methods=["POST","GET"])
def detect():
    if request.method == "POST":
        if request.files['method1'].filename != None:
            image = request.files['method1']
            if image:
            # Lưu file
                path_to_save = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
                print("Save = ", path_to_save)
                image.save(path_to_save)

            results = img(path_to_save)

            cv2.imwrite(path_to_save, results)
            return redirect(path_to_save)

        elif request.files['method2'].filename != None:
            print(request.files['method2'].filename)
            vid = request.files['method2']
            if vid:
            # Lưu file
                path_to_save = os.path.join(app.config['UPLOAD_FOLDER'], vid.filename)
                print("Save = ", path_to_save)
                vid.save(path_to_save)
                video(path_to_save)

        # if method3:
        #     # Lưu file
        #     vid.video(0)
                

    return render_template("index.html")

# @app.route("/image", methods=["POST","GET"])
# def predict():
#     if request.method == "POST":
#         image = request.files['method1']
#         if image:
#             # Lưu file
#             path_to_save = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
#             print("Save = ", path_to_save)
#             image.save(path_to_save)

#         from dt import img, video

#         results = img(path_to_save)

#         # results.render()  # updates results.imgs with boxes and labels
#         cv2.imwrite(path_to_save, results)
#         return redirect(path_to_save)

#     return render_template("image.html")

# @app.route("/video", methods=["POST","GET"])
# def predict():
#     if request.method == "POST":
#         image = request.files['file']
#         if image:
#             # Lưu file
#             path_to_save = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
#             print("Save = ", path_to_save)
#             image.save(path_to_save)

#         from dt import img, video

#         results = img(path_to_save)

#         # results.render()  # updates results.imgs with boxes and labels
#         cv2.imwrite(path_to_save, results)
#         return redirect(path_to_save)

#     return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")  # debug=True causes Restarting with stat