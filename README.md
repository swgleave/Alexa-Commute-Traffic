# Alexa-Toll
This repository contains an Alexa app I built to help me decide whether to take the toll road or not.

# Overview
I built this Alexa app to learn how Alexa apps work, and to help me with my daily decision making
for the route to take to and from work.  Google maps usually recommended two different routes to
take, one with tolls, and one without tolls.  Sometimes, the route times were similar, so I took the
route without tolls, but often, the route with tolls was faster.  This app helped me decide which route
to take, based on how much extra time I was willing to drive to avoid the tolls.  It ended up improving and simplifying the decision making process for me.  Instead of pulling up both the toll and nontoll routes and deciding if it was worth it to take the toll, the logic and origin/destination are already preprogrammed so I just have to ask Alexa what to do!  

I used the Amazon Alexa tutorial as a starting place, and left much of the framework unchanged.  https://developer.amazon.com/alexa-skills-kit/alexa-skill-python-tutorial.  I extended that basic tutorial and added a call to the Google Maps API behind the scenes, as well as calculations and decision logic to decide which route to take.  I also added user interaction to specify the destination of the driver, home or work.

*Note that I have removed the Google maps API calls in the python file as to not include personal key and information and have marked those lines where the code was removed.

# Technology

The code for this project was written in Python and hosted on AWS Lambda.  I used the Google Maps API to compute current drive times, and parsed the API calls with the urllib and json libraries.  I also learned to use the Alexa Skills Kit Developer Console to control the Alexa-User interactions.




