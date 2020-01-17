from TripletexClient import TripletexClient

request_headers = {
    'accept': 'application/json; charset=utf-8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,nb;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'content-type': 'application/json; charset=utf-8',
    'Cookie': '_ga=GA1.1.200641385.1559029547; Idea-5993d98d=14c86e63-d61c-4835-94cc-fa8331de23ab; _gid=GA1.1.1465362649.1572417148; JSESSIONID=F89B680F815C5C768A498951BA6BAFB8',
    'Host': 'localhost:8080',
    'Pragma': 'no-cache',
    'Referer': 'http://localhost:8080/execute/employeeMenu?employeeId=2072948&contextId=486505',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'x-tlx-context-id': '486505',
    'x-tlx-csrf-token': '821e904a-6f9f-4495-93d5-77964871529a',
}

client = TripletexClient(host="http://localhost:8080", request_headers=request_headers)

for i in range(1, 100):
    employee_payload = {
        "firstName": "ansattViaApi-{}".format(i),
        "userType": "NO_ACCESS",
        "department": {"id": 101472},
        "lastName": "best",
        "dateOfBirth": "2001-01-01",
    }
    employee_response = client.make_employee(employee_payload)
    employee_id = employee_response['value']['id']

    divisions = client.get_divisions()
    divisionId = divisions['values'][0]['id']

    employment_payload = {
        "startDate": "2019-09-01",
        "division": {
            "id": divisionId
        },
        "employee": {
            "id": employee_id
        },

    }
    employment_response = client.make_employment(employment_payload)
    print(employment_response)

    employment_details_payload = {
        "annualSalary": 500000,
        "percentageOfFullTimeEquivalent": 100,
        "employment": {
            "id": employment_response['value']['id']
        }
    }
    employmentDetails = client.make_employment_details(employment_details_payload)
    print(employmentDetails)
