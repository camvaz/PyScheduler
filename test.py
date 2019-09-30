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

        @staticmethod
        def tablaHasExecutions(container):
            for i in container:
            if(i.exe > 0):
                return true;
        return false;

        @staticmethod
        def vaciarCola(container, boolean):
            for i in container
                


class Proceso:
    def __init__(self,nombre,llegada,ejecucion,prioridad,nram):
        self.name = nombre;
        self.lle = llegada;
        self.exe = ejecucion;
        self.prio = prioridad;
        self.ram = nram;
        self.espera = 0;
        self.vuelta = 0;

    def __eq__(self, o):
        return self.name == o.name;

    def print(self):
        return f"{self.name}\t{self.lle}\t{self.exe}\t\t{self.prio}\t\t{self.ram}\t{self.espera}\n"


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

    def printpids(self):
        print("\t\t    TABLA DE PROCESOS\n");
        print("Nombre\tLlegada\tEjecucion\tPrioridad\tRam\tEspera")
        for i in self.procesos:
            print(i.print());

    def run(self,args,canales):
        tabla=[];

        for i in self.procesos:
            if i.ram <= self.ram:
                tabla.append(i);
            else:
                i.espera = "NA";

        llegadas = []
        cola = [];
        generacion = [];
        tiempo = 0;
        vueltaCola = 0;        

        while(Util.tablaHasExecutions(tabla)):                    


            for i in tabla:
                if i.lle == tiempo:
                    llegadas.append(i);

            Utils.sorttabla(llegadas, args);

            residuo = self.ram;

            for i in range(canales):
                
                if llegadas[i].ram <= residuo:
                    residuo -= llegadas[i].ram;
                    llegadas[i].exe -= 1;
                    if(llegadas[i].exe == 0):
                        for j in tabla:
                            if j.id = llegadas[i].id:
                                j.esp = tiempo - j.lle - j.exe;
                    else:
                        cola.append(llegadas[i]);
                        generacion.append(llegadas.pop(i));



            tiempo+=1;



                                





def main():
    plani = Scheduler("data.txt"); 
    plani.printpids();


    plani.procesos.sort(key=lambda x:(x.prio,x.lle,x.exe,-Utils.pidtoint(x.name)));


    plani.printpids();

main();
