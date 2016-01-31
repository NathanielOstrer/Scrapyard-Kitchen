import urllib

def render(data):
	i = 0
	terms = []

	for d in data:
		missing = d[3]

		key = str(d[0])

		title = d[1] + ' (missing ' + str(missing) + ' ingredients)'

		if d[2] != "":
			image = d[2]
		else:
			image = "http://static01.nyt.com/images/icons/t_logo_291_black.png"

		link = '/recipe?key=' + key# + 'missing=' + 

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


	terms,
	
	
	"</center>",

	"</html>"
	]

	good = []
	good.extend([''.join(line).replace("u'", '').replace("' ", '') for line in lines])
	
	return good