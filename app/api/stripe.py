def stripe_webhook(event):
    if event["type"] == "checkout.session.completed":
        user_email = event["data"]["object"]["customer_email"]
        plan = "builder"
        # upgrade user plan
