## Ativa o bot de tempos em tempos para atualização dos dados.
# > Usuario pode customizar o tempo no qual o bot vai fazer a coleta no site do governo.


from threading import Thread
from time import sleep

class ScheduleBot(object):
    def __init__(self,time,bot,manipulator,db,*args,**kwargs):
        self.time=time
        self.bot=bot
        self.manipulator=manipulator
        self.db=db
        self.kwargs=kwargs
        self.check =False
    
    def start(self):
        t = Thread(target=self.run(),args=('thread initializable'))
        t.start()
        return t
    def run(self):
        self.check=True
        while self.check:
            self.bot.download_csv_page(False)
            csv_update= self.bot.validate_config_csv()
            q = self.manipulator.reader_csv(csv_update)
            self.db.create_table()
            self.db.insert(q)
            time.sleep(self.time)
    
    def stop(self):
        self.check=check



