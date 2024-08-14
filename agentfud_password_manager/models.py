
import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Mapped, sessionmaker, mapped_column
from typing import Optional

db = sa.create_engine("sqlite:///passwords.sqlite")
Session = sessionmaker(bind=db)

class Base(DeclarativeBase):
    pass

class Config(Base):
    __tablename__ = 'config'

    id: Mapped[int] = mapped_column(primary_key=True)
    master_password_hash: Mapped[str]
    device_salt: Mapped[str]