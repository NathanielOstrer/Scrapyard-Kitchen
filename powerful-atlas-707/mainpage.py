def render(data):
	message = "This is the main page!"

	lines = [
	"<html>",

	"<center>",

	"<h1>",
	
	'<p style="font-family: signpainter; font-size: 250%"> Scrapyard Kitchen </p>',
	
	"</h1>",

	'<form action="/search">',

	'<input type="text" name=ingredients>',

	"</form>",

	"</center>",

	"</html>"
	]

	return lines