import requests


url = "http://localhost:8000/get_form"


data = [
    {
        "lead_name": "text",
        "lead_phone_number": "phone",
        "lead_email": "email",
        "lead_date_birthday": "date"
    },
    {
        "feedback_author": "John Doe",
        "feedback_email": "john.doe@example.com"
    },
    {
        "question_1": "How satisfied are you?",
        "question_2": "Would you recommend us?",
        "question_3": "How old are you?"
    },
    {
        "question_1": "How satisfied are you?",
        "question_2": "Would you recommend us?",
        "question_3": "How old are you?",
        "question_4": "Where are you from?",
        "question_5": "What is your name?",
        "question_6": "Are you ok?",
    },
    {
        "product_name": "Product ABC",
        "quantity": "2",
        "shipping_address": "123 Main St, City"
    },
    {
        "employee_name": "Alice Smith",
        "employee_id": "12345",
        "department": "Human Resources"
    },
    {
        "subscriber_name": "Bob Johnson",
        "subscriber_email": "bob.johnson@example.com"
    },
    {
        "client_name": "Charlie Brown",
        "appointment_time": "3:00 PM"
    },
    {
        "client_name": "Charlie Brown",
        "appointment_time": "31.01.2001"
    },
    {
        "client_name": "Ivan",
        "appointment_date": "2001-04-23",
        "appointment_time": "6 PM"
    }
]

for form_data in data:
    response = requests.post(url, json=form_data)

    print(f"Response for form data: {form_data}")
    print("Status Code:", response.status_code)
    print("Response Content:")
    print(response.text)
    print("-" * 30)
