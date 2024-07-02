import markdown

main_languages = ['cpp','python','java']

def _code_custom_formatter(source, language, class_name, options, md, **kwargs):
    code_block = md.preprocessors['fenced_code_block'].extension.superfences[0]['formatter'](
        source, language, options, md, **kwargs
    )

    clipboard_button = """\
<button class="code-clipboard hover:text-accent-400 active:text-accent-700 transition-colors absolute top-2.5 right-0 md:right-3.5">\
<i class="fa-regular fa-copy"></i>\
</button>"""
    if language in main_languages:
        left_div = f"""<div :class="{{ 'hidden' : $store.language.language != '{language}'}}" class="relative hidden {language}">"""
    else:
        left_div = f"""<div class="relative {language}">"""

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
