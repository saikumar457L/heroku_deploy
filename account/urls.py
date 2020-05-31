from django.urls import path

from django.contrib.auth import views as auth_views


from .views import dashboard,new_user,edit,just_try




urlpatterns = [
    path("login/",auth_views.LoginView.as_view(), name='login'),
    path("logout/",auth_views.LogoutView.as_view(), name='logout'),
    path("change_password/",auth_views.PasswordChangeView.as_view(),name="password_change"),
    path("password_change/done/",auth_views.PasswordChangeDoneView.as_view(),name="password_change_done"),
    path("password_reset/",auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/sent_to_mail/",auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password_reset/<uidb64>/<token>/confirm/",auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password_reset/done/",auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path("create_account/",new_user, name="create_account"),
    path("edit/",edit,name="update_profile"),
    path("",dashboard, name="dashboard"),
    path("home/",just_try,name="home"),
]
