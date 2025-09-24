from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class EventCreate(BaseModel):
    title: str
    description: Optional[str] = None
    venue: Optional[str] = None
    timezone: Optional[str] = None
    type: Optional[str] = None
    capacity: Optional[int] = None
    is_online: bool = False
    start_datetime: Optional[datetime] = None
    end_datetime: Optional[datetime] = None


class EventOut(EventCreate):
    id: int

    class Config:
        from_attributes = True


class TicketTypeCreate(BaseModel):
    event_id: int
    name: str
    description: Optional[str] = None
    price: float = 0
    currency: str = "USD"
    capacity: Optional[int] = None


class TicketTypeOut(TicketTypeCreate):
    id: int

    class Config:
        from_attributes = True


class TicketCreate(BaseModel):
    event_id: int
    ticket_type_id: int
    purchaser_email: str


class TicketOut(BaseModel):
    id: int
    event_id: int
    ticket_type_id: int
    purchaser_email: str
    status: str
    price_paid: float
    currency: str

    class Config:
        from_attributes = True


class AttendeeCreate(BaseModel):
    event_id: int
    ticket_id: Optional[int] = None
    name: str
    email: str
    phone: Optional[str] = None
    company: Optional[str] = None
    designation: Optional[str] = None
    category: str = "General"


class AttendeeOut(AttendeeCreate):
    id: int

    class Config:
        from_attributes = True


class SessionCreate(BaseModel):
    event_id: int
    title: str
    description: Optional[str] = None
    type: str = "Breakout"
    location: Optional[str] = None
    start_datetime: Optional[datetime] = None
    end_datetime: Optional[datetime] = None
    capacity: Optional[int] = None
    requires_registration: bool = False
    access_level: str = "All"


class SessionOut(SessionCreate):
    id: int

    class Config:
        from_attributes = True

