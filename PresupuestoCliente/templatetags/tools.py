from django import template

register = template.Library()

@register.filter(name='get')
def get(dictionary: dict, key: str):
    value = dictionary.get(key, "")
    value = value if value is not None else ""
    return value

@register.simple_tag
def setvar(val=None):
  return val

@register.filter(name='remove_dots')
def remove_dots(value):
    return value.replace('.', '')

@register.filter(name='day_to_text')
def day_to_text(value):
    days = {
        '0': 'Lunes',
        '1': 'Martes',
        '2': 'Miércoles',
        '3': 'Jueves',
        '4': 'Viernes',
        '5': 'Sábado',
        '6': 'Domingo',
    }
    return days[value] if value else ''

@register.filter
def intpoint(value):
    # Formatear el valor como entero y luego como cadena sin decimales
    formatted_value = '{:,.0f}'.format(float(value))
    return formatted_value.replace(',', '.')
