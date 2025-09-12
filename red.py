# more_test_secrets.py
# A second script with a different set of fake secrets for testing.

# --- Fake Cloud Provider Keys ---

# AWS Credentials (often found in config files)
aws_config = {
    'aws_access_key_id': 'AKIAABCDEFGHIJKLMNOP',
    'aws_secret_access_key': 'aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890/aBcD',
    'region': 'us-east-1'
}

# Google Cloud (service account JSON key placeholder)
gcp_service_account_key_json = """
{
  "type": "service_account",
  "project_id": "fake-project-12345",
  "private_key_id": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2",
  "private_key": "-----BEGIN PRIVATE KEY-----\\nFAKEKEYDATAHEREFAKEKEYDATAHEREFAKEKEYDATAHERE\\n-----END PRIVATE KEY-----\\n",
  "client_email": "fake-service-account@fake-project-12345.iam.gserviceaccount.com",
  "client_id": "123456789012345678901",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token"
}
"""

# --- Fake Social Media & Communication API Keys ---

# Twitter/X API v2 Bearer Token
twitter_bearer_token = "AAAAAAAAAAAAAAAAAAAAALeftintentionallyBlankAAAAAAAAAAAAAAAAAAAAA%2FthisIsAFakeTokenForTestingPurposesOnly"

# Slack Bot Token
slack_bot_token = "xoxb-123456789012-1234567890123-aBcDeFgHiJkLmNoPqRsTuVwXy"

# Twilio Credentials
twilio_account_sid = "ACa1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"
twilio_auth_token = "0987654321fedcba0987654321fedcba"


# --- Fake Database and Other Credentials ---

# Redis Password
redis_password = "aVeryStrongRedisPassword!@#"

# Generic JWT Token
jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"


# --- Fake Cryptographic Keys ---

# A placeholder for a private SSH key
ssh_private_key_pem = """
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,FAKEDATAFAKEDATA

THISISAPLACERHOLDERFORANENCRYPTEDSSHPRIVATEKEYITCONTAINSNOREAL
KEYMATERIALANDISINTENDEDFORTESTINGSECRETSSCANNERSAFELYPLEASEDO
NOTUSETHISFORANYTHINGELSEITISSIMPLYMOCKDATAFORVISUALANDPATTERN
RECOGNITIONTESTINGPURPOSESONLYTHANKYOUVERYMUCHHAVEANICEDAYOKAY
-----END RSA PRIVATE KEY-----
"""

print("This file contains multiple types of fake secrets for testing.")
