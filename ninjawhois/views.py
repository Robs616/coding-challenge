from django.views.generic import TemplateView
from ninjify.models import Result

#home page view (/templates)
class HomePageView(TemplateView):
    template_name = 'home.html'

	#get search results for the table in home.html
    def get_context_data(self, **kwargs):
       context = super(HomePageView, self).get_context_data(**kwargs)
       context['results'] = Result.objects.all().filter(found=True).order_by('-id')[:10]
       return context

