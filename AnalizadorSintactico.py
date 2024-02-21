parser_table = {
    ('E', 'delete'): ['delete', 'D'],
    ('D', 'from'): ['from', 'I', 'O'],
    ('I', 'alpha'): ['L', 'R'],
    ('L', 'alpha'): ['alpha'],
    ('R', 'alpha'): ['L', 'R'],
    ('R', 'where'): ['epsilon'],
    ('R', "'"): ['epsilon'],
    ('R', '$'): ['epsilon'],
    ('R', '='): ['epsilon'],
    ('O', 'where'): ['where', 'C'],
    ('O', '$'): ['epsilon'],
    ('C', 'alpha'): ['I', '=', 'V'],
    ('V', 'digit'): ['D', 'RE'],
    ('V', "'"): ["'", 'I', "'"],
    ('RE', 'digit'): ['D', 'RE'],
    ('RE', '$'): ['epsilon'],
    ('D', 'digit'): ['digit']
}

terminales = set([clave[1] for clave in parser_table.keys()])
palabras_reservadas = ['delete', 'from', 'where']

def organizador(palabras):
    simbolos = []
    for palabra in palabras:
        if palabra in palabras_reservadas:
            simbolos.append(palabra)
        else:
            for letra in palabra:
                if letra.isalpha():
                    simbolos.append('alpha')
                elif letra.isdigit():
                    simbolos.append('digit')
                else:
                    simbolos.append(letra)
    return simbolos

def analizador_sintactico(entrada):
    stack = ['$', 'E']
    text = str(stack) + '\n'
    entrada = entrada.strip() + ' $'
    palabras = entrada.split(' ')
    simbolos = organizador(palabras)
    index = 0
    while True:
        X = stack.pop()
        a = simbolos[index]
        if X in terminales:
            if X == a:
                index += 1    
                text += str(stack) + '\n'
                if X == '$':
                    return text
            else:
                return text + '\nError de sintaxis'
        else:
            if (X, a) in parser_table:
                producciones = parser_table[(X, a)]
                if producciones != ['epsilon']:
                    for produccion in reversed(producciones):
                        stack.append(produccion)
                text += str(stack) + '\n'
            else:
                return text + '\nError de sintaxis'
            
    
        