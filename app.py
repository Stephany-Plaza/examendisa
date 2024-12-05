from flask import Flask, render_template
import random

app = Flask(__name__)

# Lista de preguntas organizadas por tipo
preguntas = {
    "opcion_multiple": [
        #PREGUNTAS FLOWER
        {"pregunta": "¿Cuántos años de experiencia tiene Dulces Flower en el mercado colombiano??", "opciones": ["A) 47", "B) 80", "C) 65", "D) 30"], "respuesta": "A"},
        {"pregunta": "En cuantos paises esta presente dulces flower? Y cuales son?", "opciones": ["A) 3 paises: Nicaragua, Venezuela, Ecuador", "B) 2 paises:Venezuela y Colombia", "C) 3 paises: Venezuela, Colombia y Panama"], "respuesta": "C"},
        {"pregunta": "¿Cuál es el lema fundamental de Dulces Flower?", "opciones": ["A)Buen precio ", "B) Calidad", "C) empresa familiar", "D) Calidad Total"], "respuesta": "D"},
        {"pregunta": "¿Cuál es el tiempo de vida útil de la mermelada de guayaba?", "opciones": ["A) 6 meses", "B) 2 meses", "C) 11 meses", "D) 12 meses"], "respuesta": "A"},
        {"pregunta": "¿Qué producto de Flower se puede utilizar como acabado final en helados?", "opciones": ["A) Gel de brillo", "B)Leche condensada ", "C) Sirope de fresa"], "respuesta": "B"},
        {"pregunta": "¿Cuál es la presentación del coco deshidratado?", "opciones": ["A) Bolsa 1 kg y 3kg", "B) Bolsa 2.5kg y 4 Kg", "C) Bolsa 1 kg y 5 kg", "D) Ninguna de las anteriores"], "respuesta": "C"},
        {"pregunta": "¿Qué tipo de presentación tiene la crema de coco?", "opciones": ["A) Bolsa Flex Up de 400 g", "B) Bolsa Flex Up de 200 g", "C) Bolsa Flex Up de 250 g", "D) Bolsa Flex Up de 120 g"], "respuesta": "A"},
        #PREGUNTAS MARCONA
        {"pregunta": "¿En qué año se fundó Chocolates La Marcona?", "opciones": ["A) 1890", "B) 1968", "C) 1999"], "respuesta": "B"},
        {"pregunta": "¿Cuál es la procedencia de la familia fundadora de Chocolates La Marcona?", "opciones": ["A) Colombia", "B) Portugal", "C) España", "D) Brasil"], "respuesta": "C"},
        {"pregunta": "¿De donde proviene el cacao utilizado por chocolates la marcona para la elaboracion de sus productos?", "opciones": ["A) Venezuela", "B) Holanda", "C) Colombia", "D) Brasil"], "respuesta": "A"},
        {"pregunta": "¿La empresa Chocolates La Marcona se especializa en la combinación de sabores de qué dos tierras?", "opciones": ["A) Venezuela y Colombia", "B) España y Venezuela", "C) España y Colombia"], "respuesta": "B"},
        #PREGUNTAS MASTERT TOP
        {"pregunta": "¿Cómo se recomienda batir la Crema Tipo Chantilly de Master Top para obtener los mejores resultados?", "opciones": ["A) Dejar enfriar el producto por 12/16 horas y batir entre 9 a 15°C", "B) Dejar enfriar el producto por 15 horas y batir entre 1 a 5°C", "C)Dejar enfriar el producto por 12/24 horas y batir entre 3 a 7°C ", "D) Dejar enfriar el producto por 8 horas y batir entre 2 a 9°C"], "respuesta": "C"},
        {"pregunta": "¿Puede utilizarse el Jarabe sabor Tres Leches con licores?", "opciones": ["A) SI", "B) NO"], "respuesta": "A"},
         #PREGUNTAS ACONCAGUA
        #{"pregunta": "¿Que presentaciones tiene Disa disponible del melocoton aconcagua?", "opciones": ["A) ", "B) ", "C) "], "respuesta": "B"},
        #PREGUNTAS FULLER
        {"pregunta": "¿En qué presentación viene Fuller Gel Antibacterial para manos?", "opciones": ["A) Galon 2.75 LT", "B) 1.528 LT", "C) Galon 3.785 LT", "D) 4.589 LT"], "respuesta": "C"},
        {"pregunta": "¿Cual es el producto ideal para limpieza de vidrios?", "opciones": ["A) Fullguard", "B) Limpia Vidrios Profesional", "C) Fulsol"], "respuesta": "B"},
    ],
    "desarrollo": [
        #PREGUNTAS FLOWER
        {"pregunta": "¿Para que se utiliza el arequipe de decoracion?"},
        {"pregunta": "¿Qué diferencia hay entre el arequipe de decoración y el arequipe de relleno?"},
        {"pregunta": "¿Cuánto tiempo de vida útil tiene el arequipe de decoración?"},
        {"pregunta": "¿Cuál es la presentación del arequipe de decoración Premium?"},
        {"pregunta": "¿Qué tipo de arequipe es ideal para ser horneado?"},
        {"pregunta": "¿Para qué se recomienda la mermelada de guayaba?"},
        {"pregunta": "¿Qué usos tiene la azúcar pulverizada en la panadería?"},
        {"pregunta": "¿Por qué no se puede usar el arequipe de decoración en productos horneados?"},
        {"pregunta": "¿Qué diferencia hay entre el arequipe de decoración y el arequipe de decoración el corral?"},
        {"pregunta": "¿Por qué es importante mencionar que los productos son ideales para altas temperaturas?"},
        {"pregunta": "¿Cuál es la función principal de la azúcar pulverizada en productos de pastelería?"},
        {"pregunta": "¿Cuáles son los usos del coco deshidratado?"},
        #PREGUNTAS MARCONA
        {"pregunta": "¿Cual es la diferencia entre chocolate bitter y chocolate bitter?"},
        {"pregunta": "¿cual es el argumento de los clientes donde no has logrado posicionar chocolates la marcona? que les dices?"},
         #PREGUNTAS MASTERTOP
        {"pregunta": "¿Cuál es la especialidad de la marca Master Top?"},
        {"pregunta": "¿Master Top es una marca local o internacional?"},
        {"pregunta": "¿Qué tipo de recetas pueden ser potenciadas con los productos Master Top?"},
        {"pregunta": "¿Cuál es un beneficio clave de usar el Jarabe sabor Tres Leches de Master Top?"},
        {"pregunta": "¿Para qué se puede utilizar la Crema para Cocina de Master Top?"},
        {"pregunta": "¿Cuál es la importancia de mantener la cadena de frío en productos como la Chantilly?"},
        {"pregunta": "¿Qué se recomienda hacer antes de usar la Crema para Cocina?"},
        {"pregunta": "¿Por qué la Crema para Cocina de Master Top es ideal para gratinados?"},
        {"pregunta": "¿Puede usarse la Crema para Cocina en platos dulces?"},
        {"pregunta": "¿Cómo debe ser el recipiente para la Crema Tipo Chantilly durante la preparación?"},
        {"pregunta": "¿Cuál es el efecto del almacenamiento incorrecto de la Chantilly?"},
        {"pregunta": "¿cual es el argumento de los clientes donde no has logrado posicionar las bebidas greenstar? que les dices?"},
        #PREGUNTAS ACONCAGUA
        {"pregunta": "¿Cómo se presenta el melocotón ACONCAGUA dentro del envase?"},
        {"pregunta": "¿En qué líquido se conserva el melocotón?"},
        {"pregunta": "¿Cómo crees que se diferencia Aconcagua de otras marcas de conservas de fruta?"},
        {"pregunta": "¿A que tipo de cliente le recomendarias el melocoton aconcagua?"},
        {"pregunta": "¿Cuánto es el peso escurrido de Melocotón En Almibar Aconcagua 820gr y 3kg?"},
        {"pregunta": "¿cual es el argumento de los clientes donde no has logrado posicionar el melocoton aconcagua? que les dices?"},
        #PREGUNTAS FULLER
        {"pregunta": "¿Cuál es el producto de Fuller que se utiliza para Limpiar Quirofanos?"},
        {"pregunta": "¿Como se llama el producto para limpiar vidrios de fuller?"},
        {"pregunta": "¿Menciona 3 productos fuller que puedan disolverse con agua? y para que se utilizan?"},
        {"pregunta": "¿Menciona 3 productos fuller que se deban utilizar concentrados, es decir, sin disolverse y para que se utilizan?"},

    ]
}

# Función para generar el examen
def generar_examen(num_preguntas, num_opcion_multiple, num_desarrollo):
    examen = []
    
    # Seleccionar preguntas de opción múltiple
    opcion_multiple_seleccionadas = random.sample(preguntas["opcion_multiple"], num_opcion_multiple)
    examen.extend(opcion_multiple_seleccionadas)
    
    # Seleccionar preguntas de desarrollo
    desarrollo_seleccionadas = random.sample(preguntas["desarrollo"], num_desarrollo)
    examen.extend(desarrollo_seleccionadas)
    
    # Barajar las preguntas seleccionadas
    random.shuffle(examen)
    
    return examen

@app.route('/')
def mostrar_examen():
    # Definir cuántas preguntas de cada tipo queremos
    num_preguntas = 20
    num_opcion_multiple = 15
    num_desarrollo = 5
    
    examen = generar_examen(num_preguntas, num_opcion_multiple, num_desarrollo)
    
    # Pasar el examen generado a la plantilla HTML
    return render_template('index.html', examen=examen)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
