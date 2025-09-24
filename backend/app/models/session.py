from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey, DateTime, Boolean, Text
from datetime import datetime
from ..database import Base


class Speaker(Base):
    __tablename__ = "speakers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id", ondelete="CASCADE"), index=True)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str | None] = mapped_column(String(255))
    bio: Mapped[str | None] = mapped_column(Text)
    company: Mapped[str | None] = mapped_column(String(255))
    title: Mapped[str | None] = mapped_column(String(255))


class Session(Base):
    __tablename__ = "sessions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id", ondelete="CASCADE"), index=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(Text)
    type: Mapped[str] = mapped_column(String(32), default="Breakout")
    location: Mapped[str | None] = mapped_column(String(255))
    start_datetime: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    end_datetime: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    capacity: Mapped[int | None] = mapped_column(Integer)
    requires_registration: Mapped[bool] = mapped_column(Boolean, default=False)
    access_level: Mapped[str] = mapped_column(String(32), default="All")


class SessionRegistration(Base):
    __tablename__ = "session_registrations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    session_id: Mapped[int] = mapped_column(ForeignKey("sessions.id", ondelete="CASCADE"), index=True)
    attendee_id: Mapped[int] = mapped_column(ForeignKey("attendees.id", ondelete="CASCADE"), index=True)
    status: Mapped[str] = mapped_column(String(32), default="registered")
    checked_in: Mapped[bool] = mapped_column(Boolean, default=False)

