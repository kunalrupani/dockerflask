from flask import Flask, redirect, url_for,request, render_template, Response, jsonify

#from pymongo import MongoClient

app = Flask(__name__)

#client = MongoClient()
#db= client.hcmdb


@app.route('/')
def todo():
	return "Hello!"

@app.route('/new', methods=['POST'])
def new():
		return redirect(url_for('todo'))

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)