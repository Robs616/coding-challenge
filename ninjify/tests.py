from django.test import TestCase
from django.core import management
from buzzwords.models import BuzzwordCategory, Buzzword
import random, json


#test the result with words from buzzword
class NinjifyTestCase(TestCase):
    def setUp(self):
        #call command feeddb /buzzwords/management/commands
    	management.call_command('feeddb')

    #check the buzzword count for each category
    def test_ninjify_result(self):
    	print("Ninjify Result")
    	all_buzzword = []

    	#get all buzzword category
    	for item in BuzzwordCategory.objects.all():
    		all_buzzword.append(item.name)
    	#get all buzzword name
    	for item in Buzzword.objects.all():
    		all_buzzword.append(item.name)
    	
    	
    	#generate the result for 20 random sample of words (5 max)
    	for x in range(20):
    		sample = ','.join(random.sample(all_buzzword,random.randint(1, 5))).lower()
			#call the ninjify api and extract json
    		result = self.client.get('/ninjify/?x=' + sample).content.strip()
    		result = json.loads(result)['name']
    		print(sample + " : " + result)

    		