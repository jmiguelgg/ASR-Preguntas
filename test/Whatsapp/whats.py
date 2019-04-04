from twilio.rest import Client

account_sid = ''
auth_token = ''

cliente = Client(account_sid, auth_token)

mensaje = cliente.messages.create(
    body = 'Ya hay whatsapp !!',
    from_= 'whatsapp:+',
    to = 'whatsapp:+'
)

print(mensaje.sid)
