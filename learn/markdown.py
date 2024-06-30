import markdown

md = markdown.Markdown(
        output_format="html",
        extensions=[
            # 'extra',
            'toc',
            'markdown_katex',
            'pymdownx.extra',
            'pymdownx.highlight',
            'pymdownx.saneheaders',
        ],
        extension_configs = {
            'markdown_katex': {
                'insert_fonts_css': False,
            },
            'pymdownx.highlight': {
            },
        }
    )
