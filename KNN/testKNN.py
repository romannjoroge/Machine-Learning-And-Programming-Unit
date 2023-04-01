from typing import Tuple
Vector = Tuple[float]
from KNN import euclidian_distance, square_block_distance, calculate_distances, select_neighbor, predict_neighbor

def test_euclidian_distance():
    print(f"\n\n------------------------EUCLIDIAN DISTANCE TEST----------------------------\n\n")
    try :
        print("Making a and b values that aren't tuples")
        euclidian = euclidian_distance('Hi', "Dude")
    except AssertionError as e:
        print(e)
        print("TEST 1 PASS")
    except Exception as e:
        print(e)
        print("Wrong Error Thrown")
        print()
    else:
        print("TEST 1 FAIL: Error Was Meant To Be Thrown")
    finally:
        print("------------------------TEST 1----------------------------")
    
    # Testing with inputs of different lengths
    try:
        print("Making a and b have different lenghts")
        euclidian = euclidian_distance((1, 2), (1, 2, 3))        
    except AssertionError as err:
        print(err)
        print("TEST 2 PASS")
    except Exception as e:
        print(e)
        print("TEST 2 FAIL: Wrong Error Thrown")
    else:
        print("TEST 2 FAIL Error Meant To Be Thrown")
    finally:
        print("------------------------TEST 2----------------------------")

    # Checking that right value is returned
    try:
        assert euclidian_distance((1, 2), (1, 2)) == 0
        print("TEST 3 PASS")
    except Exception as e:
        print(e)
        print("TEST 3 FAILED: Wrong Value Returned")
    finally:
        print("------------------------TEST 3----------------------------")

def test_square_distance():
    print(f"\n\n------------------------SQUARE DISTANCE TEST----------------------------\n\n")
    try:
        print("Testing that a and b have to be tuples")
        square_block_distance("Hi", "Dude")
    except AssertionError as e:
        print(e)
        if str(e) == "a and b should be points":
            print("TEST 1 PASS")
        else:
            print("TEST 1 FAILED: Wrong Assertion Thrown")
    except Exception as e:
        print(e)
        print("TEST 1 FAILED: Wrong Error Thrown")
    else:
        print("TEST 1 FAILED: Error Not Thrown")
    finally:
        print("------------------------TEST 1----------------------------")

    try:
        print("Testing that a and b have to be of the same length")
        square_block_distance((1,), (1, 2))
    except AssertionError as err:
        print(err)
        if str(err) == "a and b should have the same dimensionality":
            print("TEST 2 PASS")
        else:
            print("TEST 2 FAILED: Wrong Assertion Thrown")
    except Exception as err:
        print(err)
        print("TEST 2 FAILED: Wrong Error Thrown")
    else:
        print("TEST 2 FAILED: Error Not Thrown")
    finally:
        print("------------------------TEST 2----------------------------")

    try:
        print("Testing that right value is returned")
        square_distance = square_block_distance((1, 2), (3, 4))
        assert square_distance == 4
    except AssertionError:
        print("TEST 3 FAILED: Returned Value Not Same")
    except Exception as e:
        print(e)
        print("TEST 3 FAILED: Wrong Error Thrown")
    else:
        print("TEST 3 PASS")
    finally:
        print("------------------------TEST 3----------------------------")

def test_calculate_distance():
    print(f"\n\n------------------------CALCULATE DISTANCE TEST----------------------------\n\n")
    try:
        print("Asserting that it throws an error if distance is not a function")
        calculate_distances([(1,), (2,), (3,)], "Hello", (1, 2))
    except AssertionError as e:
        if str(e) == "distance should be a function":
            print("TEST 1 PASS")
        else:
            print(e)
            print("TEST 1 FAIL: Wrong Assertion Thrown")
    except Exception as e:
        print(e)
        print("TEST 1 FAIL: Wrong Error Thrown")
    else:
        print("TEST 1 FAIL: Error Should Be Thrown")
    finally:
        print("------------------------TEST 1----------------------------")

    try:
        print("Asserting that correct distances are returned")
        distances = calculate_distances([(5, 2), (6, 7)], square_block_distance, (1, 1))
        assert [5, 11] == distances, "Wrong Value Returned"
        print("TEST 2 PASS")
    except AssertionError as e:
        if str(e) == "Wrong Value Returned":
            print(f"TEST 2 FAIL: {str(e)}")
            print(f"Returned Value Was {distances}")
        else:
            print(e)
            print("TEST 2 FAIL: Wrong Assertion Thrown")
    except Exception as e:
        print(e)
        print("TEST 2 FAIL: Error Thrown")
    finally:
        print("------------------------TEST 2----------------------------")


def test_select_neighbor():
    print(f"\n\n------------------------SELECT NEIGHBOR TEST----------------------------\n\n")
    try:
        print("Assert that function should only accept a list of floats as distances")
        select_neighbor(['I', 'will', 'break', 'your', 'code'], ['Boom'])
    except AssertionError as e:
        if str(e) == "distances should contain floats":
            print("TEST 1 PASS")
        else:
            print(e)
            print("TEST 1 FAIL: Wrong Assertion Thrown")
    except Exception as e:
        print(e)
        print("TEST 1 FAIL: Wrong Error Thrown")
    else:
        print("TEST 1 FAIL: Error Not Thrown")
    finally:
        print("------------------------TEST 1----------------------------")

    try:
        print("Assert That Function Returns Correct Value")
        predicted_class = select_neighbor([5, 11], ['A', 'B'])
        assert predicted_class == 'A', "Wrong Class Predicted"
    except AssertionError as e:
        if str(e) == "Wrong Class Predicted":
            print(f"TEST 2 FAIL: {str(e)}")
        else:
            print(e)
            print("TEST 2 FAIL: Assertion Thrown")
    except Exception as e:
        print(e)
        print("TEST 2 FAILED: Error Thrown")
    else:
        print("TEST 2 PASS")
    finally:
        print("------------------------TEST 2----------------------------")

def test_predict_neighbor():
    print(f"\n\n------------------------PREDICT NEIGHBOR TEST----------------------------\n\n")
    try:
        print("Testing If Correct Neighbor is predicted")
        neigbor = predict_neighbor("test_data.csv", (5,1), square_block_distance)
        assert neigbor == 'B', "Wrong Class Predicted"
    except AssertionError as e:
        if str(e) == "Wrong Class Predicted":
            print(f"TEST 1 FAIL: {str(e)}")
        else:
            print(e)
            print("TEST 1 FAIL: Wrong Assertion Error Thrown")
    except Exception as e:
        print(e)
        print("TEST 1 FAIL: Error Thrown")
    else:
        print("TEST 1 PASS")
    finally:
        print("------------------------TEST 1----------------------------")

def test() :
    test_euclidian_distance()
    test_square_distance()
    test_calculate_distance()
    test_select_neighbor()
    test_predict_neighbor()

test()