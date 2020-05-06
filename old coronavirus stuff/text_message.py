import twilio
from twilio.rest import Client
import time

time.sleep(0)
account_sid = 'AC571ee0d507ff2c7880ad0079ff854f28'
auth_token = '7b9d5b6e9e2333a226e3215380b91734'

client = Client(account_sid, auth_token)

client.messages.create(
	to = '+12813233707',
	from_ = '+12816231038',
	body = 'Tot Tracker: Your child, HARSHINI, has activated their Tot Tracker and could be in danger!\nLatitude: 29.602232500000003\nLongitude: -95.5398029\nAddress: Stafford Middle School, 1625 Staffordshire Rd, Stafford, TX  77477, United States'
)