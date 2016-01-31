#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import models
from google.appengine.ext import db
import mainpage, recipepage, searchpage
from fuzzywuzzy import process

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	for line in mainpage.render(None):
    		self.response.out.write(line)

class RecipeHandler(webapp2.RequestHandler):
	def get(self):
		for line in recipepage.render(None):
			self.response.out.write(line)

class SearchHandler(webapp2.RequestHandler):
	def get(self):
		terms = self.request.get('ingredients').split(',')
		# terms = ["u'" + term + "'" for term in terms]

		# query = ((str(terms).replace('[', '').replace(']', '')).replace('u"', '"').replace(', ', ' in tags and ')) + ' in tags'

		query = 'SELECT * FROM Recipe WHERE "cheese" in tags'

		print query

		results = db.GqlQuery(query).fetch(100)

		results = [recipe.name for recipe in results]

		searchpage.render(results)

class UploadRecipe(webapp2.RequestHandler):
	def post(self):
		name = self.request.get('name').encode('ascii', 'ignore')
		tags = self.request.get('tags').encode('ascii', 'ignore').replace('[','').replace(']','').split(', ')
		description = self.request.get('description').encode('ascii', 'ignore')
		link = self.request.get('link').encode('ascii', 'ignore')
		author = self.request.get('author').encode('ascii', 'ignore')
		yield_ = self.request.get('yield').encode('ascii', 'ignore')
		cookTime = self.request.get('cookTime').encode('ascii', 'ignore')
		image = self.request.get('image').encode('ascii', 'ignore')
		imageCredit = self.request.get('imageCredit').encode('ascii', 'ignore')
		ingredients = self.request.get('ingredients').encode('ascii', 'ignore')
		instructions = self.request.get('instructions').encode('ascii', 'ignore')

		recipe = models.Recipe(name=name, tags=tags, description=description, link=link, author=author, yield_=yield_,
		 cookTime=cookTime, image=image, imageCredit=imageCredit, ingredients=ingredients, recipe=instructions)
		recipe.put()

class Tags(webapp2.RequestHandler):
	def get(self):
		offset = int(self.request.get('offset'))
		tags = db.GqlQuery("SELECT distinct tags FROM Recipe").fetch(limit=1000, offset=offset)

		for tag in tags:
			self.response.out.write(tag.tags[0])
			self.response.out.write("\n")

with open("tags.txt") as f:
    taglist = f.readlines()

class SearchTags(webapp2.RequestHandler):
	def get(self):
		term = self.request.get('term')
		self.response.out.write(str([ing[0].rstrip() for ing in process.extract(term, taglist, limit=10)]).replace("'", '"'))

class UploadTag(webapp2.RequestHandler):
	def get(self):
		tag = self.request.get("tag")
		t = models.Tag(tag=tag)
		t.put()


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/recipe', RecipeHandler),
    ('/search', SearchHandler),
    ('/tags', Tags),
	('/terms', SearchTags),
    ('/uploadtag', UploadTag),
    ('/uploadrecipe', UploadRecipe),
], debug=True)
