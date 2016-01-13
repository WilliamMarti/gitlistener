from flask import Flask
from flask import render_template, request
from subprocess import call
import git, json, os

newname = "gitlistener"
from ctypes import cdll, byref, create_string_buffer
    
libc = cdll.LoadLibrary('libc.so.6')    #Loading a 3rd party library C
buff = create_string_buffer(len(newname)+1) #Note: One larger than the name (man prctl says that)
buff.value = newname                 #Null terminated string as it should be
libc.prctl(15, byref(buff), 0, 0, 0) #Refer to "#define" of "/usr/include/linux/prctl.h" for the misterious value 16 & arg[3..5] are zero as the man page says.

import git, json
import os,sys

app = Flask(__name__)

@app.route("/", methods=['POST'])
def index():

	if request.method == 'POST':

		repo = git.Repo('/var/www/lunch_app')
		print repo.git.status()
		print repo.git.pull()
		
		f = open("keyfile.txt")
		pw = f.read()
		os.popen("sudo service apache2 restart", "w").write(pw)

	else:
		
		print "Wrong"

	return "Ran"


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001)




