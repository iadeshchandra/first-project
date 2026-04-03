import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Initialize Firestore database
db = firestore.client()

class SyncService:
    def __init__(self, collection_name):
        self.collection_name = collection_name

    def add_document(self, doc_id, data):
        db.collection(self.collection_name).document(doc_id).set(data)

    def get_document(self, doc_id):
        doc = db.collection(self.collection_name).document(doc_id).get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None

    def update_document(self, doc_id, data):
        db.collection(self.collection_name).document(doc_id).update(data)

    def delete_document(self, doc_id):
        db.collection(self.collection_name).document(doc_id).delete()