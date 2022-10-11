import smtplib, email.message, main, db_connect

Email_Subject = f"Melhores preços de hoje produto: {main.product_text}"
Email_sender = "" # Email que será enviado
Email_addressee = "" ## Email para envio
password = "" ## Senha do email de envio

def send_email():
    body_email = f"""
    <p>Olá Sr. Braullio, como vai? espero que esteja bem.</p>

    <p>Estou lhe enviando os melhores preços dos Produtos {main.product_text} de hoje, Aproveite as ofertas limitadas.</p>

    <p>Abs</p>
    <p>Melhorespreços.com</p>
    """

    msg = email.message.Message()
    msg['Subjet'] = Email_Subject
    msg['From'] = Email_sender
    msg['To'] = Email_addressee
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(send_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print(f"Email Enviando para {Email_addressee} com sucesso")

send_email()