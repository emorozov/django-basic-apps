from django.conf.urls import patterns, url
from basic.blog.views import PostList, PostArchiveYear, PostArchiveMonth, PostArchiveDay, PostDetail, CategoryDetail


urlpatterns = patterns('basic.blog.views',
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        view=PostDetail.as_view(),
        name='blog_detail'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/$',
        view=PostArchiveDay.as_view(),
        name='blog_archive_day'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
        view=PostArchiveMonth.as_view(),
        name='blog_archive_month'
    ),
    url(r'^(?P<year>\d{4})/$',
        view=PostArchiveYear.as_view(),
        name='blog_archive_year'
    ),
    url(r'^categories/(?P<slug>[-\w]+)/$',
        view=CategoryDetail.as_view(),
        name='blog_category_detail'
    ),
    url (r'^categories/$',
        view='category_list',
        name='blog_category_list'
    ),
    url(r'^tags/(?P<slug>[-\w]+)/$',
        view='tag_detail',
        name='blog_tag_detail'
    ),
    url (r'^search/$',
        view='search',
        name='blog_search'
    ),
    url(r'^page/(?P<page>\d+)/$',
        view=PostList.as_view(),
        name='blog_index_paginated'
    ),
    url(r'^$',
        view=PostList.as_view(),
        name='blog_index'
    ),
)
