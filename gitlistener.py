from flask import Flask
from flask import render_template
from subprocess import call
import git

app = Flask(__name__)

@app.route("/")
def index():
	
	filelocation = "/home/wmarti/github/lunch_app"

	g = git.cmd.Git(filelocation)
	g.pull()
	return "Hello" 

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001)




