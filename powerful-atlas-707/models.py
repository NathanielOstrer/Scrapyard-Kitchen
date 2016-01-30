from google.appengine.ext import db

class Recipe(db.Model):
	name = db.StringProperty(multiline=True)
	tags = db.StringListProperty()
	description = db.StringProperty(multiline=True)
	link = db.StringProperty(multiline=True)
	author = db.StringProperty(multiline=True)
	yield_ = db.StringProperty(multiline=True)
	cookTime = db.StringProperty(multiline=True)
	image = db.StringProperty(multiline=True)
	imageCredit = db.StringProperty(multiline=True)

	ingredients = db.TextProperty()
	recipe = db.TextProperty() #can't be a string property because can be rather long
	