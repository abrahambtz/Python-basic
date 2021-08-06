from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'login'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

# routes
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST', 'GET'])
def add_contact():
    if request.method == 'POST':
        action = request.form['action']
        if(action == 'add'):
            fullname = request.form['fullname']
            #phone = request.form['phone']
            email = request.form['email']
            email = hash(email)
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO contacts (usuario, password) VALUES (%s,%s)", (fullname, email))
            mysql.connection.commit()
            flash('Usuario agregado')
        if(action == 'match'):
            fullname = request.form['fullname']
            #phone = request.form['phone']
            email = request.form['email']
            email = hash(email)
            cur = mysql.connection.cursor()
            cur.execute('SELECT password FROM contacts WHERE usuario LIKE  %s', [fullname])
            data = cur.fetchall()
      
            password = "".join(data[0])
            
            if(password == email):
                flash('Usuario y contraseñas validas')
            else:
                flash('Usuario y contraseñas NO validas')
           
        return redirect(url_for('Index'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        #phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts
            SET fullname = %s,
                email = %s,
                phone = %s
            WHERE id = %s
        """, (fullname, email, id))
        flash('Actualizado')
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Se elimino correctamente')
    return redirect(url_for('Index'))



def hash(cadena):
    #cadena = input('Ingresa la cadena: ')
    
    lista_ascii = [ord(i) for i in cadena]
    
    unir_cadena = ''
    for i in range(len(lista_ascii)):
        unir_cadena = unir_cadena + str(lista_ascii[i])
   
    list_pares = []
    longitud_cadena = len(unir_cadena)
    cont = 0
    reducir = longitud_cadena
    while cont < longitud_cadena:
        reducir = reducir - 2
        if(reducir < 0):
            par = unir_cadena[cont]
            list_pares.append(par)
        else:
            par = unir_cadena[cont] + unir_cadena[cont+1]
            list_pares.append(par)    
        cont = cont + 2
    
    for i in range(longitud_cadena-1, -1, -1):
        if(es_primo(i)):
            primo_cercano = i
            break
   
    longitud_lista_pares = len(list_pares) #Conocer el tamaño de la lista
    tabla_modular = [[]] * (primo_cercano ) #Instanciamos nuestra tabla modular
    
    
    for i in range(longitud_lista_pares-1, -1, -1):
        indice =  int(list_pares[i]) % primo_cercano  # Localizamos el indice de acuerdo al modulo/primo
        #listEx.append(longitud_lista_pares[i])
        tabla_modular[indice] = tabla_modular[indice] +[list_pares[i]] # Ingresamos datos en la tabla
    # print('Tabla modular: ', tabla_modular)
    i = 0
    # print('i: ', i)
    # print('Tamaño de la tabla: ', len(tabla_modular))
    while i < len(tabla_modular): #Recorre toda la tabla hasta encontrar listas
        # print('Si: i ' + str(i) + ' < tamaño de la tabla modular' + str(len(tabla_modular)))
        if len(tabla_modular[i])>1: # Si encuentra una lista mayor a 1 realiza lo siguiente:
            # print('Si: tamaño de la tabla modular ' + str(len(tabla_modular[i])) + ' > 1  :  i ' + str(i))
            mover_numero = [tabla_modular[i][-1]] # Obtiene el ultimo numero
            for j in range(len(tabla_modular)): # Busca de nuevo en la tabla una casilla vacia.
                if len(tabla_modular[j])<1 : #Pregunta en cada casilla si es menor a 1
                    # print('Si: tamaño de la tabla modular en J' + str(len(tabla_modular[j])) + ' < 1  : j ' + str(j))
                    tabla_modular[j] = mover_numero # Movemos nuestro numero 
                    # print('Ultimo numero ',tabla_modular[i][:-1])
                    tabla_modular[i].pop(-1)
                    break
                
        else:
            i= i+1
    lista_a_cadena = ''
    for i in range(len(tabla_modular)):
        if len(tabla_modular[i]) > 0: 
            lista_a_cadena =lista_a_cadena + ''.join(str(tabla_modular[i][0]))
    
    #print(lista_a_cadena)
    list_dividida = dividir_en_dos(lista_a_cadena[::-1])
    #print(list_dividida)
    cadena_final = ''
    for x in range(len(list_dividida)):
      cadena_final = cadena_final + hex(int(list_dividida[x])).split('x')[-1]
    return cadena_final

  

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True    
    
def dividir_en_dos(unir_cadena):
  list_pares = []
  longitud_cadena = len(unir_cadena)
  cont = 0
  reducir = longitud_cadena
  while cont < longitud_cadena:
      reducir = reducir - 2
      if(reducir < 0):
          par = unir_cadena[cont]
          list_pares.append(par)
      else:
          par = unir_cadena[cont] + unir_cadena[cont+1]
          list_pares.append(par)    
      cont = cont + 2
  return list_pares



# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
