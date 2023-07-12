from django.contrib import admin
from .models import (
    Case, 
    CaseDocument,
    Evidence,
    CaseProcedure,
    CaseCategory,
    Hearing,
    Court,
    State,
)
# Register your models here.
admin.site.register(Case)
admin.site.register(CaseDocument)
admin.site.register(Evidence)
admin.site.register(CaseProcedure)
admin.site.register(CaseCategory)
admin.site.register(Hearing)
admin.site.register(Court)
admin.site.register(State)