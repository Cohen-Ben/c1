# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json

apiKey = '3a9ecf6c8c0154fa75bcce7f802a4398'

def numberOfCustomers():
	url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey);
	response = requests.get(
	url,
	headers={'content-type':'application/json'},
	)

	customers = response.json();
	return len(customers);

def addCustomer():
	url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey);
	customerData = {
	  "first_name": "A",
	  "last_name": "A",
	  "address": {
	    "street_number": "1",
	    "street_name": "Friend Center",
	    "city": "Princeton",
	    "state": "NJ",
	    "zip": "08544"
	  }
	}

	response = requests.post(
		url,
		data=json.dumps(customerData),
		headers={'content-type':'application/json'},
		)

	return response.json()["objectCreated"]["_id"];

def addMerchant(topic = None):

	if topic is None:
		merchantData = {
		  "name": "A",
		  "category": "A",
		  "address": {
		    "street_number": "1",
		    "street_name": "Friend Center",
		    "city": "Princeton",
		    "state": "NJ",
		    "zip": "08544"
		  },
		  "geocode": {
		    "lat": 0,
		    "lng": 0
		  }
		}
	else:
		merchantData = {
		  "name": "A",
		  "category": topic,
		  "address": {
		    "street_number": "1",
		    "street_name": "Friend Center",
		    "city": "Princeton",
		    "state": "NJ",
		    "zip": "08544"
		  },
		  "geocode": {
		    "lat": 0,
		    "lng": 0
		  }
		}

	url = 'http://api.reimaginebanking.com/merchants?key={}'.format(apiKey);

	response = requests.post(
		url,
		data=json.dumps(merchantData),
		headers={'content-type':'application/json'},
		)

	return response.json()["objectCreated"]["_id"];

def numberOfMerchants():
	url = 'http://api.reimaginebanking.com/merchants?key={}'.format(apiKey);

	response = requests.get(
		url,
		headers={'content-type':'application/json'},
		)
	merchants = response.json();
	return len(merchants);