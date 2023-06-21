from django.urls import path
from . import views



urlpatterns = [
   
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('join/', views.join_view, name='join'),
    path('request_sent', views.request_sent_view, name='request_sent'),
    path('ui', views.ui_view, name='ui'),
    path('manage_records', views.manage_records_view, name='manage_records'),
    path('add_record_types', views.add_record_types_view, name='add_record_types'),
    path('home/', views.HomePageView, name = "home"),
    path("request_report/", views.VehiclesListView.as_view(), name = "request_report"),
    path("report_details/<int:pk>/", views.VehicleDetailsView.as_view(), name = "report_details"),
    path("search_edit", views.SearchEditListView.as_view(), name='search_edit'),
    path("search_edit_details/<int:pk>/", views.SearchEditDetailsView.as_view(), name = "search_edit_details"),
    path("vehicle/<int:pk>/", views.VehicleDetailsView.as_view(), name = "vehicle_detail"),
    path("vehicle/<int:pk>/<str:plate>/edit", views.VehicleUpdateView.as_view(), name = "vehicle_edit" ),
    path('CustomsRecord/<int:pk>/edit/', views.CustomsRecordUpdateView.as_view(), name='CustomsRecord_edit'),
    path("Ownership/<int:pk>/<str:plate>/<int:vehicle_pk>/edit", views.OwnershipUpdateView.as_view(), name = "Ownership_edit" ),
    path("NumberPlate/<int:pk>/<str:plate>/<int:vehicle_pk>/edit", views.NumberPlateUpdateView.as_view(), name = "NumberPlate_edit" ),
    path("FinanceRecord/<int:pk>/<str:plate>/<int:vehicle_pk>/edit", views.FinanceRecordUpdateView.as_view(), name = "FinanceRecord_edit" ),
    path("AccidentRecord/<int:pk>/<str:plate>/<int:vehicle_pk>/edit", views.AccidentRecordUpdateView.as_view(), name = "AccidentRecord_edit" ),
    path("PoliceRecord/<int:pk>/<str:plate>/<int:vehicle_pk>/edit", views.PoliceRecordUpdateView.as_view(), name = "PoliceRecord_edit" ),
    path("MaintenanceRecord/<int:pk>/<str:plate>/<int:vehicle_pk>/edit", views.MaintenanceRecordUpdateView.as_view(), name = "MaintenanceRecord_edit" ),
    path("vehicle/new/", views.VehicleCreateView.as_view(), name = "vehicle_new"),
    path("CustomsRecord/new/", views.CustomsRecordCreateView.as_view(), name = "CustomsRecord_new"),
    path("Ownership/new/", views.OwnershipCreateView.as_view(), name = "Ownership_new"),
    path("NumberPlate/new/", views.NumberPlateCreateView.as_view(), name = "NumberPlate_new"),
    path("FinanceRecord/new/", views.FinanceRecordCreateView.as_view(), name = "FinanceRecord_new"),
    path("AccidentRecord/new/", views.AccidentRecordCreateView.as_view(), name = "AccidentRecord_new"),
    path("PoliceRecord/new/", views.PoliceRecordCreateView.as_view(), name = "PoliceRecord_new"),
    path("MaintenanceRecord/new/", views.MaintenanceRecordCreateView.as_view(), name = "MaintenanceRecord_new"),
    path("vehicle/<int:pk>/delete", views.VehicleDeleteView.as_view(), name = "vehicle_delete" ),
    
  
]
