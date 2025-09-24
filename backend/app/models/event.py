from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime, Boolean, Text
from datetime import datetime
from ..database import Base


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    venue: Mapped[str | None] = mapped_column(String(255), nullable=True)
    timezone: Mapped[str | None] = mapped_column(String(64), nullable=True)
    type: Mapped[str | None] = mapped_column(String(64), nullable=True)
    capacity: Mapped[int | None] = mapped_column(Integer, nullable=True)
    is_online: Mapped[bool] = mapped_column(Boolean, default=False)
    start_datetime: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    end_datetime: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)

