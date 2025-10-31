# variables 

my_variable= "my string variable"
print(my_variable)

my_int_variable= 5
print(my_int_variable)

my_variable_1=str(my_int_variable)

print(my_int_variable,my_variable) 
#separados por una coma 
# me preinterpreta para corregir errores 

print(type(my_variable_1))



#esto de aca abajop se llama 
#concatenacion de variables en print
print(my_variable_1,my_int_variable,my_variable)


""""
print(len(my_variable))

#en el caso que vimos arriba la funcion del sistema len no cuenta la cantidad de caracteres que tiene esa variable 

minutos_del_video_en_el_que_vamos=("1:11:04") 

print(minutos_del_video_en_el_que_vamos)

#variables en una sola linea 
name,surname,alias,age= ("cristian", "marcado", "escannor", 28)
print("minombre es:", name, surname,"mi edad es:", age,"mi alias es:", alias)

#ojo no abusar de la sintaxis de arriba
#puede complicar el codigo
"""
 
#uso de inputs
first_name= input('¡cual es tu nombre?')
age= input('¿que edad tienes ?')

print(first_name)
print(age)