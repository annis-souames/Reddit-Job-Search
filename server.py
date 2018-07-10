from flask import *
from search import *
app = Flask(__name__)

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/search")
def search():
    data = request.args
    print data
    keyword = data["q"]
    print keyword
    results = search_reddit(query = keyword)
    print results
    return render_template("results.html", post_list = results)

app.run(debug = True)