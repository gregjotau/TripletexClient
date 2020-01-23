import base64

import swagger_client
import json
# auth_payload = base64.b64encode(str.encode("0:{}".format(session_token))).decode('utf-8')
# headers_with_auth = {'Content-Type': 'application/json; charset=utf-8',
#                      'Authorization': 'Basic {}'.format(auth_payload)}
# client.default_headers = headers_with_auth

client = swagger_client.api_client.ApiClient()
session_token = ""
client.configuration.username = "0"
client.configuration.password = session_token
customerApi = swagger_client.CustomerApi(api_client=client)
curApi = swagger_client.CurrencyApi(api_client=client)
orderAPI = swagger_client.OrderApi(api_client=client)

orders = orderAPI.search("2019-01-01", "2019-06-06",_preload_content=False)
print(json.loads(orders.data))
# res2 = curApi.search()
# print(res2)
# res = customerApi.search(count=1)
#
# print(res)
