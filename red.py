# more_test_secrets.py
# A second script with a different set of fake secrets for testing.

# --- Fake Cloud Provider Keys ---

# AWS Credentials (often found in config files)
aws_config = {
    'aws_access_key_id': 'U2FsdGVkX197rSZnB0fUB1VyvgCwvSLaJYvD68rW5cI5tJ7ztlc5675ajlOxSk/A',
    'aws_secret_access_key': 'U2FsdGVkX1/zOkFyXvSc3K27DzKGq+DiY7FBtFg3RGuX6fZ9yqztPKNZFlUR1J/FJQo8Tx3zNjCtAb5q5q2ueA==',
    'region': 'us-east-1'
}

# Google Cloud (service account JSON key placeholder)
gcp_service_account_key_json = """
{
  "type": "service_account",
  "project_id": "fake-project-12345",
  "private_key_id": "U2FsdGVkX1812z3UVPo13DzAo4CfBcPAq/pYXJmKNOnUZSOjnGVE3/ZU4IVvXyKkdrxPJZS20bWokApQHyiReA==",
  "private_key": "U2FsdGVkX18AUlfQdt/b7NXHd7kvEJ5G5mpN//QN26LhPRtUTU8Jm9mLNHduWneQAlMjV+OK44ErN6uJAo1F42+HzE3lK6AHYzPZKv/KeN07Pt34/9fJ6aW+Q56su11lHeQdIatPRDwTwz8iazEaC6CKu2R2eL2bdLKSavtNl5c=",
  "client_email": "fake-service-account@fake-project-12345.iam.gserviceaccount.com",
  "client_id": "123456789012345678901",
  "auth_uri": "U2FsdGVkX19JtH5rguD3qFH3iezAvYLCMvzqNsPaQLZus2U5lVOiVOOZmd2mgyzdwSoeH3iT4s4ioeUVsMM1xQ==",
  "token_uri": "U2FsdGVkX18AXmsYSdkcISBXmBRh9ENdloxnEPyBEE6BHPoiHwhNbCV9fMAg1SedqtIYfr9uoj0RkgDElrHbWQ=="
}
"""

# --- Fake Social Media & Communication API Keys ---

# Twitter/X API v2 Bearer Token
twitter_bearer_token = "U2FsdGVkX1+uhDDa/ird71sLk4ZqeeeKRKNJvAH3iU5X3rsGB8N5Ftgj7f0wjHFb99DKrBHX7He9GTENR5rWlWo+AGAuT9qM/7xisq8Lf2lbFxXGbhHaLel9bRaFbD7vGdT24mYNGgn7P8cG7IhtG/luOjugts1Pdi5iprhVPB4="

# Slack Bot Token
slack_bot_token = "U2FsdGVkX18s3mIN5ANImVuAajkjGGBDUJJgM51ne5vWzuSRQJf7nJ4c4ir3AmylblCvYORCYlws4BhILRqAjsyXM6z8QdCA7nZcVv1I/q8="

# Twilio Credentials
twilio_account_sid = "ACa1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"
twilio_auth_token = "U2FsdGVkX18kl1TdJRWG4BP3ZnZfaO4BVqRx0az4q2Cjd6OxJgw+xPCRAdArD02wHlkFLR56GP5a90Of2kl1hw=="


# --- Fake Database and Other Credentials ---

# Redis Password
redis_password = "U2FsdGVkX194S2CD7JE8yQs/LrZYmv1ajGoy6ShvgdLFHlDRAN2TTOC5HIthEu08"

# Generic JWT Token
jwt_token = "U2FsdGVkX1+Hbt7dFJ40FqYzfa9o5hEwyHuFuBaFjFth614Cgo9Lc/yEk5Q39gbB96v9w+8GpVRDFGWULB04M2zBNupV5Nb6u6esL6PbNFJOEaWKpnwreZezGZjeQZ+XlAm4F4J1+I4h6QPa1bdzP+rkORMQhX33JNLFVP+zX+yiMrqh8yrsBomugi/sQsthrQJ17c4v+FVk5pPi4hpK58eDGbw6ITrFXuwZv3Ob8uU="


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
