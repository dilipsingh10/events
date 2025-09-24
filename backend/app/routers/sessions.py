from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models.session import Session as EventSession
from ..schemas import SessionCreate, SessionOut
from ..security import require_role


router = APIRouter()


@router.post("/", response_model=SessionOut, dependencies=[Depends(require_role(["organizer", "staff"]))])
def create_session(payload: SessionCreate, db: Session = Depends(get_db)):
    s = EventSession(**payload.dict())
    db.add(s)
    db.commit()
    db.refresh(s)
    return s


@router.get("/by-event", response_model=List[SessionOut])
def list_sessions(event_id: int, db: Session = Depends(get_db)):
    return db.query(EventSession).where(EventSession.event_id == event_id).all()


@router.put("/{session_id}", response_model=SessionOut, dependencies=[Depends(require_role(["organizer", "staff"]))])
def update_session(session_id: int, payload: SessionCreate, db: Session = Depends(get_db)):
    s = db.query(EventSession).get(session_id)
    if not s:
        raise HTTPException(status_code=404, detail="Not found")
    for k, v in payload.dict().items():
        setattr(s, k, v)
    db.commit()
    db.refresh(s)
    return s

