# NEVEGA POR COMANDO PARA SALVAR SENHAS E OUTRAS FUNÇOES

import os
from builtins import print
import pandas


def create_base_archive():
    archive = open('D:\PycharmProjects\SAVE_SENHAS_BETA\kkk.txt','w')
    archive.close()
# Press the green button in the gutter to run the script.

def check_path(path):
    try:
        path_exists = os.path.lexists(path)
        if path_exists == False:
            archive = open(path,"w")
            archive.close()
            print(f'txt file not found ...\ncreating new one at {archive.name}')
            return True
        elif path_exists == True :
            print(f'Txt file found at {os.path.abspath(path)}')
            return True
    except:
        print('error')

class comands:

    def __init__(self,path_txt):
        self.path_txt = path_txt
    '''''
    def creat_file(self):
        archive = open(self.path_txt, "w")
        archive.close()
    '''''

    def add_new_password(self, site, login, senha):
        file_exists = check_path(self.path_txt)
        print(file_exists)
        pass_dataframe = pandas.DataFrame([[site,login,senha]],columns=['site','login','senha'])


        if file_exists == True:
            try:
                existed_dataframe = pandas.read_csv(self.path_txt,sep=';')
            except:
                existed_dataframe = pandas.DataFrame(columns=['site','login','senha'])

            existed_dataframe = existed_dataframe.append(pass_dataframe,ignore_index=True)
            writed_archive = open(self.path_txt,'w')
            writed_archive.write(existed_dataframe.to_csv(sep=';',index = None))
            writed_archive.close()
        else:
            print("file don't exist")

    def delete_password(self,site=None,login=None,senha=None):

        try:
            existed_dataframe = pandas.read_csv(self.path_txt,sep=';',header=0)
        except:
            print('No registries detected.')
            return False
        for index in existed_dataframe.index:
            if existed_dataframe.loc[index,'site'] == site:
                changed_dataframe = existed_dataframe.drop(index)
        archive = open(self.path_txt,'w')
        archive.write(changed_dataframe.to_csv(sep=';',index=None))
        archive.close()

    def change_dados(self,site=None,login=None,senha=None):

        try:
            existed_dataframe = pandas.read_csv(self.path_txt,sep=';')
        except:
            print('No registries detected.')
            return False
        for index in existed_dataframe.index:
            if existed_dataframe.loc[index,'site'] == site:
                existed_dataframe.loc[index,'login'] = 'changed login'

        archive = open(self.path_txt, 'w')
        archive.write(existed_dataframe.to_csv(sep=';', index=None))
        archive.close()





'''
path = self.path_txt
data_frame = pandas.DataFrame([['teste','gabriel','senha']],columns=['site','login','senha'])
write_data = open(path,'w')
write_data.write(data_frame.to_csv(sep=';',index=None))
write_data.close()
 print(data_frame)
'''

if __name__ == '__main__':
    Path = comands('D:\PycharmProjects\SAVE_SENHAS_BETA\senhas.txt')
    #Path.add_new_password('teste','RPGTroll3','gfonso33')
    #Path.delete_password(site='teste')
    Path.change_dados(site='teste')
    print('fim')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
