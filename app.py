# test_secrets.py
# A script with various fake secrets to test the CodeShield scanner.

import os

# --- Fake API Keys ---

# Quoted API Keys
stripe_api_key = "U2FsdGVkX1/MX3NEJ1iOxgtqm4BIFa/6B98Cbw+0kM9Ni8nvb1QnjyGiNVt3OY6kTe8uFn8Td0eU08ucD7gotQ=="
google_maps_api_key = "U2FsdGVkX1/a56Z4AlcPwNzTMEEYb1U92iFSwzsXJad1hgsAk4wwHYV308NSDk9HLzMOt+nuEopPUrHxyFC9fA=="
sendgrid_api_key = "U2FsdGVkX18qx3iDqwboiOTlLjwxABtc9UA1SUs72D/xYHQb0bEQnmyo38mnEgiPFRTS3zGC9QBWJidNWUWbscuKtn7zCDYV7OBpIkSWno9+b1x8Z+Fw2tszeixmAPPD"

# Unquoted API Key (common in .env files, but shown here for testing)
# Note: This is not valid Python syntax but is included to test raw text scanning.
# To make this file runnable, you would need to wrap the key in quotes.
# raw_aws_access_key_id = "U2FsdGVkX18vVlnfJ5pje6WaHZtvjWo58SodZ216Y9G5hk2WZ1h0URW8P0b71E30"

class Config:
    # Secrets within a class structure
    SECRET_KEY = "U2FsdGVkX19fUD3yQ/YWWosls63TjFPnfVeXpBSTwndBOhBrp7yyW7nPCL1GjDugWVPwqV1xHFxc9FY5adxvng=="
    GITHUB_TOKEN = "U2FsdGVkX19lBjX2WKC8v9Wf87XuL74gkXadqmhmpU/FupmaeGyDNJgtNkVWdPWycIb0JSjsa5NOOrUsJ2BsGQ=="

# --- Fake Passwords and Credentials ---

# Simple password
database_password = "U2FsdGVkX1/PzvHVYhgZBaSw6b2LIVPxloMYyF8RF5TBunCkBe8FwtWqVl2Y19lC"

# Database connection string with credentials
db_connection_string = "postgresql://user:U2FsdGVkX18KX8DBcKO98EL7Y++HIjEUhsJWjbe+55A=@localhost:5432/mydatabase"
mongo_db_uri = "mongodb+srv://testuser:U2FsdGVkX18mII/Q/FjC1yuSmSwue650d2fGaRUxAYs=@cluster0.abcde.mongodb.net/myFirstDatabase"


# --- Fake Personal Information ---

# User contact details
user_email = "test.user@example.com"
contact_phone = "U2FsdGVkX198G05IhmpZppuYyRPMIaJoMuYCPuF+68fppCfmM/pk47RIw/5F9N5o"
mobile_number = "U2FsdGVkX1/POvkeOVwRpe4DixLVIkLLaxGFJCng1HU="

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
