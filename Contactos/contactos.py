# -*- coding: utf-8 -*-

class Contacto:

    def __init__(self, nombre, tel, email):
        self.nombre = nombre
        self.tel = tel
        self.email = email

class Agenda:

    def __init__(self):
        self._contactos = []

    def agregar(self, nombre, tel, email):
        contacto = Contacto(nombre, tel, email)
        self._contactos.append(contacto)
        #print('nombre: {}, teléfono: {}, Email: {}'.format(nombre, tel, email))

    def mostrar_todos(self):
        for contacto in self._contactos:
            self._imprimir_contacto(contacto)

    def _imprimir_contacto(self, contacto):
        print('___ * ___ * ___ * ___ * ___ * ___ * ___')
        print ('Nombre: {}'.format(contacto.nombre))
        print ('Teléfono: {}'.format(contacto.tel))
        print ('Email: {}'.format(contacto.email))
        print('___ * ___ * ___ * ___ * ___ * ___ * ___')

    def eliminar(self, nombre):
        for idx, contacto in enumerate(self._contactos):
            if contacto.nombre.lower() == nombre.lower():
                del self._contactos[idx]
                break

    def buscar(self, nombre):
        for contacto in self._contactos:
            if contacto.nombre.lower() == nombre.lower():
                self._imprimir_contacto(contacto)
                break
        else:
            self._no_resultados()

    def actualizar(self, nombre):
        for idx, contacto in enumerate(self._contactos):
            if contacto.nombre.lower() == nombre.lower():
                contacto.nombre = str(input('Ingrese un nuevo nombre: '))
                contacto.tel = str(input('Ingrese un nuevo teléfono: '))
                contacto.email = str(input('Ingrese un nuevo correo: '))
                self._contactos[idx] = contacto
                break
        else:
            self._no_resultados()


    def _no_resultados(self):
        print('**********')
        print('No hay contactos con ese nombre')
        print('**********')





def run():

    agenda = Agenda()
    while True:
        comando = str(input('''
        ¿Qué deseas hacer?

        [a] Añadir contacto
        [ac] Actualizar contacto
        [b] Buscar contacto
        [e] Eliminar contacto
        [l] Listar Contactos
        [s] salir
        '''  ))

        if comando == 'a':
            nombre = str(input('Escribe el nombre del contacto: '))
            tel = str(input('Escribe el teléfono del contacto: '))
            email = str(input('Escribe el correo del contacto: '))

            agenda.agregar(nombre, tel, email)

        elif comando == 'b':
            nombre = str(input('Escribe el nombre del contacto que deseas buscar: '))
            agenda.buscar(nombre)

        elif comando == 'ac':
            nombre = str(input('Escribe el nombre del contacto que deseas buscar: '))
            agenda.actualizar(nombre)

        elif comando == 'l':
            agenda.mostrar_todos()

        elif comando == 'e':
            nombre = str(input('Escribe el nombre del contacto que deseas eliminar: '))
            agenda.eliminar(nombre)

        elif comando == 's':
            break



if __name__ == '__main__':
    run()
