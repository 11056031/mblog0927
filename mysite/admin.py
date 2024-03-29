from django.contrib import admin
from mysite.models import Post
from mysite.models import NewTable
from mysite.models import NewTable, Product,Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text','pub_date')

admin.site.register(Post,PostAdmin)
admin.site.register(NewTable)
admin.site.register(Product)
admin.site.register(Comment, CommentAdmin)



