from django.views.generic import TemplateView
from django.db.models import Q
from buzzwords.models import Buzzword
from ninjify.models import Result
from django.http import JsonResponse
from django.template.response import TemplateResponse


#result view for the permalink /resultat/id
class ResultView(TemplateView):
    template_name = 'result.html'

	#get results from the database
    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        try:
            context['result'] = Result.objects.get(id=kwargs['result_id'])
        except Result.DoesNotExist:
            context['result'] = None
        return context

#add a result in the database (string,string,bool)
def setResult(search,result,found):
     r = Result(search=search, result=result, found=found)
     r.save()
     return r.id

#return html to update the ninja name [/static/main.js]
def getResultNinjify(request,template_name="ajax/result_ninjify.html"):
	if request.is_ajax and request.method == "GET":
		args = {}
		return TemplateResponse(request, template_name, args)

#return html to update the result name [/static/main.js]
def getResultTable(request,template_name="ajax/result_table.html"):
	if request.is_ajax and request.method == "GET":
		args = {}
		args['results'] = Result.objects.all().filter(found=True).order_by('-id')[:10]
		return TemplateResponse(request, template_name, args)


#return the ninja name based on request x
def getNinjify(request): 
    ninja_names = []
    ajax = True
    #request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
    	
    	#get the parameter X from get else return empty response
    	para_x = request.GET.get("x", None)
    	if para_x is None:
    		return JsonResponse({}, status = 400)

		#check if request is for the front-end
    	if request.GET.get("ajax", None) is None:
    		ajax = False

			
    	queries = para_x.split(',')
    	original_query = para_x
		#loop from the get (x) results
    	for query in queries:
			#try to match request with the buzzword name and description
    		buzzwords = Buzzword.objects.filter(
            	Q(name__icontains=query) | Q(description__icontains=query)
        	)

			#loop in the query results
    		for item in buzzwords:   		
    			#grab a word from the description
    			if item.description:
    				ninja_names.append(getWordFromDescription(item.description,queries))
    				           		
				#grab the category of the buzzword
    			if item.category.name:
    				ninja_names.append(item.category.name.strip())

    			#grab the name of the buzzword 
    			if item.name != query:
    				ninja_names.append(item.name.strip())
				

		#clean the list from duplicates
    	ninja_names = list(dict.fromkeys(ninja_names))
    	for ninja_name in ninja_names:
    		if ninja_name.lower().strip() == query.lower().strip():
    			ninja_names.remove(ninja_name)
    	
    	
    	ninja_name = getNinjaNameFromList(ninja_names)
		
		#add result in database
    	if ninja_name == "Unfound Ninja":
    		result_id = setResult(original_query,ninja_name,False)
    	else:
    		result_id = setResult(original_query,ninja_name,True)
		
		#return the result id to the front-end for the permalink
    	if ajax:
    		return JsonResponse({"name":ninja_name,'result_id':result_id}, status = 200)
    	
    	return JsonResponse({"name":ninja_name}, status = 200)

    return JsonResponse({}, status = 400)



#return a word from the description based on average length of the words 
def getWordFromDescription(description,queries):
	result = ""
	#get minumum,maximum and calculate the average of the words length
	mins = min(len(word) for word in description.split())
	maxs = max(len(word) for word in description.split())
	average = int((int(mins) + int(maxs)) / 2)

	#keep a word  >= our average
	for word in description.split():
		if int(len(word)) >= average:
			#check if the word is not in the original query and return the result
			for query in queries:
				if query.lower().strip() not in word.lower().strip():
					result = word
					break
	
	return result



def getNinjaNameFromList(ninja_names):
	ninja_name = ""
	#split list in 3 parts if more than 3 words
	if len(ninja_names) >= 3:
		avg = len(ninja_names) / float(3)
		out = []
		last = 0.0

		#split the main list in 3 equal list
		while last < len(ninja_names):
    			out.append(ninja_names[int(last):int(last + avg)])
    			last += avg
    		
		#get one word from each list based on average length of list
		avg = avg / 2
		ninja_name1 = str(out[0][int(avg)]).title().strip(".")
		ninja_name2 = str(out[1][int(avg)]).title().strip(".")
		ninja_name3 = str(out[2][int(avg)]).title().strip(".")
		ninja_name = ninja_name1 + " " + ninja_name2 + " " + ninja_name3
		
	#return the result we have if less than 3 words
	else:
		name = ""
		for item in ninja_names:
			name += item.title().strip(".") + " "
			ninja_name = name

		if not ninja_name:
			ninja_name = "Unfound Ninja"

	return ninja_name