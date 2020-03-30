# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:51:01 2020

@author: user
"""
#import tkinter as tk
import json
import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#%matplotlib inline

def Plot(x):
    data1 = json.dumps({
        "success":True,
            "data":[
                {
                        
                    "record_id":258585618,
                    "subject":"EMF",
                    "bytes":x
    
                }
                ,
                {
                    "record_id":258585604,
                    "subject":"PWRELC",
                    "bytes":8,
                }
                ,
                {
                    "record_id":258584399,
                    "subject":"MCWV",
                    "bytes":20,
                }
            ]
        })
    
    data = json.loads(data1)
    subject1 = [i['subject'] for i in data["data"]]
    values = [i['bytes'] for i in data['data']]
    
    df = pd.DataFrame({'subject':subject1, 'values':values})
    
    print(df.sort_values(by='subject'))
    
    plt.bar(subject1, values)
    
    plt.savefig('static/images/performance.png')
    
    
    ################GUI GUI GUI GUI GUI GUI GUI ######################################
    
