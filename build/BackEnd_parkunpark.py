import numpy as np
import pandas as pd
import datetime as dt

logs = pd.read_csv('C:\\Users\\alama\\OneDrive\\Desktop\\Figma to Python 3.0\\ParkingLogs.csv')
lotnum = np.array(logs['lot_num']); timenow = np.array(logs['timestamp']); nowcount = np.array(logs['parked_counter'])

monitor = pd.read_csv('C:\\Users\\alama\\OneDrive\\Desktop\\Figma to Python 3.0\\Park-Monitor.csv')


def go_park(newlotnum, newtime):
    print('======PARKING======')
    for i in range(15):
        if lotnum[i]==newlotnum:
            monitor.iloc[i,1] = False

            newCount = nowcount[-1]+1
            newLog = pd.DataFrame({'timestamp':[newtime],
                                   'lot_num':[newlotnum[i]],
                                   'in_out':[True],
                                   'parked_counter':[newCount]})
            
            monitor.to_csv('C:\\Users\\alama\\OneDrive\\Desktop\\Figma to Python 3.0\\Park-Monitor.csv', index=False)
            newLog.to_csv('C:\\Users\\alama\\OneDrive\\Desktop\\Figma to Python 3.0\\ParkingLogs.csv', mode='a', index=False, header=False)



def go_unpark():
    print()