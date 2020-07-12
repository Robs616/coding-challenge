from django.test import TestCase
from django.core import management
from .models import BuzzwordCategory, Buzzword


#feed database buzzwords test
class BuzzwordFeedTestCase(TestCase):
    def setUp(self):
        #call command feeddb /buzzwords/management/commands
    	management.call_command('feeddb')

    #check the buzzword count for each category
    def test_category_not_empty(self):
    	print("Category | Buzzword Count")
    	for item in BuzzwordCategory.objects.all():
    		print(item.name + " : " + str(Buzzword.objects.filter(category=item).count()))
    		
    	
        


