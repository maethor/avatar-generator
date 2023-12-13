# Avatar Generator

Generates default avatars from a given string (such as username). This is
mainly for an usage in web apps, but you can also use it to populate LDAP
"jpegPhoto" field, for instance.

![](examples/photo3.png "")
![](examples/photo2.png "")
![](examples/photo1.png "")

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
