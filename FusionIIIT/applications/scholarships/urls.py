from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from applications.scholarships.api.views import GetWinnersView
from applications.scholarships.api.views import create_award,McmUpdateView, McmRetrieveView, DirectorSilverRetrieveView,DirectorSilverUpdateView,DirectorGoldRetrieveView,DirectorGoldUpdateView,ProficiencyDmRetrieveView,ProficiencyDmUpdateView,AwardAndScholarshipCreateView
from applications.scholarships.api.views import ScholarshipDetailView,StudentDetailView,DirectorSilverDetailView,DirectorGoldDetailView,DirectorGoldListView,ReleaseCreateView,McmStatusUpdateView,DirectorSilverDecisionView,DirectorGoldAcceptRejectView,DirectorSilverListView
# ,DirectorSilverAcceptRejectView



app_name = 'spacs'

urlpatterns = [

    url(r'^$', views.spacs, name='spacs'),
    url(r'^student_view/$', views.student_view, name='student_view'),
    url(r'^convener_view/$', views.convener_view, name='convener_view'),
    url(r'^staff_view/$', views.staff_view, name='staff_view'),
    url(r'^stats/$', views.stats, name='stats'),
    url(r'^convenerCatalogue/$', views.convenerCatalogue, name='convenerCatalogue'),
    url(r'^getWinners/$', views.getWinners, name='getWinners'),
    url(r'^get_MCM_Flag/$', views.get_MCM_Flag, name='get_MCM_Flag'),
    url(r'^getConvocationFlag/$', views.getConvocationFlag, name='getConvocationFlag'),
    url(r'^getContent/$', views.getContent, name='getContent'),
    url(r'^updateEndDate/$', views.updateEndDate, name='updateEndDate'),
    #app -->
    url(r'get-winners/', GetWinnersView.as_view(), name='get-winners'),
    url(r'create-award/', create_award.as_view(), name='create-award'),
    url(r'mcm_update/', McmUpdateView.as_view(), name='mcm-update'),
    url(r'mcm_show/', McmRetrieveView.as_view(), name='mcm-show'),
    url(r'directorsilver_show/', DirectorSilverRetrieveView.as_view(), name='director-silver--show'),
    url(r'directorsilver_update/', DirectorSilverUpdateView.as_view(), name='director-silver-update'),
    url(r'directorgold_show/', DirectorGoldRetrieveView.as_view(), name='director-gold-show'),
    url(r'directorgold_update/', DirectorGoldUpdateView.as_view(), name='director-gold-update'),
    url(r'proficiencydm_update/', ProficiencyDmUpdateView.as_view(), name='proficiency-dm-update'),
    url(r'proficiencydm_show/', ProficiencyDmRetrieveView.as_view(), name='proficiency-dm-update'),
    path('award/', AwardAndScholarshipCreateView.as_view(), name='award-create'),  # URL for convenor catalog
    
    path('scholarship-details/', ScholarshipDetailView.as_view(), name='scholarship-list'),
    path('director_gold_list/', DirectorGoldListView.as_view(), name='director_gold_list'),
    #path('scholarship-details/<int:student_id>/', ScholarshipDetailView.as_view(), name='scholarship-detail'),
    url(r'student_file_show/', StudentDetailView.as_view(), name='student-file-show'),
    path('director_silver_show/', DirectorSilverDetailView.as_view(), name='director_silver_detail'),    
    path('director_gold_view/', DirectorGoldDetailView.as_view(), name='director_gold_detail'),
    path(r'release', ReleaseCreateView.as_view(), name='release_create'),
    
    # url(r'student_file_show/', StudentDetailView.as_view(), name='student-file-show'),
    path('mcm/status-update/', McmStatusUpdateView.as_view(), name='mcm-status-update'),
    path('api/director_silver/decision/', DirectorSilverDecisionView.as_view(), name='director_silver_decision'),
    path('director-gold/accept-reject/', DirectorGoldAcceptRejectView.as_view(), name='director-gold-accept-reject'),   
    path('director-silver/', DirectorSilverListView.as_view(), name='director-silver-list'),
    # path('director-silver/accept-reject/', DirectorSilverAcceptRejectView.as_view(), name='director-silver-accept-reject'),
]