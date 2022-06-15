from jurassic_park import dinosaurs
from lista import Lista
from cola import Cola
class Alert:
    def __init__(self, hora, zona, numero_dinosaurio, nivel_alerta, nombre):
        self.hora = hora
        self.zona = zona
        self.numero_dinosaurio = numero_dinosaurio
        self.nivel_alerta = nivel_alerta
        self.nombre= nombre

    def __str__(self):
        return f"{self.hora} | {self.zona} | {self.numero_dinosaurio} | {self.nivel_alerta} | {self.nombre}"

def busqueda(buscado):
    for dino in dinosaurs:
        if(int(buscado) == dino['number']):
            return dino['name']
lista_alerta=Lista()
lista_alerta2=Lista()

file = open('alerts.txt')

lineas = file.readlines()
lineas.pop(0)
lista_alerta=Lista()
for linea in lineas:
    dato = linea.split(';')
    dato[3] = dato[3][:-1]
    dato.append(busqueda(dato[2]))
    lista_alerta.insertar(Alert(dato[0],
                             dato[1],
                             dato[2],
                             dato[3],
                             dato[4]),
                        campo='hora')
    lista_alerta2.insertar(Alert(dato[0],
                             dato[1],
                             dato[2],
                             dato[3],
                             dato[4]),
                        campo='nombre')

aux=0
for dinosaurio in dinosaurs:
    aux2=int(dinosaurio['named_by'][-4:])
    if aux2 > aux:
        aux=int(dinosaurio['named_by'][-4:])
for dinosaurio in dinosaurs:
    if dinosaurio['named_by'][-4:]== str(aux):
        print(f"El ultimo dinosaurio en ser descubierto fue: {dinosaurio['name']} y lo hizo: {dinosaurio['named_by'][:-6]}")
print()

print('Listado ordenado por hora: ')   
lista_alerta.barrido()
print()

print('Listado ordenado por dinosaurio: ')
lista_alerta2.barrido()
print()
# Dr. Wu
pos=lista_alerta.busqueda('WYG075', 'zona')
lista_alerta.eliminar(pos.info)
pos=lista_alerta.busqueda('SXH966', 'zona')
lista_alerta.eliminar(pos.info)
pos=lista_alerta.busqueda('LYF010', 'zona')
lista_alerta.eliminar(pos.info)
pos=lista_alerta.busqueda('HYD195', 'zona')
pos.info.nombre='Mosasaurus'

pos=lista_alerta2.busqueda('WYG075', 'zona')
lista_alerta2.eliminar(pos.info)
pos=lista_alerta2.busqueda('SXH966', 'zona')
lista_alerta2.eliminar(pos.info)
pos=lista_alerta2.busqueda('LYF010', 'zona')
lista_alerta2.eliminar(pos.info)
pos=lista_alerta2.busqueda('HYD195', 'zona')
pos.info.nombre='Mosasaurus'

print('Listado de los dinosaurios: Tyrannosaurus Rex, Spinosaurus, Giganotosaurus con nivel critical o high: ')
lista_alerta.barrido_simon_masrani()
print()

cola_carnivoros=Cola()
cola_herbivoros=Cola()
for linea in lineas:
    dato = linea.split(';')
    dato[3] = dato[3][:-1]
    dato.append(busqueda(dato[2]))
    if dato[3] != 'low' and dato[3] != 'medium':
        aux=dato[4]
        for dinosaurio in dinosaurs:
            if aux==dinosaurio['name'] and dinosaurio['type']=='carnívoro ':
                cola_carnivoros.arribo(Alert(dato[0],
                                        dato[1],
                                        dato[2],
                                        dato[3],
                                        dato[4]))
            else:
                if aux==dinosaurio['name'] and dinosaurio['type']=='herbívoro ':
                    cola_herbivoros.arribo(Alert(dato[0],
                                            dato[1],
                                            dato[2],
                                            dato[3],
                                            dato[4]))
print('Carníboros exceptuando los de nivel low o medium y los provenientes de la zona EPC944: ')
while not cola_carnivoros.cola_vacia():
    dato=cola_carnivoros.atencion()
    if dato.zona!= 'EPC944':
        print(dato)
print()

#print('Herbívoros: ')
#while not cola_herbivoros.cola_vacia():
#    dato=cola_herbivoros.atencion()
#    print(dato)

print('Listado de los dinosaurios dinosaurios Raptors y Carnotaurus y los códigos de las zonas donde puedo encontrar Compsognathus: ')
lista_alerta.barrido_owen_grady()
print()

palabra='mosquito'
vec=[]
for i in range(len(palabra)):
    aux= ord(palabra[i])
    vec.append(aux)

indice=0
def obtener_clave(vector, ind):
    if ind==len(vector):
        return print(vector) 
    elif vector[ind] % 3 == 0:
        vector[ind]=(vector[ind]//2) + 9
    else:
        vector[ind]=vector[ind] - 14
    if 33 <= vector[ind] <= 47:
        obtener_clave(vector, ind+1)
    else:
        obtener_clave(vector, ind)
print(f'La clave es: {obtener_clave(vec, indice)}')