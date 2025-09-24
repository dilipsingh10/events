from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models.ticket import TicketType, Ticket
from ..schemas import TicketTypeCreate, TicketTypeOut, TicketCreate, TicketOut
from ..security import require_role


router = APIRouter()


@router.post("/types", response_model=TicketTypeOut, dependencies=[Depends(require_role(["organizer", "staff"]))])
def create_ticket_type(payload: TicketTypeCreate, db: Session = Depends(get_db)):
    tt = TicketType(**payload.dict())
    db.add(tt)
    db.commit()
    db.refresh(tt)
    return tt


@router.get("/types", response_model=List[TicketTypeOut])
def list_ticket_types(event_id: int, db: Session = Depends(get_db)):
    return db.query(TicketType).where(TicketType.event_id == event_id).all()


@router.post("/", response_model=TicketOut)
def create_ticket(payload: TicketCreate, db: Session = Depends(get_db)):
    tt = db.query(TicketType).get(payload.ticket_type_id)
    if not tt or tt.event_id != payload.event_id:
        raise HTTPException(status_code=400, detail="Invalid ticket type")
    ticket = Ticket(event_id=payload.event_id, ticket_type_id=payload.ticket_type_id, purchaser_email=payload.purchaser_email, status="reserved", price_paid=tt.price, currency=tt.currency)
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


@router.get("/by-event", response_model=List[TicketOut])
def list_tickets(event_id: int, db: Session = Depends(get_db)):
    return db.query(Ticket).where(Ticket.event_id == event_id).all()

