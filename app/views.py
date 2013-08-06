from flask import render_template, flash, redirect, session, url_for, request
from app import app, db
from swim2 import makeSet, setStroke, totalTime, setInterval
from forms import NewSetForm
from models import Set, Workout
import saving
from saving import saving_Set, creating_Workout

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
	set_id = saving_Set(new_set)		#savingSet returns the set's id in the db.
	time = totalTime(new_set)
	session['sets'] = new_set
	return render_template("newset.html", 
		set_dict = session['sets'], 
		set_id = set_id)

@app.route('/add/<set_id>')
def add(set_id):
	if session['workout']:
		s = Set.query.filter_by(id=set_id).first()
		print s.id
		print s.stroke
		s.workout_id = session['workout']
		print session['workout']
		db.session.commit()
	else:
		workout_id = creating_Workout()
		session['workout'] = workout_id
		s = Set.query.filter_by(id=set_id)
		s.workout_id = workout_id
		db.session.commit()
	return redirect('yourworkout')

@app.route('/yourworkout')
def yourworkout():
	w = session['workout']
	sets = Set.query.filter_by(workout_id = w).all()
	print sets[0]
	return render_template('yourworkout.html', sets = sets)


