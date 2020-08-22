import numpy as np

def calculate(list):

    try:
      len(list)>=9

      a = np.array(list)
      b = a.reshape(3,3)
      calculations = {'mean': [[np.mean(b[:,0]), np.mean(b[:,1]), np.mean(b[:,2])], [np.mean(b[0,:]),np.mean(b[1,:]),np.mean(b[2,:])], np.mean(b[:,:]) ], 
      'variance': [[np.var(b[:,0]), np.var(b[:,1]), np.var(b[:,2])], [np.var(b[0,:]),np.var(b[1,:]),np.var(b[2,:])], np.var(b[:,:]) ],     
      'standard deviation': [[np.std(b[:,0]), np.std(b[:,1]), np.std(b[:,2])], [np.std(b[0,:]),np.std(b[1,:]),np.std(b[2,:])], np.std(b[:,:]) ],                 
      'max': [[np.max(b[:,0]), np.max(b[:,1]), np.max(b[:,2])], [np.max(b[0,:]),np.max(b[1,:]),np.max(b[2,:])], np.max(b[:,:]) ],   
      'min': [[np.min(b[:,0]), np.min(b[:,1]), np.min(b[:,2])], [np.min(b[0,:]),np.min(b[1,:]),np.min(b[2,:])], np.min(b[:,:]) ],  
      'sum': [[np.sum(b[:,0]), np.sum(b[:,1]), np.sum(b[:,2])], [np.sum(b[0,:]),np.sum(b[1,:]),np.sum(b[2,:])], np.sum(b[:,:]) ]  
      }

      #print(b)
      return calculations

    except ValueError:
      raise ValueError("List must contain nine numbers.")