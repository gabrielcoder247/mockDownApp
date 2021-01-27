# from django.conf.urls import include
from django.conf import settings
from django.urls import path,re_path
from django.contrib.auth import logout
from django.conf.urls.static import static
# from . import views as core_views


# from . import views as core_views
# from django.contrib.auth import logout
from . import views

urlpatterns=[
    # path(r'',views.index,name = 'index_page'),
    re_path(r'index/(\d+)/$', views.home, name = 'home_page'),
    re_path(r'^new/yesNoBar/$', views.yesNoBar, name='yesNoBar'),
    # re_path(r'^new/state$',views.state,name='state_form'),
    # re_path(r'^new/ward$',views.ward,name='ward_form'),
    # re_path(r'^new/lga$',views.lga,name='lga_form'),
    re_path(r'^signup/$',views.signup, name='signup'),
    re_path(r'^sign-out/$', logout, name='logout'),
    # re_path(r'^lga/(\w{2,})/$',views.lga_filter,name = 'lga'),
    # re_path(r'^polls/(\w+)/$',views.polls,name = 'polls'),




]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)