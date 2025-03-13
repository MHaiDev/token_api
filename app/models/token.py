from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Token(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    symbol = Column(String, unique=True, nullable=False)
    launch_date = Column(DateTime, default=datetime.utcnow, nullable=True)  # Fixed issue

    def __repr__(self):
        return f"<Token(id={self.id}, name={self.name}, symbol={self.symbol}, launch_date={self.launch_date})>"
