# -*- coding: utf-8 -*-
import os
from twilio.rest import Client

def handler(event, context):
    call_to = event.get('to_number')
    call_from = os.environ['from_number']
    sid = os.environ['twilio_sid']
    token = os.environ['twilio_token']
    print "Calling %s" % call_to


    client = Client(sid, token)

    # Make the call
    # call = client.api.account.calls \
    #     .create(to=call_to,
    #     from_=call_from,
    #     url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")

    return True