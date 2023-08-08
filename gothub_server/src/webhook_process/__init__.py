from pathlib import Path

import firebase_admin
from firebase_admin import auth, credentials, firestore

DIR_PATH = Path(__file__).absolute().parent.parent.parent.parent

_cred = credentials.Certificate(DIR_PATH / "gothubai-firebase-admin-sdk.json")
firebase_admin.initialize_app(_cred)


firestore_client = firestore.client()
