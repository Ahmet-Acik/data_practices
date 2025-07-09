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

def sort_dict_by_values(d: Dict[Any, Any], reverse: bool = False) -> Dict[Any, Any]:
    """
    Sort a dictionary by its values in ascending or descending order.
    
    :param d: Dictionary to sort.
    :param reverse: If True, sort in descending order; otherwise, sort in ascending order.
    :return: Sorted dictionary by values.
    """
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))

def sort_dict_by_items(d: Dict[Any, Any], reverse: bool = False) -> Dict[Any, Any]:
    """
    Sort a dictionary by its items (key-value pairs) in ascending or descending order.
    
    :param d: Dictionary to sort.
    :param reverse: If True, sort in descending order; otherwise, sort in ascending order.
    :return: Sorted dictionary by items.
    """
    return dict(sorted(d.items(), key=lambda item: (item[0], item[1]), reverse=reverse))

def sort_dict_by_custom_key(d: Dict[Any, Any], key_func: callable, reverse: bool = False) -> Dict[Any, Any]:
    """
    Sort a dictionary by a custom key function in ascending or descending order.
    
    :param d: Dictionary to sort.
    :param key_func: Function to extract the sorting key from each item.
    :param reverse: If True, sort in descending order; otherwise, sort in ascending order.
    :return: Sorted dictionary by custom key.
    """
    return dict(sorted(d.items(), key=key_func, reverse=reverse))

def sort_dict_by_length(d: Dict[Any, Any], reverse: bool = False) -> Dict[Any, Any]:
    """
    Sort a dictionary by the length of its keys or values in ascending or descending order.
    
    :param d: Dictionary to sort.
    :param reverse: If True, sort in descending order; otherwise, sort in ascending order.
    :return: Sorted dictionary by length of keys or values.
    """
    return dict(sorted(d.items(), key=lambda item: (len(str(item[0])), len(str(item[1]))), reverse=reverse))

