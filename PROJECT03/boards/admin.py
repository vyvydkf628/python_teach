from django.contrib import admin
from .models import Board

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title','content','created_at','updated_at')
# Register your models here.
