"""定义learning_logs的URL模式"""
from django.urls import path
from . import views
urlpatterns = [
    #主页
    path(r'',views.index,name='index'),
    path(r'topics/$',views.topics,name='topics'),
    #特定主题页的详细页面
    path(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    #新建主题的url模式
    path(r'^new_topic/$',views.new_topic,name='new_topic'),
    #新的主体条目
    path(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
    #编辑条目
    path(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry')
]
app_name = 'learning_logs'