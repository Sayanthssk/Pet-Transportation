from django.urls import path

from .views import *

urlpatterns = [
    path('viewuser/', Viewuser.as_view(), name='viewuser'),
    path('viewservice/', Viewservice.as_view(), name='viewservice'),
    path('viewcomplaint/', Viewcomplaint.as_view(), name='viewcomplaint'),
    path('reply/<int:pk>', Reply.as_view(), name='reply'),
    path('viewfeedback/', Feedview.as_view(), name='viewfeedback'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Login.as_view(), name='logout'),
    path('admindash/', Admin_dash.as_view(), name='admindash'),

]
