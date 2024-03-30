// ace setup
ace.require("ace/ext/language_tools");

var editor = ace.edit("editor");

//adds html snippets
var snippetManager = ace.require("ace/snippets").snippetManager;
const htmlSnippetsContent = ace.require("ace/snippets/html").snippetText;
const htmlSnippets = snippetManager.parseSnippetFile(htmlSnippetsContent);
// const customSnippets = snippetManager.parseSnippetFile(customSnippetsContent);

snippetManager.register(htmlSnippets, 'markdown');
// snippetManager.register(customSnippets, 'markdown');

editor.setTheme("ace/theme/tomorrow");
editor.session.setMode("ace/mode/markdown");

// enable autocompletion and snippets
editor.setOptions({
	enableBasicAutocompletion: true,
	enableSnippets: true,
	enableLiveAutocompletion: true
});

// converts editor text to preview
var preview = document.getElementById("preview"); 
var converter = new showdown.Converter();
converter.setFlavor('github');

function updatePreview(){
	const text = editor.getValue();
	const html = converter.makeHtml(text);
	preview.innerHTML = html;
}

//every time the editor changes the preview updates
editor.session.on('change', updatePreview);
