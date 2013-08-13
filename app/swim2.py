import random
import datetime
import intervals

def makeSet(total_yardage, size):
	if size == "short":
		types = [25, 50, 75, 100]
		t = random.choice(types)
		if total_yardage % t == 0:
			return {'reps': total_yardage/t, 'items':t, 'stroke':None, 'interval':None, 'easy':None, 'type_of_set':size, 'total_yardage':total_yardage}
		else:
			return {'reps': total_yardage/t, 'items':t, 'stroke':None, 'interval':None, 'easy':total_yardage%t, 'type_of_set':size, 'total_yardage':total_yardage}
	elif size == "long":
		types = [200, 225, 250, 300, 400, 450, 500, 600, 800]
		t = random.choice(types)
		if total_yardage % t == 0:
			return {'reps': total_yardage/t, 'items':t, 'stroke':None, 'interval':None, 'easy':None, 'type_of_set':size, 'total_yardage':total_yardage}
		else:
			return {'reps': total_yardage/t, 'items':t, 'stroke':None, 'interval':None, 'easy':total_yardage%t, 'type_of_set':size, 'total_yardage':total_yardage}
	elif size == "mid":
		types = [125, 150, 175]
		t = random.choice(types)
		if total_yardage % t == 0:
			return {'reps': total_yardage/t, 'items':t, 'stroke':None, 'interval':None, 'easy':None, 'type_of_set':size, 'total_yardage':total_yardage}
		else:
			return {'reps': total_yardage/t, 'items':t, 'stroke':None, 'interval':None, 'easy':total_yardage%t, 'type_of_set':size, 'total_yardage':total_yardage}
	else:
		return "invalid set size"


def setStroke(swim_set_array, stroke):
	if stroke == 'FR':
		swim_set_array['stroke'] = 'Freestyle'
		return swim_set_array
	elif stroke == 'BK':
		swim_set_array['stroke'] = 'Backstroke'
		return swim_set_array
	elif stroke == 'BR':
		swim_set_array['stroke'] = 'Breaststroke'
		return swim_set_array
	elif stroke == 'FL':
		swim_set_array['stroke'] = 'Butterfly'
		return swim_set_array
	elif stroke == 'DR':
		swim_set_array['stroke'] = 'Drill'
		return swim_set_array
	elif stroke == 'KI':
		swim_set_array['stroke'] = 'Kick'
		return swim_set_array
	elif stroke == 'PU':
		swim_set_array['stroke'] = 'Pull'
		return swim_set_array
	else:
		return "enter a valid stroke code"

def setInterval(swim_set_array, speed):
	if speed == "1:15":
		ints = intervals.INTS_115
		if swim_set_array["stroke"] == None or swim_set_array['stroke'] == 'Freestyle':	
			a = swim_set_array["items"]
			swim_set_array["interval"] = ints[a]
			return swim_set_array
		else:
			return swim_set_array
	elif speed == "1:20":
		ints  = intervals.INTS_120
		if swim_set_array["stroke"] == None or swim_set_array['stroke'] == 'Freestyle':	
			a = swim_set_array["items"]
			swim_set_array["interval"] = ints[a]
			return swim_set_array
		else:
			return swim_set_array
	elif speed == "1:25":
		ints = intervals.INTS_125
		if swim_set_array["stroke"] == None or swim_set_array['stroke'] == 'Freestyle':	
			a = swim_set_array["items"]
			swim_set_array["interval"] = ints[a]
			return swim_set_array
		else:
			return swim_set_array
	elif speed =="1:30":
		ints = intervals.INTS_130
		if swim_set_array["stroke"] == None or swim_set_array['stroke'] == 'Freestyle':	
			a = swim_set_array["items"]
			swim_set_array["interval"] = ints[a]
			return swim_set_array
		else:
			return swim_set_array
	elif speed =="1:40":
		ints = intervals.INTS_140
		if swim_set_array["stroke"] == None or swim_set_array['stroke'] == 'Freestyle':	
			a = swim_set_array["items"]
			swim_set_array["interval"] = ints[a]
			return swim_set_array
		else:
			return swim_set_array
	elif speed == "1:50":
		ints = intervals.INTS_150
		if swim_set_array["stroke"] == None or swim_set_array['stroke'] == 'Freestyle':	
			a = swim_set_array["items"]
			swim_set_array["interval"] = ints[a]
			return swim_set_array
		else:
			return swim_set_array
	elif speed == "2:00":
		ints = intervals.INTS_200
		if swim_set_array["stroke"] == None or swim_set_array['stroke'] == 'Freestyle':	
			a = swim_set_array["items"]
			swim_set_array["interval"] = ints[a]
			return swim_set_array
		else:
			return swim_set_array
	else:
		return "Invalid speed"
		


def for115(swim_set_array):
	ints = {25:"0:20", 50:'0:40', 75:'1:00', 100:"1:15", 125:"1:35",
		150:"2:00", 175:"2:15", 200:"2:30", 225:"2:50", 250:"3:10", 
		300:"3:45", 400:"5:00", 450:"5:40", 500:"6:15", 600:"7:30", 
		800:"10:00", 1000:"12:30", 1650:'20:40'}
	if swim_set_array["stroke"] == None or swim_set_array['stroke'] == 'Freestyle':	
		a = swim_set_array["items"]
		swim_set_array["interval"] = ints[a]
		return swim_set_array
	else:
		return swim_set_array


