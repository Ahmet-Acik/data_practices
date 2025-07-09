# sorting 
# functions for sorting lists, tuples, and dictionaries in Python
from typing import List, Tuple, Dict, Any
def sort_list(arr: List[Any], reverse: bool = False) -> List[Any]:
    """
    Sort a list in ascending or descending order.
    
    :param arr: List of elements to sort.
    :param reverse: If True, sort in descending order; otherwise, sort in ascending order.
    :return: Sorted list.
    """
    return sorted(arr, reverse=reverse)

def sort_tuple(tup: Tuple[Any, ...], reverse: bool = False) -> Tuple[Any, ...]:
    """
    Sort a tuple in ascending or descending order.
    
    :param tup: Tuple of elements to sort.
    :param reverse: If True, sort in descending order; otherwise, sort in ascending order.
    :return: Sorted tuple.
    """
    return tuple(sorted(tup, reverse=reverse))

def sort_dict_by_keys(d: Dict[Any, Any], reverse: bool = False) -> Dict[Any, Any]:
    """
    Sort a dictionary by its keys in ascending or descending order.
    
    :param d: Dictionary to sort.
    :param reverse: If True, sort in descending order; otherwise, sort in ascending order.
    :return: Sorted dictionary by keys.
    """
    return dict(sorted(d.items(), key=lambda item: item[0], reverse=reverse))

