import re

from django.core.exceptions import ValidationError

from foodgram.settings import REGULAR_CHECK_LOGIN_VALID, RESERVED_NAMES


def validate_username(username):
    if username.lower() in RESERVED_NAMES:
        raise ValidationError(
            'Этот логин уже используется.'
        )
    if not re.match(REGULAR_CHECK_LOGIN_VALID, username):
        raise ValidationError(
            'В логине нельзя использовать символы кроме букв,'
            'цифр, знаков подчеркивания,'
            'точки, знаков +, - и @'
        )
    return username
