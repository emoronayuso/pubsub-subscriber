import os
from google.cloud import pubsub_v1

SUBSCRIPTION_PATH = 'projects/pruebas-pubsub-systerminal/subscriptions/topic_cf-subscription'

def subscriber_cf(message: pubsub_v1.subscriber.message.Message) -> None:

    ##############################
    # read data from topic!

    subscriber = pubsub_v1.SubscriberClient()

    print(f"Received {message}.")
    message.ack()

#    blob = bucket.get_blob(event['name'])
#    data_json_str = blob.download_as_string()
#    data_json = json.loads(data_json_str)

#    sensor_name = data_json['sensorName']
#    temperature = data_json['temperature']
#    humidity = data_json['humidity']


    ###############################
    # move the data to Firestore!


