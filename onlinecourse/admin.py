from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Choice, Question

# <HINT> Register QuestionInline and ChoiceInline classes here

class ChoicesInline(admin.StackedInline):
    model = Choice
    extra = 5

class QuestionInline(admin.TabularInline):
    model = Question
    inlines = [ChoicesInline]
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'grade_point')
    inlines = [ChoicesInline]
   

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)