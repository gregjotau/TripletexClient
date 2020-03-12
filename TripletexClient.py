import base64
import json

import requests


class TripletexClient:
    def __init__(self,
                 consumer_token=None,
                 employee_token=None,
                 expiration_date="2050-01-01",
                 session_token=None,
                 host="https://tripletex.no",
                 request_headers=None,
                 ):
        self.host = host
        if not consumer_token and not employee_token and not session_token and not request_headers:
            print("Missing needed credentials to communicate with Tripletex")
        if not session_token and consumer_token is not None:
            url = "{}/v2/token/session/:create".format(self.host)
            querystring = {
                "consumerToken": consumer_token,
                "employeeToken": employee_token,
                "expirationDate": expiration_date
            }

            response = requests.request("PUT", url, params=querystring)
            session_token = response.json()['value']['token']

        if session_token is not None:
            auth_payload = base64.b64encode(str.encode("0:{}".format(session_token))).decode('utf-8')
            self.headers_with_auth = {'Content-Type': 'application/json; charset=utf-8',
                                      'Authorization': 'Basic {}'.format(auth_payload)}

        if request_headers is not None:
            self.headers_with_auth = request_headers

    def make_order(self, payload):
        url = "{}/v2/order".format(self.host)
        payload = json.dumps(payload)
        response = requests.request("POST", url, data=payload, headers=self.headers_with_auth)
        order_id = response.json()['value']['id']
        return order_id

    def get_products(self):
        url = "{}/v2/product".format(self.host)
        response = requests.request("GET", url, headers=self.headers_with_auth)
        tripletex_products = response.json()['values']
        return tripletex_products

    def make_product(self, payload):
        url = "{}/v2/product".format(self.host)
        return requests.request("POST", url, data=json.dumps(payload), headers=self.headers_with_auth).json()

    def make_orderlines(self, payload):
        url = "{}/v2/order/orderline/list".format(self.host)
        requests.request("POST", url, data=json.dumps(payload), headers=self.headers_with_auth).json()

    def make_employee(self, payload):
        url = "{}/v2/employee".format(self.host)
        return requests.request("POST", url, data=json.dumps(payload), headers=self.headers_with_auth).json()

    def make_employment(self, payload):
        url = "{}/v2/employee/employment".format(self.host)
        return requests.request("POST", url, data=json.dumps(payload), headers=self.headers_with_auth).json()

    def make_employment_details(self, payload):
        url = "{}/v2/employee/employment/details".format(self.host)
        return requests.request("POST", url, data=json.dumps(payload), headers=self.headers_with_auth).json()

    def get_divisions(self):
        url = "{}/v2/division".format(self.host)
        return requests.request("GET", url, headers=self.headers_with_auth).json()

    def get_accounts(self):
        url = "{}/v2/ledger/account".format(self.host)
        return requests.request("GET", url, headers=self.headers_with_auth).json()

    def make_voucher(self,payload):
        url = "{}/v2/ledger/voucher".format(self.host)
        return requests.request("POST", url, data=json.dumps(payload), headers=self.headers_with_auth).json()
