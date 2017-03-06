from django.conf.urls import url
from django.views.generic import TemplateView

from views import upload_file

urlpatterns = [
    url(r'^upload/$', upload_file, name='upload_file'),
    # url(r'^success/$', name='success'),
    url(r'^success/$', TemplateView.as_view(template_name="msg.html"), name='success'),
]
