from google.cloud import firestore

db = firestore.Client()
doc_ref = db.collection(u'data')

query_ref = doc_ref.where(u'sensorId', u'==', 0).stream()

for doc in query_ref:
    print(doc.to_dict())

