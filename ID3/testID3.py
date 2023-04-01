from ID3 import calculate_information, calculate_entropy, calculate_information_gain, select_best_attribute, split_data, get_information_gains


def test_calculate_information():
    print(f"\n\n------------------------CALCULATE INFORMATION TEST----------------------------\n\n")
    try:
        print("Asserting that it rejects invalid types")
        calculate_information("Break", "Code")
    except AssertionError as e:
        if str(e) == "Parameters must be ints":
            print("TEST 1 PASS")
        else:
            print(e)
            print("TEST 1 FAIL: Wrong Assertion Thrown")
    except Exception as e:
        print(e)
        print("TEST 1 FAIL: Error Thrown")
    else:
        print("TEST 1 FAIL: No Error Thrown")
    finally:
        print("------------------------TEST 1----------------------------")

    try:
        print("Test That function Returns Right Thing")
        assert 0 == calculate_information(1, 1), "Wrong Value Returned"
    except AssertionError as e:
        print(e)
        print(f"TEST 1 FAIL: {e}")
    except Exception as e:
        print(e)
        print("TEST 2 FAIL: Error Thrown")
    else:
        print("TEST 2 PASS")
    finally:
        print("------------------------TEST 2----------------------------")


def test_calculate_entropy():
    print(f"\n\n------------------------CALCULATE ENTROPY TEST----------------------------\n\n")
    try:
        print("Assert that it only takes a list of tuples")
        calculate_entropy(['Hello', 12])
    except AssertionError as e:
        if str(e) == "data should be a list of points":
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
        print("See if Function Returns Right Thing")
        assert calculate_entropy(
            [(1, "One"), (1, "Two")]) == 1, "Wrong Value Returned"
    except AssertionError as e:
        print(e)
        print(f"TEST 2 FAIL: {e}")
    except Exception as e:
        print(e)
        print("TEST 2 FAIL: Error Thrown")
    else:
        print("TEST 2 PASS")
    finally:
        print("------------------------TEST 2----------------------------")

    try:
        print("See if Function Returns 0 if values of 1 attribute are in data")
        assert calculate_entropy(
            [(1, "One"), (2, "One"), (3, "One")]) == 0, "Wrong Value Returned"
    except AssertionError as e:
        print(f"TEST 3 FAIL: {e}")
    except Exception as e:
        print(e)
        print("Test 3 FAIL: Error Thrown")
    else:
        print("TEST 3 PASS")
    finally:
        print("------------------------TEST 3----------------------------")


def test_calculate_information_gain():
    print(f"\n\n------------------------CALCULATE INFORMATION GAIN TEST----------------------------\n\n")
    try:
        print("Assert that attribute is in attribute list")
        calculate_information_gain([(1, "One")], 'NA', ['Not Here'])
    except AssertionError as e:
        if str(e) == "attribute should be in attribute_list":
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
        print("Assert That The Number of Attributes in attribute list is same as those in data")
        calculate_information_gain([(1,)], "Test", ['Test', 'Missing Value'])
    except AssertionError as e:
        if str(e) == "All attributes in attribute list should be in data":
            print("TEST 2 PASS")
        else:
            print(e)
            print("TEST 2 FAIL: Wrong Assertion Thrown")
    except Exception as e:
        print(e)
        print("TEST 2 FAIL: Wrong Error Thrown")
    else:
        print("TEST 2 FAIL: Error Not Thrown")
    finally:
        print("------------------------TEST 2----------------------------")

    try:
        print("Assert That Function Returns Right Thing")
        inforamtion_gain = calculate_information_gain([
            ('Red', 'Square', 'Big', 'Like'),
            ('Blue', 'Square', 'Big', 'Like'),
            ('Red', 'Round', 'Small', 'Dislike'),
            ('Green', 'Square', 'Small', 'Dislike'),
            ('Red', 'Round', 'Big', 'Like'),
            ('Green', 'Round', 'Big', 'Dislike'),
        ], 'Shape', ['Colour', 'Shape', 'Size', 'Class'])
        assert round(inforamtion_gain, 4) == 0.0817
    except AssertionError as e:
        print(e)
        print(f"TEST 3 FAIL: {e}")
    except Exception as e:
        print(e)
        print("TEST 3 FAIL")
    else:
        print("TEST 3 PASS")
    finally:
        print("------------------------TEST 3----------------------------")

def test_select_best_attribute():
    print(f"\n\n------------------------SELECT BEST ATTRIBUTE TEST----------------------------\n\n")
    try:
        print("Assert That It Only Accepts a Dictionary")
        select_best_attribute(['q', '1'])
    except AssertionError as e:
        if str(e) == "information gains should be a dictionary":
            print("TEST 1 PASS")
        else:
            print(e)
            print(f"TEST 1 FAIL: {e}")
    except Exception as e:
        print(e)
        print("TEST 1 FAIL: Wrong Error Thrown")
    else:
        print("TEST 1 FAIL: No Error Thrown")
    finally:
        print("------------------------TEST 1----------------------------")

    try:
        print("Test if Function Returns Right Thing")
        att = select_best_attribute({"small": 1, "medium": 2, "large": 3})
        assert att == "large", "Wrong Value Returned"
    except AssertionError as e:
        print(f"TEST 2 FAIL: {e}")
        print(f"att is {att}")
    except Exception as e:
        print(e)
        print("TEST 2 FAIL: Wrong Error Thrown")
    else:
        print("TEST 2 PASS")
    finally:
        print("------------------------TEST 2----------------------------")

