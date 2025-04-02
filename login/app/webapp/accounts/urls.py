from django.urls import path
from .views import xss_demo, home  # Import the new view
from .views import home, login_view, logout_view, dashboard_view

urlpatterns = [
    path("", home, name="home"),  # Home page route
    path("xss-demo/", xss_demo, name="xss_demo"),
    path("", home, name="home"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboard_view, name="dashboard"),
]
