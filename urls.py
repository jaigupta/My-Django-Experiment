from django.conf.urls.defaults import *
import os
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
site_media = os.path.join(os.path.dirname(__file__), 'site_media')

urlpatterns = patterns('',
  # Example:
  # (r'^randompeople/', include('randompeople.foo.urls')),
  # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
  # to INSTALLED_APPS to enable admin documentation:
  # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
  # Uncomment the next line to enable the admin:
  (r'^admin/', include(admin.site.urls)),
  (r'^chat/$','apps.chat.views.index'),
  (r'^$','apps.creative.views.getfront'),
  (r'^index.php','apps.chat.views.index'),
  (r'^chat/startchat/$','apps.chat.views.chat'),
  (r'^chat/search_user/$','apps.chat.views.search_user'),
  (r'^chat/logout/$','apps.chat.views.logout_user'),
  (r'^chat/endthischat/$','apps.chat.views.endthischat'),
  (r'^chat/reviel/$','apps.chat.views.identityreviel'),
  (r'^chat/savedet/$','apps.chat.views.saveDet'),
  (r'^chat/relogin/$','apps.chat.views.index2'),
  (r'^chat/random/$','apps.chat.views.getchat'),
  (r'^chat/subm/$','apps.chat.views.getchat2'),
  (r'^chat/randomzz/$','apps.chat.views.getchatzz'),
  (r'^chat/chatForm/$','apps.chat.views.getform'),
  (r'^chat/hidden/$','apps.chat.views.getpart'),
  (r'^chat/random/$','apps.chat.views.blank'),
  (r'^chat/randomzz.jai$','apps.chat.views.getchatzz'),
  (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': site_media}),

  (r'^ism/upload/$','uplo.views.addthis'),
  (r'^ism/uploadf/$','uplo.views.formpage'),

  (r'^svg/$', 'apps.svgmaker.views.getsvg'),
  (r'^svg/getit$', 'apps.svgmaker.views.getit'),
  (r'^svg/bar.svg$', 'apps.svgmaker.views.getbar'),
  (r'^svg/tryjson$', 'apps.svgmaker.views.tryjson'),
  (r'^svg/saveform$', 'apps.svgmaker.views.saveform'),
  (r'^svg/showform/$', 'apps.svgmaker.views.showform'),
  (r'^svg/getform/$', 'apps.svgmaker.views.getform'),
  (r'^svg/submitform/$', 'apps.svgmaker.views.submitform'),
  (r'^svg/allform$', 'apps.svgmaker.views.allform'),
  (r'^svg/reviewform/$', 'apps.svgmaker.views.reviewform'),
  (r'^svg/getbargraph.svg$', 'apps.svgmaker.views.getbargraph'),
  (r'^svg/getpiechart.svg$', 'apps.svgmaker.views.getpiechart'),
  (r'^svg/excel.xls$', 'apps.svgmaker.views.getxls'),
  (r'^svg/csv.csv$', 'apps.svgmaker.views.getcsv'),

  (r'^creative/submit/$', 'apps.creative.views.submit'),
  (r'^creative/getimage.svg', 'apps.creative.views.getImage'),
  (r'^creative/getit/$', 'apps.creative.views.getit'),
  (r'^creative/mysubmit', 'apps.creative.views.submitx'),
  (r'^creative/viscom', 'apps.creative.views.getfront'),
  (r'^creative/sendma', 'apps.creative.views.sendit'),
)
