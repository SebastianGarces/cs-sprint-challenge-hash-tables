def get_indices_of_item_weights(weights, length, limit):

    my_dict = {}
    result = []

    if length == 2 and weights[0] + weights[1] == limit:
        return (1, 0)

    for index in range(length):
        my_dict.setdefault(weights[index], index)

    for weight, index in my_dict.items():
        if my_dict.__contains__((limit - weight)):
            result.append(index)

    if len(result) > 0:
        if result[0] < result[1]:
            result.reverse()

        return (result[0], result[1])

    return None
