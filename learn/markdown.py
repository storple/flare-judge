import markdown

main_languages = ['cpp','python','java']

def _code_custom_formatter(source, language, class_name, options, md, **kwargs):
    code_block = md.preprocessors['fenced_code_block'].extension.superfences[0]['formatter'](
        source, language, options, md, **kwargs
    )

    classes = kwargs['classes']
    id_value = kwargs['id_value']
    attrs = kwargs['attrs']

    classes = ' ' + ' '.join(classes) if classes else ''
    id_value = f'id="{id_value}" ' if id_value else ''
    attrs = ' ' + ' '.join(f'{k}="{v}"' for k, v in attrs.items()) if attrs else ''

    clipboard_button = """\
<button class="code-clipboard hover:text-accent-400 active:text-accent-700 transition-colors absolute top-2.5 right-0 md:right-3.5">\
<i class="fa-regular fa-copy"></i>\
</button>"""

    left_div = f"""<div {id_value}class="relative lang {language}{classes}"{attrs}>"""

    return f"""{left_div}{clipboard_button}{code_block}</div>"""

md = markdown.Markdown(
        output_format="html",
        extensions=[
            # 'extra',
            'toc',
            'markdown_katex',
            'pymdownx.extra',
            'pymdownx.saneheaders',
            'pymdownx.inlinehilite',
            'pymdownx.highlight',
        ],
        extension_configs = {
            'markdown_katex': {
                'insert_fonts_css': False,
            },
            'pymdownx.extra': {
                "pymdownx.superfences": {
                    "custom_fences": [ { "name" : language, "class": "","format": _code_custom_formatter} for language in main_languages]
                }
            }
        }
    )
