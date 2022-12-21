import os
from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS, cross_origin
import cv2
import numpy as np
from dt import img, video, webcam
app = Flask(__name__)

# Apply Flask CORS
CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = "static"

@app.route("/", methods=["POST","GET"])
def detect():
    if request.method == "POST":
        file_end = request.files['method1']
        img_end = ['jpg', 'png']
        video_end = ['mp4', 'avi']
        
        if file_end.filename.split('.')[-1] in img_end:
            path_to_save = os.path.join(app.config['UPLOAD_FOLDER'], file_end.filename)
            print("Save = ", path_to_save)
            file_end.save(path_to_save)
            results = img(path_to_save)

            cv2.imwrite(path_to_save, results)
            return render_template("index.html", file = file_end.filename, img_end = img_end)
        elif file_end.filename.split('.')[-1] in video_end:
            path_to_save = os.path.join(app.config['UPLOAD_FOLDER'], file_end.filename)
            print("Save = ", path_to_save)
            file_end.save(path_to_save)
            video(path_to_save)
            return render_template("index.html", file = file_end.filename, video_end = video_end)
        else: 
            # webcam()
            return render_template("index.html", file = 1)


    return render_template("index.html", file = 0)

if __name__ == "__main__":
    app.run(host="0.0.0.0")  # debug=True causes Restarting with stat