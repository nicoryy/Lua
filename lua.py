
import datetime
import email_assistente as ea
try:
    from time import sleep
    import speech_recognition as sr
    import voz
    import pyautogui as pa
    import os
    import keyboard as kb
    import google.demo as gg
    # import datetime
    import sys
    


    def alarme(hora, min):
        os.startfile(R'C:\Users\pedro\AppData\Local\Programs\Python\Python310\Lib\site-packages\calarme\alarmevisual.pyw')
        sleep(1.5)
        pa.write(f'{hora}')
        pa.press('tab')
        pa.write(f'{min}')
        pa.press('tab')
        pa.press('space')
        # kb.press_and_release('alt + esc')
        voz.falar('Alarme definido.') 


    def timer(tempo):
        os.startfile(R'C:\Users\pedro\AppData\Local\Programs\Python\Python310\Lib\site-packages\calarme\timer.py')
        sleep(1) 
        pa.write(f'{tempo}')
        pa.press('enter')
        kb.press_and_release('alt + esc')
        voz.falar('Timer definido.') 


    def reiniciar():
        os.startfile(R'C:\Users\pedro\Desktop\nicory\projetos\projetosProntos\falas\restartassis.py')
        quit()

    dias ={
        'Monday':'Segunda-Feira',
        'Tuesday':'Terça-Feira',
        'Wednesday':'Quarta-Feira',
        'Thursday':'Quinta-Feira',
        'Friday':'Sexta-Feira',
        'Saturday':'Sábado',
        'Sunday':'Domingo'
        }
    dias_key = {
        'Segunda-Feira':0,
        'Terça-Feira':1,
        'Quarta-Feira':2,
        'Quinta-Feira':3,
        'Sexta-Feira':4,
        'Sábado':5,
        'Domingo':6
    }
    key_dias = dict((v, k) for k, v in dias_key.items())




    contador_reiniciar_ = 0
    rec = sr.Recognizer()


    #-------------------------- PROGRAMA PRINCIPAL --------------------------
    try:
        timeee = datetime.datetime.now().time()
        inicial = f"""
        <p>Programa Lua iniciado às {timeee}.<p>
        """
        #ea.enviar('Lua iniciado', inicial)    

        while True:

            
    # Abrir microfone para detecção de voz
            hr, min = datetime.datetime.now().hour, datetime.datetime.now().minute

            timeee = datetime.datetime.now().time()

            if contador_reiniciar_ == 50:
                reiniciar()

            with sr.Microphone(1) as mic:
                rec.adjust_for_ambient_noise(mic)
                # print(rec.energy_threshold)
                print(f'fale ({timeee})')
                audio = rec.listen(mic, phrase_time_limit=5)
                try:
                    texto = rec.recognize_google(audio, language='pt-BR')
                except:
                    print('nao entendi')
                    # reiniciar()
                    contador_reiniciar_ += 1
                    print(contador_reiniciar_)
                    continue
            
    # Comando para desligar lua
            if 'desligar' in texto.lower():
                voz.falar('Desligando...')
                try:
                    os.remove('pera.mp3') 
                except:
                    pass
                quit()
    # COMANDo para desligar alarme/timer
            elif 'acordei' in texto.lower():
                kb.press('space')
                kb.release('space')
    # Condição para iniciar comandos:
            elif 'lua' in texto.lower().split():

                comand = texto.lower().split().copy()
                comand.remove('lua')

                # bom dia
                if 'bom' and 'dia' in comand:
                    voz.falar('Bom dia pedro.')
                    comand.remove('bom')
                    comand.remove('dia')

                # comando vazio
                if len(comand) == 0:
                    continue
                
                # comandoo para cancelar comando lua
                elif 'cancela' in comand:
                    voz.falar('ok')
                    continue

                

                # comandoo que horas sao
                elif 'horas' and 'são' in comand:
                    voz.horas()


                # comandos midia
                elif 'música' in comand:
                    comand.remove('música')
                    lista = ['muda', 'próxima', 'volta', 'anterior', 'para', 'pausa', ]
                    for n in comand:

                        if n == 'muda':
                            kb.press('next track')
                        elif n == 'próxima':
                            kb.press('next track')
                        elif n == 'passa':
                            kb.press('next track')
                        elif n == 'volta':
                            kb.press('previous track')
                        elif n == 'anterior':
                            kb.press('previous track')
                            sleep(0.5)
                            kb.press('previous track')
                        elif n == 'para':
                            kb.press('play/pause media')
                        elif n == 'pausa':
                            kb.press('play/pause media')
                        elif n == 'play':
                            kb.press('play/pause media')
                        elif n == 'toca':
                            kb.press('play/pause media')
                        
                        else:
                            pass     
                    print(comand)

                # comandoo ativar alarme 
                elif 'ativar' in comand:
                    print(comand)
                    if 'alarme' in comand:
                        try:
                            if 'para' in comand:
                                comand.remove('para')
                            if 'ativar' in comand:
                                comand.remove('ativar')
                            if 'alarme' in comand:
                                comand.remove('alarme')
                            if 'as' in comand:
                                comand.remove('as')

                            cfrase = comand
                            if not 'e' in cfrase:
                                try:
                                    hora, min = cfrase[0].split(':')
                                except:
                                    horas = comand.index('horas')
                                    hora = cfrase[0]
                                    min = 0
                                alarme(hora, min) 
                                print(comand)
                            else:
                                try:
                                    e = cfrase.index('e')
                                    hora, min = cfrase[e - 1], cfrase[e + 1]
                                    min = int(min)
                                    hora = int(hora)
                                    if min == 6:
                                        min = 30
                                    alarme(hora, min)
                                except Exception as e:
                                    print(e)
                                    voz.erro()
                                    print('foi aqui')
                                    print(cfrase)
                        except Exception as e:
                            print(comand)
                            print(e)
                            voz.erro()
                            print('foi nao')
                        
                    
                    #comando timer
                    elif 'timer' in comand:
                        if 'ativar' in comand:
                            comand.remove('ativar')
                        if 'de' in comand:
                            comand.remove('de')
                        if 'para' in comand:
                            comand.remove('para')
                        
                        tempo = int(comand[1])
                        
                        if 'segundos' in comand[2]:
                            pass
                        elif 'minutos' in comand[2]:
                            tempo *= 60
                        elif 'horas' in comand[2]:
                            tempo *= 3600

                        timer(tempo)
                    
                    else:
                        pass


                # comando listar eventos calendario

                elif 'agenda' in comand: 
                    
                    print(comand)
                    if 'mostrar' or 'mostra' in comand:
                        try:
                            calendar = [[],[],[],[],[],[],[]]
                            for agenda in gg.listarEventosSemanaGERAL():
                                
                                data = agenda['data'].split('/')
                                dt = datetime.datetime.date(datetime.datetime(int(data[2]),int(data[1]),int(data[0])))

                                
                                dia_semana = dias[f'{dt.strftime("%A")}']

                                if len(agenda) == 4:
                                    # print(agenda['nome'], agenda['horario'], agenda['data'])
                                    ag = agenda['nome'], agenda['horario'], agenda['data']
                                else:
                                    # print(agenda['nome'], agenda['data'])
                                    ag = agenda['nome'], agenda['data']
                                    
                                calendar[dias_key[f'{dia_semana}']].append(ag)
                                
                                print('day Name:', dia_semana)


                            print(calendar)
                            d = -1
                            for i in calendar:
                                d += 1
                                if len(i) == 0:
                                    continue 
                                else:
                                    voz.falar(f'Na {key_dias[d]} você tem')
                                    print(len(i))
                                    for e in range(len(i)):
                                        voz.falar(f'{i[e][0]} as {i[e][1]}')

                        
                        except Exception as e:
                            print(f'An error has ocorred: {e}')
                        calendar.clear()
                    else:
                        pass                        


                elif 'fala' in comand:
                    comand.remove('fala')
                    num = ''
                    for n in comand:
                        num = num + f'{n}'
                        num = num + ' '
                    voz.falar(f'{num}', 'pera')
                    print(comand)
                
                # comando fniciar
                elif 'reiniciar' in comand:
                    voz.falar('Reiniciando.')
                    reiniciar()
        
    
                # nao reconhece comandoo
                else:
                    voz.falar('Comando não reconhecido.')
                    print(comand)
                    continue
                    
                # print(comand)

            else:
                continue

    except Exception as e:
        print('Ocorrou um erro:',e)
        os.system("pause")
        
# enviar email de desligamento e erro 
except IOError:
    type, value, traceback = sys.exc_info()
    e = f'Error opening %s: %s' % (value.filename, value.strerror)
    erro = f"""
    <p>Às {datetime.datetime.now().ctime()}, lua foi encerrada.</p>
    <p>Erro: {e}</p>
    """

    ea.enviar('Lua desligada!', erro)
    print('Ocorrou um erro:',e)
    os.system("pause")

