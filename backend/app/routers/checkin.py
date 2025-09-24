from fastapi import APIRouter

router = APIRouter()


@router.post("/event")
def checkin_event(qr: str, event_id: int):
    # TODO: decode QR and record log
    return {"status": "ok", "scope": "event", "event_id": event_id}


@router.post("/session")
def checkin_session(qr: str, session_id: int):
    # TODO: decode QR and record log
    return {"status": "ok", "scope": "session", "session_id": session_id}

