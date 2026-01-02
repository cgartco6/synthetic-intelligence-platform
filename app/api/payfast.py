from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/payfast/itn")
async def payfast_itn(request: Request):
    data = await request.form()
    email = data.get("email_address")
    amount = data.get("amount_gross")

    # TODO: verify signature with PayFast docs
    # Upgrade user plan here

    return "OK"
