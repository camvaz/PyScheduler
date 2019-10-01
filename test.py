import sys;
class Utils:
    @staticmethod
    def pidtoint(name):
        str=""
        for i in name[1: :1]:
            str+=i;
        return int(str);

    @staticmethod
    def sorttabla(container,arg):
        #EL SWITCH NO EXISTE EN PYTHON XD ????????
        if(arg == 0):
            # PRIORIDAD ASCENDENTE, LLEGADA ASCENDENTE, EJECUCION ASCENDENTE, ID ASCENDENTE 
            container.sort(key=lambda x:(x.prio,x.exr,x.lle,Utils.pidtoint(x.name)));
        
        if(arg == 1):
            # PRIORIDAD ASCENDENTE LLEGADA ASCENDENTE, EJECUCION ASCENDENTE, ID DESCENDENTE
            container.sort(key=lambda x:(x.prio,x.exe,x.lle,-Utils.pidtoint(x.name)));

        if(arg == 2):
            # PRIORIDAD ASCENDENTE LLEGADA ASCENDENTE, EJECUCION DESCENDENTE, ID ASCENDENTE
            container.sort(key=lambda x:(x.prio,x.exe,-x.lle,Utils.pidtoint(x.name)));

        if(arg == 3):
            # PRIORIDAD ASCENDENTE LLEGADA ASCENDENTE, EJECUCION DESCENDENTE, ID DESCENDENTE 
            container.sort(key=lambda x:(x.prio,x.exe,-x.lle,-Utils.pidtoint(x.name)));
        
        if(arg == 4):
            # PRIORIDAD ASCENDENTE LLEGADA DESCENDENTE, EJECUCION ASCENDENTE, ID ASCENDENTE 
            container.sort(key=lambda x:(x.prio,-x.exe,x.lle,Utils.pidtoint(x.name)));

        if(arg == 5):
            # PRIORIDAD ASCENDENTE, LLEGADA DESCENDENTE, EJECUCION ASCENDENTE, ID DESCENDENTE
            container.sort(key=lambda x:(x.prio,-x.exe,x.lle,-Utils.pidtoint(x.name)));

        if(arg == 6):
            # PRIORIDAD ASCENDENTE, LLEGADA DESCENDENTE, EJECUCION DESCENDENTE, ID ASCENDENTE 
            container.sort(key=lambda x:(x.prio,-x.exe,-x.lle,Utils.pidtoint(x.name)));

        if(arg == 7):
            # PRIORIDAD ASCENDENTE, LLEGADA DESCENDENTE, EJECUCION DESCENDENTE, ID DESCENDENTE 
            container.sort(key=lambda x:(x.prio,-x.exe,-x.lle,-Utils.pidtoint(x.name)));

        if(arg == 8):
            # PRIORIDAD DESCENDENTE, LLEGADA ASCENDENTE, EJECUCION ASCENDENTE, ID ASCENDENTE 
            container.sort(key=lambda x:(-x.prio,x.exe,x.lle,Utils.pidtoint(x.name)));
        
        if(arg == 9):
            # PRIORIDAD DESCENDENTE LLEGADA ASCENDENTE, EJECUCION ASCENDENTE, ID DESCENDENTE
            container.sort(key=lambda x:(-x.prio,x.exe,x.lle,-Utils.pidtoint(x.name)));

        if(arg == 10):
            # PRIORIDAD DESCENDENTE LLEGADA ASCENDENTE, EJECUCION DESCENDENTE, ID ASCENDENTE
            container.sort(key=lambda x:(-x.prio,x.exe,-x.lle,Utils.pidtoint(x.name)));

        if(arg == 11):
            # PRIORIDAD DESCENDENTE LLEGADA ASCENDENTE, EJECUCION DESCENDENTE, ID DESCENDENTE 
            container.sort(key=lambda x:(-x.prio,x.exe,-x.lle,-Utils.pidtoint(x.name)));
        
        if(arg == 12):
            # PRIORIDAD DESCENDENTE LLEGADA DESCENDENTE, EJECUCION ASCENDENTE, ID ASCENDENTE 
            container.sort(key=lambda x:(-x.prio,-x.exe,x.lle,Utils.pidtoint(x.name)));

        if(arg == 13):
            # PRIORIDAD DESCENDENTE, LLEGADA DESCENDENTE, EJECUCION ASCENDENTE, ID DESCENDENTE
            container.sort(key=lambda x:(-x.prio,-x.exe,x.lle,-Utils.pidtoint(x.name)));

        if(arg == 14):
            # PRIORIDAD DESCENDENTE, LLEGADA DESCENDENTE, EJECUCION DESCENDENTE, ID ASCENDENTE 
            container.sort(key=lambda x:(-x.prio,-x.exe,-x.lle,Utils.pidtoint(x.name)));

        if(arg == 15):
            # PRIORIDAD DESCENDENTE, LLEGADA DESCENDENTE, EJECUCION DESCENDENTE, ID DESCENDENTE 
            container.sort(key=lambda x:(-x.prio,-x.exe,-x.lle,-Utils.pidtoint(x.name)));

        if(arg == 16):
            container.sort(key=lambda x:Utils.pidtoint(x.name));

    @staticmethod
    def tablaHasExecutions(container):
        for i in container:
            if i.esp == 0:
                return True;
        return False;

    @staticmethod
    def vaciarCola(cola, tabla, tiempo):
        ct = 0;
        for i in tabla:
            if i.lle < tiempo and i.finalizado==0:
                ct+=1;

        print(f"Contador: {ct} Tamanio cola: {len(cola)}")
        return ct == len(cola);        

    @staticmethod
    def finSchedule(tabla):
        for i in tabla:
            if i.finalizado == 0:
                return True;
        
        return False;

