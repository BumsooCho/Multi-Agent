from pydantic import BaseModel

class AccountResponse(BaseModel):
  email: str
  name: str