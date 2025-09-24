from fastapi import APIRouter

router = APIRouter()


@router.post("/intent")
def create_payment_intent(amount: float, currency: str = "USD"):
    # Placeholder: integrate Stripe/Razorpay later. Return dummy client secret.
    return {"provider": "dummy", "client_secret": "test_client_secret", "amount": amount, "currency": currency}

