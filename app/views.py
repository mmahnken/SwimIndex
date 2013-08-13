from flask import render_template, flash, redirect, session, url_for, request
from app import app, db
from swim2 import makeSet, setStroke, totalTime, setInterval, totalYardage 
from forms import NewSetForm
from models import Set, Workout, FreestyleInt
import saving
from saving import saving_Set, creating_Workout, queryConfig

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
	if 'workout' in session:
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
	return render_template('yourworkout.html', sets = sets)

@app.route('/charts')
def charts():
	all_freestyle_ints = FreestyleInt.query.all()
	chart_names = ["25 Yards", "50 Yards", "75 Yards",
	"100 Yards", "125 Yards", "150 Yards", "175 Yards",
	"200 Yards", "225 Yards", "250 Yards",
	"300 Yards", "400 Yards", "450 Yards", "500 Yards",
	"600 Yards", "800 Yards", "1000 Yards", "1650 Yards"]
	return render_template("charts.html", 
	all_freestyle_ints = all_freestyle_ints,
	chart_names = chart_names)

@app.route('/create_own_set')
def create_own_set():
	form = NewSetForm()
	return render_template("create_own_set.html", form = form)

@app.route('/add_own_set', methods = ["POST", "GET"])
def add_own_set():
	print ""
	print "speed for 10X100 is:"
	print request.form['interval']
	print ""
	swim_set_array = {}
	swim_set_array['easy'] = None
	swim_set_array['stroke'] = request.form["stroke"]
	swim_set_array['reps'] = request.form['reps']
	swim_set_array['items'] = request.form['items']
	a = swim_set_array['items']
	if a==25 or a==50 or a==75 or a==100:
		swim_set_array['type_of_set'] = 'short'
	elif a==125 or a==150 or a==175:
		swim_set_array['type_of_set'] = 'mid'
	else:
		swim_set_array['type_of_set'] = 'long'
	if request.form['interval'] is not None:
		swimmer=FreestyleInt.query.filter_by(speed = request.form['interval']).first()
		print "query successful"
		print swimmer
		print "this swimmers time fo ra 25 is:"
		print swimmer.a25
		int_for_set = queryConfig(request.form['items'], swimmer)
		print int_for_set
		swim_set_array['interval'] = int_for_set
	else:
		swim_set_array['interval'] = request.form['int_for_set']
	totalYardage(swim_set_array)
	set_id = saving_Set(swim_set_array)		#savingSet returns the set's id in the db.
	time = totalTime(swim_set_array)
	print ''
	print swim_set_array
	print swim_set_array['reps']
	print type(swim_set_array['reps'])
	print ''
	session['sets'] = swim_set_array
	return render_template("newset.html", 
		set_dict = session['sets'], 
		set_id = set_id)




