from django.contrib import admin
from models import Feedback, New, Company, NewsComment, FeedbackComment


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'active', )


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

class NewsCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'date', )


    class Meta:
        model = NewsComment
admin.site.register(NewsComment, NewsCommentAdmin)


class FeedbackCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'date', )


    class Meta:
        model = FeedbackComment
admin.site.register(FeedbackComment, FeedbackCommentAdmin)