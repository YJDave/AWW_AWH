from django.conf.urls import url
from django.contrib import admin
from aww.views import (
	HomePage,
	SubscribeUser,
	ListCirculars,
	ListVacancies,
	ApplyForVacancy,
	VacancyResult,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePage.as_view(), name="home_page"),
    url(r'^subscribe/$', SubscribeUser.as_view(), name="subscription"),
    url(r'^circulars/$', ListCirculars.as_view(), name="circulars"),
    url(r'^vacancies/$', ListVacancies.as_view(), name="vacancies"),
    url(r'^apply/$', ApplyForVacancy.as_view(), name="apply"),
    url(r'^results/$', VacancyResult.as_view(), name="results"),
]
