from flask import Flask, render_template
from flask import request
import os, cv2
import numpy as np
from dotenv import dotenv_values

from app.verify import *

env = dotenv_values()
db_path = env.get("db_path","database")
if db_path == "database" or not os.path.exists(db_path):
    try: os.mkdir("database")
    except: pass
    db_path = "database"

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add/name", methods = ["GET", "POST"])
def add_name():
    if request.method == "GET":
        return render_template("addName.html", message = "GET")
    elif request.method == "POST":
        os.mkdir(db_path+f"/{request.form.get('name')}")
        return render_template("addName.html", message = "Added")
    return "Invalid"

@app.route("/add/face", methods = ["GET", "POST"])
def add_face_to_name():
    if request.method == "GET":
        return render_template("addFace.html", message = "GET")
    elif request.method == "POST":
        name = request.form.get('name')
        if os.path.exists(db_path+f"/{name}"):
            file = request.files['file']
            if file:
                l = len(os.listdir(db_path+f"/{name}"))
                file.save(db_path+f"/{name}/"+str(l)+".jpg")
                return render_template("addFace.html", message = "Added")
            return render_template("addFace.html", message = "Something went wrong")
        return render_template("addFace.html", message = "Add user first")
    return "Invalid"

@app.route("/verify", methods = ["GET", "POST"])
def verify_faces():
    if request.method == "GET":
        return render_template("verifyFaces.html", message = "GET")
    elif request.method == "POST":
        file1 = request.files['file1']
        file2 = request.files['file2']
        img1 = cv2.imdecode(np.frombuffer(file1.read(), np.uint8),cv2.IMREAD_UNCHANGED)
        img2 = cv2.imdecode(np.frombuffer(file2.read(), np.uint8),cv2.IMREAD_UNCHANGED)
        result = verify(img1, img2)
        if result['verified'] == True:
            message = "Matched\n" + str(result)
        else:
            message = "Not Matched\n" + str(result)
        return render_template("verifyFaces.html", message = message)
    return "Invalid"

@app.route("/find", methods = ["GET", "POST"])
def find_face():
    if request.method == "GET":
        return render_template("findFace.html", message = "GET")
    elif request.method == "POST":
            file = request.files['file']
            image = cv2.imdecode(np.frombuffer(file.read(), np.uint8),cv2.IMREAD_UNCHANGED)
            result = find(image, db_path)
            return render_template("findFace.html", message = result)
    return "Invalid"