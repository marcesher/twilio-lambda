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
    url = os.environ['url_single_click']
    if click_type == "DOUBLE":
        call_to = os.environ['to_number_double_click']
        url = os.environ['url_double_click']
    elif click_type == "LONG":
        call_to = os.environ['to_number_long_click']
        url = os.environ['url_long_click']
    print "Calling %s" % call_to


    client = Client(sid, token)
    call = client.api.account.calls.create(to=call_to, from_=call_from, url=url)

    return True