class Proceso:
    def __init__(self,nombre,llegada,ejecucion,prioridad,nram):
        self.name = nombre;
        self.lle = llegada;
        self.exe = ejecucion;
        self.ejecuciones = ejecucion;
        self.prio = prioridad;
        self.ram = nram;
        self.esp = 0;
        self.finalizado = 0;

    def __eq__(self, o):
        return self.name == o.name;

    def print(self):
        return f"{self.name}\t{self.lle}\t{self.ejecuciones}\t\t{self.exe}\t\t{self.prio}\t{self.ram}\t{self.esp}\t{self.finalizado}\n"

class Scheduler:
    procesos = [];
    def __init__(self, nram, filename):
        self.name = "Planificador de procesos.";
        self.ram = nram;
        f = open(filename);

        for line in f:
            arrdata = line.split(","); 
            name = arrdata.pop(0); arrdata.pop();
            for i in range(len(arrdata)):
                arrdata[i] = int(arrdata[i]);
            
            self.procesos.append(Proceso(name, arrdata[0], arrdata[1],arrdata[2],arrdata[3]));        

        f.close();

    def printpids(self, tabla):
        print("\t\t    TABLA DE PROCESOS\n");
        print("Nombre\tLlegada\tEjecucion\tExe\tPrioridad\tRam\tEspera\tFinalizado")
        for i in tabla:
            print(i.print());
        print("final de tabla\n")

    def run(self,args,canales,ram):
        try:
            tabla=[];
            for i in self.procesos:
                if i.ram <= ram:
                    tabla.append(i);
                else:
                    i.espera = "NA";

            channels = canales;

            llegadas = []
            cola = [];
            tiempo = 0;

            while(Utils.finSchedule(tabla)):                    
                print(f"Iteración: {tiempo}\n") 
                self.printpids(tabla);
                print("Tabla de cola de espera:\n")
                self.printpids(cola);

                if(Utils.vaciarCola(cola,tabla,tiempo)):
                    for i in cola:
                        llegadas.append(i)

                    cola.clear(); 
                    print("Vaciado de cola\n")

                for i in tabla:
                    if i.lle == tiempo:
                        llegadas.append(i);
        
                Utils.sorttabla(llegadas, args);

                print("\nTabla de llegadas:\n")
                self.printpids(llegadas);

                channels = canales;
                residuo = ram;
                itr = 0;
                rampass = 0;

                while itr < channels and Utils.finSchedule(tabla):
                    # print(Utils.finSchedule(tabla))
                    if llegadas[itr+rampass].ram <= residuo:
                        residuo -= llegadas[itr+rampass].ram;
                        if(llegadas[itr+rampass].exe == 0):
                            for j in tabla:
                                if j.name == llegadas[itr+rampass].name:
                                    j.esp = tiempo - j.lle - j.ejecuciones;
                                    j.finalizado=1;
                                    print(f"Espera de {j.name} tiempo {j.esp}");
                            llegadas.pop(itr+rampass);
                        else:
                            llegadas[itr+rampass].exe -= 1;
                            cola.append(llegadas.pop(itr+rampass));
                        channels-=1;
                    else:
                        rampass+=1;
                tiempo+=1;

            print("\nTabla final:\n")
            self.printpids(tabla);
        except:
            print("Unexpected error:", sys.exc_info()[0],"\n")
            raise
                                





def main():
    plani = Scheduler(10,"data.txt"); 
    plani.run(16,2,10);



main();
