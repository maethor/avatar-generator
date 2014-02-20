#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

"""
    Usage:

    >>> from avatar_generator import Avatar
    >>> photo = Avatar.generate(128, "example@sysnove.fr")
"""

import os
from random import randint, seed
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

__all__ = ['Avatar']


class Avatar(object):

    FONT_COLOR = (255, 255, 255)

    @classmethod
    def generate(cls, size, string):
        """
            Generates a squared avatar with random background color.

            :param size: size of the avatar, in pixels
            :param string: string to be used to print text and seed the random
        """
        image = Image.new('RGB', (size, size), cls._background_color(string))
        draw = ImageDraw.Draw(image)
        font = cls._font(size)
        text = cls._text(string)
        draw.text(cls._text_position(size, text, font),
                  text,
                  fill=cls.FONT_COLOR,
                  font=font)
        stream = BytesIO()
        image.save(stream, format="JPEG", optimize=True)
        return stream.getvalue()

    @staticmethod
    def _background_color(s):
        """
            Generate a random background color.
            Brighter colors are dropped, because the text is white.

            :param s: Seed used by the random generator
            (same seed will produce the same color).
        """
        seed(s)
        r = v = b = 255
        while r + v + b > 255*2:
            r = randint(0, 255)
            v = randint(0, 255)
            b = randint(0, 255)
        return (r, v, b)

    @staticmethod
    def _font(size):
        """
            Returns a PIL ImageFont instance.

            :param size: size of the avatar, in pixels
        """
        path = os.path.join(os.path.dirname(__file__), 'font',
                            "Inconsolata.otf")
        return ImageFont.truetype(path, size=int(0.8 * size))

    @staticmethod
    def _text(string):
        """
            Returns the text to draw.
        """
        if len(string) == 0:
            return "#"
        else:
            return string[0].upper()

    @staticmethod
    def _text_position(size, text, font):
        """
            Returns the left-top point where the text should be positioned.
        """
        width, height = font.getsize(text)
        left = (size - width) / 2.0
        # I just don't know why 5.5, but it seems to be the good ratio
        top = (size - height) / 5.5
        return left, top
