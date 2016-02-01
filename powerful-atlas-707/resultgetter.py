#gets results
from google.appengine.ext import db

def getResults(terms):
	
	res = []

	for i in range(len(terms)):
		query = 'WHERE tags = :one'
		res.extend(db.GqlQuery("SELECT * FROM Recipe " + query, one=terms[i]).fetch(250))

	doesnthave = [r.tags for r in res]

	for i in range(len(res)):
		doesnthave[i] = list(set(doesnthave[i]).symmetric_difference(terms))


	lengths = [len(i) for i in doesnthave]

	print lengths
	
	a = [[y, x] for (y,x) in sorted(zip(res,lengths), key=lambda x: x[1])]

	print a

	return a