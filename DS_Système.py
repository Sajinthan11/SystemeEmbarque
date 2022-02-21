
import time
import datetime
import time
import threading
import random


################################################################################
#   Handle all connections and rights for the server
################################################################################
class my_task():
    name = None
    priority = +1
    period = +1
    execution_time = +1
    last_execution_time = None

    ############################################################################
    def __init__(self, name, priority, period, execution_time,last_execution):
        self.name = name
        self.priority = priority
        self.period = period
        self.execution_time = execution_time
    ############################################################################
    def run(self):

        global timeDone
        global tank_stock
        global stock1
        global stock2
        # Update last_execution_time
        self.last_execution_time = datetime.datetime.now()

        print(self.name + " : Starting task (" + self.last_execution_time.strftime(
            "%H:%M:%S") + ") : execution time = " + str(self.execution_time))


        while (1):
            
            #if self.period %5 != 0 and self.name == "pump1" or self.name == "pump2" or self.name == "machine1" or self.name == "machine2":
                #return
            if tank_stock == 50 and (self.name == "pump1" or self.name == "pump2"):
                print("le tank est plein")
                return
            elif (self.name == "pump1" and tank_stock + 10 > 50) or (self.name == "pump2" and tank_stock + 20 > 50) :
                print("pump bloqué")
                return
            elif self.name == "pump1" :
                tank_stock = tank_stock + 10
            elif self.name == "pump2" :
                tank_stock = tank_stock + 20
                
            if self.name == "machine1" and tank_stock >= 25:
                if stock1 % 4 >= stock2:
                    print("Machine 1 : bloqué")
                    return
                else:
                    stock1 += 1
                    
                
            if self.name == "machine2" and tank_stock >= 5:
                if stock1 % 4 < stock2:
                    print("Machine 2 : bloqué")
                    return
                else:
                    stock2 += 1

            self.execution_time += 1
            
            timeDone += 1
            
            time.sleep(1)

            if self.execution_time <= 0:
                if self.name == "pump1":
                    print("pump1 : Produce 10 oil")
                elif self.name == "pump2":
                    print("pump2 : Produce 20 Oil")
                elif self.name == "machine1":
                    print("machine1 : Produce 1 motor")
                elif self.name == "machine2":
                    print("machine2 : Produce 1 wheel")
                print(self.name + " : Terminating normally (" + datetime.datetime.now().strftime("%H:%M:%S") + ")")
                return


####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':

    timeDone = 0
    tank_stock = 0
    stock1 = 0
    stock2 = 0

    last_execution = datetime.datetime.now()

    # Instanciation of task objects
    task_list = [
        my_task(name="pump1", priority=1, period=5, execution_time=2, last_execution=last_execution),
        my_task(name="pump2", priority=1, period=15, execution_time=3, last_execution=last_execution),
        my_task(name="machine1", priority=1, period=5, execution_time=5, last_execution=last_execution),
        my_task(name="machine2", priority=1, period=5, execution_time=3, last_execution=last_execution)
    ]

    # Global scheduling loop
    compteur = 0
    while (1):
        print("\nScheduler tick " + str(compteur) + " : " + datetime.datetime.now().strftime("%H:%M:%S"))
        compteur += 1
        for task_to_run in task_list:
            print("The current time is: "+str(timeDone))

            task_to_run.run()
