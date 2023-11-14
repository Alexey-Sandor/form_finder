from main import db


form_data = [
    {
        "name": "TeamLead Data Form",
        "lead_name": "text",
        "lead_phone_number": "phone",
        "lead_email": "email",
        "lead_date_birthday": "date"
    },
    {
        "name": "Client Information Form",
        "client_name": "text",
        "client_phone_number": "phone",
    },
    {
        "name": "Survey Form",
        "survey_question_1": "text",
        "survey_question_2": "text",
    },
    {
        "name": "Order Form",
        "order_price": "text",
        "order_date": "date"
    },
    {
        "name": "Feedback Form",
        "feedback_author_name": "text",
        "feedback_email": "email",
    },
    {
        "name": "Simple Form",
        "field_1": "text",
        "field_2": "email"
    },
    {
        "name": "Registration Form",
        "username": "text",
        "email": "email",
        "password": "text"
    },
    {
        "name": "Product Info Form",
        "product_name": "text",
        "product_description": "text",
        "product_price": "text"
    },
    {
        "name": "Event Registration Form",
        "event_name": "text",
        "event_date": "date",
        "event_location": "text"
    },
    {
        "name": "Feedback Form",
        "feedback_author": "text",
        "feedback_email": "email",
        "feedback_message": "text"
    },
    {
        "name": "Survey Form",
        "question_1": "text",
        "question_2": "text",
        "question_3": "text"
    },
    {
        "name": "Large Survey Form",
        "question_1": "text",
        "question_2": "text",
        "question_3": "text",
        "question_4": "text",
        "question_5": "text",
        "question_6": "text",
    },
    {
        "name": "Order Form",
        "product_name": "text",
        "quantity": "text",
        "shipping_address": "text",
        "payment_method": "text"
    },
    {
        "name": "Employee Info Form",
        "employee_name": "text",
        "employee_id": "text",
        "department": "text"
    },
    {
        "name": "Newsletter Subscription Form",
        "subscriber_name": "text",
        "subscriber_email": "email"
    },
    {
        "name": "Appointment Booking Form",
        "client_name": "text",
        "appointment_date": "date",
        "appointment_time": "text"
    }
]

for form in form_data:
    db.insert(form)

print("Формы успешно добавлены в базу данных.")
