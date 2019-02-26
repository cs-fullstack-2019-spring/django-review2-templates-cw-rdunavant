from django.urls import path
# import endpoints_app
from . import views
urlpatterns = [
    path('templates/', views.templates, name='templates'),
    path('templates/<int:template>/', views.template, name='templates'),
]