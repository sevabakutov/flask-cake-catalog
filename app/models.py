from datetime import datetime
from typing import List
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    BIGINT, Numeric, String, func,
    Boolean, ForeignKey, DateTime,
)
from sqlalchemy.orm import (
    DeclarativeBase, Mapped,
    mapped_column, relationship,
    registry
)

registry(type_annotation_map={
        int: BIGINT,
        str: String(100)
})

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class CakeBakery(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    bakery_id: Mapped[id] = mapped_column(ForeignKey("bakery.id", ondelete="CASCADE"))
    cake_id: Mapped[id] = mapped_column(ForeignKey("cake.id", ondelete="CASCADE"))

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), server_onupdate=func.now())

    def __repr__(self) -> str:
        return f"id: {self.id} cake_id: {self.cake_id} bakery_id: {self.bakery_id}"

class Cake(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    flavor: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    available: Mapped[bool] = mapped_column(Boolean, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), server_onupdate=func.now())

    bakeries: Mapped[List["Bakery"]] = relationship("Bakery", back_populates="cakes", secondary=CakeBakery.__table__)

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "flavor": self.flavor,
            "price": self.price,
            "available": self.available
        }

    def __repr__(self) -> str:
        return f"id: {self.id} name: {self.name} flavor: {self.flavor} price: {self.price} available: {self.available}"

class Bakery(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(Numeric(1, 2), default=0)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), server_onupdate=func.now())

    cakes: Mapped[List["Cake"]] = relationship("Cake", back_populates="bakeries", secondary=CakeBakery.__table__)

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "rating": self.rating
        }

    def __repr__(self) -> str:
        return f"id: {self.id} name: {self.name} location: {self.location} rating: {self.rating}"