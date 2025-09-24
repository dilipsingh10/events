from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .database import init_db


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(o) for o in settings.cors_allowed_origins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    from .routers import auth, events, sessions, attendees, tickets, payments, checkin

    app.include_router(auth.router, prefix="/api/auth", tags=["auth"]) 
    app.include_router(events.router, prefix="/api/events", tags=["events"]) 
    app.include_router(sessions.router, prefix="/api/sessions", tags=["sessions"]) 
    app.include_router(attendees.router, prefix="/api/attendees", tags=["attendees"]) 
    app.include_router(tickets.router, prefix="/api/tickets", tags=["tickets"]) 
    app.include_router(payments.router, prefix="/api/payments", tags=["payments"]) 
    app.include_router(checkin.router, prefix="/api/checkin", tags=["checkin"]) 

    @app.on_event("startup")
    def on_startup() -> None:
        init_db()

    @app.get("/api/health")
    def health() -> dict:
        return {"status": "ok"}

    return app


app = create_app()

