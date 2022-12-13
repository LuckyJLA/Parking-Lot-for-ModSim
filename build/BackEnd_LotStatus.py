import pandas as pd
import numpy as np

def init_csv():
    global csv_file, lot, stat
    csv_file = pd.read_csv('C:\\Users\\alama\\OneDrive\\Desktop\\Figma to Python 3.0\\Park-Monitor.csv')
    lot = np.array(csv_file['lot_num']); stat = np.array(csv_file['available'])

def button_color(lot_num):
    init_csv()
    
    for i in range(15):
        if lot[i]==lot_num:
            if stat[i] == True: 
                return '#00DC16' 
            
            # False means someone already parked    
            elif stat[i] == False: 
                return '#FF0000'