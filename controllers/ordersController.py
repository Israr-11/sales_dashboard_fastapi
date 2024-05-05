from fastapi import APIRouter, Body, Depends, HTTPException, status
from datetime import datetime, timezone
from models.orders import Order
from services.newCustomerCheck import is_new_customer
from services.coordinates import get_coordinates
from utils.database import dBConnection

router = APIRouter()

db, client, collection=dBConnection()

@router.post("/place_order", response_model=dict)
async def place_order(order_data: Order = Body(...)) -> dict:
    try:
        print("order data:", order_data)
        print("database connection:", db + collection)
        existing_customer = await is_new_customer(db, order_data.customerName, order_data.phoneNumber)
        new_customer = not existing_customer

        city_latitude, city_longitude, country_latitude, country_longitude = await get_coordinates(
            order_data.customerCity, order_data.customerCountry
        )

        new_order_data = order_data.model_dump()
        new_order_data['newCustomer'] = new_customer
        new_order_data['cityLatitude'] = city_latitude
        new_order_data['cityLongitude'] = city_longitude
        new_order_data['countryLatitude'] = country_latitude
        new_order_data['countryLongitude'] = country_longitude
        new_order_data['entryTime'] = datetime.now(timezone.utc)

        inserted_id = collection.insert_one(new_order_data).inserted_id

        response = {
            "message": "Order placed Successfully",
            "order_id": str(inserted_id),
            "status": "SUCCESSFUL",
        }

        return response

    except Exception as e:
        print(f"An error occurred while placing the order: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to place order")
