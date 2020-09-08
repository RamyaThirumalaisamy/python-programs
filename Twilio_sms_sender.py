# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
#give your twilio account sid number or use environmental variable
account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
#give your twilio token number
auth_token = 'fxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
#create a instance
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="HI this is Ramya!",
                     #give your twilio number which you buy in twilio
                     from_='+1xxxxxxxxxx',
                     #give your mobile number
                     to='+91xxxxxxxxxx'
                 )

print(message.sid)
