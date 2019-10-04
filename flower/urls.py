from . import views
from django.urls import re_path, include

urlpatterns = [
    re_path(r'^post_hoa/$', views.PostHoa.as_view(), name=views.PostHoa.name),
    re_path(r'^get_hoa/$', views.GetHoa.as_view(), name=views.GetHoa.name),

    # re_path(r'^', views.ApiRoot.as_view(), name=views.ApiRoot.name),

]