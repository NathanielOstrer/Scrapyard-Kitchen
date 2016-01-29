import urllib

links = open('justlinks.html').readlines()

i = 0

for link in links:
	i = i + 1 
	print i
	try:
		url = 'http://cooking.nytimes.com' + link
		html = urllib.urlopen(url).read()
		title = html[html.index('<title>')+len('<title>'):html.index(' - NYT Cooking')]
		f = open(('recipeshtml/' + title.replace('/', '') + '.html'), 'w')
		f.write(html)
		f.close()
	except Exception:
		print 'errorrr'
		print 'error: ' + link