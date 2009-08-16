# $Id: models.py 858ffff7c9a1 2009/08/16 12:42:35 jpartogi $ 

from django.db import models
from django.contrib.admin import widgets as admin_widgets
from wmd import widgets as wmd_widgets

class MarkDownField(models.TextField):
    def formfield(self, **kwargs):
        defaults = {'widget': wmd_widgets.MarkDownInput}
        defaults.update(kwargs)
        
        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = wmd_widgets.AdminMarkDownInput
        
        return super(MarkDownField, self).formfield(**defaults)
    