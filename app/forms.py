from flask.ext.wtf import Form, TextField, TextAreaField, BooleanField, Required, SelectField

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

