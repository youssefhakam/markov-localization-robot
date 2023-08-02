# Markov Cache-based Robot Location Prediction
![Capture](https://github.com/youssefhakam/markov-localization-robot/assets/88097330/54b89173-d3fc-4e16-808b-fdd5b665d84a)

## Description 
The "Markov Cache-based Robot Location Prediction" project is a state-of-the-art initiative aimed at developing an intelligent system to predict the location of a mobile robot using Markov cache techniques. The project focuses on localizing a robot within a warehouse environment by utilizing past observations and probabilistic modeling.
The core concept of this project involves implementing Markov models and caching mechanisms to optimize and expedite the robot's localization process. Markov models allow us to represent the robot's movement probabilities within the warehouse based on historical data. Meanwhile, caching techniques facilitate the storage and retrieval of critical information to avoid redundant computations and enhance prediction accuracy.
The agent can move within an area of 15 square tiles. In the mini-warehouse, there is a shelf located between the tiles {S1, S12}, {S13, S14}, {S14, S15}, {S3, S4}, {S4, S5}, and {S6, S7}. In technical terms, we can say that the agent's environment consists of 15 discrete states. Time is also discrete. At each subsequent time step, the robot is programmed to change its position with a probability of 84% and randomly move to a different neighboring tile. Whenever the robot moves, we receive four readings from the detection system.

![image](https://github.com/youssefhakam/markov-localization-robot/assets/88097330/b97c9641-65c9-4559-ad55-088723396fec)

## Key Objectives
* Markov Model Implementation: Develop a robust Markov model that captures the probabilistic relationships between the robot's successive positions and movements within the warehouse.
* Cache Mechanism: Design an efficient cache system to store past observations and predictions, enabling the robot to leverage historical data for real-time localization.
* Prediction Algorithm: Create a sophisticated prediction algorithm that combines the power of the Markov model and cache mechanism to accurately forecast the robot's future location based on its current state.
* Real-world Testing: Evaluate the developed system through extensive simulations and real-world scenarios to assess its accuracy, robustness, and computational efficiency within an actual warehouse environment.

##  hidden markov 
* transition matrix
  The transition model is the probability of a transition from state i to state j. This can be expressed mathematically as follows:

  $$A(i,j) = P(X = j / X = i)$$

* Observation matrix
  The sensor model consists of evidence, which allows making inferences about the agent's position in the environment. At the first time step, the robot detects walls in the following directions: North, South, West, and East.

  $$B(i,j) = P(E = j/X = i) = (1 - e)^{4-d}) \cdot e^d$$

  Different sensor error rates, where d is the discrepancy - the number of signals that differ between the true values for tile i and the actual reading. This means that the probability of a sensor obtaining all the correct directions is (1 - e)^(4-d), and the probability of making a mistake is e^d. There are 9 observation matrices: SWE, NWE, W, E, NW, NE, SW, SE, No detection.






