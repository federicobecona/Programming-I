class Cuatro_en_linea():
    def __init__(self):
        self.tablero = []
        for filas in range(6):
            self.tablero.append([])
            for espacios_en_filas in range(7):
                self.tablero[filas].append(" ")       
    def posicion_de_ficha(self,columna):
        for filas in range(6):
            if self.tablero[5-filas][int(columna)-1] == " ":
                return 5-filas       
    def movimento_de_fichasX(self,columna):
        self.tablero[self.posicion_de_ficha(columna)][int(columna)-1] = "X" #el -1 se pone porque los índices de la lista comienzan en 0 y los números que ingresa el jugador desde el 1
    def movimento_de_fichasO(self,columna):
        self.tablero[self.posicion_de_ficha(columna)][int(columna)-1] = "O" #el -1 se pone porque los índices de la lista comienzan en 0 y los números que ingresa el jugador desde el 1
    def evaluacion_horizontal(self):
        for filas in self.tablero:
            if "XXXX" in "".join(filas):
                return "finalizador_1"
            if "OOOO" in "".join(filas):
                return "finalizador_2"
    def evaluacion_vertical(self):
        contador_x = 0
        contador_o = 0
        for columna in range(7):
            for fila_inicial in range(3): #filas en las que puede haber cuatro en línea vertical empezando desde arriba
                for fila_final in range(4): #fila en las que los demás se encontrarían
                    if self.tablero[fila_inicial+fila_final][columna]=="X":
                       contador_x += 1
                    if self.tablero[fila_inicial+fila_final][columna]=="O":
                       contador_o += 1                    
                if contador_x == 4:                
                    return "finalizador_1"
                if contador_o == 4:                
                    return "finalizador_2"
                contador_x = 0
                contador_o = 0
    def evaluacion_diagonal(self):
        contador_x = 0
        contador_o = 0
        for fila_inicial in range(3): #posiciones desde las que puede empezar todas las diagonales
            for columna_inicial in range(4): #lugares de las filas desde las que puede empezar todas las diagonales de izquierda a derecha
                for diagonal in range(4):
                    if self.tablero[fila_inicial+diagonal][columna_inicial+diagonal]=="X":
                       contador_x += 1
                    if self.tablero[fila_inicial+diagonal][columna_inicial+diagonal]=="O":
                       contador_o += 1                    
                if contador_x == 4:                
                    return "finalizador_1"
                if contador_o == 4:                
                    return "finalizador_2"
                contador_x = 0
                contador_o = 0
            for columna_inicial in range(3,7): #lugares de las filas desde las que puede empezar todas las diagonales de derecha a izquierda
                for diagonal in range(4):
                    if self.tablero[fila_inicial+diagonal][columna_inicial-diagonal]=="X":
                       contador_x += 1
                    if self.tablero[fila_inicial+diagonal][columna_inicial-diagonal]=="O":
                       contador_o += 1                    
                if contador_x == 4:                
                    return "finalizador_1"
                if contador_o == 4:                
                    return "finalizador_2"
                contador_x = 0
                contador_o = 0
    def empate(self):
        contador_e = 0
        for columnas in range(7):
            for filas in range(6):
                if self.tablero[filas][columnas]!= " ":
                    contador_e += 1
        if contador_e == 42: #cantidad de casillas del tablero
            return "finalizador_E"
    def evaluacion(self):
        if self.evaluacion_horizontal()=="finalizador_1" or self.evaluacion_vertical()=="finalizador_1" or self.evaluacion_diagonal()=="finalizador_1":
            return "gano_1"
        elif self.evaluacion_horizontal()=="finalizador_2" or self.evaluacion_vertical()=="finalizador_2" or self.evaluacion_diagonal()=="finalizador_2":
            return "gano_2"
        elif self.empate()=="finalizador_E":
            return "empate"
    def llena(self,entrada):
        columna = int(entrada)-1
        lista = []
        for fila in range(6):
            lista.append(self.tablero[fila][columna])
        if " " not in lista:
            return "completa"
    def imprimir_tablero(self):
        for fila in self.tablero:
            print(" "*32 + "|"+"|".join(fila)+"|")
    def una_jugada(self,jugador):
        print("-"*79)
        print("Para la opción de problemas o consultas adicionales ingrese la palabra consulta")
        entrada = input("→Ingrese el número " + jugador + " : ")
        return entrada
    def proceso(self,jugador):
        entrada = self.una_jugada(jugador)
        while entrada not in ["1","2","3","4","5","6","7"] or self.llena(entrada)=="completa":
            if entrada.lower()!="consulta":
                print(" "*13 + "Esa columna no está disponible, intente otra vez " + jugador)
                self.imprimir_tablero()
                entrada = self.una_jugada(jugador)
            else:
                print()            
                print("Creador: Federico Becoña, Mail: fmbecona@gmail.com. " + "\n"+ jugador + ", usted puede enviarnos sus dudas a esa casilla de correo electronico.")
                print()
                self.imprimir_tablero()
                entrada = self.una_jugada(jugador)
        if jugador == "Jugador 1":
            self.movimento_de_fichasX(entrada)
        elif jugador == "Jugador 2":
            self.movimento_de_fichasO(entrada)
        evaluador = self.evaluacion()
        self.imprimir_tablero()            
        if evaluador == "gano_1":
            print("-"*83 + "\n"*2 + " "*27 + "¡Ha ganado el jugador 1!" + "\n")
            return "ganador"
        elif evaluador == "gano_2":
            print("-"*83 + "\n"*2 + " "*27 + "¡Ha ganado el jugador 2!" + "\n")
            return "ganador"
        elif evaluador == "empate":
            print("-"*83 + "\n"*2 + " "*33 + "¡Es un empate!" + "\n")
            return "ganador"
def reproducir():
    partida = Cuatro_en_linea()
    print(" "*27 + "¡Bienvenido a 4 en línea!" + "\n" + " "*29 + "Que comience el juego")
    partida.imprimir_tablero()
    para_iterar_jugadas = 0
    while partida.proceso("Jugador 1")!= "ganador" and partida.proceso("Jugador 2") != "ganador":
        para_iterar_jugadas += 1
    return "\n" + " "*28 + "El juego ha finalizado"
print(reproducir())
