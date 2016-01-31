def render(data):
	terms = data.split(' ')

	lines = [
	"<html>",

	"<center>",

	"<h1>",
	
	"your terms are: ",

	terms,
	
	"</h1>",
	
	"</center>",

	"</html>"
	]
	
	return lines