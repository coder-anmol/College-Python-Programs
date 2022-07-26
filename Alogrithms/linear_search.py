"""
Linear Search

1. Take an unsorted array.
2. Take search input.
3. Iterate over each element in list untill the search input is found.
4. Show the result.

"""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
search_query = 1


def linear_search(array, search_query):
    for i in range(0, len(array)):
        if (search_query == array[i]):
            return True
    return False


result = linear_search(numbers, search_query)
print(result)
