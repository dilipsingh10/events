from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.ticket import TicketType, Ticket
from ..models.attendee import Attendee
from ..schemas import AttendeeOut


router = APIRouter()


@router.post("/simple", response_model=AttendeeOut)
def simple_registration(event_id: int, ticket_type_id: int, name: str, email: str, db: Session = Depends(get_db)):
    ticket_type = db.query(TicketType).get(ticket_type_id)
    if not ticket_type or ticket_type.event_id != event_id:
        raise HTTPException(status_code=400, detail="Invalid ticket type for event")

    ticket = Ticket(event_id=event_id, ticket_type_id=ticket_type_id, purchaser_email=email, status="reserved", price_paid=ticket_type.price, currency=ticket_type.currency)
    db.add(ticket)
    db.flush()

    attendee = Attendee(event_id=event_id, ticket_id=ticket.id, name=name, email=email, category="General")
    db.add(attendee)
    db.commit()
    db.refresh(attendee)
    return attendee

