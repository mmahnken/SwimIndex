from models import Set
from app import app, db

def saving_Set(swim_set_dict):
	s = Set(items = swim_set_dict['items'], 
	stroke = swim_set_dict['stroke'],
	interval = swim_set_dict['interval'],
	reps = swim_set_dict['reps'],
	easy = swim_set_dict['easy'],
	type_of_set = swim_set_dict['type_of_set'],
	total_yardage = swim_set_dict['total_yardage'])
	db.session.add(s)
	db.session.commit()
	return


