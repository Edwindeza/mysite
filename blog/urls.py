from django.conf.urls import include, url
from . import views

urlpatterns = [
	# url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.post_list),
]