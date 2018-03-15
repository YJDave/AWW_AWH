from django.conf.urls import url, include
from django.contrib import admin
from aww.views import (
	HomePage,
	SubscribeUser,
	ListCirculars,
	ListVacancies,
	ApplyForVacancy,
	ListVacancyResults,
	VacancyResult,
	ListEligibility,
	ListLearningMaterials,
)

from adminsite.views import (
	AdminHomePage,
	ListCenters,
	CenterInfo,
	CenterApplications,
	ApplicationInfo,
)

from django.contrib.auth.views import login, logout

admin_site_urlpatterns = [
    url(r'^$', AdminHomePage, name="admin_home_page"),
    url(r'^login/$', login, name="admin_login"),
    url(r'^logout/$', logout, name="admin_logout"),
    url(r'^centers/$', ListCenters, name="admin_list_centers"),
    url(r'^centers/(?P<center_id>[\d]+)$', CenterInfo, name="admin_center"),
    url(r'^centers/(?P<center_id>[\d]+)/applications/$', CenterApplications,
    	name="admin_applications"),
    url(r'^centers/(?P<center_id>[\d]+)/applications/(?P<application_id>[\d]+)/$', ApplicationInfo,
    	name="admin_applications"),

]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePage, name="home_page"),
    url(r'^admin-user/', include(admin_site_urlpatterns), name="admin_urls"),
    url(r'^subscribe/$', SubscribeUser, name="subscription"),
    url(r'^circulars/$', ListCirculars, name="circulars"),
    url(r'^vacancies/$', ListVacancies, name="vacancies"),
    url(r'^apply/$', ApplyForVacancy, name="apply"),
    url(r'^results/$', ListVacancyResults, name="results"),
    url(r'^results/(?P<result_id>[\d]+)/$', VacancyResult, name="results"),
    url(r'^eligibility/$', ListEligibility, name="eligibility"),
    url(r'^learning-materials/$', ListLearningMaterials, name="learning_materials"),
]
