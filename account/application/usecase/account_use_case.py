from account.infrastructure.repository.account_repository_impl import AccountRepositoryImpl
from account.infrastructure.service.account_use_service import AccountUseService
from account.domain.account import Account

class AccountUseCase:
  
  __instance = None
  
  def __new__(cls, *args, **kwargs):
    if cls.__instance is None:
      cls.__instance = super().__new__(cls)
      cls.__instance.account_repo = AccountRepositoryImpl.getInstance()
    return cls.__instance
  
  @classmethod
  def getInstance(cls):
    if cls.__instance is None:
      cls.__instance = cls()
    return cls.__instance
      
  def create_or_get_account(self, email, name):
    account = Account(email=email, name=name)
    return self.account_repo.create_or_get_account(account)