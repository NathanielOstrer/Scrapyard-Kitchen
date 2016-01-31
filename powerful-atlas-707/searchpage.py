def render(data):

	i = 0
	terms = []

	for d in data:
		missing = d[3]

		title = d[1] + ' missing ' + str(missing)
		image = d[2] 
		link = "google.com"
		term = ''
		term = term + """<div class="img" style="background-image: url('""" + image + """');">"""
		term = term + '<a href="' + link + '">'
		term = term + '<span class="text-content"><span>'
		term = term + '<span class="headline">' + title + '</span>'
		term = term + "</span></span></a></div>"
		
		
		terms.append(term)

	lines = [
	"<html>",

	"""<link rel="stylesheet" href="http://newsin.pictures/style.css">""",

	"<center>",

	#"""<table>""",

	terms,
	
	#"</tr></table>",

	"</center>",

	"</html>"
	]

	good = []
	good.extend([''.join(line).replace("u'", '').replace("' ", '') for line in lines])
	
	return good