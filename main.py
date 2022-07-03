import os
import json
from google.cloud import pubsub_v1

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

    json_str = json.loads(event)

    print("EVENT -> {}",event)

    if 'data' in event:
        sensor_name = json_str['readings']['sensorName']
        temperature = json_str['readings']['temperature']
        humidity = json_str['readings']['humidity']
    else:
        sensor_name = 0
        temperature = 0
        humidity = 0

    subscriber = pubsub_v1.SubscriberClient()
    message = subscriber.message.Message
    message.ack()

#    blob = bucket.get_blob(event['name'])
#    data_json_str = blob.download_as_string()
#    data_json = json.loads(data_json_str)

#    sensor_name = data_json['sensorName']
#    temperature = data_json['temperature']
#    humidity = data_json['humidity']


    ###############################
    # move the data to Firestore!


