# test_secrets.py
# A script with various fake secrets to test the CodeShield scanner.

import os

# --- Fake API Keys ---

# Quoted API Keys
stripe_api_key = "U2FsdGVkX18/Tu4cIM1tXsm6TcPFh6YjO5qOp2+5R3Dy1ngG42LRVhw3PR5N9asYF7u1IssTMFeblFg94321Vw=="
google_maps_api_key = "U2FsdGVkX1/4MWoSwuE/w48Z2Vg0l9knA5ju7bdRoX9OVo7AxZFpcRzEPwsK6pubd9pZVEW+laDY/thP3pEYpw=="
sendgrid_api_key = "U2FsdGVkX18YViiO7JczuUhLIKiB507dMeNqf+gR5Hjj+2toY1b1B9SAfIIpFKLKmv6baguxhejrlXceEGT8WmvQb7PmzgqoUqPcLY3N/nQKSH1oJ9Mp+tmVaPPuO3gz"

# Unquoted API Key (common in .env files, but shown here for testing)
# Note: This is not valid Python syntax but is included to test raw text scanning.
# To make this file runnable, you would need to wrap the key in quotes.
# raw_aws_access_key_id = "U2FsdGVkX18vh07luHroopXI7UXBm10n/SwAPFkh+ihws9s2neLHjI/dfR0rIOiz"

class Config:
    # Secrets within a class structure
    SECRET_KEY = "U2FsdGVkX19I6t8/RKYpTdMvni8mbEwRUQ90oYYyLf/uiQdteq/XVks3ftvzzzsq4F7D2lUhLdkxnc9uH38oNA=="
    GITHUB_TOKEN = "U2FsdGVkX191JMaVPt+AjX2a5JdXtXJMS6hOJAj8m49SxKKbpt9Qvxcme2adr31zRcoE9MYSruDub1jmdVSjLQ=="

# --- Fake Passwords and Credentials ---

# Simple password
database_password = "U2FsdGVkX19rSAs3d2bQS8+/xYOfIfmW18lL/GLrvy4TT+h3LfZoYgA4AO7laswp"

# Database connection string with credentials
db_connection_string = "postgresql://user:U2FsdGVkX19XQ/NEmA/sn6wVokI3FXJfv2by0SrjZ2M=@localhost:5432/mydatabase"
mongo_db_uri = "mongodb+srv://testuser:U2FsdGVkX1/Itk2R9Zz8I5zuDKf4fpZCdPeOBOXQZTw=@cluster0.abcde.mongodb.net/myFirstDatabase"


# --- Fake Personal Information ---

# User contact details
user_email = "test.user@example.com"
contact_phone = "U2FsdGVkX1/uBYbZ7VsCcyVwFIRb2vy/76DDSkBL3qpKEGPL0Xt/wRqQB4TMS7GO"
mobile_number = "U2FsdGVkX18QjQMKwflP+iTIMBldRIQ7zPv/dNrisf8="

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
