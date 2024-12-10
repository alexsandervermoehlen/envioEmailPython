import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Uktikizado servidor de email do googl para esta aplicação se ultilizar outro servidor os dados se alteram

clientes = pd.read_excel('./clientes.xlsx')

for index, cliente in clientes.iterrows():
    msg = MIMEMultipart()
    msg['Subject'] = 'Recebido email :'
    msg['From'] = 'email'
    msg['To'] = cliente['email']
    message = f"Olá, {cliente['nome']}, Email recebido em sua conta"
    msg.attach(MIMEText(message, 'plain'))

    # servidor smtp do gmail se for outro servidor as informa;coes mudam
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # insira seu email e sua senha
    server.login('email','senha')
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()