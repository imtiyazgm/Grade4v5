from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     
    path('',views.home , name="home"),
    path('SubPage',views.SubPage , name="SubPage"),
    path('EngNotes',views.EngNotes , name="EngNotes"),
    path('HinNotes',views.HinNotes , name="HinNotes"),
    path('AraNotes',views.AraNotes , name="AraNotes"),
    path('MatNotes',views.MatNotes , name="MatNotes"),
    path('SciNotes',views.SciNotes , name="SciNotes"),
    path('IssNotes',views.IssNotes , name="IssNotes"),
    path('UssNotes',views.UssNotes , name="UssNotes"),

    path('Upload_Notes',views.Upload_Notes , name="Upload_Notes"),
    path('Upload_Hin_Notes',views.Upload_Hin_Notes , name="Upload_Hin_Notes"),
    path('Upload_Ara_Notes',views.Upload_Ara_Notes , name="Upload_Ara_Notes"),
    path('Upload_Mat_Notes',views.Upload_Mat_Notes , name="Upload_Mat_Notes"),
    path('Upload_Sci_Notes',views.Upload_Sci_Notes , name="Upload_Sci_Notes"),
    path('Upload_Iss_Notes',views.Upload_Iss_Notes , name="Upload_Iss_Notes"),
    path('Upload_Uss_Notes',views.Upload_Uss_Notes , name="Upload_Uss_Notes"),

    path('EngClassNotes/<int:pk>',views.deleteEngNotes, name ='deleteEngNotes'),
    path('deleteHinNotes/<int:pk>',views.deleteHinNotes, name ='deleteHinNotes'),
    path('deleteAraNotes/<int:pk>',views.deleteAraNotes, name ='deleteAraNotes'),
    path('deleteMatNotes/<int:pk>',views.deleteMatNotes, name ='deleteMatNotes'),
    path('deleteSciNotes/<int:pk>',views.deleteSciNotes, name ='deleteSciNotes'),
    path('deleteIssNotes/<int:pk>',views.deleteIssNotes, name ='deleteIssNotes'),
    path('deleteUssNotes/<int:pk>',views.deleteUssNotes, name ='deleteUssNotes'),
    path('logout_Page',views.logout_Page, name='logout_Page'),
        
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
