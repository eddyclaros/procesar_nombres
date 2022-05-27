""" archivo=open("nombres.txt")
print(archivo) """

import unicodedata

cadena_con_acentos = 'áéíóúasdfwañ'
"""
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn') """

def limpiar_acentos(text):
	acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'Á': 'A', 'E': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
	for acen in acentos:
		if acen in text:
			text = text.replace(acen, acentos[acen])
	return text

#print(limpiar_acentos(cadena_con_acentos))
#exit()

lista_excepciones=['S.R.L.',
                    'S.R.L',
                    'L.T.D.A',
                    'SRL',
                    'S.A.',
                    'S.A',
                    'SOCIEDAD',
                    'EMPRESA',
                    'LIMITADA',
                    'LTDA',
                    'SERVICIOS',
                    'SALESIANA',
                    'GOBIERNO',
                    'MUNICIPAL',
                    'GMBH',
                    'AV.',
                    'AVENIDA',
                    'CONSULTORA',
                    'MOVIMIENTO',
                    'DESARROLLO',
                    'ZONA',
                    'EQUIPETROL',
                    'SRL.',
                    'CONDOMINIO',
                    'CENTRO',
                    '1','2','3','4','5','6','7','8','9','0',
                    'INTERNACIONAL',
                    'HIJAS',
                    'PASTORAL',
                    'MINERA',
                    'VAGONETA',
                    'MOVIMIENTO',
                    'AUTOMOVIL',
                    'CAMIONETA'
                    'JEEP',
                    'MOTOCICLETA',
                    'COOPERATIVA',
                    'PRELATURA',
                    'IGLESIA'

                    ]


print ("+++ 1 ++++")
datos = []
with open("nombres_completo.txt") as fname:
	lineas = fname.readlines()
	for linea in lineas:
		datos.append(linea.strip('\n'))
#print (datos)
print ("+++")

datos2=[]

#quitar acentos y convertir a mayusculas en datos2
for d in datos:
    nombre=limpiar_acentos(d)
    nombre=nombre.upper()
    datos2.append(nombre)
    
#eliminar duplicados
##datos3 = list(set(datos2))  ##desordena la lista
datos3=[]
for item in datos2:
    if item not in datos3:
        datos3.append(item)

#print('datos2->',len(datos2),'datos3->',len(datos3))

""" for d in datos3:
    print('d',d) """

datos4=[]
juridicas=[]
cont=0
for exep in lista_excepciones:
    sw=0
    datos4=[]
    for d in datos3:
        res=d.find(exep)
        if(res==-1):
            sw=1
            datos4.append(d)
        else:
            juridicas.append(d)
    
    
    datos3=[]    
    datos3=datos4.copy()
    #print(datos3)
    """ cont+=1
    if (cont==4):
        print(datos3)
        exit() """
    #print('d4->',len(datos4))
    


juridicas_final=[]
for item in juridicas:
    if item not in juridicas_final:
        juridicas_final.append(item)


salida = "result116.txt"
with open(salida, "w") as archivo_salida:
    for d in datos3:
        archivo_salida.write(d+'\n')
    
salida = "juridicas1.txt"
with open(salida, "w") as archivo_salida:
    for d in juridicas_final:
        archivo_salida.write(d+'\n')






