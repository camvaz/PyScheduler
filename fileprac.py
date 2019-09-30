class Scheduler:
    pids = []
    def __init__(self):
        self.name= "task"

    def addpid(self,pidn):
        self.pids.append(pidn)
    
    def printpid(self):
        print(self.pids)

plani = Scheduler()

str = "1t3t0t1t27";

data = str.split('t');

for i in data:
    plani.addpid(i);


print(data);
plani.printpid()
