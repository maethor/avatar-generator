# vim: ai ts=4 sts=4 et sw=4 nu
"""
    Generates default avatars from a given string (such as username).

    Usage:

    >>> from avatar_generator import Avatar
    >>> photo = Avatar.generate(128, "example@sysnove.fr", "PNG")
"""

import os
from random import randint, seed
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont

__all__ = ['Avatar']


class Avatar():
    """ Avatar base class. """
    FONT_COLOR = (255, 255, 255)
    MIN_RENDER_SIZE = 512

    @classmethod
    def generate(cls, size, string, filetype="JPEG"):
        """
            Generates a squared avatar with random background color.

            :param size: size of the avatar, in pixels
            :param string: string to be used to print text and seed the random
            :param filetype: the file format of the image (i.e. JPEG, PNG)
        """
        render_size = max(size, Avatar.MIN_RENDER_SIZE)
        image = Image.new('RGB', (render_size, render_size),
                          cls._background_color(string))
        draw = ImageDraw.Draw(image)
        font = cls._font(render_size)
        text = cls._text(string)
        draw.text(cls._text_position(render_size, text, font),
                  text,
                  fill=cls.FONT_COLOR,
                  font=font)
        stream = BytesIO()
        image = image.resize((size, size), Image.Resampling.LANCZOS)
        image.save(stream, format=filetype, optimize=True)
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
        path = os.path.join(os.path.dirname(__file__), 'data',
                            "Inconsolata.otf")
        return ImageFont.truetype(path, size=int(0.8 * size))

    @staticmethod
    def _text(text):
        """
            Returns the text to draw, or a sharp if there is not.

            :param text: text to normalize.
        """
        if text:
            return text[0].upper()

        return "#"

    @staticmethod
    def _text_position(size, text, font):
        """
            Returns the left-top point where the text should be positioned.

            :param size: size of the avatar.
            :param text: text of the avatar.
            :param font: font used to render the text.
        """
        left, top, right, bottom = font.getbbox(text)

        width = right - left
        left = (size - width) / 2.0

        # I just don't know why 5.5, but it seems to be the good ratio
        height = bottom - top
        top = (size - height) / 5.5

        return left, top
