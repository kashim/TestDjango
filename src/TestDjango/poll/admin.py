'''
Created on Jul 16, 2011

@author: kashim
'''
from models import Poll
from models import Choice
from django.contrib import admin

#admin.site.register(Poll)
#admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
                 ( 'General Information', { 'fields': ['question'] } ),
                 ( 'Date information', { 'fields': ['pub_date'], 'classes': [ 'collapse' ] } )
                ]
    inlines = [ChoiceInline]
    list_display = ( 'pub_date', "question", 'is_published_today' )
    list_filter = [ 'pub_date', 'question' ]
    search_fileds = [ 'pub_date' ]
    date_hierarchy = 'pub_date'
#    fields = ['pub_date', 'question']
    
admin.site.register( Poll, PollAdmin )