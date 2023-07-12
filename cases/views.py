# from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from .models import Case, CaseProcedure, Evidence
from .forms import (
    CaseForm,
    ProceedingForm, 
    EvidenceForm, 
    HearingForm,
    JudgeAssignmentForm,
    LawyerAssignmentForm,
    EvidenceStatusForm,
    TrialForm,
)
from .decorators import (
    judge_required,
    chief_judge_required,
    lawyer_required,
    clerk_required,
)


def case_list(request):
    user = request.user
    cases = Case.objects.all()

    if user.is_authenticated:
        if user.is_clerk:
            cases = cases.filter(clerk=user)
        elif user.is_lawyer:
            cases = cases.filter(assigned_lawyer=user)
        elif user.is_judge:
            cases = cases.filter(judge=user)
        elif user.is_chief_judge:
            cases = cases
        elif user.is_plaintief:
            cases = cases.filter(plaintiff=user)
        elif user.is_defendant:
            cases = cases.filter(defendant=user)
        else:
            cases = Case.objects.none()
        print(cases)
    return render(request, 'case_list.html', {'case_list': cases})


def case_detail(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    proceedings = case.proceedings.all()
    evidence = case.evidence.all()
    hearings = case.hearings.all()
    trials = case.trials.all()

    return render(request, 'case_detail.html', {'case': case, 'proceedings': proceedings, 'evidence':evidence, 'hearings': hearings, 'trials': trials})

############ CLERK ####################
@clerk_required
def add_case(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            case = form.save(commit=False)
            case.clerk = request.user  # Set the current clerk as the assigned clerk
            case.save()
            return redirect('case_list')  # Replace 'case-list' with the URL name for the case list view
    else:
        form = CaseForm()
    return render(request, 'add_case.html', {'form': form})


# add proceeding
@clerk_required
def add_proceeding(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    
    if request.method == 'POST':
        form = ProceedingForm(request.POST)
        if form.is_valid():
            proceeding = form.save(commit=False)
            proceeding.case = case
            proceeding.save()
            return redirect('case_detail', case_id=case_id)  # Replace 'case_detail' with the URL name for the case detail view
    else:
        form = ProceedingForm()
    
    return render(request, 'add_proceeding.html', {'form': form, 'case': case})



@clerk_required  # Decorate the view with the necessary permission requirement
def add_evidence(request, case_id):
    case = get_object_or_404(Case, id=case_id)

    if request.method == 'POST':
        form = EvidenceForm(request.POST, request.FILES)
        if form.is_valid():
            evidence = form.save(commit=False)
            evidence.case = case
            evidence.save()
            return redirect('case_detail', case_id=case_id)  # Redirect to the case detail page
    else:
        form = EvidenceForm()

    return render(request, 'add_evidence.html', {'case': case, 'form': form})


@clerk_required  # Decorate the view with the necessary permission requirement
def add_hearing(request, case_id):
    case = get_object_or_404(Case, id=case_id)

    if request.method == 'POST':
        form = HearingForm(request.POST)
        if form.is_valid():
            hearing = form.save(commit=False)
            hearing.case = case
            hearing.save()
            return redirect('case_detail', case_id=case_id)  # Redirect to the case detail page
    else:
        form = HearingForm()

    return render(request, 'add_hearing.html', {'case': case, 'form': form})



@clerk_required
def add_trial(request, case_id):
    case = get_object_or_404(Case, id=case_id)

    if request.method == 'POST':
        form = TrialForm(request.POST)
        if form.is_valid():
            trial = form.save(commit=False)
            trial.case = case
            trial.save()
            return redirect('case_detail', case_id=case.id)  # Replace 'case_detail' with the URL name for the case detail view
    else:
        form = TrialForm()

    return render(request, 'add_trial.html', {'case': case, 'form': form})

############### CHIEF JUDGE ###############################

@chief_judge_required
def assign_judge(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    if request.method == 'POST':
        form = JudgeAssignmentForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect('case_detail', case_id=case.id)  # Replace 'case_detail' with the URL name for the case detail view
    else:
        form = JudgeAssignmentForm(instance=case)

    return render(request, 'chiefJudge_assign_judge.html', {'case': case, 'form': form})



#### JUDGE ##########

@judge_required
def assign_lawyer(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    if request.method == 'POST':
        form = LawyerAssignmentForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect('case_detail', case_id=case.id)  # Replace 'case_detail' with the URL name for the case detail view
    else:
        form = LawyerAssignmentForm(instance=case)

    return render(request, 'judge_assign_lawyer.html', {'case': case, 'form': form})


@judge_required
def update_evidence_status(request, case_id, evidence_id):
    case = get_object_or_404(Case, id=case_id)
    evidence = get_object_or_404(Evidence, id=evidence_id, case=case)

    if request.method == 'POST':
        form = EvidenceStatusForm(request.POST, instance=evidence)
        if form.is_valid():
            form.save()
            return redirect('case_detail', case_id=case.id)  # Replace 'case_detail' with the URL name for the case detail view
    else:
        form = EvidenceStatusForm(instance=evidence)

    return render(request, 'update_evidence_status.html', {'case': case, 'evidence': evidence, 'form': form})


