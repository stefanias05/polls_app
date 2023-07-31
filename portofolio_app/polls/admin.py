from django.contrib import admin
from .models import Choice, Question

"""
Scriu ceea ce vreau sa inregistrez in BD prin admin interface.
Mentionez care sunt campurile editabile din modelele mele.
Clasa StackedInline face ca obiectele sa fie afisate unele sub altele.
Clasa TabularInline - arata inregistrarile ca o lista de randuri
"""


# admin.site.register(Question)

# odata ce adaug intrebarea in bd, inregistrez si optiunile in acelasi timp.

class ChoiceQuestion(admin.TabularInline):
    model = Choice # modelul cu care e asociata clasa
    extra = 3  # specific cate option am

class QuestionAdmin(admin.ModelAdmin):
    """
    Am personalizat adiministrarea tabelei question.
    Specific ca editez campurile text_question and date
    """
    fields = ['text_question', 'date']
    inlines = [ChoiceQuestion]  # specific ca trebuie afisate obiectele Choice in admin odata cu editarea modelulul Q


# am inregostrat modelul  Question in interfata admin si am mentionat ca am personalizat modelul prin Questionadmin
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)





