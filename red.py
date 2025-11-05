# more_test_secrets.py
# A second script with a different set of fake secrets for testing.

# --- Fake Cloud Provider Keys ---

# AWS Credentials (often found in config files)
aws_config = {
    'aws_access_key_id': 'U2FsdGVkX18I3cmajDaeqB/nCZ8M4cDz2m101PcoGfKVMMBQ2+y3Ru6o2wH210QI',
    'aws_secret_access_key': 'U2FsdGVkX18ihs5oxv1P18A05IN1AqVcHDFitwUuZPRswMJQH5fk9lYghAxQSv+c60lKtySDI9N2I/zd4m+y8g==',
    'region': 'us-east-1'
}

# Google Cloud (service account JSON key placeholder)
gcp_service_account_key_json = """
{
  "type": "service_account",
  "project_id": "fake-project-12345",
  "private_key_id": "U2FsdGVkX1//koq4AufC7O2kcjYUy9Fkm17uNkO38RRKr6Jbf1xdlnM9UWr+ga6157NSBQVCCHkP1xgASEIUxA==",
  "private_key": "U2FsdGVkX18wZKdYoXbCJ/Cod4WR8zEd/HW+0u32kf5g1EyLnUPa/5PW6vHBRqwKGf0PgjMyb9x1U1qmwwRceTU5OQmjNj0Ifr3MccYrj7s5Z3UWkOE59FS7hA4tEhWkXvCPk2rphPiVUrBVCxsssQbwj5DQkqiGIpSuKr4j6Ho=",
  "client_email": "fake-service-account@fake-project-12345.iam.gserviceaccount.com",
  "client_id": "123456789012345678901",
  "auth_uri": "U2FsdGVkX19/+agFXIUhXFoEDqsV94NPwEiTfauC0xDxqg+kMsaEN9KCK8zuEM0k2RLq/1j4VnMv3aEIweUKMg==",
  "token_uri": "U2FsdGVkX19FtLLbbeA3VOdtsInGF002YfRRWz0ZhD8xg968GoTt8im05Pe2w7IYsRwM9XYgs7eclMwR3TnKZg=="
}
"""

# --- Fake Social Media & Communication API Keys ---

# Twitter/X API v2 Bearer Token
twitter_bearer_token = "U2FsdGVkX18zwxiWnG4Z5UdqPP13k1p//wOGQth1O+gBaJ0CIF2pDkXY9yV1gJ5n/u4J/G/NADQnFp4pKexZ8lVaWCmdwktiaPYXAq0v7rLoZyl0faP9NRSfANFFzOaaKSz1mBfvus5YEWNv1q31l157AJMqMa456QQ4QH/F7Lg="

# Slack Bot Token
slack_bot_token = "U2FsdGVkX18H9pwjLAQ3Mpx0pDBlikQglC7OZcrd3K7Lfb6XygO066zya7XINrdrjvRUquezMHKynzrDhLU103Z4KrhiAdeZ4FrrE9R5Ssc="

# Twilio Credentials
twilio_account_sid = "ACa1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"
twilio_auth_token = "U2FsdGVkX19NI6I+Cnb8y7ygsJal3oMwuQOlpkIUairoiAZNflBt0kJIVRZeawSrcRaf7vBG4JuvEY8Y2dcv8A=="


# --- Fake Database and Other Credentials ---

# Redis Password
redis_password = "U2FsdGVkX1/TXOoI0+AiVCjf1ADYeqBbUckhxOCcxgrsR1uVLAfO4X6lo2GIDvs8"

# Generic JWT Token
jwt_token = "U2FsdGVkX19uWqFSx4o5dMxBpFZds8lplNqZm6Sv0gTDYTuJDRaJUBYpU9dgN8VSZgy6xUsyAnFzMjNPiNz/+ypvRBNqwWjAiQKViDsLrK+tsteBNh8Syf+q6sh+86HP5vuLWSZ1lYgEtzzJScSxv2cIgPUmFRxJjv4dl8fSIP0uSc9d2FgsTZDWckcBsd5PieD93+bhqXl4mwDTFtb7FHp++HH/J+sSobMAuvDD7/Y="


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
