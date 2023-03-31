import math
from collections import Counter, defaultdict
from typing import List, Tuple, Dict, Type
import pandas as pd

def calculate_information(total_instances: int, occurences: int) -> float:
    """
    The function calculates the values that are negated to calcuate entropy i.e p*log(p)
    Inputs:
        total_instances: int. The total number of items in the dataset
        occurences: int. The total number of instances that belong to a specific class
    Output: float.

    The function assumes that occurences is smaller than or equal total instances and that they are ints
    """
    # Assertions
    assert type(total_instances) == int and type(occurences) == int, "Parameters must be ints"
    assert occurences <= total_instances, "Occurences cannot be more than total instances"

    # Calculate the value
    propotion = occurences / total_instances
    return propotion * math.log2(propotion)

def calculate_entropy(data: List[Tuple]) -> float:
    """
    Calculates the entropy of the dataset
    Inputs:
        data: A list of the data points where each point is a tuple. The target variable is assumed to be the last item in each tuple
    Outputs:
        The entropy of the dataset

    Assume that both variables are strings
    """
    # Assertions
    assert type(data) == list, "data should be a list"
    assert all([type(item) == tuple for item in data]), "data should be a list of points"

    # Get total number of instances
    total_instances = len(data)

    # Get propotion of items
    c = Counter([point[-1] for point in data])

    # If all the instances are of one target class attribute entropy is 1
    if(len(c.items()) == 1):
        entropy = 0
    else:
        # Get a list of information calculations of every unique target value in data
        informations = [calculate_information(total_instances, propotion[-1]) for propotion in c.items()]

        # Subract each value in informations
        entropy = 0
        for i in informations:
            entropy -= i
    return entropy

def calculate_information_gain(data: List[Tuple], attribute: str, attribute_list: List[str]) -> float:
    """
    Calculate information gain of data using a specific attribute.

    Inputs:
        data: list of data points where each point is a tuple
        attribute: attribute to use to split data set
        attribute_list: a list of attributes in data
    Output:
        information gain of data and attribute

    Assumes that attribute is in attribute list and that the position of attribute in attribute list 
    is the same as the position of the attibute value in the tuple
    """
    # Assertions
    assert type(data) == list and type(attribute_list) == list, "data and attribute_list must be lists"
    assert type(attribute) == str, "attribute should be a string"
    assert attribute in attribute_list, "attribute should be in attribute_list"
    assert all([len(attribute_list) == len(item) for item in data]), "All attributes in attribute list should be in data"

    # Calculate entropy of entire data set
    entropy = calculate_entropy(data)

    # Divide data by unique values of attribute
    divided_data = defaultdict(list)
    # Go through data and split by 
    position_in_tuple = attribute_list.index(attribute)
    for d in data:
        divided_data[d[position_in_tuple]].append(d)

    # Get entropy of each subdivision
    entropies = defaultdict(float)
    for key, value in divided_data.items():
        entropies[key] = calculate_entropy(value)

    # Multiply entropy by probabilites and add
    # Get propotions of each target value
    total_instances = len(data)
    sum_of_entropies = 0
    for key, val in divided_data.items():
        occurences = len(val)
        sum_of_entropies += (occurences/total_instances) * entropies[key]
    
    # Remove entropy of entire dataset to sum of entropies
    return entropy - sum_of_entropies

def get_information_gains(data: List[Tuple], attribute_list: List[str]) -> Dict[str, float]:
    """
    Get information gains of all attributes in data
    Inputs:
        data: A list of all the data points in system
        attribute_list: List of all attributes in data
    Outputs:
        A dictionary containing name of attribute and information gain

    Assumes that data is a list of tuples and that each point has as many values as attribute_list
    """
    # Assertions
    assert type(data) == list and type(attribute_list) == list, "data and attribute list should be lists"
    assert all([type(item) == tuple for item in data]), "data should contain points"
    assert all([len(attribute_list) == len(item) for item in data]), "data should contain as many value as attribute list"

    # Get information gain of every attribute
    information_gains = defaultdict(float)
    for i in range(len(attribute_list) - 1):
        information_gains[attribute_list[i]] = round(calculate_information_gain(data, attribute_list[i], attribute_list), 4)

    # Return dict
    return dict(information_gains)

def select_best_attribute(information_gains: Dict[str, float]) -> str:
    """
    Given a list containing dictionaries that have attribute as key and information gain as value return the attribute
    with the best information gain
    Inputs:
        information_gains: A dicitionaries where the key of each dictionary is attribute name and value is information gain
    Outputs:
        best attribute

    Assumes that information_gains is a list of dictionaries
    """
    # Assertions
    assert type(information_gains) == dict, "information gains should be a dictionary"

    # Go through all the dictionaries values and return the attribute with the largest value
    largest_value = 0
    attribute = ''
    for key, value in information_gains.items():
        if value > largest_value:
            largest_value = value
            attribute = key
        else:
            continue
    return attribute

