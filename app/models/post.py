from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so
from typing import Optional
from datetime import datetime, timedelta
import app.models as models

class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key = True)
    user: so.Mapped[models.Usuario] = so.relationship(back_populates='posts')
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(models.Usuario.id), index=True)
    date: so.Mapped[datetime] = so.mapped_column(index=True, default=sa.func.now())
    title: so.Mapped[str] = so.mapped_column(sa.String(128), index=True, nullable=True, default="Post")
    body: so.Mapped[str] = so.mapped_column(sa.String(256))