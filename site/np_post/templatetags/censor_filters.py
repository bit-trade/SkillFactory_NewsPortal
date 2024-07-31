import re
from django import template
from ..consts import CURSE_WORDS


register = template.Library()


@register.filter()
def censor(value):
    for curse_word in CURSE_WORDS:
        pattern = curse_word
        repl = len(curse_word) * '*'
        value = re.sub(pattern, repl, value)

    return value

