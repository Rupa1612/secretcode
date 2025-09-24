# test_secrets.py
# A script with various fake secrets to test the CodeShield scanner.

import os

# --- Fake API Keys ---

# Quoted API Keys
stripe_api_key = "U2FsdGVkX18O7qBtFwm4UOW7YoMvcI6We74YyTGPapOy7liwzmbeTxVaVH/QOPXjr81oXtGAsyTPAmUIFSlltw=="
google_maps_api_key = "U2FsdGVkX1+Fja+9giYXaZDUQE0cBbARyT+s3+G/CFTWpfdOGBE5nseVHu15fJjkny8/v7UEy3FAhLn1AfIwTg=="
sendgrid_api_key = "U2FsdGVkX18hLVRydKpowB2xoAXxWJEtqUUsbnlwP2JvE74qXH5oISb9V2GwnLbiC8wI5fdDhU4b+pn9KFACn8x7AI6HMnhAT2WhZiPCIh8sGA0YhZg+P46FJV8D40ir"

# Unquoted API Key (common in .env files, but shown here for testing)
# Note: This is not valid Python syntax but is included to test raw text scanning.
# To make this file runnable, you would need to wrap the key in quotes.
# raw_aws_access_key_id = "U2FsdGVkX1/8DRPi5nbEwAIQ6cdO2HODZjt1+6V1fEqDyhhY2JQVuZZEEWOLZf2C"

class Config:
    # Secrets within a class structure
    SECRET_KEY = "U2FsdGVkX192gUKzh28wK0s4sXzCP3cLvMBVGHEmt4UZ6D0PDihnq8wrn9FyjiW+q9phnMbC2n2KWJs8hAT8pw=="
    GITHUB_TOKEN = "U2FsdGVkX1+SLFjj+687bOMXoGSBObMD4Qu+JDe7KSfZPLP7bvMNOcUA/f3X9blwTuKSmsIfoK7gfH2DhrFRlg=="

# --- Fake Passwords and Credentials ---

# Simple password
database_password = "U2FsdGVkX1/YM55X3TOCTTfRoL6mV4cGspjSjtbZTbImrjsRethy/TIv1DV8N5nq"

# Database connection string with credentials
db_connection_string = "postgresql://user:U2FsdGVkX18LLLEhrRhMj75KLRbAArtnL8BVhY1xxNI=@localhost:5432/mydatabase"
mongo_db_uri = "mongodb+srv://testuser:U2FsdGVkX19wfKzNfZITNFhYZVk3mZYOZchikD3n438=@cluster0.abcde.mongodb.net/myFirstDatabase"


# --- Fake Personal Information ---

# User contact details
user_email = "test.user@example.com"
contact_phone = "U2FsdGVkX19D+lyHfdBnFU0Ik1XCeYP/5AEc90R/Mf3OMaRUhEY9C1T0E0IYuq8o"
mobile_number = "U2FsdGVkX1/pKVnvRFE03w6brIBZvtmKg9XmqKSQEBs="

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
