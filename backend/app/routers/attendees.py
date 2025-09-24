from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models.attendee import Attendee
from ..schemas import AttendeeCreate, AttendeeOut
from ..security import require_role


router = APIRouter()


@router.post("/", response_model=AttendeeOut)
def create_attendee(payload: AttendeeCreate, db: Session = Depends(get_db)):
    attendee = Attendee(**payload.dict())
    db.add(attendee)
    db.commit()
    db.refresh(attendee)
    return attendee


@router.get("/by-event", response_model=List[AttendeeOut])
def list_attendees(event_id: int, db: Session = Depends(get_db)):
    return db.query(Attendee).where(Attendee.event_id == event_id).all()


@router.put("/{attendee_id}", response_model=AttendeeOut, dependencies=[Depends(require_role(["organizer", "staff"]))])
def update_attendee(attendee_id: int, payload: AttendeeCreate, db: Session = Depends(get_db)):
    attendee = db.query(Attendee).get(attendee_id)
    if not attendee:
        raise HTTPException(status_code=404, detail="Not found")
    for k, v in payload.dict().items():
        setattr(attendee, k, v)
    db.commit()
    db.refresh(attendee)
    return attendee

