
from fastapi import APIRouter, HTTPException

from account.application.usecase.account_use_case import AccountUseCase
from account.adapter.input.web.request.account_request import AccountRequest
from account.adapter.input.web.response.account_response import AccountResponse

account_router = APIRouter()
usecase = AccountUseCase.getInstance()

@account_router.post("/create_or_get_account", response_model=AccountResponse)
def create_or_get_account(request: AccountRequest):
  account = usecase.create_or_get_account(request.email, request.name)
  return AccountResponse(
    email = account.email,
    name = account.name
  )