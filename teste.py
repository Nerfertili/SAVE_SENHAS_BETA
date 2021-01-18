# NEVEGA POR COMANDO PARA SALVAR SENHAS E OUTRAS FUNÇOES

import os
from builtins import print
import pandas


def create_base_archive():
    archive = open('D:\PycharmProjects\SAVE_SENHAS_BETA\kkk.txt', 'w')
    archive.close()


# Press the green button in the gutter to run the script.

def check_path(path):
    try:
        path_exists = os.path.lexists(path)
        if path_exists == False:
            archive = open(path, "w")
            archive.close()
            print(f'txt file not found ...\ncreating new one at {archive.name}')
            return True
        elif path_exists == True:
            print(f'Txt file found at {os.path.abspath(path)}')
            return True
    except:
        print('error')


class comands:

    def __init__(self, path_txt):
        self.path_txt = path_txt

    '''''
    def creat_file(self):
        archive = open(self.path_txt, "w")
        archive.close()
    '''''

    def add_new_password(self, site, login, senha):
        file_exists = check_path(self.path_txt)
        print(file_exists)
        pass_dataframe = pandas.DataFrame([[site, login, senha]], columns=['site', 'login', 'senha'])

        if file_exists == True:
            try:
                existed_dataframe = pandas.read_csv(self.path_txt, sep=';')
            except:
                existed_dataframe = pandas.DataFrame(columns=['site', 'login', 'senha'])

            existed_dataframe = existed_dataframe.append(pass_dataframe, ignore_index=True)
            writed_archive = open(self.path_txt, 'w')
            writed_archive.write(existed_dataframe.to_csv(sep=';', index=None))
            writed_archive.close()
        else:
            print("file don't exist")

    def delete_password(self, site, login, senha):

        try:
            existed_dataframe = pandas.read_csv(self.path_txt, sep=';')
        except:
            print('No registries detected.')
            return False

        target = existed_dataframe.iloc(site)
        print(target)