# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *
from pagedown.widgets import AdminPagedownWidget
from django.db import models


# Register your models here.
admin.site.register(Assignment)
#admin.site.register(Author)
admin.site.register(UserProfile)

# admin.site.register(ItemComment)
# admin.site.register(Item)
# admin.site.register(Cart)


class AssignmentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

class assignment_comment_model(admin.ModelAdmin):
	list_filter=["checked", "blog"]
	class Meta:
		model=AssignmentComment

admin.site.register(AssignmentComment, assignment_comment_model)