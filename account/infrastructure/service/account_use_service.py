from account.domain.account import Account

class AccountUseService:
  def create_or_get_account(self, email, name) -> Account:
    self.email = email
    self.name = name
    
    return Account