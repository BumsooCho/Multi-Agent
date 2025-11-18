from account.infrastructure.service.account_use_service import AccountUseService

class AccountUseCase:
  def __init__(self, service: AccountUseService):
    self.service = service
  
  def create_or_get_account(self, email, name):
    return self.service.create_or_get_account(self, email, name)