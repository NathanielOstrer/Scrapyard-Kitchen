def render(data):
	message = "This is the main page!"

	lines = [
    "<html>",
    "<head>",
    '<link rel="stylesheet" href="./TrinHackStyle.css">',
    "<title>Scrapyard Kitchen</title>",
	"<script src='https://code.jquery.com/ui/1.11.4/jquery-ui.js'></script>",
	"<script src='https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js'></script>"
    "</head>",
    '<body class="bground" style="background-image: url(bground.jpg);">',
    '<span class="backbox">',
    '<input type="text" placeholder="add ingredient" id="ingred" autocomplete="on">',
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
    "</script>",
    "</body>",
    "</html>",
	]

	return lines