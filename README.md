# Avatar Generator

Generates default avatars from a given string (such as username). This is
mainly for an usage in web apps, but you can also use it to populate LDAP
"jpegPhoto" field, for instance.

![Example 3](https://raw.githubusercontent.com/maethor/avatar-generator/master/examples/photo3.png)
![Example 2](https://raw.githubusercontent.com/maethor/avatar-generator/master/examples/photo2.png)
![Example 1](https://raw.githubusercontent.com/maethor/avatar-generator/master/examples/photo1.png)

## Installation

    pip install avatar-generator

## Example in a Flask app

    from avatar_generator import Avatar
    from flask import make_response

    @app.route("/photo.png")
    def photo():
        avatar = Avatar.generate(128, "example@sysnove.fr", "PNG")
        headers = { 'Content-Type': 'image/png' }
        return make_response(avatar, 200, headers)

## Licence

This code is under [WTFPL](https://en.wikipedia.org/wiki/WTFPL). Just do what the fuck you want with it.
