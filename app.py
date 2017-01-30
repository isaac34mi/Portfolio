from collections import defaultdict
from flask import Flask, render_template

app = Flask(__name__)

site = defaultdict(lambda: "404.html",{"resume": "resume.html", "about":"about.html", "project1":"projects.html"})


@app.route('/<page_name>')
def pages(page_name):
	return render_template(site[page_name])


if __name__ == '__main__':
	app.run(debug = True)