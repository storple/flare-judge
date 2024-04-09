// ace setup
ace.require("ace/ext/language_tools");

var editor = ace.edit("editor");

editor.setTheme("ace/theme/tomorrow");
editor.session.setMode("ace/mode/markdown");

// enable autocompletion and snippets
editor.setOptions({
	enableBasicAutocompletion: true,
	enableSnippets: true,
	enableLiveAutocompletion: true
});

// converts editor text to preview
let hidden_Textarea = document.getElementsByClassName("hidden-textarea")[0];
let preview = document.getElementById("preview"); 
let converter = new showdown.Converter();
converter.setFlavor('github');
// initially renders the html witout triggering editor change
updatePreview();

function updatePreview(){
	const text = editor.getValue();
	const html = converter.makeHtml(text);
	hidden_Textarea.value = text;
	preview.innerHTML = html;
}

//every time the editor changes the preview updates
editor.session.on('change', updatePreview);
