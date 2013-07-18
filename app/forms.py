from flask.ext.wtf import Form, TextField, TextAreaField, BooleanField, Required, SelectField

#class NewWorkoutForm(Form):
	

class NewSetForm(Form):
	total_yardage = TextField('total_yardage', validators = [Required()])
	type_of_set = SelectField('total_yardage', choices=[('mid', 'Middle Distance'),
		('long', 'Long Distance'), ('short', 'Short Distance')])
	stroke = SelectField('stroke', choices=[('FR', 'Freestyle'), ('BR', 'Breastroke'), 
		('BK', 'Backstroke'), ('FL', 'Butterfly'), ('DR', 'Drill'), 
		('KI', 'Kick'), ('PU', "Pull")])
	interval = SelectField('interval', choices = [(None, ''), ('115', '1:15'), ('120', '1:20'), ('125', '1:25'),
		('130', '1:30'), ('140', '1:40'), ('150', '1:50'), ('200', '2:00')])

