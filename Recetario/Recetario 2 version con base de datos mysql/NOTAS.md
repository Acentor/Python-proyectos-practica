Sobre objetivos

La busqueda solo aplica a nombre exacto de la receta, la razon fue priorizar otras problematicas, para no tener que generar una nueva ventana de resultados
El creador, genera un archivo ingredientes.json para guardar los datos y poder usarlos en fuera de la clase
El tiempo de coccion, preparacion y fecha, se adjunta al final del texto de la receta(fecha formateada x/x/x)
La unidad de medida, se deja a criterio del usuario, porque en cocina se usan terminos como pizca, a gussto, un poco, e incluso no se especifica, por ejemplo agua, la necesaria
La vista de imagen de la receta se hace a través de un link a un buscador web, que usa el nombre de la receta para no forzar la carga de la imagen al crear la receta




Sobre Funcionamiento

Antes de abrir la venta verifica que exista el archivo recetas.csv, si el archivo no se encuentra lo crea con una lista base, evita errores


Al crear receta
Se hace una comprovacion para evitar nombre de receta repetidos, nombre vacio, ingredientes vacios, preparacion vacia
Al pedir ingredientes, tiempos de coccion y preparacion coloca un valor por defecto

Al leer la lista
El lector permite un scroll para poder visualizar todas las recetas
Al borrar la lista borra el elemento del visor y del archivo de lista, no necesita recargar, no afecta al funcionamiento

Al leer la receta
El lector de recetas limita el tamaño del nombre y lo muestra con un salto, si exede un largo de caracteres, teniendo la ventana espacio para 3 lineas, permite mostrar siempre el nombre
El lector de recetas formatea los ingredientes para ser visto en una columna de pares con un scroll vertical para poder ver todos los ingredientes
El lector de recetas muestra la receta con un scroll y limite de caracteres por linea, asi el texto es legible de modo facil, sin importar su extencion

Al editar 
Se reutiliza el nombre de la receta(no se modifica), permite importar los ingredientes ya usados o modificarlos todos, presenta la preparacion anterior en una caja de texto para poder ser editada
Permite abrir un lector de receta para ver la receta antes de ser editada