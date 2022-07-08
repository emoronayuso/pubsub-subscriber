import os
import json
from google.cloud import pubsub_v1
from google.cloud import firestore
from datetime import datetime

SUBSCRIPTION_PATH = 'projects/pruebas-pubsub-systerminal/subscriptions/topic_cf-subscription'

def subscriber_cf(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """

    print("This Function was triggered by messageId {} published at {}".format(context.event_id, context.timestamp))

    ##############################
    # read data from topic!

    #if 'data' in event:
    #    sensor_id = event['data']['readings']['sensorId']
    #    temperature = event['data']['readings']['temperature']
    #    humidity = event['data']['readings']['humidity']
    #else:
    #    sensor_name = 0
    #    temperature = 0
    #    humidity = 0

    subscriber = pubsub_v1.SubscriberClient()
    message = subscriber.message.Message
    message.ack()

    ###############################
    # move the data to Firestore!

    # Add a new data to document
    db = firestore.Client()
    doc_ref = db.collection(u'data').document(u'sensors')

    data = json.dumps(event['data']['readings'])

    #data['sensorId'] = sensor_id
    #data['temperature'] = temperature
    #data['humidity'] = humidity
    data['datetime'] = datetime.now() 

    doc_ref.set(data)

#    doc_ref.set({
#        u'sensorId': sensor_id,
#        u'temperature': temperature,
#        u'humidity': humidity,
#        u'datetime': datetime.now()
#    })

