# test_secrets.py
# A script with various fake secrets to test the CodeShield scanner.

import os

# --- Fake API Keys ---

# Quoted API Keys
stripe_api_key = "sk_live_abcdefghijklmnopqrstuvwxyz1234567890"
google_maps_api_key = "AIzaSyABCDEFGHIJKLmnopqrstuvwxyz123456"
sendgrid_api_key = "SG.abcdefghijklmnopqrstuvwxyz.1234567890abcdefghijklmnopqrstuvwxyz"

# Unquoted API Key (common in .env files, but shown here for testing)
# Note: This is not valid Python syntax but is included to test raw text scanning.
# To make this file runnable, you would need to wrap the key in quotes.
# raw_aws_access_key_id = AKIAIOSFODNN7EXAMPLE

class Config:
    # Secrets within a class structure
    SECRET_KEY = "pkey_thisIsAFakeSuperSecretKeyForTesting123!"
    GITHUB_TOKEN = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890"

# --- Fake Passwords and Credentials ---

# Simple password
database_password = "mySuperSecurePassword123"

# Database connection string with credentials
db_connection_string = "postgresql://user:password123@localhost:5432/mydatabase"
mongo_db_uri = "mongodb+srv://testuser:mongodbpassword@cluster0.abcde.mongodb.net/myFirstDatabase"


# --- Fake Personal Information ---

# User contact details
user_email = "test.user@example.com"
contact_phone = "+1 (555) 123-4567"
mobile_number = "9876543210"

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
