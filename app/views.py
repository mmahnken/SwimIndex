from flask import render_template, flash, redirect, session, url_for, request, g 
from app import app
from flask.ext.login import login_user, logout_user, current_user, login_required
from swim2 import makeSet, setStroke, totalTime, for115, for120, for125, for130, for140, for200 
from forms import NewSetForm
import saving
from saving import saving_Set

@app.route('/')
@app.route('/index')
def index():
	form = NewSetForm()
	return render_template('index2.html', form = form)

@app.route('/newset', methods = ["POST", "GET"])
def newset():
	stroke = request.form["stroke"]
	total_yardage = int(request.form["total_yardage"])
	type_of_set = request.form["type_of_set"]
	new_set = makeSet(total_yardage, type_of_set)
	setStroke(new_set, stroke)
	if request.form['interval'] != None:
		interval = request.form['interval']
	if interval == '115':
		for115(new_set)
	elif interval =='120':
		for120(new_set)
	elif interval =='125':
		for125(new_set)
	elif interval =='130':
		for130(new_set)
	elif interval =='140':
		for140(new_set)
	elif interval =='200':
		for200(new_set)
	else:
		pass
	set_as_string = str(new_set['reps']) + " X " + str(new_set['items']) + " " +str(new_set['stroke'])
	saving_Set(new_set)
	if new_set['interval'] != None and new_set['easy'] != None:
		time = totalTime(new_set).__str__()
		easy = new_set['easy']
		return render_template("newset.html", set = set_as_string,
			easy = easy, time = time, interval = new_set['interval'])
	elif new_set['interval'] == None and new_set['easy'] !=None:
		easy = new_set['easy']
		return render_template("newset.html", set = set_as_string,
			easy = easy)
	elif new_set['interval'] != None and new_set['easy'] ==None:
		time = totalTime(new_set).__str__()
		return render_template("newset.html", set = set_as_string,
			time = time, interval = new_set['interval'])
	else:
		return render_template("newset.html", set = set_as_string)

@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		session['remember_me'] = form.remember_me.data
		return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
	return render_template('login.html',
		title = 'Sign In',
		form = form,
		providers = app.config['OPENID_PROVIDERS'])

@app.before_request
def before_request():
	g.user = current_user

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

