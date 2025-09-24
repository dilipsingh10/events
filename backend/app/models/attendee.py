from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey, Boolean
from ..database import Base


class Attendee(Base):
    __tablename__ = "attendees"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id", ondelete="CASCADE"), index=True)
    ticket_id: Mapped[int | None] = mapped_column(ForeignKey("tickets.id", ondelete="SET NULL"), index=True)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), index=True)
    phone: Mapped[str | None] = mapped_column(String(32))
    company: Mapped[str | None] = mapped_column(String(255))
    designation: Mapped[str | None] = mapped_column(String(255))
    category: Mapped[str] = mapped_column(String(32), default="General")
    checked_in: Mapped[bool] = mapped_column(Boolean, default=False)

