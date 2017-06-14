# -*- coding: utf-8 -*-
import os
from twilio.rest import Client

def handler(event, context):
    print "Event is "
    print event

    print "Context is"
    print context

    call_from = os.environ['from_number']
    sid = os.environ['twilio_sid']
    token = os.environ['twilio_token']
    click_type = event.get("clickType")

    call_to = os.environ['to_number_single_click']
    if click_type == "DOUBLE":
        call_to = os.environ['to_number_double_click']
    elif click_type == "LONG":
        call_to = os.environ['to_number_long_click']
    print "Calling %s" % call_to


    client = Client(sid, token)
    call = client.api.account.calls \
        .create(to=call_to,
        from_=call_from,
        url="http://twimlets.com/message?Message%5B0%5D=Hooray%20you%20found%20me&Message%5B1%5D=I%20and%20love%20and%20you")

    return True


