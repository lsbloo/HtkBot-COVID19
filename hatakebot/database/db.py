import psycopg2
import time
from datetime import time
from .settings import SETTINGS_DATABASE_QUERY,SETTINGS_DATABASE

class CovidGov(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            print('{0} = {1}'.format(key,value))
    



class OperatorDatabase(object):

    def __init__(self,instance_db):
        try:
            if instance_db == None:
                raise Error('Instance DB', 'Instance Database Object dont found')
        except Error as e:
            print(e)
        finally:
            self.instance_db = instance_db
            print("Instance: %s " %str(self.instance_db))
    
    def create_table(self):
        pass

    
class InstanceException(Exception):
    pass
class Error(InstanceException):
    def __init__(self,expression,message):
        self.expression=expression
        self.message=message


