import app
from flask import session
from app import app, db
from app import models, intervals

interval_dicts = [intervals.INTS_115, intervals.INTS_120, intervals.INTS_125, intervals.INTS_130, intervals.INTS_140, intervals.INTS_150, intervals.INTS_200]
speeds = ["1:15", "1:20", "1:25", "1:30", "1:40", "1:50", "2:00"]

for interval_dict in interval_dicts:	
	index_for_speed = interval_dicts.index(interval_dict)	
	s = models.FreestyleInt(a25 = interval_dict[25],
		a50 = interval_dict[50],
		a75 = interval_dict[75],
		a100 = interval_dict[100],
		a125 = interval_dict[125],
		a150 = interval_dict[150],
		a175 = interval_dict[175],
		a200 = interval_dict[200],
		a225 = interval_dict[225],
		a250 = interval_dict[250],
		a300 = interval_dict[300],
		a400 = interval_dict[400],
		a450 = interval_dict[450],
		a500 = interval_dict[500],
		a600 = interval_dict[600],
		a800 = interval_dict[800],
		a1000 = interval_dict[1000],
		a1650 = interval_dict[1650],
		speed = speeds[index_for_speed])
	db.session.add(s)
db.session.commit()
