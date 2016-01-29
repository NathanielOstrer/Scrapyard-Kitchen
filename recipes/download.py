import urllib

first_page = 1
final_page = 367

output = open('linkstorecipes.html', 'w')

for i in range(first_page, final_page+1):
	print i
	url = 'http://cooking.nytimes.com/search?q=&page=' + str(i)
	data = urllib.urlopen(url).read()
	
	output.write(data)

output.close()