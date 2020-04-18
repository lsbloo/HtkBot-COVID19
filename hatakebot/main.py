from scrapper.scrappercovid import get_instance_bot
from util.csv_validator import get_instance_manipulator
from database.db import get_instance_db
from database.db import OperatorDatabase
from schedule import ScheduleBot
from audio.gaudio import get_instance_audio
import time
import sys

def options():
    print("---------------------------------------------------------------------------")
    print(" ARGUMENTS VALID")
    print()
    print('python3 execute.py --help')
    print()
    print("python3 execute.py hatake collect firefox-open")
    print()
    print("python3 execute.py hatake collect firefox-closed")
    print()
    print("python3 execute.py hatake collect schedule <time>")
    print()
    print("python3 execute.py hatake drop-table")
    print()
    print("python3 execute.py hatake drop-csv")
    print()
    print("python3 execute.py hatake delete-audio")
    print()
    print("---------------------------------------------------------------------------")


def helper():
    print('Olá.')
    print('Aqui segue as informações detalhadas sobre cada comando executando do bot.')
    print()
    print('Comando 1: python3 execute.py hatake collect firefox-open')
    print("           -> Coleta as informações no site do governo covid.saude. Este metodo abre o navegador firefox e mostra passo a passo o download do arquivo a leitura do mesmo e a inserção na base de dados. Neste comando não há drop de tabela logo os dados existentes são inseridos novamente. Execute este comando no terminal.")
    print()
    print()
    print('Comando 2: python3 execute.py hatake collect firefox-closed')
    print("          -> Semelhante ao primeiro comando, porem não abre o navegador firefox. O bot trabalha apenas pela linha de comando.")
    print()
    print()
    print('Comando 3: python3 execute.py hatake collect schedule <time>')
    print("         -> Coleta as informações no site do governo covid.saude de tempos em tempos. Este metodo não abre o comando e atualiza os dados no banco automaticamente.")
    print()
    print()
    print('Comando 4: python3 execute.py hatake drop-table')
    print("         -> Dropa a tabela criada no banco de dados.")
    print()
    print()
    print('Comando 5: python3 execute.py hatake drop-csv')
    print("        -> Apaga todos os arquivos .csv do diretorio setado no bot. Cuidado ao setar o diretorio de arquivos .csv")
    print()
    print()
    print('Comando 6: python3 execute.py hatake delete-audio')
    print("        -> Apaga os arquivos de audio mp3 carregados pelo bot")
    print()
    

def main():
    args=[]
    for parameter in sys.argv[1:]:
        args.append(parameter)
    try:
        if args[0] == "--help":
            helper()
        if args[0]=='hatake':
            if args[1] == 'collect':
                if args[2] == 'firefox-open':
                    htkbot = get_instance_bot()
                    htkbot_audio = get_instance_audio()
                    manipulator = get_instance_manipulator()
                    db = OperatorDatabase(get_instance_db())
                    htkbot_audio.create_audio("htk_bot")
                    htkbot_audio.play("htk_bot")

                    manipulator.drop_all_csv()
                    html = htkbot.download_csv_page(True)
                    if html != None:
                        htkbot_audio.create_audio("download")
                        htkbot_audio.play("download")
                        xd = htkbot.validate_config_csv()
                        q= manipulator.reader_csv(xd)
                        if q != None:
                            db.create_table()
                            db.insert(q.get("dataset:"))
                            htkbot_audio.create_audio("insert")
                            htkbot_audio.play("insert")

                            time.sleep(0.5)
                            htkbot_audio.create_audio("fim")
                            htkbot_audio.play("fim")

                            print('------------------------------------------------------')
                            print()
                            print('Execução Terminada !')
                            print()
                            print('-------------------------------------------------------')
                elif args[2] == 'firefox-closed':
                    htkbot = get_instance_bot()
                    htkbot_audio = get_instance_audio()
                    manipulator = get_instance_manipulator()
                    db = OperatorDatabase(get_instance_db())
                    htkbot_audio.create_audio("htk_bot")
                    htkbot_audio.play("htk_bot")

                    manipulator.drop_all_csv()
                    html = htkbot.download_csv_page(False)
                    if html != None:
                        htkbot_audio.create_audio("download")
                        htkbot_audio.play("download")
                        xd = htkbot.validate_config_csv()
                        q= manipulator.reader_csv(xd)
                        if q != None:
                            db.create_table()
                            db.insert(q.get("dataset:"))
                            htkbot_audio.create_audio("insert")
                            htkbot_audio.play("insert")

                            time.sleep(0.5)
                            htkbot_audio.create_audio("fim")
                            htkbot_audio.play("fim")

                            print('------------------------------------------------------')
                            print()
                            print('Execução Terminada !')
                            print()
                            print('-------------------------------------------------------')

                elif args[2] == 'schedule':
                    if args[3] != None:
                        htkbot = get_instance_bot()
                        htkbot_audio = get_instance_audio()
                        manipulator = get_instance_manipulator()
                        db = OperatorDatabase(get_instance_db())
                        htkbot_audio.create_audio("bot_schedule")
                        htkbot_audio.play("bot_schedule")

                        scheduleHtkBot = ScheduleBot(int(args[3]),htkbot,manipulator,db)
                        
                        thread = scheduleHtkBot.start()

            if args[1] == 'drop-csv':

                htkbot_audio = get_instance_audio()
                
                manipulator = get_instance_manipulator()
                
                htkbot_audio.create_audio("drop_csv")
                htkbot_audio.play("drop_csv")
                

                time.sleep(0.3)

                htkbot_audio.create_audio("fim")
                htkbot_audio.play("fim")

                print('------------------------------------------------------')
                print()
                print('Execução Terminada !')
                print()
                print('-------------------------------------------------------')

            if args[1] == 'drop-table':
                htkbot_audio = get_instance_audio()
                db = OperatorDatabase(get_instance_db())
                db.drop()
                htkbot_audio.create_audio("drop")
                htkbot_audio.play("drop")
                time.sleep(0.3)
                htkbot_audio.create_audio("fim")
                htkbot_audio.play("fim")

                print('------------------------------------------------------')
                print()
                print('Execução Terminada !')
                print()
                print('-------------------------------------------------------')

            if args[1] == 'delete-audio':
                htkbot_audio = get_instance_audio()
                
                res = htkbot_audio.delete_audios()

                if res:
                    print("Audios Deletados com sucesso!")
                    print()
                else:
                    print(" Ocorreu um erro ao deletar os audios.")
                    print()
                
                time.sleep(0.3)
                

                print('------------------------------------------------------')
                print()
                print('Execução Terminada !')
                print()
                print('-------------------------------------------------------')
    except Exception as e:
        print("Error Input: ", e)
        options()




main()





