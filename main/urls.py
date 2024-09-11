from django.urls import path
from main.views import show_main
from main.views import show_main, create_mood_entry
from main.views import show_main, create_mood_entry, show_xml
from main.views import show_main, create_mood_entry, show_xml, show_json
from main.views import show_main, create_mood_entry, show_xml, show_json, show_xml_by_id, show_json_by_id


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-mood-entry', create_mood_entry, name='create_mood_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]