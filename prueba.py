
datos = []
with open("result116.txt") as fname:
	lineas = fname.readlines()
	for linea in lineas:
		datos.append(linea.strip('\n'))

nombre_final=[]
nom_especiales=[]
for d in datos:
    nombre=''
    pa=''
    sa=''
    #print('dddd',len(d.split()))
    palabras=d.split()
    nom_completo=''
    #print (palabras,len(palabras))
    
    if(len(palabras)==4):
        nombre=palabras[0]+' '+palabras[1]+'|'
        pa=palabras[2]+'|'
        sa=palabras[3]
        nom_completo=nombre+pa+sa
        nombre_final.append(nom_completo)
    elif(len(palabras)==2):
        nombre=palabras[0]+'|'
        pa=palabras[1]
        nom_completo=nombre+pa
        nombre_final.append(nom_completo)
    elif(len(palabras)==3):
        nombre=palabras[0]+'|'
        pa=palabras[1]+'|'
        sa=palabras[2]
        nom_completo=nombre+pa+sa
        nombre_final.append(nom_completo)
    elif(len(palabras)>=5):
        #print("entra")
        tam=len(palabras)
        """ for i in range(0,tam-1):
            if(i==0):
                nombre=palabras[i]
            elif(palabras[i]=='DE'):
                if(pa==''):
                    pa=palabras[i]
                elif(sa==''):
                    sa=palabras[i]
            elif(palabras[i]=='LA'):
                if(pa=='DE'):
                    pa=pa+' '+palabras[i]
                elif(sa=='LA'):
                    sa=sa+' '+palabras[i]
            elif(i==2): """



                    
                    

        nom_especiales.append(d)
    
print(nom_especiales)
salida = "nombres_final1.txt"
with open(salida, "w") as archivo_salida:
    for d in nombre_final:
        archivo_salida.write(d+'\n')

salida = "nombres_extras.txt"
with open(salida, "w") as archivo_salida:
    for d in nom_especiales:
        archivo_salida.write(d+'\n')
    





