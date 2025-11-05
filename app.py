# test_secrets.py
# A script with various fake secrets to test the CodeShield scanner.

import os

# --- Fake API Keys ---

# Quoted API Keys
stripe_api_key = "U2FsdGVkX19o9Lbtz/qlGFauxdQQnK5yudnR9iIoO8f8QaCY4qSMtTJ+D4mNC6oGoM2VLH9nk5JG3DL7/KeLgQ=="
google_maps_api_key = "U2FsdGVkX18ks1Y0igRjC1/lMv6SdELNa+1dmV2GkV1EbSkQIqlsa5xvmmzSUf5UZoqDr0miL78UjuC5G6pxMQ=="
sendgrid_api_key = "U2FsdGVkX19JeaIVLhBH2XyVNYwllKLgH0pcNUtIw06TZHrcZhnSNbWLGUtlUvjikBkBwCOqFocSwDQZocuqXEokofpC1Q65ercZPofYpH6j5AcMEOVZKbm5LPWivDp1"

# Unquoted API Key (common in .env files, but shown here for testing)
# Note: This is not valid Python syntax but is included to test raw text scanning.
# To make this file runnable, you would need to wrap the key in quotes.
# raw_aws_access_key_id = "U2FsdGVkX188YSwPP0iTVRlYK1c/lsmWrFtBryjoYpheK8hOsdSZBYZJ+lvGK8X4"

class Config:
    # Secrets within a class structure
    SECRET_KEY = "U2FsdGVkX18kCwKSxL2x7aVa0TDeQfHYBwcTFdvjXOOWsJ5GoLDc/+HDZ60Qy8BiZ51WQJiXBmd0MuQaK94w3A=="
    GITHUB_TOKEN = "U2FsdGVkX1/i9zitOc42DySuPj1lPSmefppNaqGaV82/D1M6C0x7v99k7reWru6rZ2tbo9xrwQ62FsTiH7+tVQ=="

# --- Fake Passwords and Credentials ---

# Simple password
database_password = "U2FsdGVkX18jSPn9cVV81t5XLvh21B+DMI7Iu4vJPqfntzaBYkyfHASiQovprGMw"

# Database connection string with credentials
db_connection_string = "postgresql://user:U2FsdGVkX18mDHDZ63MK+UKpNdi1xXeYuqBXzmZDfoY=@localhost:5432/mydatabase"
mongo_db_uri = "mongodb+srv://testuser:U2FsdGVkX185HLr0yhHgDxYfU8E9HhykdjWCe3pl8rI=@cluster0.abcde.mongodb.net/myFirstDatabase"


# --- Fake Personal Information ---

# User contact details
user_email = "test.user@example.com"
contact_phone = "U2FsdGVkX1+i605jnvF/3e5VYz+8wzWoXnQz12i+O0vLLxAyY5v5pQ9I6rKrHdXZ"
mobile_number = "U2FsdGVkX18EHQP0f3Ugq4d99VMJRGBTtlM3Z5SFqLU="

def connect_to_services():
    """
    A fake function demonstrating the use of hardcoded secrets.
    """
    print("Connecting to Stripe with key:", stripe_api_key)
    print("Using Google Maps with key:", google_maps_api_key)
    print("Connecting to database with password:", database_password)
    print(f"User contact info: {user_email}, {contact_phone}")

if __name__ == "__main__":
    connect_to_services()
