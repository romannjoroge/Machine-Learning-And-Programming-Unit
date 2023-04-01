"""
Author: Roman Njoroge
Version: V1
Functionality: Get 1-Nearest Neighbor using either euclidean or square distance method using data in a csv file
HOW TO RUN: Call the predict_neighbor function with the file location as a string, point you want to predict as a tuple and method to calculate
distance with

"""

from typing import Tuple, List, Callable
import math
import pandas as pd

Point = Tuple[float]

def euclidian_distance(a: Point, b: Point) -> float:
    """
    This function is used to calculate the euclidian distance between 2 Points.
    Inputs:
        a: Point
        b: Point
    Output:
        euclidian distance
    a and b are assumed to contain floats and be of the same length
    """
    assert type(a) is tuple and type(b) is tuple, "a and b should be Points"
    assert all(type(item) is float or type(item) is int for item in a), "a should contain numeric values"
    assert all(type(item) is float or type(item) is int for item in b), "b should contain numeric values"
    assert len(a) == len(b), "a and b should be of the same length"

    # Calculate squares of difference
    diff = []
    for i in range(len(a)):
        diff.append((a[i] - b[i]) ** 2)
    
    sum_differences = sum(diff)
    return math.sqrt(sum_differences)

def square_block_distance(a: Point, b: Point) -> float:
    """
    Returns the square block / manhattan distance between 2 points a and b
    Inputs:
        a: Point
        b: Point
    Output:
        float 
    Assumes that points a and b have the same dimensionality
    """
    # Assertions
    assert type(a) is tuple and type(b) is tuple, "a and b should be points"
    assert all(type(item) is float or type(item) is int for item in a), "a should contain numeric values"
    assert all(type(item) is float or type(item) is int for item in b), "b should contain numeric values"
    assert len(a) == len(b), "a and b should have the same dimensionality"

    # Calculate absolute sum of differences between values in a and b
    manhattan_distance = 0
    for i in range(len(a)):
        manhattan_distance += abs(a[i] - b[i])
    return manhattan_distance

# Load data as tuples
def load_data(csv_file: str) -> Tuple[List[str], List[Tuple]]:
    """
    Load data from a csv file and returns a list of class labels and data points as tuples
    Input:
        csv_file: str. Name of csv file
    Output:
        class_labels: List of class labels
        data: List of tuples
    Assumes csv_file is a string and that class lables are in a Category column
    """
    # Assertions
    assert type(csv_file) is str, "CSV file location must be a string"

    df = pd.read_csv(csv_file)
    class_labels = list(df['Category'].array)

    # Remove Category 
    df_no_class = df.drop(columns=['Category'])

    # Convert data to list of tuples
    data = list(df_no_class.itertuples(index=False, name=None))
    
    return class_labels, data

# Loop through all the data storing distance of each data point
def calculate_distances(data: List[Point], distance: Callable[[Point, Point], float], point: Point) -> List[float]:
    """
    The function accepts a list of Points and a function to calculate distance that takes 2 points and returns a float
    The function returns a list of distances
    """
    # Assertions
    assert type(data) is list, "data should be a list of points"
    assert callable(distance), "distance should be a function"
    assert type(point) is tuple, "point should be a point"

    # Calculate the distance between point and every element in data
    distances = list()
    for x in data:
        distances.append(distance(x, point))

    # Return list of distances
    return distances

# Select class of closest data point
def select_neighbor(distances: List[float], class_labels: List[str]) -> str:
    """
    Returns the category of the value with the lowest distance
    Inputs:
        distances: A list of the distances between a point to predict neighbor of and the other data points in system
        class_labels: A list of all the class labels of the points in the system

    Outputs:
        Label of the nearest neighbor 

    The function assumes that the ith value in class_labels is the class label for the distance between ith point and point to find
    neighbor of
    """
    # Assertions
    assert type(distances) is list, "distances should be a list of values"
    assert all(type(item) is float or type(item) is int for item in distances), "distances should contain floats"
    assert type(class_labels) is list, "class_labels should be a list of values"
    assert all(type(item) is str for item in class_labels), "class_labels should contain strings"
    assert len(distances) == len(class_labels), "distances and class_labels should be of the same length"

    # Find smallest value and its index
    min_value = min(distances)
    min_index = distances.index(min_value)

    # Return class label of min value
    return class_labels[min_index]

def predict_neighbor(csv_file: str, point: Point, distance: Callable[[Point, Point], float]) -> str:
    """
    Given the file location of a csv file containing data points and a point to predict class of it returns class using provided 
    distance
    """
    # Load data and class labels
    class_labels, data = load_data(csv_file)

    # Find distances
    distances = calculate_distances(data, distance, point)

    # Find nearest neighbor
    return select_neighbor(distances, class_labels)

print(predict_neighbor("data.csv", (10,30,5), square_block_distance))

