from flask.ext.wtf import Form, TextField, TextAreaField, BooleanField, Required, SelectField, IntegerField, DateTimeField

class LoginForm(Form):
	openid = TextField('openid', validators = [Required()])
	remember_me = BooleanField('remember_me', default = False)
	
class NewSetForm(Form):
	total_yardage = TextField('total_yardage', validators = [Required()])
	type_of_set = SelectField('total_yardage', choices=[('mid', 'Middle Distance'),
		('long', 'Long Distance'), ('short', 'Short Distance')])
	stroke = SelectField('stroke', choices=[('FR', 'Freestyle'), ('BR', 'Breastroke'), 
		('BK', 'Backstroke'), ('FL', 'Butterfly'), ('DR', 'Drill'), 
		('KI', 'Kick'), ('PU', "Pull")])
	interval = SelectField('interval', choices = [(None, ''), ('1:15', '1:15'), ('1:20', '1:20'), ('1:25', '1:25'),
		('1:30', '1:30'), ('1:40', '1:40'), ('1:50', '1:50'), ('2:00', '2:00')])
	reps = IntegerField('reps')
	items = SelectField('items', choices=[(25, 25), (50, 50), (75, 75),
				(100, 100), (125, 125), (150, 150), (175, 175),
				(200, 200), (225, 225), (250, 250), (300, 300),
				(400, 400), (450, 450), (500, 500), (600, 600),
				(800, 800), (1000, 1000), (1650, 1650) ])
	int_for_set = DateTimeField('int_for_set')

