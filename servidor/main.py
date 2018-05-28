# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request
from modelo_contacto import Contacto
app = Flask(__name__)

@app.route(r'/', methods = ['GET'])
def contact_book():
    return render_template("contact_book.html")
 
@app.route(r'/add', methods = ['GET', 'POST'])    
def add_contact():
    if request.form:
        contacto = Contacto(nombre=request.form.get('nombre'), tel=request.form.get('tel'), email=request.form.get('email'))
        #print(request.form.get('nombre'))
        #print(request.form.get('tel'))#Lo que va dentro del parentesis es el atributo "name" del objeto
        #print(request.form.get('correo'))
        contacto.put() 
        
    return render_template('add_contact.html')
    
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