def split_data(data: List[Tuple], splitting_attribute: str, attribute_list: List[str]) -> Dict[str, List]:
    """
    Splits data into multiple lists based on value of splitting attribute.
    Inputs:
        data: A list of data points where each data point is a tuple
        splitting_attribute: str. Name of the attribute to split data by
        attribute_list: List of attribute names
    Output:
        Multiple lists that have entries with unique values of splitting attribute

    Assumes that data and attribute list are lists.
    Assumes that each point the same number of values as attribute list
    Assumes that splitting attribute is in attribute_list
    """
    # Assertions
    assert type(data) == list and type(attribute_list) == list, "data and attribute_list are lists"
    assert type(splitting_attribute) == str, "splitting attribute should be a string"
    assert splitting_attribute in attribute_list, "splitting attribue should be in attribute list"
    assert all([type(item) == tuple for item in data]), "data should contain a list of points"
    assert all(len(attribute_list) == len(item) for item in data), "data points should have as many attributes as attribute_list"

    # Go through all data points and create a separate list for every attribute value
    # Get position of attribute
    pos = attribute_list.index(splitting_attribute)

    split_list = defaultdict(list)
    for item in data:
        split_list[item[pos]].append(item)
    
    # Return dictionary where key is unique attribute value and val is list of data points that have attribute value
    return split_list

class Node:
    """
    Node in the tree
    """
    def __init__(self, title: str = None, parent_attribute: str = None, parent_attr_type: str = None) -> None:
        self.title = title
        self.parent_attribute = parent_attribute
        self.parent_attr_type = parent_attr_type

    children = []

    def insertChild(self, child):
        """
        Give a node a child
        Assumes child is a Node
        """
        # Assertions
        assert isinstance(self, Node)

        # Insert child in children
        self.children.append(child)

    def __str__(self):
        return(f"{self.title} Node: Children {len(self.children)}")


def create_tree(data: List[Tuple], attribute_list: List[str], node: Type[Node] = None):
    """
    Creates a node in the tree using data
    Inputs:
        data: A list of all the points in the data set as tuples. Assumes that the class attribute is the last item in tuple
        attribute_list: List of attributes in attribute list
    Outputs:
        A node in the tree
    """

    if node == None:
        print(f"\n\nBEGINNING\n\n")
        node = Node()

    # Check if node is leaf node
    # Get propotions of class attribute values
    c = Counter([item[-1] for item in data])
    if(len(c.keys()) == 1):
        # Only one attribute is in data so is leaf node
        node.title = data[0][-1]
        print(f"\n\nLeaf Node Reached: Parent Attribute is {node.parent_attr_type}, {node.parent_attribute}. Value is {node.title}")
        return node

    # Check if there are no more attributes
    if(len(attribute_list) == 0): 
        node.title = "No More Attributes"
        return node

    # Get splitting node
    # Get information gain from every attribute
    print(f"\n\ndata is {data}")
    print(f"Parent Attribute is: {node.parent_attr_type}, {node.parent_attribute}")
    print(f"attribute list is {attribute_list}\n\n")
    information_gains = get_information_gains(data, attribute_list)
    print(f"Information gains is {information_gains}")

    # Get splitting node
    splitting_node = select_best_attribute(information_gains)
    print(f"Splitting Node is {splitting_node}")

    # Assign Node splitting node
    node = Node(splitting_node)

    # Split data according to attributes
    splitted_data = split_data(data=data, splitting_attribute=splitting_node, attribute_list=attribute_list)

    # Remove attribute from attribute list and each list in split data
    indexToRemove = attribute_list.index(splitting_node)
    edited_list = attribute_list[:]
    edited_list.remove(splitting_node)
    new_split_data = defaultdict(list)
    for key, value in splitted_data.items():
        # Remove attribute from each list in value
        newValue = []
        for val in value:
            newVal = list(val)
            newVal.pop(indexToRemove)
            newValue.append(tuple(newVal))
        new_split_data[key] = newValue
        
    print(f"Split Data is: {new_split_data}")
    print(f"New Attribute List is {edited_list}")
    
    # Add nodes as children
    node.children = [Node(parent_attribute=key, parent_attr_type=splitting_node) for key in new_split_data.keys()]
    print(f"\n\nFUNCTION END\n\n")

    # Repeat for each child
    for child in node.children:
        create_tree(new_split_data[child.parent_attribute], edited_list, child)
    
    return node

df = pd.read_csv("ID3data.csv")
data = list(df.itertuples(index=False, name=None))
attribute_list = list(df.columns)

print(create_tree(data, attribute_list))