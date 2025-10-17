api_response = {
    "status": "success",
    "data": {"user_id": 101, "user_name": "John Doe", "logged_in": False}
}
print(api_response["data"]["user_name"])  # Output: John Doe
