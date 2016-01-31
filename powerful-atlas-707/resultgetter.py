#gets results
from google.appengine.ext import db

def getResults(terms):
	
	if(len(terms) == 1):
		query = 'WHERE tags = :one'
		res = db.GqlQuery("SELECT * FROM Recipe " + query, one=terms[0]).fetch(500)
	elif(len(terms) >= 2):
		query = 'WHERE tags = :one and tags = :two'
		res = db.GqlQuery("SELECT * FROM Recipe " + query, one=terms[0], two=terms[1]).fetch(500)
	
	doesnthave = [r.tags for r in res]

	for i in range(len(res)):
		doesnthave[i] = list(set(doesnthave[i]).symmetric_difference(terms))


	lengths = [len(i) for i in doesnthave]

	print lengths
	
	a = [[y, x] for (y,x) in sorted(zip(res,lengths), key=lambda x: x[1])]

	print a

	return a