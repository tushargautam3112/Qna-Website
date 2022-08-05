from django.contrib import admin
from . models import users
from . models import post_q
from . models import qna_db

#Register your models here.
admin.site.register(users)
admin.site.register(post_q)
admin.site.register(qna_db)