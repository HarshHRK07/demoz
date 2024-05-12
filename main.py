from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/stripeinbuilt', methods=['GET'])
def stripe_integration():
    # Extracting parameters from the request URL
    card_info = request.args.get('cc').split('|')
    card_number = card_info[0]
    exp_month = card_info[1]
    exp_year = card_info[2]
    client_secret = request.args.get('client_secret')
    publishable_key = request.args.get('pk')

    # Extracting payment intent ID from client secret
    payment_intent_id = client_secret.split("_secret_")[0]

    # API endpoint to create a payment method
    create_payment_method_url = "https://api.stripe.com/v1/payment_methods"

    # Payload data to create a payment method
    create_payment_method_payload = {
        "type": "card",
        "card[number]": card_number,
        "card[exp_month]": exp_month,
        "card[exp_year]": exp_year
    }

    # Request headers to create a payment method
    create_payment_method_headers = {
        'Authorization': f'Bearer {publishable_key}',
        'Content-Type': "application/x-www-form-urlencoded",
    }

    # Send the request to create a payment method
    response = requests.post(create_payment_method_url, data=create_payment_method_payload, headers=create_payment_method_headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract payment method ID from the response
        payment_method_id = response.json()["id"]
        
        # API endpoint to confirm payment intent
        confirm_payment_intent_url = f"https://api.stripe.com/v1/payment_intents/{payment_intent_id}/confirm"

        # Payload data to confirm payment intent
        confirm_payment_intent_payload = {
            "payment_method": payment_method_id,
            "client_secret": client_secret
        }

        # Headers to confirm payment intent
        confirm_payment_intent_headers = {
            'Authorization': f'Bearer {publishable_key}',
            'Content-Type': "application/x-www-form-urlencoded",
        }

        # Send the request to confirm payment intent
        confirm_response = requests.post(confirm_payment_intent_url, data=confirm_payment_intent_payload, headers=confirm_payment_intent_headers)

        # Return the raw response
        return confirm_response.text

    else:
        # Return error message
        return response.text

@app.route('/cvv', methods=['GET'])
def handle_cvv():
    # Extracting parameters from the request URL
    card_info = request.args.get('cc').split('|')
    card_number = card_info[0]
    exp_month = card_info[1]
    exp_year = card_info[2]
    cvc = card_info[3]
    client_secret = request.args.get('client_secret')
    publishable_key = request.args.get('pk')

    # Extracting payment intent ID from client secret
    payment_intent_id = client_secret.split("_secret_")[0]

    # API endpoint to create a payment method
    create_payment_method_url = "https://api.stripe.com/v1/payment_methods"

    # Payload data to create a payment method
    create_payment_method_payload = {
        "type": "card",
        "card[number]": card_number,
        "card[exp_month]": exp_month,
        "card[exp_year]": exp_year,
        "card[cvc]": cvc
    }

    # Request headers to create a payment method
    create_payment_method_headers = {
        'Authorization': f'Bearer {publishable_key}',
        'Content-Type': "application/x-www-form-urlencoded",
    }

    # Send the request to create a payment method
    response = requests.post(create_payment_method_url, data=create_payment_method_payload, headers=create_payment_method_headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract payment method ID from the response
        payment_method_id = response.json()["id"]
        
        # API endpoint to confirm payment intent
        confirm_payment_intent_url = f"https://api.stripe.com/v1/payment_intents/{payment_intent_id}/confirm"

        # Payload data to confirm payment intent
        confirm_payment_intent_payload = {
            "payment_method": payment_method_id,
            "client_secret": client_secret
        }

        # Headers to confirm payment intent
        confirm_payment_intent_headers = {
            'Authorization': f'Bearer {publishable_key}',
            'Content-Type': "application/x-www-form-urlencoded",
        }

        # Send the request to confirm payment intent
        confirm_response = requests.post(confirm_payment_intent_url, data=confirm_payment_intent_payload, headers=confirm_payment_intent_headers)

        # Return the raw response
        return confirm_response.text

    else:
        # Return error message
        return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    
