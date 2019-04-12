from twilio.rest import Client

account_sid = 'ACb149282acccbdf97c1004710c2e3d11d'
auth_token = '8d0aa7e211ea99f907ea7b6de8f4ca46'

cliente = Client(account_sid, auth_token)

mensaje = cliente.messages.create(
    body = 'Ya hay whatsapp !!',
    from_= 'whatsapp:+14155238886',
    to = 'whatsapp:+5215586141860'
)

print(mensaje.sid)
