
import win32com.client as win32

# criar a integração com o outlook
outlook = win32.Dispatch('outlook.application')
# criar um email
email = outlook.CreateItem(0)

def enviar(Assunto, corpoHTML, emailTo='pedronicory@gmail.com'):


    # configurar as informações do seu e-mail
    email.To = f"{emailTo}"
    email.Subject = f'{Assunto}'
    email.HTMLBody = f'{corpoHTML}'
    email.Send()



