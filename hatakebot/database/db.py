import psycopg2
import time
from datetime import time
import sys

from .settings.config_variables import SETTINGS_DATABASE,SETTINGS_DATABASE_QUERY

class CovidGov(object):
    def __init__(self, **kwargs):
        param=[]
        for key, value in kwargs.items():
            #print('{0} = {1}'.format(key,value))
            param.append([key,value])
        self.db_name=param[0][1]
        self.db_host=param[1][1]
        self.db_user=param[2][1]
        self.db_password=param[3][1]
        self.db_port=param[4][1]
    
    def get_instance(self):
        instance = psycopg2.connect(dbname=self.db_name,user=self.db_user,password=self.db_password,host=self.db_host,port=self.db_port)
        if instance != None:
            instance.autocommit= True
            return instance
        
        return None
    

def get_instance_db():
        return CovidGov(database_name=SETTINGS_DATABASE[0],database_host=SETTINGS_DATABASE[1],database_user=SETTINGS_DATABASE[2],database_password=SETTINGS_DATABASE[3],
        database_port=SETTINGS_DATABASE[4]).get_instance()


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
        cursor = self.instance_db.cursor()
        sql_ = SETTINGS_DATABASE_QUERY[0]
        cursor.execute(sql_)
        cursor.close()
        print('Table Create')

        

    
class InstanceException(Exception):
    pass
class Error(InstanceException):
    def __init__(self,expression,message):
        self.expression=expression
        self.message=message



