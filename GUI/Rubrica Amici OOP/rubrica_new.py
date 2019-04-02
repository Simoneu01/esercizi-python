from appJar import gui
import sys
import time
#sys.path.append("../../")


# OOP
class Rubrica(object):
    def __init__(self, file_contatti, file_categorie):
        self.file_contatti = file_contatti
        self.file_categorie = file_categorie
        self.categorie = gen_list_from_txt(self.file_categorie, ',', 1)
        self.contatti = gen_list_from_txt(self.file_contatti, ',', 1)
        self.rubrica = [Contatto(i) for i in self.contatti]
        self.categorie = [Categoria(i) for i in self.categorie]

    def add_contatto(self, lista):
        self.rubrica.append(Contatto(lista))

    def add_categoria(self, lista):
        self.categorie.append(Categoria(lista))

    def remove_contatto(self, id_contatto):
        self.rubrica.pop(id_contatto)

    def remove_categoria(self, id_categoria):
        self.categorie.pop(id_categoria)

    def save(self):
        with open(self.file_contatti, 'w') as f:
            f.writelines('Nome,Cognome,Numero di telefono,E-mail,Categoria Amico,\n')
            for i in rubrica.rubrica:
                f.writelines(i.get()[0]+','+i.get()[1]+','+i.get()[2]+','+i.get()[3]+','+i.get()[4]+',\n')

        with open(self.file_categorie, 'w') as f:
            f.writelines('Categorie Amici,Descrizione,\n')
            for i in rubrica.categorie:
                f.writelines(i.get()[0]+','+i.get()[1]+',\n')


class Contatto(object):
    def __init__(self, lista):
        self.nome = lista[0]
        self.cognome = lista[1]
        self.telefono = lista[2]
        self.email = lista[3]
        self.categoria = lista[4]

    def modifica(self, lista):
        self.nome = lista[0]
        self.cognome = lista[1]
        self.telefono = lista[2]
        self.email = lista[3]
        self.categoria = lista[4]

    def get(self):
        get_lista = [self.nome, self.cognome, self.telefono, self.email, self.categoria]
        return get_lista


class Categoria(object):
    def __init__(self, lista):
        self.categoria = lista[0]
        self.descrizione = lista[1]

    def modifica(self, lista):
        self.categoria = lista[0]
        self.descrizione = lista[1]

    def get(self):
        return [self.categoria, self.descrizione]


# Programma
def gen_list_from_txt(nome_file, sep=';', header=0, delete_chars='\n'):
    with open(nome_file) as f:
        data = [record.split(sep) for record in f.readlines()[header:]]
        for record in range(len(data)):
            try:
                data[record].remove(delete_chars)
            except:
                pass
        return data


rubrica = Rubrica('amici.txt', 'categorie.txt')
