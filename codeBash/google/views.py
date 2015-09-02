from django.shortcuts import render
from django.http import HttpResponse
import json
from connect import GoogleAnalytic
import math, datetime
from operator import itemgetter

# Create your views here.
def getData(startTime, endTime,dimensions=None, metrics=None):
	data = GoogleAnalytic(startTime, endTime, dimensions, metrics)
	newData = data.getData()
	return newData

def home(request):	
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

def reports(request):
	startDate = ""
	endDate = ""
	metric = ""
	dimension=""
	maxResults="10"
	if request.method == "GET":
		startDate = request.GET.get('startDate', '2012-01-01')
		endDate = request.GET.get('endDate', '2015-01-01')
		metric = request.GET.get('metric', 'users')
		dimension = request.GET.get('dimension', 'continent')
		maxResults = request.GET.get('numResults','10')

	else:
		startDate = "2012-01-01"
		endDate = "2015-01-01"
		metric='users'
		dimension = 'continent'

	data = getData(startDate,endDate,dimensions='ga:'+dimension,metrics='ga:'+metric)
	newData = []
	for x in data:
		newData.append([x[0],float(x[1])])
	sortedData = sorted(newData, key=itemgetter(1), reverse=True)
	counter = 0
	lastData=[]
	for x in sortedData:
		if counter < int(maxResults):
			lastData.append(x)
			counter += 1
		else:
			break
	
	tsvString = 'letter\tfrequency\n'
	counter = 0
	for ind,obj in enumerate(lastData):
		if obj[0] == u'Am\xe3':
			continue
		tsvString += obj[0]+"\t"+str(obj[1])+"\n"
	x = open('/var/www/django/codeBash/static/dataFiles/home.tsv','w')
	x.write(tsvString)
	x.close
	context = {'maxResultsReturned': int(maxResults)}
	return render(request, 'report.html',context)

def analytics(request):
	dim = ""
	startDate = ""
	endDate = ""
	metric = ""
	if request.method == "GET":
		startDate = request.GET.get('startDate', '2012-01-01')
		endDate = request.GET.get('endDate', '2015-01-01')
		dim = request.GET.get('days', 'nthWeek')
		metric = request.GET.get('metric', 'users')
	else:
		startDate = "2012-01-01"
		endDate = "2015-01-01"
		dim = 'nthWeek'
		metric='users'
	days=7
	if dim == 'nthWeek':
		days=7
	elif dim == 'nthMonth':
		days = 30
	elif dim == 'nthDay':
		days = 1
	td=datetime.timedelta(days=int(days))
	u = datetime.datetime.strptime(startDate,"%Y-%m-%d")
	data = getData(startDate,endDate,dimensions='ga:'+dim,metrics='ga:'+metric)

	tsvString = "date\tclose\n" 
	for ind, week in enumerate(data):
		tsvString+=str(str(u).split()[0])+"\t"+str(week[1])+"\n"
		u+=td

	x = open('/var/www/django/codeBash/static/dataFiles/analytics.tsv','w')
	x.write(tsvString)
	x.close
	
	return render(request, 'analytics.html')


def export(request):
	data = getData("2012-01-01","2015-01-01",dimensions='ga:browser')

	jsonString = '{"name": "flare","children":[{"name":"analytics","children":['
	for ind,browser in enumerate(data):
		jsonString+='{"name": "'+browser[0]+'", "size": '+str(math.ceil((int(browser[1])/10)))+'}'
		if ind != (len(data)-1):
			jsonString+=','
	jsonString+=']}]}'

	x = open('/var/www/django/codeBash/static/dataFiles/export.json','w')
	x.write(jsonString)
	x.close
	return render(request, 'export.html')

def settings(request):
	return render(request, 'settings.html')

def help(request):
	return render(request, 'help.html')

def pageViews(request):
	startDate = "2012-01-01"
	endDate = "2015-01-01"
	data = getData(startDate,endDate,dimensions='ga:hour,ga:dayOfWeek',metrics='ga:pageviews')
	tsvString = "day\thour\tvalue\n" 
	for ind, view in enumerate(data):
		tsvString+=str(int(view[1]) + 1)+"\t"+str(int(view[0]) + 1)+"\t"+str(view[2])+"\n"
	x = open('/var/www/django/codeBash/static/dataFiles/views.tsv','w')
	x.write(tsvString)
	x.close
	return render(request, 'pageViews.html')

def demogra(request):
	return render(request, 'demogra.html')
