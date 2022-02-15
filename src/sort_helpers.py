"""
    Helper functions for sorting food items.
"""

def _swap(lst, index1, index2):
    """
        Given a list and two indices, swap the elements at those indices.
        Assume the indices are in bounds.
    """
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst


def _partition_by_calories(list_of_foods, start, end):
    """
        Apply quick sort algorithm to the list of foods:
            1) select the last item as pivot
            2) move all items with fewer calories than the pivot in front of it,
                and all items with more calories than the pivot behind it
        This method is where most of the sorting work is done.
        :param list_of_foods: list of FoodItem objects to sort
        :param start: start index of list we're trying to sort
        :param end: end index of list we're trying to sort
        :return: the index of the pivot item. When this function exits, the pivot
            is guaranteed to be in its proper position.
    """
    pivot = list_of_foods[end].calories
    pivot_index = start
    # Loop through the list, and put elements less than the pivot in front of
    # the pivot index.
    for i in range(start, end):
        if list_of_foods[i].calories <= pivot:
            _swap(list_of_foods, i, pivot_index)
            pivot_index += 1
    _swap(list_of_foods, pivot_index, end)  # move pivot to its proper position
    return pivot_index


def _partition_by_fat(list_of_foods, start, end):
    """
        Apply quick sort algorithm to the list of foods:
            1) select the last item as pivot
            2) move all items with less fat than the pivot in front of it,
                and all items with more fat than the pivot behind it
        This method is where most of the sorting work is done.
        :param list_of_foods: list of FoodItem objects to sort
        :param start: start index of list we're trying to sort
        :param end: end index of list we're trying to sort
        :return: the index of the pivot item. When this function exits, the pivot
            is guaranteed to be in its proper position.
        """
    pivot = list_of_foods[end].fat
    pivot_index = start
    # Loop through the list, and put elements less than the pivot in front of
    # the pivot index.
    for i in range(start, end):
        if list_of_foods[i].fat <= pivot:
            _swap(list_of_foods, i, pivot_index)
            pivot_index += 1
    _swap(list_of_foods, pivot_index, end)  # move pivot to its proper position
    return pivot_index


def _partition_by_taste_score(list_of_foods, start, end):
    """
        Apply quick sort algorithm to the list of foods:
            1) select the last item as pivot
            2) move all items with less taste score than the pivot in front of it,
                and all items with more taste score than the pivot behind it
        This method is where most of the sorting work is done.
        :param list_of_foods: list of FoodItem objects to sort
        :param start: start index of list we're trying to sort
        :param end: end index of list we're trying to sort
        :return: the index of the pivot item. When this function exits, the pivot
            is guaranteed to be in its proper position.
    """
    pivot = list_of_foods[end].taste_score
    pivot_index = start
    # Loop through the list, and put elements less than the pivot in front of
    # the pivot index.
    for i in range(start, end):
        if list_of_foods[i].taste_score <= pivot:
            _swap(list_of_foods, i, pivot_index)
            pivot_index += 1
    _swap(list_of_foods, pivot_index, end)  # move pivot to its proper position
    return pivot_index


def _quicksort_food_by_calories(list_of_foods, start, end):
    """
        Sort the list of foods by ascending calories.
        :param list_of_foods: list of FoodItem objects to sort
        :param start: start index of list we're trying to sort
        :param end: end index of list we're trying to sort
        :return: None
    """
    if start < end:
        pivot_index = _partition_by_calories(list_of_foods, start, end)
        _quicksort_food_by_calories(list_of_foods, start, pivot_index - 1)
        _quicksort_food_by_calories(list_of_foods, pivot_index + 1, end)


def _quicksort_food_by_fat():
    """
        Sort the list of foods by ascending fat.
        :param list_of_foods: list of FoodItem objects to sort
        :param start: start index of list we're trying to sort
        :param end: end index of list we're trying to sort
        :return: None
    """
    if start < end:
        pivot_index = _partition_by_fat(list_of_foods, start, end)
        _quicksort_food_by_fat(list_of_foods, start, pivot_index - 1)
        _quicksort_food_by_fat(list_of_foods, pivot_index + 1, end)


def _quicksort_food_by_taste_score():
    """
        Sort the list of foods by ascending taste score.
        :param list_of_foods: list of FoodItem objects to sort
        :param start: start index of list we're trying to sort
        :param end: end index of list we're trying to sort
        :return: None
    """
    if start < end:
        pivot_index = _partition_by_taste_score(list_of_foods, start, end)
        _quicksort_food_by_taste_score(list_of_foods, start, pivot_index - 1)
        _quicksort_food_by_taste_score(list_of_foods, pivot_index + 1, end)

