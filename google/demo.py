from pprint import pprint
from shutil import rmtree
from Google import Create_Service
import datetime
import os
from google.auth.exceptions import RefreshError
# import sys
import pyautogui as pa
from time import sleep


CLIENT_SECRET_FILE = 'client_secret_908468041465-4g1h5c1bm8laqhqgm07440b812up58l1.apps.googleusercontent.com.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']
UTC = 'America/Fortaleza'
INFINITY = 'kbu4cee53fekqpv46n3g3o1f84@group.calendar.google.com'
NICORY = 'primary'
IFCE = 'h48848c44j9au5fj85n7r1im0g@group.calendar.google.com'
calendars = [NICORY, INFINITY, IFCE]

try:
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
except RefreshError:
    rmtree(R'C:\Users\pedro\Desktop\nicory\projetos\projetosProntos\falas\token files')
    sleep(5)
    a, b = pa.locateCenterOnScreen('pdrncy.png')
    # print(a)
    pa.click(a, b)
    sleep(2.5)
    c, d = pa.locateCenterOnScreen('continuar1.png')
    pa.click(c, d)
    sleep(2.5)
    pa.scroll(-200)
    sleep(2)
    e, f = pa.locateCenterOnScreen('continuar.png')
    pa.click(e, f)

    os.system("pause")
except FileNotFoundError:
    CLIENT_SECRET_FILE = fR'C:\Users\pedro\Desktop\nicory\projetos\projetosProntos\falas\google\{CLIENT_SECRET_FILE}'
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

'''
created_event = service.events().quickAdd(
calendarId='etnn5ts05j22cua76n0ci3f3s8@group.calendar.google.com',
    text='test1'
    ).execute()

-----------------------------------------------

DATETIME ex: 2022-07-22 T 09:00:00 -07
              y   m  d  /  h  m  s  UTC 
              '''

def listarCalendario():
    '''
        Retorna em uma lista o ID e o NOME dos calendarios disponíveis.
        Caso não, retorna valor vazio.
    '''
    calendar_list_entry = service.calendarList().list().execute()
    calendario = []
    try:
        for item in calendar_list_entry['items']:
            # print('Nome:' ,item['summary'])
            # print('Id: ',item['id'])
            calendarios = {
                'nome':f'{item["summary"]}',
                'id':f'{item["id"]}'
            }
            calendario.append(calendarios)
        return calendario
    except:
        return calendario == []


def semana():

    semana = []
    for n in range(7):

        d = datetime.datetime.now().date() + datetime.timedelta(days=n)

        dia, mes, ano = d.day, d.month, d.year
        if dia < 10:
            dia = f'0{dia}'
        if mes < 10:
            mes = f'0{mes}'

        data = f'{dia}/{mes}/{ano}'
        semana.append(data)
    return semana




def listarEventos(calendarId='primary', maxResults=7):
    try:
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 7 events')
        events_result = service.events().list(calendarId=calendarId, timeMin=now,
                                              maxResults=maxResults, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return 

        else:
            # Prints the start and name of the next 10 events
            eventos = []
            data = []
            datas = ''
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))

                time = start.split('T').copy()

                if len(time) == 2:
                    # print(time)
                    time.pop(0)
                    time = time[0].split('-')
                    time.pop(1)
                    time = time[0].split(':')
                    time.pop(2)
                    time = f'{time[0]}:{time[1]}'
                else:
                    time = False

                for i in start.split('T')[0].replace('-', '/'):
                    datas += i
                
                
                data.append(datas)
                a = data[0].split('/')
                dataas = f'{a[2]}/{a[1]}/{a[0]}'

                if time:
                    evento = {
                        'nome':f'{event["summary"]}',
                        'id':f'{event["id"]}',
                        'data':f'{dataas}',
                        'horario':f'{time}'
                    }
                else:
                    evento = {
                        'nome':f'{event["summary"]}',
                        'id':f'{event["id"]}',
                        'data':f'{dataas}'
                    }

                datas = ''
                data.clear()
        
                eventos.append(evento)
            return eventos
        
    except Exception as error:
        print('An error occurred: %s' % error)




def deletCalendar(calendarNome):
    num = 0
    try:
        calendar_list_entry = service.calendarList().list().execute()
        for item in calendar_list_entry['items']:
            if item['summary'] == calendarNome:
                num += 1
                calendarId = item['id']
                print('Nome:' ,item['summary'])
                print('Id: ',item['id'])
        if num == 0:
            raise Exception('Calendario nao encontrado!')
        elif num == 1:
            service.calendars().delete(calendarId=calendarId).execute()
        else:
            raise Exception('Mais de um calendario com o mesmo nome!!')
    except Exception as e:
        print(f'An error has occored: {e}')




def deletCalendarId(calendarId):
    try:
        service.calendars().delete(calendarId=calendarId).execute()
    except Exception as e:
        print('An error has occored:', e )




def criarCalendario(nome, utc=UTC):
    try:
        calendar = {
            'summary':nome,
            'timeZone':utc
        }

        service.calendars().insert(body=calendar).execute()
        print('Calendario criado com sucesso!')
    except Exception as e:
        print(e)



def nomeCalendario(calendarId='primary', id=False):
    calendar = service.calendars().get(calendarId=calendarId).execute()
    if id:
        return [calendar['sumamry'], calendar['id']]
    else:
        return calendar['summary']





