from scrapper.scrappercovid import get_instance_bot
from util.csv_validator import get_instance_manipulator
from database.db import get_instance_db
from database.db import OperatorDatabase
from schedule import ScheduleBot
from audio.gaudio import get_instance_audio
import time
import sys



htkbot = get_instance_bot()
htkbot_audio = get_instance_audio()
print(htkbot_audio.play("insert"))

#Operation web-scrapper ok collect
#htkbot.download_csv_page(False)
#xd = htkbot.validate_config_csv()

#print(xd)

manipulator = get_instance_manipulator()


# operation csv ok reader-drop
#q = manipulator.reader_csv(xd)
#manipulator.drop_all_csv()



db = OperatorDatabase(get_instance_db())


# operation db ok
#db.drop()
#db.create_table()
#db.insert(q.get("dataset:"))



## coleta os dados novos, apagando os dados antigos de tempo em tempo.
#scheduleHtkBot =ScheduleBot(60,htkbot,manipulator,db)
#thread = scheduleHtkBot.start()

# dps continuo.
for args in sys.argv:
    print(args)