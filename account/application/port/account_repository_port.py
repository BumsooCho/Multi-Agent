from abc import ABC, abstractmethod
from account.domain.account import Account

class AccountRepositoryPort(ABC):
  
  @abstractmethod
  def create_or_get_account(self, email, name) -> Account:
    pass
  