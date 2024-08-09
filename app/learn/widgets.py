from django import forms

class MarkdownEditor(forms.Widget):
    template_name = 'learn/markdown_editor_widget.html'
