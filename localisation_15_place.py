import numpy as np
import matplotlib.pyplot as plt
class HMM(object):

    def __init__(self,Transition_Matrix,initial_state):
        self.Transition_Matrix  = Transition_Matrix
        self.initial_state = initial_state 
        pass

    def filtering_estimation(self, Observ):
        new_state_No_Normalise = np.dot(Observ,np.dot(self.Transition_Matrix,self.initial_state ))
        new_state = new_state_No_Normalise/np.linalg.norm(new_state_No_Normalise)
        self.initial_state = new_state
        return new_state

    def Obseravation_matrix(self,error,no_discrepancies):
        sensor_list = []
        lenght = len (self.initial_state)
        Obsevation_Matrix = np.zeros((lenght,lenght))
        for d in no_discrepancies:
            proba = ((1-error)**(4-d))*(error**d)
            sensor_list.append(proba)
        np.fill_diagonal(Obsevation_Matrix,sensor_list)
        return Obsevation_Matrix
    
    def state_actuel(self,filtering_estimation):
        state_actuel = np.argwhere(filtering_estimation == np.amax(filtering_estimation)) + 1 
        return state_actuel.flatten().tolist()
        #print("state actuel possible ", state_actuel.flatten().tolist())

#definition des variable

transition_matrix = np.array([
    [0.16, 0.84, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.28, 0.16, 0.28, 0.28, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0.84, 0.16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0.16, 0, 0, 0, 0, 0, 0, 0.84, 0, 0, 0, 0],
    [0, 0, 0, 0, 0.16, 0.42, 0, 0, 0, 0.42, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0.42, 0.16, 0, 0, 0, 0.42, 0, 0, 0, 0, 0],
    [0 , 0, 0, 0, 0, 0, 0.16, 0.84, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0.28, 0.16, 0.28, 0, 0, 0, 0, 0, 0.28],
    [0, 0, 0, 0, 0, 0.21, 0, 0.21, 0.16, 0.21, 0, 0, 0, 0.21, 0],
    [0, 0, 0, 0, 0.21, 0, 0, 0, 0.21, 0.16, 0.21, 0, 0.21, 0, 0],
    [0, 0.21, 0, 0.21, 0, 0, 0, 0, 0, 0.21, 0.16, 0.21, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.42, 0.16, 0.42, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.42, 0, 0.42, 0.16, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0.84, 0, 0, 0, 0, 0.16, 0],
    [0, 0, 0, 0, 0, 0, 0, 0.84, 0, 0, 0, 0, 0, 0, 0.16]

]) 

initial_state = np.array([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

Model = HMM(transition_matrix,initial_state)

observation_matrix_SWE = Model.Obseravation_matrix(0.2,[0,2,2,2,3,1,2,2,4,4,4,1,1,0,0])
observation_matrix_NWE = Model.Obseravation_matrix(0.2,[2,2,0,0,1,1,0,2,4,4,4,3,3,2,2])
observation_matrix_W = Model.Obseravation_matrix(0.2,[2,0,2,2,1,3,2,2,2,2,2,1,3,3,2,2])
observation_matrix_E = Model.Obseravation_matrix(0.2,[2,2,2,2,3,1,2,0,2,2,2,3,1,2,2])
observation_matrix_SW = Model.Obseravation_matrix(0.2,[1,1,3,3,2,4,3,3,3,3,3,0,2,1,1])
observation_matrix_SE = Model.Obseravation_matrix(0.2,[1,3,3,3,4,2,3,1,3,3,3,2,0,1,1])
observation_matrix_NW = Model.Obseravation_matrix(0.2,[3,1,1,1,0,2,1,3,3,3,3,2,4,3,3])
observation_matrix_NE = Model.Obseravation_matrix(0.2,[2,3,1,1,2,0,1,1,3,3,3,4,2,3,3])
observation_matrix_ND = Model.Obseravation_matrix(0.2,[4,2,4,4,3,3,4,2,0,0,0,3,3,4,4])


#Dectionnaire 

Dictionnaire_Of_Obseravation = {
    "SWE" : observation_matrix_SWE,
    "NWE" : observation_matrix_NWE,
    "W" : observation_matrix_W,
    "E" : observation_matrix_E,
    "SW" : observation_matrix_SW,
    "SE" : observation_matrix_SE,
    "NW" : observation_matrix_NW,
    "ND" :  observation_matrix_ND,
    "NE" : observation_matrix_NE
    
} 

#file = open('donnes.txt', 'w+')

Obs = input()
Obs = Obs.upper()
while Obs == "SWE" or "NWE" or "W" or "E" or "SW" or "SE" or "NW" or "NE" or "ND" :
    state = Model.filtering_estimation(Dictionnaire_Of_Obseravation[Obs])
    print(state)
    #plt.plot(state)
    #Model.state_actuel(state)
    print("state actuel possible ", Model.state_actuel(state))
    #file.write("probabilte " + str(state) + "\n")
    #file.write("state actuel possible " + str(Model.state_actuel(state))+"\n")
    plt.bar(range(1,len(state)+1), state)
    plt.xticks(range(1, 16))
    plt.show()
    Obs = input()
    Obs = Obs.upper()

