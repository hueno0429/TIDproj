from django.urls import path
from . import views

urlpatterns = [
    path('log/', views.log_work, name='log_work'),
    path('list/', views.work_log_list, name='work_log_list'),
    path('edit/<int:pk>/', views.edit_work_log, name='edit_work_log'),
    path('all_logs_by_date/', views.all_work_logs_by_date, name='all_work_logs_by_date'),  # 新しいURL
    path('export_csv/', views.export_work_logs_csv, name='export_work_logs_csv'),  # CSVダウンロード用URL
]