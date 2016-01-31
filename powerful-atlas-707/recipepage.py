from google.appengine.ext import db

def render(data):
	recipe = db.get(data)

	message = recipe.name
	
	lines = [
	"<html>",

	"<center>",

	"<h1>",
	
	message,
	
	"</h1>",
	
	"</center>",

	"</html>"
	]
	
	return lines