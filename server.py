from flask import *
from search import *
from flask_login.login_manager import *


app = Flask(__name__)


@app.route("/")
def home():
    return app.send_static_file("index.html")


@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)


@app.route("/search")
def search():
    data = request.args
    print data
    keyword = data["q"]
    print keyword
    jobs = []
    results = search_reddit(query = keyword)
    jobs = [r for r in results]

    return render_template("results.html", post_list = jobs)


@app.route("/email-form")
def email_form():
    return app.send_static_file("email.html")


app.run(debug=True)