from utils.database import dBConnection
from fastapi import HTTPException, status


def is_new_customer(db, customer_name, phone_number):
    try:
        db, client, collection=dBConnection()
        print("The db in newCustomerCheck is:", db.collection)
        existing_customer = collection.find_one({"customerName": customer_name, "phoneNumber": phone_number})
        return existing_customer is None
    except Exception as e:
        print(f"An error occurred while checking customer: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to check the new customer")
