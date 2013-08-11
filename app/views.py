from flask import render_template, flash, redirect, session, url_for, request
from app import app, db
from swim2 import makeSet, setStroke, totalTime, setInterval
from forms import NewSetForm
from models import Set, Workout, FreestyleInt
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

@app.route('/charts')
def charts():
	all_freestyle_ints = FreestyleInt.query.all()
	chart_names = ["25 Yards", "50 Yards", "75 Yards",
	"100 Yards", "125 Yards", "150 Yards", "175 Yards",
	"200 Yards", "225 Yards", "250 Yards",
	"300 Yards", "400 Yards", "450 Yards", "500 Yards",
	"600 Yards", "800 Yards", "1000 Yards", "1650 Yards"]
	columns = ['a25', 'a50', 'a75', 'a100', 'a125', 'a150', 'a175', 'a200',
	'a225', 'a250', 'a300', 'a400', 'a450', 'a500', 'a600', 'a800', 'a1000', 
	'a1650']
	return render_template("charts.html", 
	all_freestyle_ints = all_freestyle_ints,
	chart_names = chart_names,
	columns = columns)


