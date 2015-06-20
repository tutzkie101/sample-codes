from flask import Flask, request, render_template, jsonify
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException
import time


app = Flask(__name__)


@app.after_request
def after(response):
    if request.method == "GET":
        response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.route("/weeby/magic", methods=['GET', 'POST'])
def magic(): 
    # Happy hacking :)
	return counter(request.args.get('spell'))
	
def counter(spell):
	#print("asdasdasdasd " + spell)
	counterSpell = ""
	locator = 0
	while (len(spell) > (locator+1)):
		initStr = ""
		while (match(initStr) == "false"):
			initStr += spell[locator]
			locator += 1
		counterSpell += match(initStr)
	print(counterSpell)
	return counterSpell
	
def match(strMatch):
	if (strMatch=="foo"):
		return "qux"
	if (strMatch=="qux"):
		return "corge"
	if (strMatch=="corge"):
		return "foo"
		
	return "false"

@app.route("/weeby/key.css")
def cssKey():
	return render_template('key.html')
	
@app.route("/weeby/flappy",methods=['GET', 'POST'])
def flappyChart():	
	if request.method == 'POST':
		jj = request.get_json()
		time.sleep(10)
		return jsonify(queue=[1],next=jj['t']+1)
	if request.method == 'GET':
		print("Get Is Called")
		

if __name__ == "__main__":
    app.run(host="192.168.1.124", port=1337, debug=True)

