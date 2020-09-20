### The objectives of the implementation are:
  1. Study and build the SIS model for a virus propagation.
  2. Compute the strength of a virus.
  3. Simulate the propagation of a virus in a network.
  4. Determine if a virus will lead to a pandemic.
  5. Implement one out of four immunization policies to prevent a pandemic.
  
### Instructions:
Please keep the static.network graph file in the same folder as the notebook. Use anaconda to open the notebook and run all cells.
The code runs on two different combinations of input parameter.
  1. Transmission probabilities β1 = 0.20 and Healing probabilities δ1 =0.70
  2. Transmission probabilities β2 = 0.01 and Healing probabilities δ2 = 0.60
  3. The number of vaccines available are in a range of 20 to 30 or 15 to 50.

### Libraries used:
	- igraph
	- numpy
	- scipy
	- matplotlib
  
### Things to implement further:
The next task is to implement the below-mentioned immunization policies:

  - Policy 2: Select the k nodes with highest degree for immunization
  - Policy 3: Select the node with the highest degree for immunization. Remove this node (and its incident edges) from the contact network. Repeat until all vaccines are administered.
  - Policy 4: Find the eigenvector corresponding to the largest eigenvalue of the contact network’s adjacency matrix. Find the ​k largest (absolute) values in the eigenvector. Select the k nodes at the corresponding positions in the eigenvector.
