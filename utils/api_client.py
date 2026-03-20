# utils/api_client.py
"""
Handles:
1. building request
2. calling API
3. timeout / connection / request errors
4. response validation
"""
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_data(endpoint, params=None):
    """
    Responsibilities:
    1. build URL
    2. call requests.get(..., timeout=5)
    3. handle: timeout, connection error, generic request error, validate non-200 status, parse JSON
    
    Arguments:
    1. endpoint: str (e.g., "posts", "comments", "users")
    2. params = Query parameter
    Return: data or None
    """
    
    url = f"{BASE_URL}/{endpoint}"
    
    try:
        response = requests.get(url, params=params, timeout=5)
        if response.status_code != 200:
            if response.status_code == 404:
                print("Error: Invalid endpoint or resource not found")
            else:
                print(f"Error: Received status code {response.status_code}")
            return None
        data = response.json()
        if not isinstance(data, list):
            print("Error: Unexpected API response format")
            return None
        
        return data
    except ValueError:
        print("Error: Invalid JSON response")
        return None
    except requests.exceptions.Timeout:
        print("Error: Request timed out")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect to API")
        return None
    except requests.exceptions.RequestException:
        print("Error: Request failed")
        return None