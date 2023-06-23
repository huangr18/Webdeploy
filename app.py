from flask import Flask, render_template, jsonify, request
from database import load_video_from_db, load_user_from_db, add_user_to_db
from upload_video import UploadFileForm
import os

app = Flask(__name__)



@app.route("/")
def home():
    users = load_user_from_db()
    return render_template('home.html', users=users, company_name='USS')

@app.route("/api/users")
def list_users():
    users = load_user_from_db()
    return jsonify(users)

@app.route("/user/<user_id>")
def show_user(user_id):
    user = load_video_from_db(user_id)
    if not user:
        return "Not found", 404
    return render_template('upload.html', user=user)

@app.route("/user/<user_id>/upload", methods=['GET', 'POST'])
def upload_video(user_id):
    user = load_video_from_db(user_id)
    return render_template('upload_success.html', user=user)

@app.route("/user/<id>/apply", methods=['GET', 'POST'])
def apply(id):
    data = request.form

    add_user_to_db(data)
    # send email
    return render_template('video.html', application=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)












# @app.route("/user/<id>/upload", methods=['GET', 'POST'])
# def user_upload(id):
#     data = request.form
#     videoPath = os.path.join(os.path.abspath(os.path.dirname(data.file)))
#     # isThereFile(data)
#     # form = UploadFileForm()
#     # if form.validate_on_submit():
#     print(videoPath)
#     return render_template('video.html', video=data, videoPath=videoPath)
