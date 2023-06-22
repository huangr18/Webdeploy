from flask import Flask, render_template, jsonify, request
from database import load_video_from_db, load_user_from_db
from upload_video import UploadFileForm
import os

app = Flask(__name__)




@app.route("/")
def home():
    jobs = load_video_from_db()
    return render_template('home.html', jobs=jobs, company_name='Dunder Mifflin')

@app.route("/api/jobs")
def list_jobs():
    jobs = load_video_from_db()
    return jsonify(jobs)

@app.route("/user/<id>")
def show_user(id):
    user = load_user_from_db(id)
    if not user:
        return "Not found", 404
    return render_template('upload.html', user=user)

@app.route("/user/<id>/upload", methods=['GET', 'POST'])
def user_upload(id):
    data = request.form
    # form = UploadFileForm()
    # if form.validate_on_submit():
    #     file = form.file.data
    return 'file has been uploaded', data

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

