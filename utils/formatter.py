# utils/formatter.py
"""
Handles:
1. pretty terminal output
"""

def print_records(endpoint, data, limit):
    if not data:
        print("No data to display")
        return
    for item in data[:limit]:
        if endpoint == "posts":
            print(f"ID: {item.get('id')}")
            print(f"User: {item.get('userId')}") 
            print(f"Title: {item.get('title')}")
        elif endpoint == "comments":
            print(f"ID: {item.get('id')}") 
            print(f"Email: {item.get('email')}") 
            print(f"Body: {item.get('body')}")
        elif endpoint == "users":
            print(f"ID: {item.get('id')}") 
            print(f"Name: {item.get('name')}") 
            print(f"Username: {item.get('username')}")
        # print("\nRECORDS")
        print("-" * 20)
def print_summary(summary):
    if not summary:
        print("No summary available")
        return
    print("\nSUMMARY")
    print("-" * 30)
    
    for key, value in summary.items():
        print(f"{key}: {value}")