print("Bienvenido este es un script para hallar el limite maximo tolerable")

while True:
    try:
        print("1. Particulas Inhalables 100 micrometros")
        print("2. Particulas Torácica 25 micrometros")
        print("3. Particulas Respirables 10 micrometros")
        print("4. Limite de tolerancia")
        print("5. Verificador de Caudal")
        print("6. Salir")
        a = int(input("Digite una opción: "))
        
        if a == 1:
            h = float(input("Digite el número de horas que trabaja el usuario: "))
            m = float(input("Digite el número de minutos que trabaja el usuario: "))
            t = float(input("Digite el Valor Limite Tolerable(TLV-TWA): "))
            n = float(input("Digite el número de días que trabaja el usuario: "))
            q = float(input("NIOSH 0500: Digite el flujo de succión: "))
            v = float(input("NIOSH 0500: Digite el Volumen: "))
            m1 = (m*1)/60   #minutos pasados a horas
            ht = m1+h       #horas totales al día
            hs = ht*n       #horas totales a la semana 

            df = round(ht/((v/q)/60)) #Tiempo de duración del filtro
            l = []
            for i in range(df):
                mo = float(input(f"{i+1}. Masa Inicial: "))
                mf = float(input(f"{i+1}. Masa Final: "))
                cn = (mf-mo)/v
                l.append(cn)
            twa = round(sum(l)*10**6/df,2)
            print(f"TWA = {twa} mg/m3")
                
            fcd = (8/ht)*((24-ht)/16)
            fcs = (40/hs)*((168-hs)/128)
            tlvd = t * fcd
            tlvs = t * fcs
            print(f"TLVdiario = {round(tlvd,2)} \nTLVsemanal = {round(tlvs,2)}")
            print("\n")
            print("¿Quiere calcular los Limites de Confianza: IRAM 80021?")
            b = int(input("Oprima 1 si quiere calcular y 2 si no: "))
            if b == 1:
                k = float(input("Nivel de confianza: "))
                cv = 0.05
                s = cv * twa
                LCi = twa - k*s 
                LCs = twa + k*s
                if LCs <= t:
                    print(f"{LCs} CUMPLE")
                else:
                    print(f"{LCs} NO CUMPLE")
            elif b == 2:
                break
        elif a == 2:
            print("Hola, todavia estamos en proceso")
            print("\n")
        elif a == 3:
            h = float(input("Digite el número de horas que trabaja el usuario: "))
            m = float(input("Digite el número de minutos que trabaja el usuario: "))
            t = float(input("Digite el Valor Limite Tolerable(TLV-TWA): "))
            n = float(input("Digite el número de días que trabaja el usuario: "))
            q = float(input("NIOSH 0600: Digite el flujo de succión: "))
            v = float(input("NIOSH 0600: Digite el Volumen: "))
            m1 = (m*1)/60   #minutos pasados a horas
            ht = m1+h       #horas totales al día
            hs = ht*n       #horas totales a la semana 

            df = round(ht/((v/q)/60)) #Tiempo de duración del filtro
            l = []
            for i in range(df):
                mo = float(input(f"{i+1}. Masa Inicial: "))
                mf = float(input(f"{i+1}. Masa Final: "))
                cn = (mf-mo)/v
                l.append(cn)
            twa = round(sum(l)*10**6/df,2)
            print(f"TWA = {twa} mg/m3")
                
            fcd = (8/ht)*((24-ht)/16)
            fcs = (40/hs)*((168-hs)/128)
            tlvd = t * fcd
            tlvs = t * fcs
            print(f"TLVdiario = {round(tlvd,2)} \nTLVsemanal = {round(tlvs,2)}")
            print("\n")
            print("¿Quiere calcular los Limites de Confianza: IRAM 80021?")
            b = int(input("Oprima 1 si quiere calcular y 2 si no: "))
            if b == 1:
                k = float(input("Nivel de confianza: "))
                cv = 0.045
                s = cv * twa
                LCi = twa - k*s 
                LCs = twa + k*s
                if LCs <= t:
                    print(f"{LCs} CUMPLE")
                else:
                    print(f"{LCs} NO CUMPLE")
            elif b == 2:
                break
        elif a == 4:
            n = int(input("Digite el número de agentes quimicos: "))
            l = []
            for i in range(n):
                m = float(input(f"{i+1}. Medido: "))
                t = float(input(f"{i+1}. TLV: "))
                d = m/t
                l.append(d)
            if sum(l) < 1:
                print(sum(l), "Cumple con el Limite Tolerable")
            else:
                print(sum(l), "No cumple con el Limite Tolerable")
            print("\n")
        elif a == 5:
            n = 10
            la = []
            lf = []
            for i in range(n):
                m = float(input(f"{i+1}. Antes: "))
                la.append(m)
            for j in range(n):    
                t = float(input(f"{j+1}. Despues: "))
                lf.append(t)
            qpa = sum(la)/n
            qpd = sum(lf)/n
            if (qpa - qpd) < 0.05:
                print(f"{qpa} - {qpd} es aceptable")
            else:
                print("No es aceptable")
            print("\n")
        elif a == 6:
            print("Fue un gusto ayudarte")
            break
            
    except:
        print("No has introducido algun argumento")
        print("Tienes que introducir un número del 1 al 6")
