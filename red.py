# more_test_secrets.py
# A second script with a different set of fake secrets for testing.

# --- Fake Cloud Provider Keys ---

# AWS Credentials (often found in config files)
aws_config = {
    'aws_access_key_id': 'U2FsdGVkX19uFyxD1lz20pUIcvlQ8W+XoX0ZT0HAeF5w6mTDRF+xYeYfojUzDPa9',
    'aws_secret_access_key': 'U2FsdGVkX1/xD6rgSyhRTFplAKeKOtJA6G8NidCmhr9Q1l9rD6C1P/0QzzqZMbMH5Exc0QbFChRQgbqdAyJTyw==',
    'region': 'us-east-1'
}

# Google Cloud (service account JSON key placeholder)
gcp_service_account_key_json = """
{
  "type": "service_account",
  "project_id": "fake-project-12345",
  "private_key_id": "U2FsdGVkX1+ZdE3hJ+pv2nqBMpwwwTp4w2MhmYy8gQX0J3qiz6m1YY1kMqJxn33ZZi3aYUI2qhJ0+mztW4wxyg==",
  "private_key": "U2FsdGVkX18Pbf8AHRMUX92WI5P6PCgjk7LIFD5DAhe1aFLBMF/PNnVeRLHh+F0KoDO8nIfnEHd94RfFyuqNqjGJcwuMmhZR2rseKVwaXwr1ZUR1l4WA0U8StQmMHSofiAMhCGxUHX68gfLDFXK7NEkwcaR9r6Sh8KiM1iLNRoU=",
  "client_email": "fake-service-account@fake-project-12345.iam.gserviceaccount.com",
  "client_id": "123456789012345678901",
  "auth_uri": "U2FsdGVkX18zQKjVSlYgE+VCEW1I+wb5/MnFFntt2Df8CDocfVqLMVfVLETTSn0fDqQDa9jjf5rlkbq6bwMzTA==",
  "token_uri": "U2FsdGVkX1+lS1IS5DXPnKQ0FLDSVC8iSS2bkLhc5Mqgu6f4Z0KQVGNZt46mKboSEnWYPb9iFbtmXhGcMHsJnw=="
}
"""

# --- Fake Social Media & Communication API Keys ---

# Twitter/X API v2 Bearer Token
twitter_bearer_token = "U2FsdGVkX1+4Q2KyakWxOG5AGopX8vwpj706S28RbYskPHwnwZYQ5rSG6Vk6pNeyd1MiTZXQXZj5soAMXUUz9xRVoO5aoNxuvDzNP8MC/FE5wh2Wrk44Bc20kdy042xANEum+mJ2Jl7zXJ621Hr60myAOe5VTLgdyYQqHIvAu7g="

# Slack Bot Token
slack_bot_token = "U2FsdGVkX1+e4uxOtGY14CLG+IW8+VKqidVLC6ZLycyT6wcOgydXa5xwLX25h+NwDlnnJ7Eug8SOHiIO69hUzBP4QCjLNEmg2WTqW93qq9w="

# Twilio Credentials
twilio_account_sid = "ACa1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"
twilio_auth_token = "U2FsdGVkX1/b6jUiVh67g1+Y1zQz6Brtkv2JjVdYY7AcCUMxDqMn3/NBYXOqF3JqoEp69lnoazv0J6RGPP82yw=="


# --- Fake Database and Other Credentials ---

# Redis Password
redis_password = "U2FsdGVkX1/cDY7/QPmOI5QjMwoRuVaNz4QWlqwioLiCMlrNZMI4fJxc5tr+/hXK"

# Generic JWT Token
jwt_token = "U2FsdGVkX19uQarVuImszWE+8x1hMozG4esQXXdHg6RayEHb/wlHXjioreuRJTbrmyumiGTSpeThzRNRvTp2j5meLXsardP3mz01aZsZt6khVWVupBchht9OxvWQCoY6Ea8QJc3hmqQqlr9pASf9kGqTWA5YOll5KhWe5Uh2BTzPK7ROzjU+kE1d5erxMUNmYSewq0AivL0o7XLJTMajMtk1JOc+gWF/wvaWO4urRzI="


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
