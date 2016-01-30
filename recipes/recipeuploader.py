#remember to search output for errors!

from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
import urllib, urllib2

mypath = './htmlfixed/'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

i = 0

start = 3848

for filename in onlyfiles:
	i = i + 1

	if i < start:
		continue

	print str(i) + ". " + filename

	try:
		input_ = open("htmlfixed/" + str(filename))
		
		lines = input_.readlines()
		
		text = ''
		
		for line in lines:
			text = text + line
		
		soup = BeautifulSoup(text, 'html.parser')
		
		name = ''
		tags = []
		description = ''
		link = ''
		author = ''
		yield_ = ''
		cookTime = ''
		image = ''
		imageCredit = '' 
		ingredients = ''
		instructions =  ''
	
		for tag in soup.findAll('title'): #title
			name = tag.string.split(' - NYT Cooking')[0]
	
		for tag in soup.findAll('a'): #tags
			if tag.string == None:
				pass
			else:
				tags.append(tag.string.lower())
	
		for tag in soup.findAll(attrs={'class' : 'ingredient-name'}):
			for t in tag.findAll('span'):
				if not t.string.lower() in tags:
					tags.append(t.string.lower())
		
		for tag in soup.findAll(attrs={'name':'description'}): #description
			description = tag['content']
	
		for tag in soup.findAll(attrs={'rel' : 'canonical'}): #link
			link = tag['href']
	
		for tag in soup.findAll(attrs={'class' : 'author personality'}): #author
			author = tag['data-author']
		
		for tag in soup.findAll(attrs={'itemprop' : 'recipeYield'}):  #yield
			yield_ = tag.string
		
		for tag in soup.findAll(attrs={'itemprop' : 'cookTime'}): #cook time
			cookTime = str(tag)[str(tag).index('</span>') + len('</span>'):str(tag).index('</meta>')]
	
		for tag in soup.findAll('img'): # image
			image = tag['src']
	
		for tag in soup.findAll(attrs={'class' : 'image-credit'}): #image credit
			imageCredit = tag.string.replace('\n', '')
	
		for tag in soup.findAll(attrs={'class' : 'recipe-ingredients-wrap'}): #ingredients
			ingredients = tag
	
		for tag in soup.findAll(attrs={'class' : 'recipe-steps-wrap'}): #instructions 
			instructions = tag
	
	
		url = 'http://scrapyardkitchen.com/uploadrecipe'
		data = {'name' : name, 'tags' : tags, 'description' : description, 'link' : link, 'author' : author, 'yield' : yield_, 'cookTime' : cookTime, 'image' : image, 'imageCredit' : imageCredit, 'ingredients' : ingredients, 'instructions' : instructions}
	
		for k, v in data.iteritems():
			data[k] = unicode(v).encode('utf-8')
	
		data = urllib.urlencode(data)
	
		print urllib2.urlopen(url, data).read()
	except Exception:
		print 'error!, probably fucking unicode'
	