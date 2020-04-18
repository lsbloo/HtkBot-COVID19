from .settings.config_variables import SETTINGS_PATH_SAVE_ARCH_CSV
from .model.models import Covid19
import os
import csv
import glob


class ManipulatorCSV(object):
    def __init__(self,path_csv):
        try:
            if path_csv != 'NOT SET PATH SAVE CSV':
                self.path_csv=path_csv
            else:
                print('Dont Load Variavel Path CSV')
        except Exception as e:
            print(e)
    
    @staticmethod
    def len_csv():
        pass

    def validator_csv(self,list_csv):
        dt_relevante = []
        for k in list_csv:
            if k[3] == '0' and k[4]=='0' and k[5] =='0' and k[6]=='0':
                pass
            else:
                dt_relevante.append(k)
        return dt_relevante
        


    def generate_list_models(self,list_csv_validated):
        list_covids=[]
        for k in list_csv_validated:
            list_covids.append(Covid19(k[0],k[1],k[2],k[3],k[4],k[5],k[6]))
        
        return list_covids

    def reader_csv(self,name_csv):
        with open(name_csv) as csvfile:
            spamreader = csv.reader(csvfile,delimiter=';',quoting=csv.QUOTE_MINIMAL)
            data_set=[]
            for row in spamreader:
                data_set.append(row)
        
        header = data_set[0]
        data_set_valid = data_set[1:]

        return {"header:" : header, "dataset:" : self.generate_list_models(self.validator_csv(data_set_valid))} 


    # cuidado ao usar esse metodo pois ele apagar todos os arquivos .csv do diretorio setado na configuração do ambiente;
    """
        -> Remove all archives .csv of directory set in envoriment variables; WARNNING
    """
    def drop_all_csv(self):
        try:
            os.chdir(self.path_csv)
            #print(self.path_csv)
            for file in glob.glob('*.csv*'):
                os.remove(file)
            return True
        except Exception as e:
            print(e)
            return False





def get_instance_manipulator():
    return ManipulatorCSV(SETTINGS_PATH_SAVE_ARCH_CSV[0])




    