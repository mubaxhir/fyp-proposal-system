from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
        path('', views.index, name='signin'),
        path('signin/', views.signin, name='signin'),
        path('students/', views.students, name='students'),
        path('members/', views.members, name='member'),
        path('proposal/', views.student_proposal_details, name='student_proposal_details'),
        path('create_user/', views.create_user, name='create_user'),
        path('welcome/', views.welcome, name='welcome'),
        path('enrolllment/', views.enrolllment, name='enrolllment'),
        path('student_info/', views.student_info, name='student_info'),
        path('student_proposal_info/', views.student_proposal_info, name='student_proposal_info'),
        path('proposal_info/', views.proposal_info, name='proposal_info'),
        path('project_proposal/', views.project_proposal, name='project_proposal'),
        path('member_info/', views.member_info, name='member_info'),
        path('main_page/', views.main_page, name='main_page'),
        path('logout/', views.logout_view, name='logout'),
        path('projects/<str:status>', views.projects, name='projects'),
        path('projects/', views.projects, name='projects'),
        path('proposal/update_status/<int:obj_id>/<str:status>/', views.update_status, name='update_status'),
        path('proposal/comments/', views.add_comment, name='comment'),        
]