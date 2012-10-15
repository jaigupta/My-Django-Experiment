from google.appengine.ext import db

class newchat(db.Model):
	u1=db.StringProperty()
	u2=db.StringProperty()

class bhaat(db.Model):
	name=db.StringProperty()
	thistime=db.StringProperty()
	detail=db.StringProperty()
	link=db.ReferenceProperty(newchat)
	
class auths(db.Model):
	user=db.UserProperty()
	token=db.StringProperty()
	details=db.StringProperty()
	code=db.StringProperty()
