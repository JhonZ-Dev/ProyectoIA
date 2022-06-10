def RobotRecolector():
    # El robot completa el objetivo si todos los lotes estan regados
    estadoObjetivo = {'A': '0', 'B':  '0', 'C': '0', 'D': '0', 'E': '0', 'F': '0','G': '0'}
    # Inicializmos una variable para el costo.
    costo = 0
    #Imprimimos un mensaje para decirle al usuario de como van a estar dinidos las hectareas
    print(""" 
    *****Estimado usuario, existen siete ubicaciones (Hectareas de plantación)*******
         |-------------------------*****Hectarea_1 = 'A'*****-------------------------|
         |-------------------------*****Hectarea_2 = 'B'*****-------------------------|
         |-------------------------*****Hectarea_3 = 'C'*****-------------------------|
         |-------------------------*****Hectarea_4 = 'D'*****-------------------------|
         |-------------------------*****Hectarea_5 = 'E'*****-------------------------|
         |-------------------------*****Hectarea_6 = 'F'*****-------------------------|
         |-------------------------*****Hectarea_7 = 'G'*****-------------------------|
         |-------------------------*****Hectarea_8 = 'H'*****-------------------------|
    """)
    print("Digite la ubicación del robot") #El usuario digita la ubicación del robot
    ubicacionRobot= input("") #Leeremos lo que el usuario digita
    if ubicacionRobot =='A': #Entonces usamos condicionales para ver el estado que digita el usuarui
        print("El robot se encuentra en la Hectarea_1")
        #Procedemos a preguntar el estado de las demás hectareas, esto con el objetivo
        #que si todos los demás lotes ya fueron recolectados, procedemos a marcar el estado objetivo
        #como completado.
        Hectarea_1 = input("Digite el estado de la hectarea_1")
        Hectarea_2 = input("Digite el estado de la hectarea_2")
        Hectarea_3 = input("Digite el estado de la hectarea_3")
        Hectarea_4 = input("Digite el estado de la hectarea_4")
        Hectarea_5 = input("Digite el estado de la hectarea_5")
        Hectarea_6 = input("Digite el estado de la hectarea_6")
        Hectarea_7 = input("Digite el estado de la hectarea_7")
        