def for120(swim_set_array):
	ints = {25:'0:20', 50:'0:40', 75:'1:00', 100:'1:20', 125:'1:40', 
		150:'2:00', 175:'2:20', 200:"2:40", 225:'3:00', 250:'3:20', 
		300:"4:00", 400:'5:20', 450:'6:00', 500:'6:40', 600:'8:00',
		800:"10:40", 1000:"13:20", 1650:'22:00'}
	if swim_set_array["stroke"] == None or swim_set_array['stroke'] == 'Freestyle':	
		a = swim_set_array["items"]
		swim_set_array["interval"] = ints[a]
		return swim_set_array
	else:
		return swim_set_array


def for125(swim_set_array):
	ints = {25:'0:20', 50:'0:45', 75:'1:00', 100:"1:25", 125:'1:45',
	150:"2:05", 175:'2:30', 200:'2:50', 225:'3:10', 250:'3:35', 
	300:'4:15', 400:'5:40', 450:'6:25', 500:'7:05', 600:'8:30',
	800:'11:20', 1000:'14:10', 1650:'23:22'}
	if swim_set_array["stroke"] == None or swim_set_array['stroke'] == 'Freestyle':	
		a = swim_set_array["items"]
		swim_set_array["interval"] = ints[a]
		return swim_set_array
	else:
		return swim_set_array


def for130(swim_set_array):
	ints = {25:'0:25', 50:'0:45', 75:'1:10', 100:"1:30", 125:'1:50',
	150:"2:15", 175:'2:40', 200:'3:00', 225:'3:25', 250:'3:45', 
	300:'4:30', 400:'6:00', 450:'6:45', 500:'7:30', 600:'9:00',
	800:'12:00', 1000:'15:00', 1650:'24:25'}
	if swim_set_array["stroke"] == None or swim_set_array['stroke'] == 'Freestyle':	
		a = swim_set_array["items"]
		swim_set_array["interval"] = ints[a]
		return swim_set_array
	else:
		return swim_set_array


def for140(swim_set_array):
	ints = {25:'0:25', 50:'0:50', 75:'1:10', 100:"1:35", 125:'2:00',
	150:"2:22", 175:'2:45', 200:'3:10', 225:'3:35', 250:'4:00', 
	300:'4:45', 400:'6:20', 450:'7:10', 500:'7:55', 600:'9:30',
	800:'12:40', 1000:'15:50', 1650:'26:10'}
	if swim_set_array["stroke"] == None or swim_set_array['stroke'] == 'Freestyle':	
		a = swim_set_array["items"]
		swim_set_array["interval"] = ints[a]
		return swim_set_array
	else:
		return swim_set_array


def for150(swim_set_array):
	ints = {25:'0:30', 50:'0:55', 75:'1:25', 100:"1:50", 125:'2:20',
	150:"2:45", 175:'3:10', 200:'3:40', 225:'4:10', 250:'4:35', 
	300:'5:30', 400:'7:20', 450:'8:15', 500:'9:10', 600:'11:00',
	800:'14:40', 1000:'18:20', 1650:'30:15'}
	if swim_set_array["stroke"] == None or swim_set_array['stroke'] == 'Freestyle':	
		a = swim_set_array["items"]
		swim_set_array["interval"] = ints[a]
		return swim_set_array
	else:
		return swim_set_array


def for200(swim_set_array):
	ints = {25:'0:30', 50:'1:00', 75:'1:30', 100:"2:00", 125:'2:30',
	150:"3:00", 175:'3:30', 200:'4:00', 225:'4:30', 250:'5:00', 
	300:'6:00', 400:'8:00', 450:'9:00', 500:'10:00', 600:'12:00',
	800:'16:00', 1000:'20:00', 1650:'34:30'}
	if swim_set_array["stroke"] == None or swim_set_array['stroke'] == 'Freestyle':	
		a = swim_set_array["items"]
		swim_set_array["interval"] = ints[a]
		return swim_set_array
	else:
		return swim_set_array


def totalTime(swim_set_array):
	interval = swim_set_array["interval"]
	if interval is None:
		return
	else:
		reps = int(swim_set_array["reps"])
		d = datetime.datetime.strptime(interval, '%M:%S')
		t = datetime.timedelta(minutes = d.minute, seconds = d.second)
		print "type of t is"
		print type(t)
		print t 
		print "type of reps is"
		print type(reps)
		print reps
		total = t * reps
		time = total.__str__()
		swim_set_array['time'] = time
		return swim_set_array
		
def createWorkout():
	workout = []
	return workout

def totalYardage(swim_set_array):
	#Sets the total yardage in the dictionary if both items and reps exist.
	if swim_set_array['items'] == None or swim_set_array['reps'] == None:
		return
	else:
		yardage = int(swim_set_array['reps']) * int(swim_set_array['items'])
		swim_set_array['total_yardage'] = yardage
		return 




