from django.utils.safestring import mark_safe
from django import template

register=template.Library()

@register.filter
def coloring(val):
    sig=str(val)[:1]
    if sig=="-":
        ht_str=f"<span style='color:yellowgreen'>{val}</span>"
    elif sig=="0":
        ht_str=f"<span style='color:darkcyan'>{val}</span>"
    else:
        ht_str=f"<span style='color:red'>{val}</span>"
    
    return mark_safe(ht_str)


    