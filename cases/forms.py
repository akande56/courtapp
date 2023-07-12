from django import forms
from .models import Case,CaseProcedure, Evidence, Hearing, Trial
from courtapp.users.models import User

class CaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['plaintiff'].queryset = User.objects.filter(is_plaintief=True, is_active=True)
        self.fields['defendant'].queryset = User.objects.filter(is_defendant=True, is_active=True)

    class Meta:
        model = Case
        exclude = ['judge', 'assigned_lawyer']

########## CLERK

class ProceedingForm(forms.ModelForm):
    class Meta:
        model = CaseProcedure
        fields = ['description']


class EvidenceForm(forms.ModelForm):
    class Meta:
        model = Evidence
        fields = ['description', 'document']


class HearingForm(forms.ModelForm):
    class Meta:
        model = Hearing
        fields = ['date', 'time', 'location', 'presiding_judge']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }


class TrialForm(forms.ModelForm):
    class Meta:
        model = Trial
        fields = ['date', 'location', 'result']

### CHIEF JUDGE
class JudgeAssignmentForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['judge']




### JUDGE #####

class LawyerAssignmentForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['assigned_lawyer']

class EvidenceStatusForm(forms.ModelForm):
    class Meta:
        model = Evidence
        fields = ['status']
    

