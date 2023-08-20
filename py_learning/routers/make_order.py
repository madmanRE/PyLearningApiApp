from fastapi import HTTPException, Form
import stripe
from config import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY


def create_payment(amount: int):
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd'
        )
        return {"client_secret": payment_intent.client_secret}
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=500, detail=str(e))
