def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    my_dict = dict.fromkeys(a)

    for key in my_dict.keys():

        if key == 0:
            continue

        if my_dict.__contains__(key * -1) and key > 0:
            result.append(key)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
