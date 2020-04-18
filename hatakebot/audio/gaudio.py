from gtts import gTTS
from .settings.config_variables import SETTINGS_PATH_SAVE_ARCH_CSV
import os
from os import path
import pygame
import glob



# inicializando o modulo pygame
pygame.init()


commands_result = {
    "drop": "tabela deletada com sucesso",
    "drop_csv": "Arquivos csv deletados com sucesso",
    "create": "tabela criada com sucesso",
    "download": "download csv efetuado com sucesso",
    "insert": "dados inseridos no banco de dados com sucesso",
    "fail_csv": "não foi possivel encontrar nenhum csv no diretorio.",
    "bot_schedule": "bot programado para execução com cronograma. Para parar a execução finalize o processo!",
    "htk_bot": "Olá, procurando informações sobre covid19.",
    "fim": "fim de execução."
}

FOLDER_AUDIO= "audios/"

class PlayAudio(object):
    def __init__(self,path_save):
        self.path_save=path_save
    
    def check_dir(self):
        directory = self.path_save+FOLDER_AUDIO
        if path.exists(directory):
            return True
        return False

    @staticmethod
    def folder_audio():
        print(FOLDER_AUDIO)
        
    def create_audio(self,command_result):
        pygame.init()
        
        if self.check_dir():
            os.chdir(self.path_save+FOLDER_AUDIO)
            text_correspondente = commands_result.get(command_result)
            tts = gTTS(text_correspondente, lang='pt')
            tts.save(text_correspondente+".mp3")
            return True
        else:
            os.chdir(self.path_save)
            os.mkdir(FOLDER_AUDIO)
            self.create_audio(command_result)

    
    def play(self,command_result):
        try:
            pygame.init()
            
            os.chdir(self.path_save+FOLDER_AUDIO)
            text_correspondente = commands_result.get(command_result)
            path_completo = self.path_save+FOLDER_AUDIO+text_correspondente+".mp3"
            pygame.mixer.music.load(path_completo)
            pygame.mixer.music.play()

            #volume
            pygame.mixer.music.set_volume(1)

            #clock
            clock = pygame.time.Clock()
            clock.tick(10)

            while pygame.mixer.music.get_busy():
                pygame.event.poll()
                clock.tick(10)
            return True
        except Exception as e:
            print(e)
            return False


    def delete_audios(self):
        try:
            os.chdir(self.path_save+FOLDER_AUDIO)
            for file in glob.glob('*.mp3*'):
                os.remove(file)
            
            return True
        except Exception as e:
            print(e)
            return False
        
    


def get_instance_audio():
    return PlayAudio(SETTINGS_PATH_SAVE_ARCH_CSV[0])
    




