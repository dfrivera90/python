from google.appengine.ext import nbd

class Contacto(nbd.Model):
    nombre = nbd.StringProperty()
    tel = nbd.StringProperty()
    email = nbd.StringProperty()
    