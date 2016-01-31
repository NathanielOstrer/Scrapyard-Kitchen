from google.appengine.ext import db

def render(data):
	recipe = db.get(data)

	message = recipe.name

	text = """

<html>
	<head>
		<link rel="stylesheet" href="/TrinHackRepStyle.css">
	</head>
	<body>
<title>%name%</title><p class="special-diets tag-block">"""


	for tag in recipe.tags:
		text = text + """<a href="/search?ingredients=%tag%" id="bllooop">%tag%</a>,""".replace('%tag%', tag)
	                    
	
	text = text + """
</p><meta content="%description%" name="description"/><link href="%link%" rel="canonical"/>
<span class="byline-name" itemprop="author"> %author% </span>
</a><span itemprop="recipeYield">%yield%</span><meta content="PT45M" itemprop="cookTime">
<span class="icon icon-clock">Time</span>%time%
            </meta>"""
          
	if recipe.image != "":
		text = text + """<img itemprop="image" src="%image%">"""

	text = text + """
<p class="image-credit">
                  %imagecredit%
                </p>
</img><div class="recipe-instructions">

%ingredients%

%recipe%
</div>
</body>
</html>


	"""
	text = text.replace('%name%', recipe.name).replace('%author%', recipe.author).replace('%yield%', recipe.yield_).replace('%time%', recipe.cookTime).replace('%image%', recipe.image).replace('%imagecredit%', recipe.imageCredit).replace('%ingredients%', recipe.ingredients).replace('%recipe%', recipe.recipe).replace('%description%', recipe.description).replace('%link%', recipe.link)
	
	return text