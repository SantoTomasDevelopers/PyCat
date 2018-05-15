from Eventos import EventoTablero
import numpy as np

ET       = EventoTablero()
Mesa     = [[0,0,0],[0,0,0],[0,0,0]]
Mesa     = np.array(Mesa)
MesaSize = Mesa.shape
Jugadas  = 0
Turno    = 1
TurnoAnterior = [0]

class main:
    def __init__(self):
        self.VarUno   = 0

    def Tablero( Evento, Jugada):
        global Jugadas
        global Turno
        cordenada = [['A1','A2','A3'],['B1','B2','B3'],['C1','C2','C3']]
        if(Evento == ET.Casa):
            print('|x|A|B|C|')
            print('|1|-|-|-|')
            print('|2|-|-|-|')
            print('|3|-|-|-|')
        elif(Evento == ET.JugadorUno or Evento == ET.JugadorDos):
            #print('----------Turno de: '+str(Turno)+'----------------')
            print('----------Jugada: '+str(Jugada)+'------------------')
            # if(Turno == 1):
            #     Turno = 2
            # else:
            #     Turno = 1
            if 'A' in Jugada:
                if '1' in Jugada:
                    if(Mesa[0][0]==0):
                        if(Evento == ET.JugadorUno):
                            Mesa[0][0]=1
                            Turno = 2
                        else:
                            Mesa[0][0]=2
                            Turno = 1
                    else:
                        print('Jugada invalida')
                        Turno = 3
                if '2' in Jugada:
                    if(Mesa[0][1]==0):
                        if(Evento == ET.JugadorUno):
                            Mesa[0][1]=1
                            Turno = 2
                        else:
                            Mesa[0][1]=2
                            Turno = 1
                    else:
                        print('Jugada invalida')
                        Turno = 3
                if '3' in Jugada:
                    if(Mesa[0][2]==0):
                        if(Evento == ET.JugadorUno):
                            Mesa[0][2]=1
                            Turno = 2
                        else:
                            Mesa[0][2]=2
                            Turno = 1
                    else:
                        print('Jugada invalida')
                        Turno = 3
            if 'B' in Jugada:
                if '1' in Jugada:
                    if(Mesa[1][0]==0):
                        if(Evento == ET.JugadorUno):
                            Mesa[1][0]=1
                            Turno = 2
                        else:
                            Mesa[1][0]=2
                            Turno = 1
                    else:
                        print('Jugada invalida')
                        Turno = 3
                if '2' in Jugada:
                    if(Mesa[1][1]==0):
                        if(Evento == ET.JugadorUno):
                            Mesa[1][1]=1
                            Turno = 2
                        else:
                            Mesa[1][1]=2
                            Turno = 1
                    else:
                        print('Jugada invalida')
                        Turno = 3
                if '3' in Jugada:
                    if(Mesa[1][2]==0):
                        if(Evento == ET.JugadorUno):
                            Mesa[1][2]=1
                            Turno = 2
                        else:
                            Mesa[1][2]=2
                            Turno = 1
                    else:
                        print('Jugada invalida')
                        Turno = 3
            if 'C' in Jugada:
                if '1' in Jugada:
                    if(Mesa[2][0]==0):
                        if(Evento == ET.JugadorUno):
                            Mesa[2][0]=1
                            Turno = 2
                        else:
                            Mesa[2][0]=2
                            Turno = 1
                    else:
                        print('Jugada invalida')
                        Turno = 3
                if '2' in Jugada:
                    if(Mesa[2][1]==0):
                        if(Evento == ET.JugadorUno):
                            Mesa[2][1]=1
                            Turno = 2
                        else:
                            Mesa[2][1]=2
                            Turno = 1
                    else:
                        print('Jugada invalida')
                        Turno = 3
                if '3' in Jugada:
                    if(Mesa[2][2]==0):
                        if(Evento == ET.JugadorUno):
                            Mesa[2][2]=1
                            Turno = 2
                        else:
                            Mesa[2][2]=2
                            Turno = 1
                    else:
                        print('Jugada invalida')
                        Turno = 3


        Jugadas = Jugadas + 1
        main.DiseñarTablero()
    
    def DiseñarTablero():
        
        
        print('----------Numero de jugadas: '+str(Jugadas)+'---------')
        print('|x|A|B|C|')        
        print('|1|'+str(Mesa[0][0])+'|'+str(Mesa[0][1])+'|'+str(Mesa[0][2])+'|')
        print('|2|'+str(Mesa[1][0])+'|'+str(Mesa[1][1])+'|'+str(Mesa[1][2])+'|')
        print('|3|'+str(Mesa[2][0])+'|'+str(Mesa[2][1])+'|'+str(Mesa[2][2])+'|')

    def juego(Evento, Jugada):
        global Jugadas
        global Turno
        global TurnoAnterior
        Ante = 0
        if(Turno != 3):
            main.Tablero(Evento, Jugada)
            TurnoAnterior.append(Turno)
            
        else:
            Ante = len(TurnoAnterior)
            if Turno == TurnoAnterior[Ante -1]:
                main.Tablero(Evento, Jugada)
            pass
        return Turno

    def FinalizacionJuego():
        for i in range(MesaSize[0]):
            for j in range(MesaSize[1]):
                if(Mesa[i][j]==0):
                    if(Mesa[0][0] == )