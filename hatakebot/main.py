from scrapper.scrappercovid import get_instance_bot
from util.csv_validator import get_instance_manipulator
from database.db import get_instance_db
from database.db import OperatorDatabase



htkbot = get_instance_bot()


#htkbot.download_csv_page(False)
xd = htkbot.validate_config_csv()
#print(xd)


manipulator = get_instance_manipulator()
q = manipulator.reader_csv(xd)

db = OperatorDatabase(get_instance_db())
print(db)

