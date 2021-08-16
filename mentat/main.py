from flask import Flask, render_template, redirect, request
from werkzeug.utils import secure_filename
import os

from resume_analyzer import find_keywords
from recommender import get_recommended_opportunities

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() == "pdf"

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        # handle file upload

        # check if the POST request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)

        # check if user submits nothing
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)

        # get file from request
        file = request.files['file']
        # check if user sends a valid file in pdf format
        if not file or not allowed_file(file.filename):
            flash("Selected file is not a valid pdf")
            return redirect(request.url)

        # check if upload folder exists
        if not os.path.exists(directory):
            os.makedirs(UPLOAD_FOLDER)

        # save file
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))

        # find keywords in file
        keywords = find_keywords(filename)

        # go to recommendations with keywords
        pass

    return render_template("index.html")

# an endpoint that expects keywords in the url query parameters
# ie. /recommendations?keyword=astronomy&keyword=astrophysics
@app.route("/recommendations", methods=["GET"])
def display_recommendations():
    args = request.args.to_dict(flat=False)
    if "keyword" in args:
        keywords = args["keyword"]
    else:
        keywords = []
    opportunities = get_recommended_oppurtunities(keywords)
    return render_template("recommendations.html", opportunities=opportunities)
