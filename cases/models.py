from django.db import models
from courtapp.users.models import User

class Court(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.name

class CaseCategory(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.name

class Case(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    category = models.ForeignKey(CaseCategory, on_delete=models.CASCADE)
    plaintiff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plaintiff_cases')
    defendant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='defendant_cases')
    judge = models.ForeignKey(User, on_delete=models.CASCADE, related_name='judged_cases', null=True, limit_choices_to={'is_judge': True})
    assigned_lawyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_cases', null=True, limit_choices_to={'is_lawyer': True})
    clerk = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clerk_filed_cases', limit_choices_to={'is_clerk': True})

    def __str__(self):
        return self.title

class CaseDocument(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='documents')
    document = models.FileField(upload_to='case_documents/')

    def __str__(self):
        return self.document.name

HEARING_STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Under Review', 'Under Review'),
    )

class Evidence(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='evidence')
    description = models.TextField()
    document = models.FileField(upload_to='evidence_documents/')
    status = models.CharField(max_length=100, choices=HEARING_STATUS_CHOICES)

    def __str__(self):
        return self.description

class CaseProcedure(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE,  related_name='proceedings')
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

class Hearing(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='hearings')
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    presiding_judge = models.ForeignKey(User, on_delete=models.CASCADE, related_name='presiding_judge_hearings', limit_choices_to={'is_judge': True})

    # Add other fields as needed

    def __str__(self):
        return f"Hearing for Case: {self.case.title}"

class Trial(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='trials')
    date = models.DateField()
    location = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return f"Trial for Case: {self.case.title}"