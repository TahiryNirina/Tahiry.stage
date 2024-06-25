from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.LoginPage,name='login'),
    path("index/", views.index, name="index"),
    path("home",views.home,name="home"),
    path('signup/',views.SignupPage,name='signup'),
    path('logout/',views.LogoutPage,name='logout'),
    path("<str:niveau>", views.niveau, name="niveau"),
    path("<str:niveau>/<str:matiere>", views.matiere, name='matiere'),
    path("upload/",views.uploadfichier,name="upload"),
]
    