from collections import defaultdict
from flask import Flask, render_template

app = Flask(__name__)

site = defaultdict(lambda: "404.html",{"resume": "resume.html", "about":"about.html", "project1":"projects.html","stats_app":"rFiles/statsApp.html"})

@app.route('/')
def index():
	return render_template("resume.html")

@app.route('/<page_name>')
def pages(page_name):
	return render_template(site[page_name])


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
