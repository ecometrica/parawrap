#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from parawrap import ParagraphWrapper, split, wrap, fill


class TestSplit(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(ParagraphWrapper.split(''), [''])
        self.assertEqual(ParagraphWrapper.split('\n'), [''])
        self.assertEqual(ParagraphWrapper.split('\n\n'), [''])
        self.assertEqual(ParagraphWrapper.split('\n\n\n'), [''])
        self.assertEqual(ParagraphWrapper.split('\n\n\n\n'), [''])
        self.assertEqual(ParagraphWrapper.split('\n\n \n\n'), [''])

    def test_trailing_whitespace(self):
        self.assertEqual(ParagraphWrapper.split(' '), [' '])
        self.assertEqual(ParagraphWrapper.split(' \n'), [' '])
        self.assertEqual(ParagraphWrapper.split(' \n\n'), [' ', ''])
        self.assertEqual(ParagraphWrapper.split(' \n\n\n\n'), [' ', ''])
        self.assertEqual(ParagraphWrapper.split(' \n\n \n\n'), [' ', ''])


class TestWrap(unittest.TestCase):
    def test(self):
        wrapper = ParagraphWrapper(width=5)
        self.assertEqual(
            wrapper.wrap('12\n'
                         '34\n'
                         '56\n'
                         '78\n'
                         '90\n'
                         '\n'
                         '1234567890'),
            ['12 34',
             '56 78',
             '90',
             '',
             '12345',
             '67890']
        )


class TestFill(unittest.TestCase):
    def test(self):
        wrapper = ParagraphWrapper(width=5)
        self.assertEqual(
            wrapper.fill('12\n'
                         '34\n'
                         '56\n'
                         '78\n'
                         '90\n'
                         '\n'
                         '1234567890'),
            '12 34\n'
            '56 78\n'
            '90\n'
            '\n'
            '12345\n'
            '67890'
        )


class TestConvenience(unittest.TestCase):
    def test_split(self):
        self.assertEqual(split('Paragraph 1\n'
                               '\n'
                               'Paragraph 2\n'
                               'Line 4\n'
                               '\n'
                               'Paragraph 3'),
                         ['Paragraph 1',
                          'Paragraph 2\n'
                          'Line 4',
                          'Paragraph 3'])

    def test_wrap(self):
        self.assertEqual(wrap('1234567890', width=5),
                         ['12345', '67890'])

    def test_fill(self):
        self.assertEqual(fill('1234567890', width=5),
                         '12345\n'
                         '67890')


if __name__ == '__main__':
    unittest.main()
