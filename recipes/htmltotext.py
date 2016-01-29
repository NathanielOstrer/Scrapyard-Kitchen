from bs4 import BeautifulSoup
import re
from os import listdir
from os.path import isfile, join

mypath = './recipeshtml/'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

i = 0

for filename in onlyfiles:
	i = i + 1
	print i
	input_ = open("recipeshtml/" + str(filename))
	
	lines = input_.readlines()
	
	text = ''
	
	for line in lines:
		text = text + line
	
	soup = BeautifulSoup(text, 'html.parser')
	
	#output = open(input[:-5] + '.txt', 'w')
	
	wanted = []
	
	for tag in soup.findAll('title'): #title
		wanted.append(tag)

	for tag in soup.findAll(attrs={'class' : 'special-diets tag-block'}): #tags
		wanted.append(tag)

	for tag in soup.findAll(attrs={'name' : 'description'}): #description
		wanted.append(tag)

	for tag in soup.findAll(attrs={'rel' : 'canonical'}): #link
		wanted.append(tag)
	
	for tag in soup.findAll(attrs={'class' : 'author personality'}): #author
		wanted.append(tag)
	
	for tag in soup.findAll(attrs={'itemprop' : 'recipeYield'}):  #yield
		wanted.append(tag)
	
	for tag in soup.findAll(attrs={'itemprop' : 'cookTime'}): #cook time
		wanted.append(tag)

	for tag in soup.findAll(attrs={'itemprop' : 'image'}): # image
		wanted.append(tag)

	for tag in soup.findAll(attrs={'class' : 'recipe-instructions'}): #recipe
		wanted.append(tag)
	
	output = open('./htmlfixed/' + filename, 'w')
	
	for line in wanted:
		output.write(str(line))
	
	output.close()
	
	