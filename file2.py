class Process:
    
    def __init__(self, lle, exe, pri, nram):
        self.llegada = lle;
        self.ejecucion = exe;
        self.prioridad = pri;
        self.ram = nram;
        self.espera = 0;
    

class Scheduler:
    __pids = {}   
    __queue = []
    def __init__(self, args):
        # for i in range(args):
        #     self.pids.append([0]*6);
        self.name="hhhh";    

    def addpiddata(self, name,data):
        self.__pids[name]=data;

    def addpid(self,pidn):
        self.__pids.append(pidn)
    
    def printpid(self):
        print(self.__pids)

    def run(self):
        for i in self.__pids.items():
            i[1]-=1

    


f = open("data.txt");
plani = Scheduler(10);

for line in f:
    arrdata = line.split('t');
    name = arrdata.pop(0); arrdata.pop();
    for i in range(len(arrdata)):
        arrdata[i] = int(arrdata[i]);
    plani.addpiddata(name,arrdata);



plani.printpid();
plani.run();
plani.printpid();
f.close();

print(plani.__pids);