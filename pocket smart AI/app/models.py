from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(120)
    )

    category: Mapped[str] = mapped_column(
        String(60),
        index=True
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2)
    )

    expense_date: Mapped[date] = mapped_column(
        Date,
        index=True
    )

    note: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )


class Budget(Base):
    __tablename__ = "budgets"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    category: Mapped[str] = mapped_column(
        String(60),
        unique=True,
        index=True
    )

    monthly_limit: Mapped[Decimal] = mapped_column(
        Numeric(12, 2)
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )