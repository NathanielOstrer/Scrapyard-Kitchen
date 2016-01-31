#gets results
from google.appengine.ext import db

def getResults(terms):
	if len(terms) == 1:
		query = 'WHERE tags = :one'
		return db.GqlQuery("SELECT * FROM Recipe " + query, one=terms[0]).fetch(100)

	if len(terms) == 2:
		print 'yooooo'
		query = ''
		return db.GqlQuery('SELECT * FROM Recipe WHERE tags = "cheese" and tags = "almonds"', one=terms[0], two=terms[1]).fetch(100)

	if len(terms) == 3:
		query = 'WHERE tags = :one and tags = :two and tags = :three'
		return db.GqlQuery("SELECT * FROM Recipe " + query, terms[0], terms[1], terms[2]).fetch(100)

	if len(terms) == 4:
		query = 'WHERE tags = :one and tags = :two and tags = :three and tags = :four'
		return db.GqlQuery("SELECT * FROM Recipe " + query, terms[0], terms[1], terms[2], terms[3]).fetch(100)

	if len(terms) == 5:
		query = 'WHERE tags = :one and tags = :two and tags = :three and tags = :four and tags = :five'
		return db.GqlQuery("SELECT * FROM Recipe " + query, terms[0], terms[1], terms[2], terms[3], terms[4]).fetch(100)

	if len(terms) == 6:
		query = 'WHERE tags = :one and tags = :two and tags = :three and tags = :four and tags = :five and tags = :6'
		return db.GqlQuery("SELECT * FROM Recipe " + query, terms[0], terms[1], terms[2], terms[3], terms[4], terms[5]).fetch(100)

	if len(terms) == 7:
		query = 'WHERE tags = :one and tags = :two and tags = :three and tags = :four and tags = :five and tags = :6 and tags = :7'
		return db.GqlQuery("SELECT * FROM Recipe " + query, terms[0], terms[1], terms[2], terms[3], terms[4], terms[5], terms[6]).fetch(100)

	if len(terms) == 8:
		query = 'WHERE tags = :one and tags = :two and tags = :three and tags = :four and tags = :five and tags = :6 and tags = :7 and tags = :8'
		return db.GqlQuery("SELECT * FROM Recipe " + query, terms[0], terms[1], terms[2], terms[3], terms[4], terms[5], terms[6], terms[7]).fetch(100)


	if len(terms) == 9:
		query = 'WHERE tags = :one and tags = :two and tags = :three and tags = :four and tags = :five and tags = :6 and tags = :7 and tags = :8 and tags = :9'
		return db.GqlQuery("SELECT * FROM Recipe " + query, terms[0], terms[1], terms[2], terms[3], terms[4], terms[5], terms[6], terms[7], terms[8]).fetch(100)

	if len(terms) >= 10:
		query = 'WHERE tags = :one and tags = :two and tags = :three and tags = :four and tags = :five and tags = :6 and tags = :7 and tags = :8 and tags = :9 and tags = :one0'
		return db.GqlQuery("SELECT * FROM Recipe " + query, terms[0], terms[1], terms[2], terms[3], terms[4], terms[5], terms[6], terms[7], terms[8], terms[9]).fetch(100)
