# -*- coding: utf-8 -*-
"""Create svg graphics.

requires python3-cssselect
"""

import os
from svglib.svglib import SvgRenderer
from lxml import etree


def rel_path(*fname):
    """relative path"""

    return os.path.join(os.path.dirname(os.path.realpath(__file__)), *fname)

def fromstring(xml_string, replacements=None, **kwargs):
    """create svg graphics from string"""

    if replacements:
        for (key, value) in replacements.items():
            xml_string = xml_string.replace(("{%s}" % key).encode(), value.encode())
    parser = etree.XMLParser(remove_comments=True, recover=True)
    svg = etree.fromstring(xml_string, parser=parser)

    # convert to a RLG drawing
    svg_renderer = SvgRenderer("", **kwargs)
    drawing = svg_renderer.render(svg)

    return drawing

def fromfile(path, replacements=None, **kwargs):
    """create svg graphics from file"""

    with open(path, 'rb') as fhandle:
        xml_string = fhandle.read()
    return fromstring(xml_string, replacements, **kwargs)
