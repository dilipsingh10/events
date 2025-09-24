from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey, Numeric, DateTime
from datetime import datetime
from ..database import Base


class TicketType(Base):
    __tablename__ = "ticket_types"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id", ondelete="CASCADE"), index=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str | None] = mapped_column(String(255))
    price: Mapped[float] = mapped_column(Numeric(10, 2), default=0)
    currency: Mapped[str] = mapped_column(String(8), default="USD")
    capacity: Mapped[int | None] = mapped_column(Integer)
    sales_start: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    sales_end: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))


class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id", ondelete="CASCADE"), index=True)
    ticket_type_id: Mapped[int] = mapped_column(ForeignKey("ticket_types.id", ondelete="RESTRICT"), index=True)
    purchaser_email: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(32), default="reserved")
    price_paid: Mapped[float] = mapped_column(Numeric(10, 2), default=0)
    currency: Mapped[str] = mapped_column(String(8), default="USD")
    issued_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

