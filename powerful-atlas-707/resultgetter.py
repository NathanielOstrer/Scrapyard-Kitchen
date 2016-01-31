#gets results
from google.appengine.ext import db

def getResults(terms):
	query = 'WHERE tags = :one'
	res = db.GqlQuery("SELECT * FROM Recipe " + query, one=terms[0]).fetch(100)

	doesnthave = [r.tags for r in res]

	for i in range(len(res)):
		doesnthave[i] = list(set(doesnthave[i]).symmetric_difference(terms))


	lengths = [len(i) for i in doesnthave]

	print lengths

	return [[y, x] for (y,x) in sorted(zip(res,lengths), reverse=True)]