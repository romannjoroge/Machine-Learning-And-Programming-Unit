import math
from collections import Counter, defaultdict
from typing import List, Tuple, Dict
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

def get_information_gains(data: List[Tuple], attribute_list: List[str]) -> List[Dict[str, float]]:
    """
    Get information gains of all attributes in data
    Inputs:
        data: A list of all the data points in system
        attribute_list: List of all attributes in data
    Outputs:
        A dictionary containing name of attribute and information gain
    """
    # Get information gain of every attribute
    information_gains = defaultdict(float)
    for i in range(len(attribute_list) - 1):
        information_gains[attribute_list[i]] = calculate_information_gain(data, attribute_list[i], attribute_list)

    # Return list
    return information_gains

df = pd.read_csv("testID3.csv")
data = list(df.itertuples(index=False, name=None))
attribute_list = list(df.columns)

print(get_information_gains(data, attribute_list))