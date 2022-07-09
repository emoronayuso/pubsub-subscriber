import os
import json
import base64
from google.cloud import pubsub_v1
from google.cloud import firestore
from datetime import datetime

SUBSCRIPTION_PATH = 'projects/pruebas-pubsub-systerminal/subscriptions/topic_cf-subscription'
PROJECT = 'pruebas-pubsub-systerminal'

def subscriber_cf(event, context):
    """Background Cloud Function to be triggered by Pub/Sub.
    Args:
         event (dict):  The dictionary with data specific to this type of
                        event. The `@type` field maps to
                         `type.googleapis.com/google.pubsub.v1.PubsubMessage`.
                        The `data` field maps to the PubsubMessage data
                        in a base64-encoded string. The `attributes` field maps
                        to the PubsubMessage attributes if any is present.
         context (google.cloud.functions.Context): Metadata of triggering event
                        including `event_id` which maps to the PubsubMessage
                        messageId, `timestamp` which maps to the PubsubMessage
                        publishTime, `event_type` which maps to
                        `google.pubsub.topic.publish`, and `resource` which is
                        a dictionary that describes the service API endpoint
                        pubsub.googleapis.com, the triggering topic's name, and
                        the triggering event type
                        `type.googleapis.com/google.pubsub.v1.PubsubMessage`.
    Returns:
        None. The output is written to Cloud Logging.
    """

    print("This Function was triggered by messageId {} published at {}".format(context.event_id, context.timestamp))

    ##############################
    # read data from topic!

    if 'data' in event:
        
        message = event.get("data")
        decoded_message = json.loads(base64.b64decode(message).decode('utf-8'))
        row_to_insert = {
                         "sensorId":decoded_message['readings']["sensorId"],
                         "temperature":decoded_message['readings']["temperature"],
                         "humidity":decoded_message['readings']["humidity"],
                         "datetime":datetime.now()
                        }
    else:
        row_to_insert = {"sensorId":0,"temperature":0,"humidity":0,"datetime":datetime.now()}
    
    #subscriber = pubsub_v1.SubscriberClient()
    #message = subscriber.message.Message
    #message.ack()

    ###############################
    # move the data to Firestore!

    # Add a new data to document
    db = firestore.Client()
    doc_ref = db.collection('data').document('sensors')

    doc_ref.set(row_to_insert)

    return  200, {"status": "success"}

