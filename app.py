from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Sales',
        'location': 'Scranton',
        'name': 'Jim'
    },
    {
        'id': 2,
        'title': 'Actor',
        'location': 'England',
        'name': 'Emily'
    },
    {
        'id': 3,
        'title': 'Receptant',
        'location': 'Scranton',
        'name': 'Pam'
    }
]

@app.route("/")
def home():
    return render_template('home.html', jobs=JOBS, company_name='Dunder Mifflin')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)