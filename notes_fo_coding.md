## itertools
### **1. Subset and Arrangement Problems**
#### **(a) Combinations**: Find subsets of a given size.
- Use when **order doesn't matter**.
```python
from itertools import combinations

# Example: Subsets of size 2 from [1, 2, 3]
nums = [1, 2, 3]
result = list(combinations(nums, 2))  # [(1, 2), (1, 3), (2, 3)]
```

#### **(b) Permutations**: Find all arrangements of a given size.
- Use when **order matters**.
```python
from itertools import permutations

# Example: All arrangements of size 2 from [1, 2, 3]
nums = [1, 2, 3]
result = list(permutations(nums, 2))  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
```

#### **(c) Product**: Cartesian product for arrangements with repetition.
- Use for **repetition** or **multi-dimensional grids**.
```python
from itertools import product

# Example: Cartesian product of [1, 2] repeated 2 times
nums = [1, 2]
result = list(product(nums, repeat=2))  # [(1, 1), (1, 2), (2, 1), (2, 2)]
```

---

### **2. Prefix Sums or Running Totals**
#### **(a) Accumulate**: Compute cumulative sums or other aggregates.
- Use for prefix sums, cumulative products, or custom aggregates.
```python
from itertools import accumulate

# Example: Prefix sums of [1, 2, 3, 4]
nums = [1, 2, 3, 4]
result = list(accumulate(nums))  # [1, 3, 6, 10]

# Example: Cumulative product
import operator
result = list(accumulate(nums, operator.mul))  # [1, 2, 6, 24]
```

---

### **3. Sorting and Categorizing Data**
#### **(a) Groupby**: Group elements by a key function.
- Use for grouping sorted data efficiently.
```python
from itertools import groupby

# Example: Group consecutive identical elements
data = 'aaabbcccaaa'
grouped = {key: list(group) for key, group in groupby(data)}
# Result: {'a': ['a', 'a', 'a'], 'b': ['b', 'b'], 'c': ['c', 'c', 'c']}

# Example: Group numbers by even/odd
nums = [1, 2, 2, 3, 4, 5]
grouped = {key: list(group) for key, group in groupby(sorted(nums), key=lambda x: x % 2)}
# Result: {1: [1, 3, 5], 0: [2, 2, 4]}
```

---

### **4. Lazy Slicing and Filtering**
#### **(a) Islice**: Slice without creating a full list.
- Use for efficient slicing of iterators.
```python
from itertools import islice

# Example: Take a slice of range(10) from index 2 to 8 with step 2
result = list(islice(range(10), 2, 8, 2))  # [2, 4, 6]
```

#### **(b) Filterfalse**: Filter elements where the predicate is `False`.
- Use for excluding specific elements.
```python
from itertools import filterfalse

# Example: Filter out even numbers from range(10)
result = list(filterfalse(lambda x: x % 2 == 0, range(10)))  # [1, 3, 5, 7, 9]
```

---

### **Examples in Practice**
#### Example 1: Generate all valid subsets of a set (power set).
```python
from itertools import combinations

nums = [1, 2, 3]
power_set = [list(combo) for r in range(len(nums) + 1) for combo in combinations(nums, r)]
# Result: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```

#### Example 2: Categorize strings by their starting letter.
```python
from itertools import groupby

strings = ['apple', 'banana', 'apricot', 'blueberry', 'cherry']
grouped = {key: list(group) for key, group in groupby(sorted(strings), key=lambda x: x[0])}
# Result: {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
```

#### Example 3: Running total of scores in a game.
```python
from itertools import accumulate

scores = [10, 20, -5, 30]
cumulative_scores = list(accumulate(scores))  # [10, 30, 25, 55]
```

---
