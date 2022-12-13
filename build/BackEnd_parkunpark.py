import numpy as np
import pandas as pd

def init_csv():
    global logs, timenow, nowcount, monitor,lotnum

    logs = pd.read_csv('C:\\Users\\alama\\OneDrive\\Desktop\\Figma to Python 3.0\\ParkingLogs.csv')
    timenow = np.array(logs['timestamp']); nowcount = np.array(logs['parked_counter'])

    monitor = pd.read_csv('C:\\Users\\alama\\OneDrive\\Desktop\\Figma to Python 3.0\\Park-Monitor.csv')
    lotnum = np.array(monitor['lot_num']) 


def go_park(newlotnum, newtime):
    init_csv()
    thisnum = int(newlotnum)
    print('======PARKING======')
    for i in range(15):
        if lotnum[i]==thisnum:
        
            newCount = nowcount[-1]+1
            monitor.iloc[i,1] = False
            newLog = pd.DataFrame({'timestamp':[newtime],
                                   'lot_num':[thisnum],
                                   'in_out':[True],
                                   'parked_counter':[newCount]})
            
            monitor.to_csv('C:\\Users\\alama\\OneDrive\\Desktop\\Figma to Python 3.0\\Park-Monitor.csv', index=False)
            newLog.to_csv('C:\\Users\\alama\\OneDrive\\Desktop\\Figma to Python 3.0\\ParkingLogs.csv', mode='a', index=False, header=False)
            print('done')




def go_unpark(newlotnum, newtime):
    init_csv()
    thisnum = int(newlotnum)
    print('======PARKING======')
    for i in range(15):
        if lotnum[i]==thisnum:
        
            newCount = nowcount[-1]-1
            monitor.iloc[i,1] = True
            newLog = pd.DataFrame({'timestamp':[newtime],
                                   'lot_num':[thisnum],
                                   'in_out':[False],
                                   'parked_counter':[newCount]})
            
            monitor.to_csv('C:\\Users\\alama\\OneDrive\\Desktop\\Figma to Python 3.0\\Park-Monitor.csv', index=False)
            newLog.to_csv('C:\\Users\\alama\\OneDrive\\Desktop\\Figma to Python 3.0\\ParkingLogs.csv', mode='a', index=False, header=False)
            print('done')