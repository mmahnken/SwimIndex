from flask import render_template, flash, redirect, session, url_for, request
from app import app, db
from swim2 import makeSet, setStroke, totalTime, setInterval
from forms import NewSetForm, LoginForm
import saving
from saving import saving_Set

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/create')
def create():
	form = NewSetForm()
	return render_template("create.html", form=form)

@app.route('/newset', methods = ["POST", "GET"])
def newset():
	stroke = request.form["stroke"]
	total_yardage = int(request.form["total_yardage"])
	type_of_set = request.form["type_of_set"]
	new_set = makeSet(total_yardage, type_of_set)
	setStroke(new_set, stroke)
	interval = request.form['interval']
	if interval != None:
		setInterval(new_set, interval)
	set_as_string = str(new_set['reps']) + " X " + str(new_set['items']) + " " +str(new_set['stroke'])
	saving_Set(new_set)
	time = totalTime(new_set)
	time = time.__str__()
	easy = new_set['easy']
	# return render_template("newset.html", set = set_as_string,
	# 	easy = easy, 
	# 	time = time, 
	# 	interval = interval)
	print "set added"
	print set_as_string
	return render_template('index.html')

