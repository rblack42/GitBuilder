# -*- coding: utf-8 -*-
"""
    sphinx_ext.literate
    ~~~~~~~~~~~~~~~~~~~

    Include literate programming blocks in Sphinx-generated
    documents.

    :copyright: 2019 by Roie R. Black
    :licence: BSD 3-Clause
"""
import os
from sphinx.util.docutils import SphinxDirective
from docutils.parsers.rst import directives
from docutils import nodes
from docutils.statemachine import ViewList
from sphinx.util.matching import Matcher, patfilter
from sphinx.util.nodes import explicit_title_re, set_source_info


def container_wrapper(directive, literal_node, caption):
    container_node = nodes.container('', literal_block=True,
                                     classes=['literal-block-wrapper'])
    parsed = nodes.Element()
    directive.state.nested_parse(ViewList([caption], source=''),
                                 directive.content_offset, parsed)
    if isinstance(parsed[0], nodes.system_message):
        msg = __('Invalid caption: %s' % parsed[0].astext())
        raise ValueError(msg)
    caption_node = nodes.caption(parsed[0].rawsource, '',
                                 *parsed[0].children)
    caption_node.source = literal_node.source
    caption_node.line = literal_node.line
    container_node += caption_node
    container_node += literal_node
    return container_node

class literate_node(nodes.General, nodes.Element):
    pass

class literateblklist(nodes.General, nodes.Element):
    pass

class LiterateBlock(SphinxDirective):

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
            'caption': directives.unchanged_required,
            'linenos': directives.flag,
            'blktype': directives.unchanged_required,
    }

    def run(self):
        cwd = os.getcwd()
        blkfile = open(os.path.join(cwd,'pylit_blks'),'a')
        document = self.state.document
        blkfile.write("%s\n" % document.current_source)
        code = u'\n'.join(self.content)
        location = self.state_machine.get_source_and_line(self.lineno)
        hl_lines = None
        literal = nodes.literal_block(code, code)
        literal['language'] = self.arguments[0]
        literal['linenos'] = 'linenos' in self.options
        set_source_info(self, literal)
        caption = self.options.get('caption')
        blktype = self.options.get('blktype')
        if caption:
            if blktype:
                if blktype == 'file' or blktype == 'block':
                    caption = "<<%s>>==" % caption
                elif blktype == 'add':
                    caption = "<<%s>> +=" % caption
            try:
                literal = container_wrapper(self, literal, caption)
            except ValueError as exc:
                return [document.reporter.earning(text_type(exc), line=self.lineno)]
        self.add_name(literal)
        blkfile.write("%s\n" % caption)
        blkfile.write(code)
        blkfile.write("\n")
        blkfile.close()
        return [literal]

def setup(app):
    directives.register_directive('pylit-block', LiterateBlock)

    return {
            'version': 'builtin',
            'parallel_read_safe': True,
            'parallel_write_safe': True,
    }
