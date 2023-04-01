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
The function is used to calculate **plog(p)** which is used in entropy calculations
https://github.com/romannjoroge/Machine-Learning-And-Programming-Unit/blob/00e3a3bbbb8ab98553992766fb5c1f1c063117ac/ID3/ID3.py#L38-L71
The function is used to calculate **entropy** which is the negative summation of plog(p) for every value of target class
https://github.com/romannjoroge/Machine-Learning-And-Programming-Unit/blob/00e3a3bbbb8ab98553992766fb5c1f1c063117ac/ID3/ID3.py#L74-L120
The function is used to calculate **information gain**. This is used to determine the best splitting attribute i.e the attribute with the highest information gain is selected as the best splitting attribute
https://github.com/romannjoroge/Machine-Learning-And-Programming-Unit/blob/00e3a3bbbb8ab98553992766fb5c1f1c063117ac/ID3/ID3.py#L123-L149
This function uses *calculate_information_gain* to get the information gains of every attribute in a given data set.
https://github.com/romannjoroge/Machine-Learning-And-Programming-Unit/blob/00e3a3bbbb8ab98553992766fb5c1f1c063117ac/ID3/ID3.py#L152-L176
This function performs **step 6 of algorithm**. It selects the splitting attribute from a dict containing the attribute name as key and its information gain as the value
https://github.com/romannjoroge/Machine-Learning-And-Programming-Unit/blob/00e3a3bbbb8ab98553992766fb5c1f1c063117ac/ID3/ID3.py#L179-L213
This function is used to perform **step 8 of the algorithm**. It splits the given data set into a dictionary where the key is a unique value of the splitting attribute in the data and the value is a list of data points that have the unique value.
https://github.com/romannjoroge/Machine-Learning-And-Programming-Unit/blob/00e3a3bbbb8ab98553992766fb5c1f1c063117ac/ID3/ID3.py#L216-L240
This is the definition of a node in the decision tree. Title represents the name of the attribute chosen for the node if it's not a leaf node. *parent_attr_type* is the attribute of the parent of the node. *parent_attribute* is the value of the attribute of the node's parent.
https://github.com/romannjoroge/Machine-Learning-And-Programming-Unit/blob/00e3a3bbbb8ab98553992766fb5c1f1c063117ac/ID3/ID3.py#L216-L240
The function uses all the defined functions and **implements the algorithm** using recursion
https://github.com/romannjoroge/Machine-Learning-And-Programming-Unit/blob/00e3a3bbbb8ab98553992766fb5c1f1c063117ac/ID3/ID3.py#L321-L332
The function accepts the location of a CSV file containing the data, extracts the data, transforms it into a form that can be used by the create_tree function and calls the function with the transformed data.
