from django.conf.urls.defaults import *

urlpatterns = patterns('',
#urlpatterns = patterns('dynamicform.todo.views',
    (r'^$', 'dynamicform.todo.views.index'),
    (r'thanks$', 'django.views.generic.simple.direct_to_template', {'template': 'todo/thanks.html'}),
)
