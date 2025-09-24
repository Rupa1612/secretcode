# more_test_secrets.py
# A second script with a different set of fake secrets for testing.

# --- Fake Cloud Provider Keys ---

# AWS Credentials (often found in config files)
aws_config = {
    'aws_access_key_id': 'U2FsdGVkX18KxhqtFi7tVNX58ohJi5cjq0a+sf/z/hhvf+uh6ji2DPkFQGTa58i/',
    'aws_secret_access_key': 'U2FsdGVkX1+69QTPBaGnfoSEWaH9ooXDEVxGfYuOrKx2coBAMl6zBn9/d1vp7s9b4InRDuz2bSMJF8qbrze/Og==',
    'region': 'us-east-1'
}

# Google Cloud (service account JSON key placeholder)
gcp_service_account_key_json = """
{
  "type": "service_account",
  "project_id": "fake-project-12345",
  "private_key_id": "U2FsdGVkX19myScq4rIuVHp/7AHIBZiRXIyujScW8rEet2AhQQfJLzdK89fT8CyiBAqyM9zI4wdsj7irlGO2AA==",
  "private_key": "U2FsdGVkX19Xafs/8NyrJbHvp6MmsPOUB7kxrSkUB3y53EedhvICOMtAP74RJnQyeoQUsEisjtr6CuFh83dOMi5opLwo4UYsWVhNO1WK8jD9Ke175M02LFNvVOjtR/7+Mww1TGmLFaucR7n5V9yeRFCcypa8VUhJsE5jXK2JN64=",
  "client_email": "fake-service-account@fake-project-12345.iam.gserviceaccount.com",
  "client_id": "123456789012345678901",
  "auth_uri": "U2FsdGVkX19l0qhlsMsUgEEL5Rfp/ETixJJCljdM8H2NocSSOTgPgy8J8N0sHKQv6zeYLzSVQHe8HHRtpr/U5g==",
  "token_uri": "U2FsdGVkX1/3o/ySsN0M9KkrzcYyfYZ3/xVzpPxK8R2I5N0pnZW8655BXJArq76OAL3kAF7Pn7DCmN8av02MQg=="
}
"""

# --- Fake Social Media & Communication API Keys ---

# Twitter/X API v2 Bearer Token
twitter_bearer_token = "U2FsdGVkX19APKQJmypjUaQfaqQ0WIrPcnncCDJNJ5vBaXDxrys571kdEy27ZQgUaT/7m6/gFuPWgmeYfZkhP8QNNIjqKqPMkfN15l82u4vdytpJ/IWcjQiBFrc/PYugKAYXLzmUwUOOU1hB5in/Jt6UVbwTOdJM7zwr7s1q5cY="

# Slack Bot Token
slack_bot_token = "U2FsdGVkX1+ThcdPMcfDENXniqnDCUBWHv59W4qFUSj0Ne2eM/33PlnCu1I9v2VPNk4SAqcOujuUhsh8os8e70F+2BYDVF11Nxei8Evdjrk="

# Twilio Credentials
twilio_account_sid = "ACa1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"
twilio_auth_token = "U2FsdGVkX19KEgk00PQev+jDxtxfQ/pVqTdR8s+WJ+rynFAK2GxKSP5GEAG6FnkWvxT4tWymIn4dLmMj90o10g=="


# --- Fake Database and Other Credentials ---

# Redis Password
redis_password = "U2FsdGVkX18tvDGcTYe0/ZZ2ZYgO+COjwycq0aczEn2I7Tu73HLM9Qs79ld9bok2"

# Generic JWT Token
jwt_token = "U2FsdGVkX1+q6lOAkJy0DamIXsKtcVA6rD5shPF/KwwsLJOS1m68srjxFtE47cWEWk1whcrfJoVPoPgVXBsc5AjyQl6lsDIxDYSCbCFlWkd6v+012aFc5deV6/e3rjXEeNUB4hcpQeX/rmomuUfVtAJF1/ZzXlD7PgKRr/Z2svacVF4jLABrHxovy7WjthYI+PZKpY6S2Z7wkTzQbR2A0XBnEaF/cU2sZa+AOM//2qY="


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
