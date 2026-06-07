import json
from ollama import chat

tickets=  [ 
    "users cannot login after new deployment.",
    "payment transactions are failing for all customers.",
    "application response time exeeds 10 seconds.",
    "monitoring alert  CPU usage above 95% for 30 minutes.",
    "new employee cannot access internal systems."
]

valid_priorities = ["low", "medium", "high", "critical"]

def validate_output(data):

    required_fields = [
        "category",
        "priority",
        "summary",
        "recommended_action"
    ]

    for field in required_fields:
        if field not in data:
            return False
    if  data ["priority"].lower() not in valid_priorities:
        return  False

    return True

def analyse_ticket(ticket):

    prompt = f"""

give ONLY valid JSON.
you are an IT analyst.
do not explain.
priorites must be one of : low, medium, high, critical.
do not add extra text.
do not use markdown.

JSON format:

{{
    "category":"",
    "priority":"",
    "summary":"",
    "recommended_action":""
}}

Ticket:
{ticket}
"""
    response = chat(
        model="llama3",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )
    return response["message"]["content"]


for ticket in tickets:

    print("\n"+ "-" *50)
    print("ticket:", ticket)
 
    try:
        result  = analyse_ticket(ticket)

        print("\nRAW OUTPUT:")
        print(result)

        data = json.loads(result)

        if validate_output(data):

            print("valid output")
            print(json.dumps(data, indent=4))

        else:
            print("validation failed")

    except json.JSONDecodeError:
        print("invalid JSON")
    except Exception as e:
        print("error:",e) 













