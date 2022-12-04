
from django.urls import path

from APP import views, adminviews

urlpatterns = [
    path('',views.mainpage,name='mainpage'),
    path('student',views.student,name='student'),
    path('parent',views.parent,name='parent'),

    path('admin1',views.admin1,name='admin1'),
    path('studentview',views.studentview,name='studentview'),
    path('parentview',views.parentview,name='parentview'),
    path('viewstudents',adminviews.viewstudents,name='viewstudents'),
    path('viewsparents',adminviews.viewsparents,name='viewsparents'),
    path('approve_student/<int:id>/',adminviews.approve_student,name='approve_student'),
    path('reject_student/<int:id>/',adminviews.reject_student,name='reject_student'),
    path('approve_parent/<int:id>/',adminviews.approve_parent,name='approve_parent'),
    path('reject_parent/<int:id>/',adminviews.reject_parent,name='reject_parent'),
    path('add_hostel', adminviews.add_hostel, name='add_hostel'),
    path('view_hostel', adminviews.view_hostel, name='view_hostel'),
    path('hostel_update/<int:id>/', adminviews.hostel_update, name='hostel_update'),
    path('hostel_delete/<int:id>/', adminviews.hostel_delete, name='hostel_delete'),

]