from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, ForeignKey
from datetime import datetime
from ..database import Base


class CheckinLog(Base):
    __tablename__ = "checkin_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id", ondelete="CASCADE"), index=True)
    scope: Mapped[str] = mapped_column(String(16))  # event/session
    scope_id: Mapped[int] = mapped_column(Integer, index=True)
    qr: Mapped[str] = mapped_column(String(255))
    result: Mapped[str] = mapped_column(String(16), default="success")
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

