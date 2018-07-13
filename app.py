from chalice import Chalice, Response
import boto3

import urllib.request
import xml.etree.ElementTree as ET
import json

app = Chalice(app_name='chalice_project')
app.debug = True

BUCKET = 'gmimages'  # bucket name
s3_client = boto3.client('s3')

		
@app.route('/authors/{last_name}')
def list_authors(last_name):
	url = "https://reststop.randomhouse.com/resources/authors?lastName="+last_name
	names = set()
	authornumber = 1
	authors = {}

	#Grab response from REST endpoint and put results into ElementTree object
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	root = ET.fromstring(response.read())

	# find unique names in list
	for author in root.iter('author'):
		lf = author.find('authorlastfirst').text
		names.add(lf)

	# count works for uniqueAuthor
	for uniqueAuthor in names:
		curCount = 0
		author = {}
		for author in root.iter('author'):
			if uniqueAuthor == author.find('authorlastfirst').text:
				curCount = curCount + 1
		authors[authornumber] = {}
		authors[authornumber]['count'] = curCount
		authors[authornumber]['name'] = uniqueAuthor
		authornumber = authornumber + 1
	return json.dumps(authors)
	
	
@app.route('/upload/{file_name}', methods=['PUT'],
           content_types=['application/octet-stream'])
def upload_to_s3(file_name):

	extension_test = file_name.split(".")
	
	#return extension_test[1]
	if ((len(extension_test) != 2 ) or (extension_test[1].lower() != 'png')):
		return 'not a PNG'
	
	# get raw body of PUT request
	body = app.current_request.raw_body

	# write body to tmp file
	tmp_file_name = '/tmp/' + file_name
	with open(tmp_file_name, 'wb') as tmp_file:
		tmp_file.write(body)

	# upload tmp file to s3 bucket
	s3_client.upload_file(tmp_file_name, BUCKET, file_name)

	return Response(body='upload successful: {}'.format(file_name),
					status_code=200,
					headers={'Content-Type': 'text/plain'})
					

