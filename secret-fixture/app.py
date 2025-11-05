# app.py — Demonstration code with FAKE embedded secrets for testing scanners.
# Do NOT commit real secrets like this. Use environment variables or a vault.
import os

AWS_ACCESS_KEY_ID = "U2FsdGVkX1+0ISPLo0S4WOt/FevlIgAr1GmK7eGCBBK5wi+T/ZL38mu7cGxdRxyx"
AWS_SECRET_ACCESS_KEY = "U2FsdGVkX1/s0yMSckYcLzWQoaZDskJgJW48L4QzbF966CuXJdk61TnA+zIpPkG7vEK2v5Vl2UsfnrM4HY4j/Q=="
GOOGLE_API_KEY = "U2FsdGVkX19f16HrFvRevxTgRTzWX4nhGa2lY7Fq5xTAcBffybL7UWJSrrFCXkaITsOCbMutOaP8/+1glXBwdQ=="
STRIPE_SECRET_KEY = "U2FsdGVkX19vjUaBubGyjZS+C81B41Cn9MZ2wsNdsPEL9h2LbfaCLyIQj0PHx1K4Lj4asJRJZsZNNWCSCcopqg=="
SLACK_BOT_TOKEN = "U2FsdGVkX18hPX84oueRr2ADj8IHEMR/Mg1ueEsqnCNKEUQmbvuidDTpu2bC/v/cUFNT5E+9nUnpBsfH1BS18QRgydpzdGVMIWViM8JnImw="
GITHUB_TOKEN = "U2FsdGVkX182BLCzKN4tx9JZuAqiQEqzhxMUGrRldazzoRKBku7dVQqyUhStGbsPlNQNJAOoEVpAuHpKg5Ak6g=="
JWT_SECRET = "U2FsdGVkX1/tHKFpm0YeSQRKDq3knLOH/qPRzTm3AZO+uOSUoTPhGuPEv2Q7BsOhgAGS1wdf/h4/PW9/R1oybg=="
MONGO_URI = "mongodb+srv://admin:U2FsdGVkX19vgvZxOtdPZr3Fykd50goBoBn1NNI3UO8=@cluster0.grhabc.mongodb.net/mydb?retryWrites=true&w=majority"
POSTGRES_URL = "postgresql://vtzwvl:U2FsdGVkX18zJsI1noX5QuYIP7g3I6+QuGY6p+R5VpQ=@localhost:5432/appdb"

EMAIL_USER = "test.user@example.com"
EMAIL_PASSWORD = "U2FsdGVkX18fnAX6vxkgmG/J76bkCbAEIUIWz883Y+MgZtAoOqbyKTPbNAqO1RxU"
PERSONAL_PHONE = "U2FsdGVkX18mEHx/FTm2aYyXrFgKQVgCNzbby/8Gs7w="

def connect_services():
    # Fake functions to make scanners traverse references
    return {
        "aws": (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY),
        "google": GOOGLE_API_KEY,
        "stripe": STRIPE_SECRET_KEY,
        "slack": SLACK_BOT_TOKEN,
        "github": GITHUB_TOKEN,
        "jwt": JWT_SECRET,
        "mongo": MONGO_URI,
        "postgres": POSTGRES_URL,
    }

if __name__ == "__main__":
    print("Loaded FAKE secrets. Do not use in production.")
