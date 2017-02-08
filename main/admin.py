from django.contrib import admin
from .models import Post
from .models import Test
from .models import ExtendUser

admin.site.register(Post)
admin.site.register(ExtendUser)
admin.site.register(Test)