from django.conf.urls import include, url

urlpatterns = [
    url(r'^activation/', include('nano.activation.urls')),
    url(r'^badge/', include('nano.badge.urls')),
    url(r'^blog/', include('nano.blog.urls')),
    url(r'^comments/', include('nano.comments.urls')),
    url(r'^faq/', include('nano.faq.urls')),
    url(r'^mark/', include('nano.mark.urls')),
    url(r'^privmsg/', include('nano.privmsg.urls')),
    url(r'^user/', include('nano.user.urls')),
]
