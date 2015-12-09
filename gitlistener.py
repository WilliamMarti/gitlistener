from flask import Flask
from flask import render_template, request
from subprocess import call
import git, json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def index():
	
	jsondata = request.get_json()

	
	passedpw =  jsondata["hook"]["config"]["secret"]

	f = open('keyfile.txt', 'r')
	key = f.readline().strip()

	if (passedpw == key):
		print "Correct"

		filelocation = "/home/wmarti/github/lunch_app"

		g = git.cmd.Git(filelocation)
		g.pull()

	else:
		
		print "Wrong"

	return "Ran"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5001)




