from datetime import datetime, timezone
from typing import List, Optional

from pydantic import BaseModel, Field, field_validator

class Order(BaseModel):
    customerName: str = Field(..., description="Name of the customer")
    # newCustomer: bool = Field(..., description="Indicates if the customer is actually new")
    newCustomer: Optional[bool]=None
    price: float = Field(..., gt=0, description="Order price")
    currency: str = Field(..., description="Currency of the order")
    productCategories: List[str] = Field(..., description="List of product categories")
    salesType: str = Field(..., description="Sales type for the order")
    phoneNumber: Optional[str] = Field(default=None, description="Customer's phone number (optional)")
    quantity: int = Field(..., gt=0, description="Quantity of items ordered")
    orderName: str = Field(..., description="Name of the order")
    customerCity: str = Field(..., description="City of the customer")
    customerCountry: str = Field(..., description="Country of the customer")
    # cityLatitude: float = Field(..., description="Latitude of the customer's city")
    # cityLongitude: float = Field(..., description="Longitude of the customer's city")
    # countryLatitude: float = Field(..., description="Latitude of the customer's country")
    # countryLongitude: float = Field(..., description="Longitude of the customer's country")
    cityLatitude: Optional[float] = None  # Make latitude optional
    cityLongitude: Optional[float] = None  # Make longitude optional
    countryLatitude: Optional[float] = None  # Make latitude optional
    countryLongitude: Optional[float] = None  # Make longitude optional
    entryTime: datetime = Field(default=datetime.now(timezone.utc), description="Time the order was entered")

    @field_validator('entryTime')
    def validate_entry_time(cls, v):
        if not isinstance(v, datetime):
            raise ValueError('entryTime must be a datetime object')
        return v

    def to_dict(self):
        return self.model_dump()  # Leverage Pydantic's built-in to_dict method