def criarEvento(nome, startMes, startDia, endMes, endDia, hora=9, minuto=0, descrição='Evento Criado pela Assistente.', calendarId='primary', reminder=True):    
    
    '''
    {nome}: Event's name
    {startMes}: sei la porra
    '''


    atual = datetime.datetime.now().month
    if atual < 10:
        atual = f'0{atual}'
    # print(atual)

    
    meses = {
        'janeiro':'01',
        'fevereiro':'02',
        'março':'03',
        'abril':'04',
        'maio':'05',
        'junho':'06',
        'julho':'07',
        'agosto':'08',
        'setembro':'09',
        'outubro':'10',
        'novembro':'11',
        'dezembro':'12',
        'atual':f'{atual}'
    }

    startMes, endMes = meses[f'{startMes}'], meses[f'{endMes}']
    print(startMes, endMes)


    # # ----------- CRIAR EVENTO ------------------
    try:
        if not reminder:
            request_body = {
                'summary':f'{nome}',
                'description':f'{descrição}',
                'start':{
                    'dateTime':f'2022-{startMes}-{startDia}T{hora}:{minuto}:00-03:00',
                    'timeZone':UTC
                },
                'end':{
                    'dateTime':f'2022-{endMes}-{endDia}T{hora}:{minuto}:00-03:00',
                    'timeZone':UTC
                },
                'colorId':1

            }
        else:
            request_body = {
                'summary':f'{nome}',
                'description':f'{descrição}',
                'start':{
                    'dateTime':f'2022-{startMes}-{startDia}T{hora}:{minuto}:00-03:00',
                    'timeZone':UTC
                },
                'end':{
                    'dateTime':f'2022-{endMes}-{endDia}T{hora}:{minuto}:00-03:00',
                    'timeZone':UTC
                },
                'colorId':1,
                "reminders": {
                    "useDefault": False,
                    "overrides": [
                    {
                        "method": 'popup',
                        "minutes": 1440
                    }
                    ]
                }

            }

        event = service.events().insert(calendarId=f'{calendarId}', body=request_body).execute()
        print('Id:', event['id'])
    except Exception as e:
        print(f'An error has ocorred: {e}')


# def eventoHoje(calendarId):


def deletarEvento(eventId,calendarId='primary'):
    # ---------------- excluir eventos ----------------
    try:
        service.events().delete(calendarId=calendarId, eventId=eventId).execute()
        print('Evento deletado com sucesso!!!')
    except Exception as e:
        print(e)


def listarEventosSemana(calendarId='primary', maxResults=7):
    try:
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 7 events')
        events_result = service.events().list(calendarId=calendarId, timeMin=now,
                                              maxResults=maxResults, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return 

        else:
            # Prints the start and name of the next 10 events
            eventos = []
            data = []
            datas = ''
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))

                time = start.split('T').copy()

                if len(time) == 2:
                    # print(time)
                    time.pop(0)
                    time = time[0].split('-')
                    time.pop(1)
                    time = time[0].split(':')
                    time.pop(2)
                    time = f'{time[0]}:{time[1]}'
                else:
                    time = False

                for i in start.split('T')[0].replace('-', '/'):
                    datas += i
                
                
                data.append(datas)
                a = data[0].split('/')
                dataas = f'{a[2]}/{a[1]}/{a[0]}'


                for sem in semana():
                    if dataas == sem:
                    
                        if time:
                            evento = {
                                'nome':f'{event["summary"]}',
                                'id':f'{event["id"]}',
                                'data':f'{dataas}',
                                'horario':f'{time}'
                            }
                        else:
                            evento = {
                                'nome':f'{event["summary"]}',
                                'id':f'{event["id"]}',
                                'data':f'{dataas}'
                            }

                        datas = ''
                        data.clear()
                
                        eventos.append(evento)
            return eventos
        
    except Exception as error:
        print('An error occurred: %s' % error)


def listarEventosSemanaGERAL(maxResults=7):
    eventoos = []
    calendar = []
    for c in listarCalendario():
        calendar.append(c['id'])
    try:
        for calendarios in calendar:
           
            # Call the Calendar API
            now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
            # print('Getting the upcoming 7 events')
            events_result = service.events().list(calendarId=calendarios, timeMin=now,
                                                maxResults=maxResults, singleEvents=True,
                                                orderBy='startTime').execute()
            events = events_result.get('items', [])

            if not events:
                print('No upcoming events found.')
                Empty_Value = []
                return  Empty_Value

            else:
                # Prints the start and name of the next 10 events
                eventos = []
                data = []
                datas = ''
                for event in events:
                    start = event['start'].get('dateTime', event['start'].get('date'))

                    time = start.split('T').copy()

                    if len(time) == 2:
                        # print(time)
                        time.pop(0)
                        time = time[0].split('-')
                        time.pop(1)
                        time = time[0].split(':')
                        time.pop(2)
                        time = f'{time[0]}:{time[1]}'
                    else:
                        time = False

                    for i in start.split('T')[0].replace('-', '/'):
                        datas += i
                    
                    
                    data.append(datas)
                    a = data[0].split('/')
                    dataas = f'{a[2]}/{a[1]}/{a[0]}'


                    for sem in semana():
                        if dataas == sem:
                        
                            if time:
                                evento = {
                                    'nome':f'{event["summary"]}',
                                    'id':f'{event["id"]}',
                                    'data':f'{dataas}',
                                    'horario':f'{time}'
                                }
                            else:
                                evento = {
                                    'nome':f'{event["summary"]}',
                                    'id':f'{event["id"]}',
                                    'data':f'{dataas}'
                                }

                            datas = ''
                            data.clear()
                    
                            eventos.append(evento)
                for n in eventos:
                    eventoos.append(n)
        eventoos_sorted = sorted(eventoos, key=lambda x: datetime.datetime.strptime(x['data'], '%d/%m/%Y')) 
        return eventoos_sorted
        
    except Exception as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    pprint(listarEventosSemanaGERAL())