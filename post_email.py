import smtplib, email.message

Email_Subject = "Melhores preços de hoje produto: Redmi"
Email_sender = "xxvalkemgamerxx@gmail.com"
Email_addressee = "vallkemgamer@gmail.com"
password = "lucas990230"

def send_email():
    body_email = """
    <p>Olá Sr. Braullio, como vai? espero que esteja bem.</p>
    <p>Estou lhe enviando os melhores preços dos Produtos Redmi de hoje, Aproveite as ofertas limitadas.</p>
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
    print("Email Enviado!!!")

send_email()