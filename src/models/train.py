import numpy as np
import pandas as pd
import glob
import matplotlib.pyplot as plt
import os
from sklearn import preprocessing

directory_signal = 'Data\Signals'
directory_jump='Data\Jumps'
Signal_frame=pd.DataFrame();
Jump_frame=pd.DataFrame();

for filename in os.listdir(directory_signal):
	files = os.path.join(directory_signal, filename)
	if os.path.isfile(files):
        
         df=pd.read_csv(files)
         Signal_frame=pd.concat([Signal_frame, df],   axis=1)
         
for filename in os.listdir(directory_jump):
	files = os.path.join(directory_jump, filename)
	if os.path.isfile(files):
        
         df=pd.read_csv(files)
         Jump_frame=pd.concat([Jump_frame, df],  axis=1) 
print(Signal_frame.shape)  
     
#data preprocessing
#print(Signal_frame.isnull().sum())
#print(Jump_frame.isnull().sum())

Signal_Dataframe = Signal_frame.dropna()
Jump_Dataframe = Jump_frame.dropna()   
 
#print(Signal_Dataframe.head())
#print(Signal_Dataframe.shape)       
#Signal_frame.append(pd.read_csv(files,header=none))
#Load and store the Signals into a pandas dataframe
#Signal1 = pd.read_csv("./Data/Signals/signal1.csv",header=None)
#Signal2 = pd.read_csv("./Data/Signals/signal2.csv",header=None)
#Signal3 = pd.read_csv("./Data/Signals/signal3.csv",header=None)
#Signal4 = pd.read_csv("./Data/Signals/signal4.csv",header=None)
#Signal5 = pd.read_csv("Data/signal5.csv",header=None)
#Signal6 = pd.read_csv("Data/signal6.csv",header=None)
#Signal_Dataframe = pd.concat([Signal1,Signal2,Signal3,Signal4,Signal5,Signal6],axis=1,ignore_index=True)
#Load and store the jumps into a pandas dataframe
'''Jump1 = pd.read_csv("Data/jump1.csv",header=None)
Jump2 = pd.read_csv("Data/jump2.csv",header=None)
Jump3 = pd.read_csv("Data/jump3.csv",header=None)
Jump4 = pd.read_csv("Data/jump4.csv",header=None)
Jump5 = pd.read_csv("Data/jump5.csv",header=None)
Jump6 = pd.read_csv("Data/jump6.csv",header=None)
Jump_Dataframe = pd.concat([Jump1,Jump2,Jump3,Jump4,Jump5,Jump6],axis=1,ignore_index=True)


#data preprocessing
Signal_Dataframe.isnull().sum(),Jump_Dataframe.isnull().sum()

Signal_Dataframe = Signal_Dataframe.dropna()
Jump_Dataframe = Jump_Dataframe.dropna()
figs = {}
axs = {}
for i in range(Signal_Dataframe.shape[1]):
    figs[i] = plt.figure(figsize=(10,5))
    axs[i] =figs[i].add_subplot(111)
    axs[i].plot(Signal_Dataframe[i])  
    axs[i].set_xlim(0,Signal_Dataframe[i].shape[0])
    axs[i].set_ylabel('Signal magnitude')
    axs[i].set_xlabel('Number of samples')   
    
    
    #data preprocessing
Signal_Dataframe.isnull().sum(),Jump_Dataframe.isnull().sum()

Signal_Dataframe = Signal_Dataframe.dropna()
Jump_Dataframe = Jump_Dataframe.dropna()
figs = {}
axs = {}
for i in range(Signal_Dataframe.shape[1]):
    figs[i] = plt.figure(figsize=(10,5))
    axs[i] =figs[i].add_subplot(111)
    axs[i].plot(Signal_Dataframe[i])  
    axs[i].set_xlim(0,Signal_Dataframe[i].shape[0])
    axs[i].set_ylabel('Signal magnitude')
    axs[i].set_xlabel('Number of samples') '''
    
    
store_decisions=[]
  
def anomaly_detection_mean(signal,threshold,windowsize):
    #mean_flux0 = np.mean(X)
    #decision_mean = []
    mean_comp=np.mean(signal[1:windowsize])
    
    decision_mean = np.zeros(signal.shape[0])
    time = []
    mean_comparison = []
    for i in range(windowsize+1,signal.shape[0]):
        a = (np.mean(signal[(i-window_size):i]) - mean_comp)
        b = (np.std(signal[(i-window_size):i]))/(np.sqrt(window_size))
        u = a/b
        #X_train= signal[window-window_size:window]
        #u = preprocessing.StandardScaler().fit(X_train)
        mean_comparison.append(u)
        if ((u >= threshold) | (u <= -threshold)): #threshold
            decision_mean[i] = 1
           # time.append(window - int(window_size/2)) 
        else:
            decision_mean[i] = 0
            
    return decision_mean, mean_comparison,time
signal = Signal_Dataframe.iloc[:,0]  # 6 signals (0...5)
#print(Signal_Dataframe.shape)
print(signal.shape)
threshold = 3
window_size = 20
for  j in range(1,6):
     decision_mean,mean_comparison,time = anomaly_detection_mean(Signal_Dataframe.iloc[:,j-1] ,threshold,window_size)
     plt.figure(figsize = (12, 6))
     print(decision_mean.shape)
     store_decisions.append(decision_mean)
     plt.subplot(3,2,j)
     plt.plot(decision_mean)
     
#print(decision_mean.shape)
plt.show()
print(store_decisions)