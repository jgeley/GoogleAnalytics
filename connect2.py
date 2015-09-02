import httplib2

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
        'metrics': 'ga:users',
	'dimensions': 'ga:browser',
        'start_date': '2013-01-01',
        'end_date': '2015-01-01'
        })
feed = data_query.execute()
print feed
print 'END FEED, START FEED ENTRY\n\n\n'
print feed['rows'][0][0]