def test_split_data():
    print(f"\n\n------------------------SPLIT DATA TEST----------------------------\n\n")
    try:
        print("Assert That splitting attribute is in attribute_list")
        split_data([(1, 2), (1, 1)], "Not There", ["Random"])
    except AssertionError as e:
        if str(e) == "splitting attribue should be in attribute list":
            print("TEST 1 PASS")
        else:
            print(f"TEST 1 FAIL Assertion {e} Thrown")
    except Exception as e:
        print(e)
        print("TEST 1 FAIL: Wrong Error Thrown")
    else:
        print("TEST 1 FAIL: No Error Thrown")
    finally:
        print("------------------------TEST 1----------------------------")

    try:
        print("Assert That It Only Accepts a list of tuples")
        split_data([1, (1, 1)], "Not There", ["Not There"])
    except AssertionError as e:
        if str(e) == "data should contain a list of points":
            print("TEST 2 PASS")
        else:
            print(f"TEST 2 FAIL Assertion {e} Thrown")
    except Exception as e:
        print(e)
        print("TEST 2 FAIL: Wrong Error Thrown")
    else:
        print("TEST 2 FAIL: No Error Thrown")
    finally:
        print("------------------------TEST 2----------------------------")

    try:
        print("Assert that attribute list and data points should be the same length")
        split_data([(1, 2), (1, 2)], "Test", ["Test", "Test1", "Test2"])
    except AssertionError as e:
        if str(e) == "data points should have as many attributes as attribute_list":
            print("TEST 3 PASS")
        else:
            print(f"TEST 3 FAIL Assertion {e} Thrown")
    except Exception as e:
        print(e)
        print("TEST 3 FAIL: Wrong Error Thrown")
    else:
        print("TEST 3 FAIL: No Error Thrown")
    finally:
        print("------------------------TEST 3----------------------------")

    try:
        print("Test if function returns right thing")
        split_list = split_data([(1, 1), (1, 2), (2, 1), (2, 2)], "One", ["One", "Two"])
        assert split_list == {
            1: [(1, 1), (1, 2)],
            2: [(2, 1), (2, 2)]
        }, "Wrong Value Returned"
    except AssertionError as e:
        print(f"TEST 4 FAIL: {e}")
        print(f"split_list is {split_list}")
    except Exception as e:
        print(e)
        print("TEST 4 FAIL: Wrong Error Thrown")
    else:
        print("TEST 4 PASS")
    finally:
        print("------------------------TEST 4----------------------------")


def test_get_information_gains():
    print(f"\n\n------------------------GET INFORMATION GAINS TEST----------------------------\n\n")
    try:
        print("Asserting that it can only accept a list of tuples as an argument")
        get_information_gains([1, '1'], ["Hey"])
    except AssertionError as e:
        if str(e) == "data should contain points":
            print("TEST 1 PASS")
        else:
            print(f"TEST 1 FAIL Assertion {e} Thrown")
    except Exception as e:
        print(e)
        print("TEST 1 FAIL: Wrong Error Thrown")
    else:
        print("TEST 1 FAIL: No Error Thrown")
    finally:
        print("------------------------TEST 1----------------------------")
    
    try:
        print("Asserting that each data point is as long as attribute list")
        get_information_gains([(1,), (2,)], ["Hey", "There"])
    except AssertionError as e:
        if str(e) == "data should contain as many value as attribute list":
            print("TEST 2 PASS")
        else:
            print(f"TEST 2 FAIL Assertion {e} Thrown")
    except Exception as e:
        print(e)
        print("TEST 2 FAIL: Wrong Error Thrown")
    else:
        print("TEST 2 FAIL: No Error Thrown")
    finally:
        print("------------------------TEST 2----------------------------")

    try:
        print("Asserting That it Returns Right Thing")
        infGains = get_information_gains([
            ('Red', 'Square', "Big", "Like"),
            ('Blue', 'Square', "Big", "Like"),
            ('Red', 'Round', "Small", "Dislike"),
            ('Green', 'Square', "Small", "Dislike"),
            ('Red', 'Round', "Big", "Like"),
            ('Green', 'Round', "Big", "Dislike"),
        ], ["Colour", "Shape", "Size", "Like"])
        assert infGains == dict({
            "Color": 0.5409,
            "Shape": 0.0817,
            "Size": 0.4591
        }), "Wrong Value Returned"
    except AssertionError as e:
        print(f"TEST 4 FAIL: {e}")
        print(f"infGains is {infGains}")
        print(type(dict))
    except Exception as e:
        print(e)
        print("TEST 4 FAIL: Wrong Error Thrown")
    else:
        print("TEST 4 PASS")
    finally:
        print("------------------------TEST 4----------------------------")


def test():
    test_calculate_information()
    test_calculate_entropy()
    test_calculate_information_gain()
    test_select_best_attribute()
    test_split_data()
    test_get_information_gains()


test()
