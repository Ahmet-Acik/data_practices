"""
Python Collections Framework Demo
Comparing Python collections to Java Collections Framework
"""

from collections import (
    Counter, defaultdict, OrderedDict, deque, 
    namedtuple, ChainMap
)
import heapq
from typing import List, Dict, Set, Tuple


def basic_collections_demo():
    """
    Demonstrate basic Python collections similar to Java Collections
    """
    print("=== Basic Python Collections (similar to Java) ===\n")
    
    # 1. LIST (similar to Java ArrayList/LinkedList)
    print("1. LIST (like Java ArrayList):")
    my_list = []  # or list()
    my_list.append("apple")     # add()
    my_list.append("banana")
    my_list.insert(1, "orange") # add(index, element)
    print(f"   List: {my_list}")
    print(f"   Size: {len(my_list)}")  # size()
    print(f"   Get index 1: {my_list[1]}")  # get(index)
    my_list.remove("orange")    # remove()
    print(f"   After removing 'orange': {my_list}")
    print(f"   Contains 'apple': {'apple' in my_list}")  # contains()
    print()
    
    # 2. DICT (similar to Java HashMap/TreeMap)
    print("2. DICT (like Java HashMap):")
    my_dict = {}  # or dict()
    my_dict["name"] = "John"     # put(key, value)
    my_dict["age"] = 30
    my_dict["city"] = "New York"
    print(f"   Dict: {my_dict}")
    print(f"   Get 'name': {my_dict.get('name')}")  # get(key)
    print(f"   Keys: {list(my_dict.keys())}")        # keySet()
    print(f"   Values: {list(my_dict.values())}")    # values()
    print(f"   Items: {list(my_dict.items())}")      # entrySet()
    print(f"   Contains key 'age': {'age' in my_dict}")  # containsKey()
    del my_dict["city"]  # remove(key)
    print(f"   After removing 'city': {my_dict}")
    print()
    
    # 3. SET (similar to Java HashSet/TreeSet)
    print("3. SET (like Java HashSet):")
    my_set = set()  # or set()
    my_set.add("red")      # add()
    my_set.add("green")
    my_set.add("blue")
    my_set.add("red")      # Duplicates ignored
    print(f"   Set: {my_set}")
    print(f"   Size: {len(my_set)}")  # size()
    print(f"   Contains 'red': {'red' in my_set}")  # contains()
    my_set.remove("green")  # remove()
    print(f"   After removing 'green': {my_set}")
    print()
    
    # 4. TUPLE (immutable sequence)
    print("4. TUPLE (immutable sequence):")
    my_tuple = ("apple", "banana", "cherry")
    print(f"   Tuple: {my_tuple}")
    print(f"   Index 1: {my_tuple[1]}")
    print(f"   Length: {len(my_tuple)}")
    print(f"   Immutable - cannot modify elements")
    print()


def advanced_collections_demo():
    """
    Demonstrate advanced collections from collections module
    """
    print("=== Advanced Collections Module ===\n")
    
    # 1. COUNTER (like Java's frequency counting)
    print("1. COUNTER (counting elements):")
    text = "hello world"
    counter = Counter(text)
    print(f"   Counter for '{text}': {counter}")
    print(f"   Most common 3: {counter.most_common(3)}")

    
    # Counting list elements
    fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    fruit_counter = Counter(fruits)
    print(f"   Fruit counter: {fruit_counter}")
    print()
    
    # 2. DEFAULTDICT (automatic default values)
    print("2. DEFAULTDICT (automatic default values):")
    dd = defaultdict(list)  # Default value is empty list
    dd["fruits"].append("apple")
    dd["fruits"].append("banana")
    dd["vegetables"].append("carrot")
    print(f"   DefaultDict: {dict(dd)}")
    
    # Grouping example
    dd_int = defaultdict(int)  # Default value is 0
    words = ["apple", "banana", "cherry", "apricot", "blueberry"]
    for word in words:
        dd_int[word[0]] += 1  # Count words by first letter
    print(f"   Words by first letter: {dict(dd_int)}")
    print()
    
    # 3. ORDEREDDICT (maintains insertion order - less needed in Python 3.7+)
    print("3. ORDEREDDICT (maintains insertion order):")
    od = OrderedDict()
    od["first"] = 1
    od["second"] = 2
    od["third"] = 3
    print(f"   OrderedDict: {od}")
    od.move_to_end("first")  # Move to end
    print(f"   After moving 'first' to end: {od}")
    print()
    
    # 4. DEQUE (double-ended queue, like Java ArrayDeque)
    print("4. DEQUE (double-ended queue, like Java ArrayDeque):")
    dq = deque(["middle"])
    dq.appendleft("left")    # addFirst()
    dq.append("right")       # addLast()
    dq.appendleft("far_left")
    print(f"   Deque: {dq}")
    print(f"   Pop left: {dq.popleft()}")   # removeFirst()
    print(f"   Pop right: {dq.pop()}")      # removeLast()
    print(f"   After pops: {dq}")
    
    # Rotating deque
    dq.extend([1, 2, 3])
    print(f"   Extended: {dq}")
    dq.rotate(2)  # Rotate right by 2
    print(f"   After rotate(2): {dq}")
    print()
    
    # 5. NAMEDTUPLE (immutable objects with named fields)
    print("5. NAMEDTUPLE (immutable objects with named fields):")
    Person = namedtuple('Person', ['name', 'age', 'city'])
    person1 = Person("Alice", 30, "New York")
    person2 = Person("Bob", 25, "Los Angeles")
    
    print(f"   Person1: {person1}")
    print(f"   Name: {person1.name}, Age: {person1.age}")
    print(f"   Person2: {person2}")
    
    # Converting to dict
    print(f"   Person1 as dict: {person1._asdict()}")
    print()
    
    # 6. CHAINMAP (combine multiple dicts)
    print("6. CHAINMAP (combine multiple dicts):")
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    dict3 = {"e": 5, "a": 10}  # 'a' will be overridden by dict1
    
    cm = ChainMap(dict1, dict2, dict3)
    print(f"   ChainMap: {cm}")
    print(f"   Value for 'a': {cm['a']}")  # Gets from first dict
    print(f"   All keys: {list(cm.keys())}")
    print()


