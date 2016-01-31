def render(data):
	message = "This is the main page!"

	lines = [
    "<html>",
    "<head>",
    '<link rel="stylesheet" href="./TrinHackStyle.css">',
	"<title>Scrapyard Kitchen</title>",
	"<script src='https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js'></script>",
	"<script src='https://code.jquery.com/ui/1.11.4/jquery-ui.js'></script>",
	"""
		<head>
		<link rel="stylesheet" type="text/css" href="https://code.jquery.com/ui/1.10.4/themes/pepper-grinder/jquery-ui.css">
		</head>
		<style>
		.ui-autocomplete-loading {
		background: white url("https://jqueryui.com/resources/demos/autocomplete/images/ui-anim_basic_16x16.gif") right center no-repeat;
		}
		</style>
	""",
    "</head>",
    '<body class="bground" style="background-image: url(bground.jpg);">',
    '<span class="backbox">',
	"""
		<div class="ui-widget">
		<label for="ingred">Add Ingredient: </label>
		<input id="ingred">
		</div>
	"""
    "<input type='button' onclick='changeText2()' value='Add' class='button'/>",
    "</span>",
    '<span class="list">',
    "Ingredients:",
    '<ol class="ingredient_list" id="demo"></ol>',
    "</span>",
    '<form action="submit.jsp" class="finalbut">',
    '<input type="hidden" id="csv" name="comsepvals">',
    '<input type="button" value="Find Recipes" class="finalbutton" >',
    '</form>',
    "<script>",
    "var list = document.getElementById('demo');",
    "function changeText2() {",
    "var ingred = document.getElementById('ingred').value;",
    "var csv = document.getElementById('csv').value;",
    'csv = csv + ", " + ingred;',
    "document.getElementById('csv').value = csv;",
    "var entry = document.createElement('li');",
    "entry.appendChild(document.createTextNode(ingred));",
    "list.appendChild(entry);",
    "}",
	"""
		$( "#ingred" ).autocomplete({
		source: "terms",
		minLength: 2,
		select: function( event, ui ) {
        log( ui.item ?
		"Selected: " + ui.item.value + " aka " + ui.item.id :
		"Nothing selected, input was " + this.value );
		}
		});
	""",
    "</script>",
    "</body>",
    "</html>",
	]

	return lines