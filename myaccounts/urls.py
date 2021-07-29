from django.urls import path
from myaccounts import views
app_name="myaccounts"
#from django.contrib.auth import views
urlpatterns = [
    #path('login/',views.LoginView.as_view(template_name='accounts/login.html',redirect_authenticated_user=True),name='login'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('create_new_user/',views.create_new_user,name='create_new_user')
]
