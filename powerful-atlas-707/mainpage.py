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
		<style>
		.ui-autocomplete-loading {
		background: white url("images/ui-anim_basic_16x16.gif") right center no-repeat;
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
    "<script>",
    "var list = document.getElementById('demo');",
    "function changeText2() {",
    "var ingred = document.getElementById('ingred').value;",
    "var entry = document.createElement('li');",
    "entry.appendChild(document.createTextNode(ingred));",
    "list.appendChild(entry);",
    "}",
	"""
		$( "#ingred" ).autocomplete({
		source: "terms",
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