from django.conf.urls import url
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
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePage.as_view(), name="home_page"),
    url(r'^subscribe/$', SubscribeUser.as_view(), name="subscription"),
    url(r'^circulars/$', ListCirculars.as_view(), name="circulars"),
    url(r'^vacancies/$', ListVacancies.as_view(), name="vacancies"),
    url(r'^apply/$', ApplyForVacancy.as_view(), name="apply"),
    url(r'^results/$', ListVacancyResults.as_view(), name="results"),
    url(r'^results/(?P<result_id>[\d]+)/$', VacancyResult.as_view(), name="results"),
    url(r'^apply/$', ApplyForVacancy.as_view(), name="apply"),
    url(r'^eligibility/$', ListEligibility.as_view(), name="apply"),
]
