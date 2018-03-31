from twilio.rest import Client

account_sid = "AC46edd53d931e706a6eee0460c639fef2"
auth_token  = "b3c822313fd44ac7ea68daff29c83f3c"

client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+919925504697",
    from_="+12015741903",
    url="https://raw.githubusercontent.com/YJDave/AWW_AWH/master/voice.xml"
)

print(call.sid)
