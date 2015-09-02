import httplib2,json

from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials

def connect_to_analytics():
        #f = file('googleanalytics/your-privatekey.p12', 'rb')
        f=open('apiKey.p12','rb')
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

s=connect_to_analytics()
data_query = s.data().ga().get(**{
        'ids': 'ga:68741016',
	'dimensions': 'ga:javaEnabled',
	'metrics': 'ga:users',
        'start_date': '2013-01-01',
        'end_date': '2015-01-01'
        })
feed = data_query.execute()
print feed['rows']
print 'START HERE\n\n\n'

#data = feed['rows']
#jsonString = '{"name": "flare","children":[{"name":"analytics","children":['
#for ind,browser in enumerate(data):
#	jsonString+='{"name": "'+browser[0]+'", "size": '+browser[1]+'}'
#	if ind != (len(data)-1):
#		jsonString+=','
#jsonString+=']}]}'

#print jsonString
