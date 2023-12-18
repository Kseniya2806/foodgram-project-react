import re

from django.core.exceptions import ValidationError


def validate_username(username):
    if username == 'me':
        raise ValidationError(
            ('Выберете другое имя, не <me>.'),
        )
    if re.search(r'^[a-zA-Z][a-zA-Z0-9-_.]{1,150}$', username) is None:
        raise ValidationError(
            'В логине нельзя использовать символы кроме букв,'
            'цифр, знаков подчеркивания,'
            'точки, знаков +, - и @'
        )
