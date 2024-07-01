import markdown

# from markdown.treeprocessors import Treeprocessor
# from markdown.extensions import Extension
# import xml.etree.ElementTree as etree

# class CodeClipboardProcessor(Treeprocessor):
#     def run(self, root):
#         print("running this right neow")
#         print(root.tag,root.text,root.tail)
#         # root.text = "BRUHHH"
#         # blocks = root.iter('pre')
#         # for block in blocks:
#         #     print(block.text)
#         #     print(block == root)
#         #     if len(block) == 1 and block[0].tag == 'code':
#         #         clipboard_button = etree.SubElement( block, 'button', { 'class' : 'code-clipboard' })
#         #         etree.SubElement( clipboard_button, 'i', { 'class' : 'fa-solid fa-copy' })
#         for child in root:
#             print(child.tag, child.attrib,child.text)
#             for child2 in child:
#                 print(child2.tag, child2.attrib,child2.text)
#         for element in root.iter('pre'):
#             print("found a pre right here: ",element.text)
#             clipboard_button = etree.SubElement( element, 'button', { 'class' : 'code-clipboard' })
#             etree.SubElement( clipboard_button, 'i', { 'class' : 'fa-solid fa-copy' })
#
# class CodeClipboardExtension(Extension):
#     def extendMarkdown(self, md):
#         md.treeprocessors.register(CodeClipboardProcessor(md), 'codeclipboardprocessor', 200)


def _code_custom_formatter(source, language, class_name, options, md, **kwargs):

    print(language)
    print(md.preprocessors['fenced_code_block'].extension.superfences)
    code_block = md.preprocessors['fenced_code_block'].extension.superfences[0]['formatter'](
        source, language, options, md, **kwargs
    )

    clipboard_button = """\
<button class="code-clipboard hover:text-accent-400 active:text-accent-700 transition-colors absolute top-2.5 right-0 md:right-3.5" @click="$dispatch('clipboard_notfication')" x-data>\
<i class="fa-regular fa-copy"></i>\
</button>"""
    return f'<div class="relative {language}">{clipboard_button}{code_block}</div>'
    # return code_block

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
                    "custom_fences": [
                        { "name": "cpp",    "class": "", "format": _code_custom_formatter, },
                        { "name": "c++",    "class": "", "format": _code_custom_formatter, },
                        { "name": "python", "class": "", "format": _code_custom_formatter, },
                        { "name": "java",   "class": "", "format": _code_custom_formatter, },
                    ]
                }
            }
        }
    )
