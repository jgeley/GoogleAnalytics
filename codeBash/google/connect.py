import httplib2

from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials

class GoogleAnalytic():
	def __init__(self, startTime, endTime, dimensions=None, metrics=None):
		self.session = self.connect_to_analytics()
		self.data = ""
		self.startTime=startTime
		self.endTime=endTime
		self.dimensions=dimensions
		self.metrics=metrics

	def connect_to_analytics(self):
		#f = file('googleanalytics/your-privatekey.p12', 'rb')
		f=open('/var/www/django/codeBash/google/apiKey.p12','rb')
		key = f.read()
		f.close()
		credentials = SignedJwtAssertionCredentials(
		'349341612675-993gripmec7euej862i1af56tov9urvd@developer.gserviceaccount.com',
		key,
		scope='https://www.googleapis.com/auth/analytics.readonly'#,
		)#token_uri='https://accounts.google.com/o/oauth2/token')

		http = httplib2.Http()
		http = credentials.authorize(http)
		return build('analytics', 'v3', http=http)
		#return build('analytics','v3')

	def getData(self): #dimensions and metrics need to be a comma seperate string
		#start time will look like yyyy-mm-dd
		s=self.session
		if self.dimensions != None or self.metrics != None:
			if self.dimensions != None and self.metrics != None:
		                data_query = s.data().ga().get(**{
		                        'ids': 'ga:68741016',
		                        'metrics': self.metrics,
		                        'dimensions': self.dimensions,
		                        'start_date': self.startTime,
		                        'end_date': self.endTime
		                        })
			elif self.dimensions == None:
		                data_query = s.data().ga().get(**{
		                        'ids': 'ga:68741016',
		                        'metrics': self.metrics,
		                        'start_date': self.startTime,
		                        'end_date': self.endTime
		                        })
			elif self.metrics == None:
				data_query = s.data().ga().get(**{
					'ids': 'ga:68741016',
					'metrics': 'ga:users',
					'dimensions': self.dimensions,
					'start_date': self.startTime,
					'end_date': self.endTime
					})
			feed = data_query.execute()
			return feed['rows']
		else:
			return ""
