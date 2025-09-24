from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models.event import Event
from ..schemas import EventCreate, EventOut
from ..security import require_role


router = APIRouter()


@router.get("/", response_model=List[EventOut])
def list_events(db: Session = Depends(get_db)):
    return db.query(Event).order_by(Event.start_datetime).all()


@router.post("/", response_model=EventOut, dependencies=[Depends(require_role(["organizer", "staff"]))])
def create_event(payload: EventCreate, db: Session = Depends(get_db)):
    event = Event(**payload.dict())
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


@router.get("/{event_id}", response_model=EventOut)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).get(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.put("/{event_id}", response_model=EventOut, dependencies=[Depends(require_role(["organizer", "staff"]))])
def update_event(event_id: int, payload: EventCreate, db: Session = Depends(get_db)):
    event = db.query(Event).get(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    for k, v in payload.dict().items():
        setattr(event, k, v)
    db.commit()
    db.refresh(event)
    return event


@router.delete("/{event_id}", dependencies=[Depends(require_role(["organizer"]))])
def delete_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).get(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(event)
    db.commit()
    return {"status": "deleted"}

