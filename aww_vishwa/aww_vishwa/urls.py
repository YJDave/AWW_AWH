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
    url(r'^$', AdminHomePage.as_view(), name="admin_home_page"),
    url(r'^login/$', login, name="admin_login"),
    url(r'^logout/$', logout, name="admin_logout"),
    url(r'^centers/$', ListCenters.as_view(), name="admin_list_centers"),
    url(r'^centers/(?P<center_id>[\d]+)$', CenterInfo.as_view(), name="admin_center"),
    url(r'^centers/(?P<center_id>[\d]+)/applications$', CenterApplications.as_view(),
    	name="admin_applications"),
    url(r'^centers/(?P<center_id>[\d]+)/applications/(?P<application_id>[\d]+)/$', ApplicationInfo.as_view(),
    	name="admin_applications"),

]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePage.as_view(), name="home_page"),
    url(r'^admin-user/', include(admin_site_urlpatterns), name="admin_urls"),
    url(r'^subscribe/$', SubscribeUser.as_view(), name="subscription"),
    url(r'^circulars/$', ListCirculars.as_view(), name="circulars"),
    url(r'^vacancies/$', ListVacancies.as_view(), name="vacancies"),
    url(r'^apply/$', ApplyForVacancy.as_view(), name="apply"),
    url(r'^results/$', ListVacancyResults.as_view(), name="results"),
    url(r'^results/(?P<result_id>[\d]+)/$', VacancyResult.as_view(), name="results"),
    url(r'^eligibility/$', ListEligibility.as_view(), name="eligibility"),
    url(r'^learning-materials/$', ListLearningMaterials.as_view(), name="learning_materials"),
]
