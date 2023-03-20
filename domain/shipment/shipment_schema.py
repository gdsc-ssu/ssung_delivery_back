import enum
from typing import Optional

from pydantic import BaseModel


class ShipmentIn(BaseModel):
    content: str
    receiver_name: Optional[str]
    receiver_phone_number: Optional[str]
    destination: str
    shipment_detail: Optional[str]
    identifier: list


class ShipmentOut(BaseModel):
    crew_name: Optional[str]
    crew_phone_number: Optional[str]
    sender_name: Optional[str]
    content: Optional[str]
    sender_phone_number: Optional[str]
    receiver_name: Optional[str]
    receiver_phone_number: Optional[str]
    destination: str
    shipment_detail: Optional[str] = None
    identifier: Optional[list] = None
    history: Optional[list] = None
    status: Optional[enum.Enum] = None
