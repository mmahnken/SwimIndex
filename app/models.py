from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64), index =True, unique = True)
	nickname = db.Column(db.String(120), index = True)
	# sets = db.relationship('Set', backref='user')

	def is_authenticated(self):
		return True
	
	def is_active(self):
		return True
	
	def is_anonymous(self):
		return False
	
	def get_id(self):
		return unicode(self.id)
	
	def avatar(self, size):
		return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest() + '?d=mm&s=' + str(size)

	def __repr__(self):
		return '<User %r>' % (self.username)

class Set(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	items = db.Column(db.Integer)
	stroke = db.Column(db.String(64))
	interval = db.Column(db.String(64))
	reps = db.Column(db.Integer)
	easy = db.Column(db.Integer)
	type_of_set = db.Column(db.String)
	total_yardage = db.Column(db.Integer)
	test = db.Column(db.Integer)

	def is_long(self):
		if self.type_of_set == "long":
			return True
		else:
			return False

