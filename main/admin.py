from django.contrib import admin
from models import Feedback, New, Company, Comment


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', )


    class Meta:
        model = Feedback
admin.site.register(Feedback, FeedBackAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'url', )


    class Meta:
        model = Company
admin.site.register(Company, CompanyAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', )


    class Meta:
        model = New
admin.site.register(New, NewsAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'date', )


    class Meta:
        model = Comment
admin.site.register(Comment, CommentAdmin)
