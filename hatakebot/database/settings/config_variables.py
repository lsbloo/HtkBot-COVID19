import os
import sys


#CONFIGURATION CONNECT DATABASE - LOCAL OR H;
DATABASE_NAME=os.environ.get('DATABASE_NAME', 'NOT SET DATABASE NAME')
DATABASE_HOST_CONNECT= os.environ.get('DATABASE_HOST', 'NOT SET HOST CONNECT')
DATABASE_USER= os.environ.get('DATABASE_USER', 'NOT SET DATABASE USER')
DATABASE_PASSWORD= os.environ.get('DATABASE_PASSWORD', 'NOT SET PASSWORD DATABASE')
DATABASE_PORT= os.environ.get('DATABASE_PORT', 'NOT SET PORT DATABASE')
SETTINGS_DATABASE = (
    DATABASE_NAME,
    DATABASE_HOST_CONNECT,
    DATABASE_USER,
    DATABASE_PASSWORD,
    DATABASE_PORT
)

#############################################################################################################

# DATABASE QUERYS.
CREATE_TABLE = "CREATE TABLE IF NOT EXISTS ",SETTINGS_DATABASE[0]," (regiao varchar(255), estado varchar(2), data varchar(255), casosNovos varchar(255), casosAcumulados varchar(255), obitosNovos varchar(255), obitosAcumulados varchar(255) ); "
INSERT_TABLE = "INSERT INTO ",SETTINGS_DATABASE[0]," (regiao,estado,data,casosnovos,casosacumulados,obitosnovos,obitosacumulados) VALUES ('%s','%s','%s','%s','%s','%s','%s'); "
SELECT_ALL="SELECT regiao,estado,data,casosNovos,casosacumulados,obitosnovos,obitosacumulados FROM covid19_brasil ;"
DROP_TABLE="DROP TABLE  %s ;"
SETTINGS_DATABASE_QUERY = (
    CREATE_TABLE,
    INSERT_TABLE,
    SELECT_ALL,
    DROP_TABLE,
)


