from django import template
import re
register = template.Library()


def is_empty(value, alt):
    if value:
        return value
    return alt


def n_to_br(text):
    text = text.replace('\n', '<br>')
    return text


register.filter('is_empty', is_empty)
register.filter('n_to_br', n_to_br)
