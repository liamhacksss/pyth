from flask import Flask, request
import paypalrestsdk

app = Flask(__name__)

paypalrestsdk.configure({
    "mode": 'live',  # 'sandbox' or 'live'
    "client_id": 'AZduRR0pGWaYTt3VhlVzsFtS-Y8MGjkZxOq4_v4roNvHv0BYQG2qHrysOeWjDykkaeiyLTBxGy1omhBg',
    "client_secret": 'ELt6QJAh3Cdmt-iAIyKI4AGxUPOo3VM8LQP8MYjP_41NrEfB1qAFOdV_7HHaRLEfibx3JCeL7taVFYmC'
})

@app.route('/payment/success')
def payment_success():
    payment_id = request.args.get('paymentId')
    payer_id = request.args.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        # Update your database or notify the bot about the successful payment
        return "Payment executed successfully."
    else:
        return "Payment failed."

@app.route('/payment/cancel')
def payment_cancel():
    return "Payment cancelled."

if __name__ == "__main__":
    app.run(debug=True)
