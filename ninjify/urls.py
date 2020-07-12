from django.urls import path
from .views import ResultView, getNinjify, getResultTable, getResultNinjify

urlpatterns = [
	path('',getNinjify, name='ninjify'),
	path('ajax/getNinjify/', getNinjify, name = "ninjify"),
	path('ajax/getResultTable/', getResultTable, name = "result_table"),
	path('ajax/getResultNinjify/', getResultNinjify, name = "result_ninjify"),
	path('resultat/<int:result_id>/', ResultView.as_view(), name='resultat'),
]