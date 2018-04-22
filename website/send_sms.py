from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC43fbfdaa41031ca347d0eea205ec405f"
auth_token = "089adb7ec522910c5f36233ece851172"

client = Client(account_sid, auth_token)
'''
client.api.account.messages.create(
    to="+48793979913",
    from_="+48732168077",
    body="Hello there!")


print(message.sid)
'''