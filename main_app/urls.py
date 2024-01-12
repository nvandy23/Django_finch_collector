from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/',views.all_finches_index, name ='all_finches'),
    path('finch/<int:finch_id>/', views.finch_detail, name='detail'),
    path('finch/create/', views.FinchCreate.as_view(), name='finch_create'),
    path('finch/<int:pk>/update/', views.FinchUpdate.as_view(), name='finch_update'),
    path('finch/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch_delete'),
 ]