import firebase_admin
from firebase_admin import credentials, firestore

# Initialize the Firebase Admin SDK
cred = credentials.Certificate("gothubai-firebase-admin-sdk.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Reference to all users
users_ref = db.collection("users")

# Iterate over all users
for user in users_ref.stream():
    # For each user, get their orders
    orders_ref = users_ref.document(user.id).collection("orders")

    # Query for orders with the specific prompt
    target_orders = orders_ref.where(
        "prompt", "==", "Write me a fun snake game in Python.\n"
    ).stream()

    for order in target_orders:
        print(f"Deleting order {order.id} of user {user.id}")
        order.reference.delete()

    target_orders = orders_ref.where("status", "==", "failed").stream()

    for order in target_orders:
        print(f"Deleting order {order.id} of user {user.id}")
        order.reference.delete()


print("Deletion process completed!")
