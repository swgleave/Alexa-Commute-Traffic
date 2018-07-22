

from __future__ import print_function
import json
import urllib
# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Hello Will," \
                    "I will tell you if you should take the toll or not," \
                    "are you going to work, or going home?"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = ""
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Skills Kit sample. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def get_system_status():
    session_attributes = {}
    card_title = "Traffic to Work"
    reprompt_text = ""
    should_end_session = True
 


    numero = "s"
    serviceurl = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=20331+rivercliff+ct+sterling+va&destinations=3939+campbell+ave+arlington+va&departure_time=now&key=AIzaSyDj3pON1W-alj18BE8bPRsZ7PrxVQodrPk'
    uh = urllib.urlopen(serviceurl)
    data = uh.read()

    location = json.loads(data)
    place = location['rows'][0]['elements'][0]['duration_in_traffic']['value']
    serviceurl2 = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=20331+rivercliff+ct+sterling+va&destinations=3939+campbell+ave+arlington+va&avoid=tolls&departure_time=now&key=AIzaSyDj3pON1W-alj18BE8bPRsZ7PrxVQodrPk'
    uh2 = urllib.urlopen(serviceurl2)
    data2 = uh2.read()
    location2 = json.loads(data2)
    place2 = location2['rows'][0]['elements'][0]['duration_in_traffic']['value']
    timedifference = (place2-place)/60
    response = None

    if timedifference > 5:
        response = "there is bad traffic today, take the toll road,"
    else:
        response = "travel times are similar, don't take the toll road,"
    
    speech_output = "my advice is that" + \
                    response + \
                    "Have a great day at work"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_system_status2():
    session_attributes = {}
    card_title = "Traffic Home"
    reprompt_text = ""
    should_end_session = True
 


    numero = "s"
    serviceurl = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=3939+campbell+ave+arlington+va&destinations=20331+rivercliff+ct+sterling+va&departure_time=now&key=AIzaSyDj3pON1W-alj18BE8bPRsZ7PrxVQodrPk'
    uh = urllib.urlopen(serviceurl)
    data = uh.read()

    location = json.loads(data)
    place = location['rows'][0]['elements'][0]['duration_in_traffic']['value']
    serviceurl2 = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=3939+campbell+ave+arlington+va&destinations=20331+rivercliff+ct+sterling+va&avoid=tolls&departure_time=now&key=AIzaSyDj3pON1W-alj18BE8bPRsZ7PrxVQodrPk'
    uh2 = urllib.urlopen(serviceurl2)
    data2 = uh2.read()
    location2 = json.loads(data2)
    place2 = location2['rows'][0]['elements'][0]['duration_in_traffic']['value']
    timedifference = (place2-place)/60
    response = None

    if timedifference > 3:
        response = "there is bad traffic today, take the toll road,"
    else:
        response = "travel times are similar, don't take the toll road,"
    
    speech_output = "my advice is that" + \
                    response + \
                    "Enjoy your evening!"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "getstatus":
        return get_system_status()
    elif intent_name == "getstatushome":
        return get_system_status2()
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])



    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])