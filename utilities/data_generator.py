import time
import random
import string

def generate_unique_email():
    timestamp = int(time.time())
    random_str = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f"testuser{timestamp}{random_str}@example.com"

def get_password():
    return "TestPassword@1234"