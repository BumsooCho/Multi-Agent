
from account.application.port.account_repository_port import AccountRepositoryPort
from account.domain.account import Account
from account.infrastructure.orm.account_orm import AccountORM

from sqlalchemy.orm import Session
from config.database.session import get_db_session

class AccountRepositoryImpl(AccountRepositoryPort):
  def __init__(self):
    self.db: Session = get_db_session()
  
  def create_or_get_account(self, email, name) -> Account:
    orm_account = self.db.query(AccountORM).filter(AccountORM.email == email).first()
    if orm_account:
      account = Account(
        email = orm_account.email,
        name = orm_account.name,
      )
      return account
    return None
      