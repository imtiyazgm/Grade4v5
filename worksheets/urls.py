from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     
    path('Upload_Eng_WS',views.Upload_Eng_WS , name="Upload_Eng_WS"),
    path('Upload_Hin_WS',views.Upload_Hin_WS , name="Upload_Hin_WS"),
    path('Upload_Ara_WS',views.Upload_Ara_WS , name="Upload_Ara_WS"),
    path('Upload_Mat_WS',views.Upload_Mat_WS , name="Upload_Mat_WS"),
    path('Upload_Sci_WS',views.Upload_Sci_WS , name="Upload_Sci_WS"),
    path('Upload_Iss_WS',views.Upload_Iss_WS , name="Upload_Iss_WS"),
    path('Upload_Uss_WS',views.Upload_Uss_WS , name="Upload_Uss_WS"),

    path('EngWsheet',views.EngWsheet , name="EngWsheet"),
    path('AraWsheet',views.AraWsheet , name="AraWsheet"),
    path('HinWsheet',views.HinWsheet , name="HinWsheet"),
    path('MatWsheet',views.MatWsheet , name="MatWsheet"),
    path('SciWsheet',views.SciWsheet , name="SciWsheet"),
    path('IssWsheet',views.IssWsheet , name="IssWsheet"),
    path('UssWsheet',views.UssWsheet , name="UssWsheet"),


     
    path('EngWS/<int:pk>',views.deleteEngWS, name ='deleteEngWS'),
    path('AraWS/<int:pk>',views.deleteAraWS, name ='deleteAraWS'),
    path('HinWS/<int:pk>',views.deleteHinWS, name ='deleteHinWS'),
    path('MatWS/<int:pk>',views.deleteMatWS, name ='deleteMatWS'),
    path('SciWS/<int:pk>',views.deleteSciWS, name ='deleteSciWS'),
    path('IssWS/<int:pk>',views.deleteIssWS, name ='deleteIssWS'),
    path('UssWS/<int:pk>',views.deleteUssWS, name ='deleteUssWS'),
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
