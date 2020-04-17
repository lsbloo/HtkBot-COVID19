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

# CONFIGURATION PATH INIT HTK-BOT
PATH_BINARY_FIREFOX = os.environ.get('PATH_BINARY_FIREFOX', ' NOT SET FIREFOX BINARY PATH')
SITE_EXAMPLE= os.environ.get('SITE_EXAMPLE', 'NOT SET SITE EXAMPLE BOT')
SETTINGS_PATHS_CONFIG_BOT = (
    PATH_BINARY_FIREFOX,
    SITE_EXAMPLE
)

#CONFIGURATION PATH OF DIR SAVE CSV DOWNLOAD BY BOT.
PATH_SAVE_CSV= os.environ.get('PATH_SAVE_CSV', 'NOT SET PATH SAVE CSV')
SETTINGS_PATH_SAVE_ARCH_CSV = (
    PATH_SAVE_CSV
)

#############################################################################################################

# DATABASE QUERYS.
CREATE_TABLE = "CREATE TABLE IF NOT EXISTS covid19_brasil (regiao varchar(255), estado varchar(2), data varchar(255), casosNovos varchar(255), casosAcumulados varchar(255), obitosNovos varchar(255), obitosAcumulados varchar(255) ); "
INSERT_TABLE = "INSERT INTO covid19_brasil (regiao,estado,data,casosNovos,casosAcumulados,obitosNovos,obitosAcumulados) VALUES (%s,%s,%s,%s,%s,%s,%s) ;"
SELECT_ALL="SELECT regiao,estado,data,casosNovos,casosAcumulados,obitosNovos,obitosAcmulados FROM covid19_brasil ;"
SETTINGS_DATABASE_QUERY = (
    CREATE_TABLE,
    INSERT_TABLE,
    SELECT_ALL

)


