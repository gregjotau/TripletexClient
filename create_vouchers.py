from pprint import pprint

from TripletexClient import TripletexClient

client = TripletexClient(host="https://api.tripletex.io", session_token="8b5fa3f3-b06e-45e9-bda6-bc6ed9f030b8")

accounts = client.get_accounts()

pprint(accounts)

voucher_response = client.make_voucher({"date": "2020-03-01", "description": "test voucher", "postings": [
    {"date": "2020-03-01", "description": "test 2", "account": {"id": 30999708}, "row": 1, "amount": 12,
     "amountCurrency": 12, "amountGross": 12, "amountGrossCurrency": 12},
    {"date": "2020-03-01", "description": "test 2", "account": {"id": 30999708}, "row": 1,
     "amount": -12, "amountCurrency": -12, "amountGross": -12, "amountGrossCurrency": -12}]})

pprint(voucher_response)
