from pathlib import Path

import firebase_admin
from firebase_admin import auth, credentials

DIR_PATH = Path(__file__).absolute().parent.parent.parent.parent

_cred = credentials.Certificate(DIR_PATH / "firebase_admin_sdk.json")
firebase_admin.initialize_app(_cred)
