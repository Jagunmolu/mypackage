def top_n(items, n):
    """Returns the top n items in an array, in descending order.

    Args:
        items (array): list or array-like object.
        n (int): number of items to reeturn

    Return:
        array: top n items, in descending order.

    Egs:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 4]
    """
    for i in range(n): #keep sorting until we have the top n items
        for j in range(len(items)-i-1):

            if items[j] > items[j+1]: # if this item is bigger than the next one...
                items[j], items[j+1] = items[j+1], items[j] # swap the two

    # get last n items
    top_n = items[-n:]

    # return in descending order
    return top_n[::-1]