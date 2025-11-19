from pydantic import BaseModel

class AccountRequest(BaseModel):
  email: str
  name: str