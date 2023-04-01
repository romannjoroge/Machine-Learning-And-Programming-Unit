# Machine-Learning-And-Programming-Unit
This repo contains the code I wrote while taking the unit **Machine Learning And Programming**.
The folders contain code for different things tought during the unit
## K-Nearest Neighbors
The code is in the KNN Folder. It contains CSV files used in testing and the KNN.py file that contains the code used to implement KNN.
To obtain the K-Nearest neighbur of a point Z the following is done:

### Data Used In Algorithm
1. Location of CSV file containing data points as a string
2. Point to predict class of (represented as a tuple)

### Algorithm
1. The distance between Z and all other points in the dataset are calculated using a distance function
2. The point with the smallest distance is found and its class is chosen as the class of Z

## Decision Trees Using ID3 algorithm
The code is in the ID3 folder. It contains CSV files used in testing and the ID3.py file that contains the implementation
To construct a decison tree using the ID3 algorithm:
### Data Used In Algorithm:
1. A list of data points where each point is a tuple
2. A list of attributes to select splitting node

### Algorithm
1. Create a Node
2. Check if the node is meant to be a leaf node
3. If it is a leaf node label it with the class in data and stop
4. Check if there are attributes to check in the attribute list
5. If the list is empty label the node with "No More Attributes" and stop
6. Select the best splitting attribute from the list of attributes and label the node with the attribute name
7. Remove the selected attribute from the attribute list
8. Split the data into mutliple lists based on the value of the selected node
9. Remove values that belong to the selected attribute 
10. For each unique value of the selected attribute create a child node for the node
11. Repeat for each child node with the split data and new attribute list

### Code explanation
The functions in the ID3.py folder do the following:
https://github.com/romannjoroge/Machine-Learning-And-Programming-Unit/blob/0cc4830f2421ce39752532d6b1cf6afc57872080/ID3/ID3.py#L18-L35
The function is used to calculate plog(p) which is used in entropy calculations

