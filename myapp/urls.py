from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^hello$', 
        TemplateView.as_view(template_name='hello.html'),
        name='hello'),
]