// ace setup
ace.require("ace/ext/language_tools");

let editor = ace.edit("editor");

editor.setTheme("ace/theme/tomorrow_night");
editor.session.setMode("ace/mode/markdown");

// enable autocompletion and snippets
editor.setOptions({
    enableBasicAutocompletion: true,
    enableSnippets: true,
    enableLiveAutocompletion: true,
});

editor.session.setUseWrapMode(true);

editor.setShowPrintMargin(false);

// converts editor text to preview
let hidden_Textarea = document.getElementsByClassName("hidden-textarea")[0];
// initially renders the html witout triggering editor change
update_textarea();

function update_textarea(){
    const text = editor.getValue();
    hidden_Textarea.value = text;
}

//every time the editor changes the preview updates
editor.session.on('change', update_textarea);