def java_comparison_examples():
    """
    Show direct comparisons between Java and Python collections
    """
    print("=== Java vs Python Collections Comparison ===\n")
    
    print("JAVA CODE                           |  PYTHON EQUIVALENT")
    print("-" * 70)
    print("List<String> list = new ArrayList<>();  |  my_list = [] or list()")
    print("list.add(\"item\");                     |  my_list.append(\"item\")")
    print("list.get(0);                         |  my_list[0]")
    print("list.size();                         |  len(my_list)")
    print("list.contains(\"item\");               |  \"item\" in my_list")
    print("list.remove(\"item\");                 |  my_list.remove(\"item\")")
    print()
    
    print("Map<String,Integer> map = new HashMap<>(); | my_dict = {} or dict()")
    print("map.put(\"key\", 42);                    | my_dict[\"key\"] = 42")
    print("map.get(\"key\");                        | my_dict.get(\"key\")")
    print("map.containsKey(\"key\");                | \"key\" in my_dict")
    print("map.keySet();                         | my_dict.keys()")
    print("map.values();                         | my_dict.values()")
    print()
    
    print("Set<String> set = new HashSet<>();      | my_set = set()")
    print("set.add(\"item\");                      | my_set.add(\"item\")")
    print("set.contains(\"item\");                 | \"item\" in my_set")
    print("set.remove(\"item\");                   | my_set.remove(\"item\")")
    print("set.size();                           | len(my_set)")
    print()
    
    print("Queue<String> queue = new LinkedList<>(); | from collections import deque")
    print("queue.offer(\"item\");                   | queue = deque(); queue.append(\"item\")")
    print("queue.poll();                          | queue.popleft()")
    print("queue.peek();                          | queue[0] (if not empty)")
    print()


def heap_priority_queue_demo():
    """
    Demonstrate Python's heapq module (similar to Java PriorityQueue)
    """
    print("=== Heap/Priority Queue (like Java PriorityQueue) ===\n")
    
    # Min heap (default)
    heap = []
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 4)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 5)
    
    print(f"Min heap: {heap}")
    print(f"Pop smallest: {heapq.heappop(heap)}")
    print(f"Heap after pop: {heap}")
    print(f"Peek smallest: {heap[0]}")
    
    # Convert list to heap
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    heapq.heapify(numbers)
    print(f"Heapified list: {numbers}")
    
    # Get n largest/smallest
    data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    print(f"3 largest: {heapq.nlargest(3, data)}")
    print(f"3 smallest: {heapq.nsmallest(3, data)}")
    print()


def practical_examples():
    """
    Practical examples using Python collections
    """
    print("=== Practical Examples ===\n")
    
    # 1. Word frequency counter
    print("1. Word Frequency Counter:")
    text = "the quick brown fox jumps over the lazy dog the fox is quick"
    words = text.split()
    word_count = Counter(words)
    print(f"   Text: {text}")
    print(f"   Word frequencies: {word_count}")
    print(f"   Most common word: {word_count.most_common(1)[0]}")
    print()
    
    # 2. Grouping data with defaultdict
    print("2. Grouping Students by Grade:")
    students = [
        ("Alice", "A"), ("Bob", "B"), ("Charlie", "A"),
        ("David", "C"), ("Eve", "B"), ("Frank", "A")
    ]
    
    grades = defaultdict(list)
    for name, grade in students:
        grades[grade].append(name)
    
    print(f"   Students by grade: {dict(grades)}")
    print()
    
    # 3. LRU Cache simulation using OrderedDict
    print("3. Simple LRU Cache using OrderedDict:")
    class LRUCache:
        def __init__(self, capacity):
            self.capacity = capacity
            self.cache = OrderedDict()
        
        def get(self, key):
            if key in self.cache:
                # Move to end (most recently used)
                self.cache.move_to_end(key)
                return self.cache[key]
            return None
        
        def put(self, key, value):
            if key in self.cache:
                self.cache.move_to_end(key)
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                # Remove least recently used (first item)
                self.cache.popitem(last=False)
    
    cache = LRUCache(3)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    print(f"   Cache after adding a,b,c: {dict(cache.cache)}")
    cache.get("a")  # Access 'a'
    cache.put("d", 4)  # This should remove 'b'
    print(f"   Cache after accessing 'a' and adding 'd': {dict(cache.cache)}")
    print()


def main():
    """
    Main function to run all demonstrations
    """
    print("PYTHON COLLECTIONS FRAMEWORK DEMO")
    print("=" * 50)
    print()
    
    basic_collections_demo()
    advanced_collections_demo()
    java_comparison_examples()
    heap_priority_queue_demo()
    practical_examples()
    
    print("=== Summary ===")
    print("Python's collections are more flexible and dynamic than Java's.")
    print("Key advantages:")
    print("- No need to declare types")
    print("- Mixed types allowed in collections")
    print("- Rich built-in methods and operations")
    print("- Powerful collections module for specialized needs")
    print("- Duck typing instead of interfaces")


if __name__ == "__main__":
    main()
