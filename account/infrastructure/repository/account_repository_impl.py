
from account.application.port.account_repository_port import AccountRepositoryPort
from account.domain.account import Account
from account.infrastructure.orm.account_orm import AccountORM

from sqlalchemy.orm import Session
from config.database.session import get_db_session

class AccountRepositoryImpl(AccountRepositoryPort):
  
  __instance = None
  
  def __new__(cls, *args, **kwargs):
      if cls.__instance is None:
          cls.__instance = super().__new__(cls)
      return cls.__instance
  
  @classmethod
  def getInstance(cls):
      if cls.__instance is None:
          cls.__instance = cls()
      return cls.__instance
  
  def __init__(self):
      if not hasattr(self, 'db'):
          self.db: Session = get_db_session()
  
  def save(self, account: Account) -> Account:
    orm_account = AccountORM(
      email = account.email,
      name = account.name
    )
    self.db.add(orm_account)
    self.db.commit()
    self.db.refresh(orm_account)
    
    return account
    
            
  def create_or_get_account(self, account: Account) -> Account:
    orm_account = self.db.query(AccountORM).filter(AccountORM.email == email).first()
    if orm_account:
      account = Account(
        email = orm_account.email,
        name = orm_account.name,
      )
    else:
      self.save(account)
    return account
      