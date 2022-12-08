from django.urls import path
from .views import *

app_name = 'QnAbase'

urlpatterns = [
    path('', home, name="home"),
    path('detail/<int:id>', detail,name='detail'),
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('activate/<uidb64>/<token>',activate, name='activate'),
    path('save-comment', save_comment,name='save-comment'),
    path('save-upvote', save_upvote,name='save-upvote'),
    path('save-downvote', save_downvote,name='save-downvote'),
    path('ask-question', ask_form,name='ask-question'),
    path('logout-view', logout_view, name="logout_view"),
    path('live', live, name='live'),
    path('search', search, name='search')
]
