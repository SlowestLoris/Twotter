from django.urls import include, path, re_path
from . import views

urlpatterns = [
	path("accounts/", include("django.contrib.auth.urls")),
	path("dashboard/", views.dashboard,name="dashboard"),
	path('profile/<username>/', views.profile, name="profile"),
	path("signup/", views.signup,name="signup"),
]
