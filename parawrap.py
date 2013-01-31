"""Paragraph wrapping and filling.
"""

# Copyright (C) 2013 Ecometrica.
# Written by Simon Law <sfllaw@sfllaw.ca>

from functools import partial
import re
import textwrap


__all__ = ['ParagraphWrapper', 'split', 'wrap', 'fill']


class ParagraphWrapper(textwrap.TextWrapper):
    parasep_re = re.compile(r'\n'   # Newline
                            r'\s*'  # Blank lines
                            r'\n')  # Last newline

    @classmethod
    def split(cls, text):
        """split(text : string) -> [string]

        Splits 'text' into multiple paragraphs and return a list of each
        paragraph.
        """
        result = [line.strip('\n') for line in cls.parasep_re.split(text)]
        if result == ['', '']:
            result = ['']
        return result

    def wrap(self, text):
        """wrap(text : string) -> [string]

        Reformat the multiple paragraphs in 'text' so they fit in lines of
        no more than 'self.width' columns, and return a list of wrapped
        lines.  Tabs in 'text' are expanded with string.expandtabs(),
        and all other whitespace characters (including newline) are
        converted to space.
        """
        lines = []

        linewrap = partial(textwrap.TextWrapper.wrap, self)
        for para in self.split(text):
            lines.extend(linewrap(para))
            lines.append('')    # Add newline between paragraphs

        # Remove trailing newline
        lines = lines[:-1]

        return lines


# -- Convenience interface ---------------------------------------------

def split(text):
    """Splits text into multiple paragraphs, returning a list of paragraphs.
    """
    return ParagraphWrapper.split(text)


def wrap(text, width=70, **kwargs):
    """Wrap multiple paragraphs of text, returning a list of wrapped lines.

    Reformat the multiple paragraphs  'text' so they fit in lines of no
    more than 'width' columns, and return a list of wrapped lines.  By
    default, tabs in 'text' are expanded with string.expandtabs(), and
    all other whitespace characters (including newline) are converted to
    space.  See ParagraphWrapper class for available keyword args to customize
    wrapping behaviour.
    """
    w = ParagraphWrapper(width=width, **kwargs)
    return w.wrap(text)


def fill(text, width=70, **kwargs):
    """Fill multiple paragraphs of text, returning a new string.

    Reformat multiple paragraphs in 'text' to fit in lines of no more
    than 'width' columns, and return a new string containing the entire
    wrapped text.  As with wrap(), tabs are expanded and other
    whitespace characters converted to space.  See ParagraphWrapper class for
    available keyword args to customize wrapping behaviour.
    """
    w = ParagraphWrapper(width=width, **kwargs)
    return w.fill(text)
