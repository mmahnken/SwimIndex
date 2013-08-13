from models import Set, Workout
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
	return s.id

def creating_Workout():
	w = Workout()
	db.session.add(w)
	db.session.commit()
	return w.id

def queryConfig(int_item, query_object):
	print "int_item is"
	print int_item
	print "in queryConfig, time for 800 is:"
	print query_object.a800
	if int_item== '25':
		int_for_set = query_object.a25
		return int_for_set
	elif int_item== None:
		int_for_set = None
		return int_for_set
	elif int_item == '50':
		int_for_set = query_object.a50
		return int_for_set
	elif int_item == '75':
		int_for_set = query_object.a75
		return int_for_set
	elif int_item == '100':
		int_for_set = query_object.a100
		print "int for set found successfully"
		return int_for_set
	elif int_item == '125':
		int_for_set = query_object.a125
		return int_for_set
	elif int_item == '150':
		int_for_set = query_object.a150
		return int_for_set
	elif int_item == '175':
		int_for_set = query_object.a175
		return int_for_set
	elif int_item == '200':
		int_for_set = query_object.a200
		return int_for_set
	elif int_item == '225':
		int_for_set = query_object.a225
		return int_for_set
	elif int_item == '250':
		int_for_set = query_object.a250
		return int_for_set
	elif int_item == '300':
		int_for_set = query_object.a300
		return int_for_set
	elif int_item == '400':
		int_for_set = query_object.a400
		return int_for_set
	elif int_item == '450':
		int_for_set = query_object.a450
		return int_for_set
	elif int_item == '500':
		int_for_set = query_object.a500
		return int_for_set
	elif int_item == '600':
		int_for_set = query_object.a600
		return int_for_set
	elif int_item == '800':
		int_for_set = query_object.a800
		return int_for_set
	elif int_item == '1000':
		int_for_set = query_object.a1000
		return int_for_set
	elif int_item == '1650':
		int_for_set = query_object.a1650
		return int_for_set
	else:
		return