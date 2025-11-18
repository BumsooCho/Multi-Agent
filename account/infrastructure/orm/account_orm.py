from sqlalchemy import Column, String

from config.database.session import Base

class AccountORM(Base):
  __tablename__ = "account"
  
  email = Column(String(255), primary_key=True, index=True)
  name = Column(String(100), nullable=False)
    
    
  