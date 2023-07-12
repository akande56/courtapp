from django.urls import path
from . import views



urlpatterns = [
    path('', views.case_list, name='case_list'),
    path('<int:case_id>/', views.case_detail, name='case_detail'),
    path('cases/add/', views.add_case, name='add_case'),
    path('cases/<int:case_id>/add_proceedings/', views.add_proceeding, name='add_proceeding'),
    path('cases/<int:case_id>/add-evidence/', views.add_evidence, name='add_evidence'),
    path('cases/<int:case_id>/add-hearing/', views.add_hearing, name='add_hearing'),
    path('cases/<int:case_id>/assign_judge/', views.assign_judge, name='assign_judge'),
    path('cases/<int:case_id>/assign_lawyer/', views.assign_lawyer, name='assign_lawyer'),
    path('cases/<int:case_id>/<int:evidence_id>/update_status/', views.update_evidence_status, name='update_evidence_status'),
    path('cases/<int:case_id>/add_trial/', views.add_trial, name='add_trial'),






    # path('case/<int:case_id>/update/', views.update_case, name='update_case'),

]
