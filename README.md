## lrucache (least-recently-used cache)
>It is a cache replacement policy that evicts the element which was not used for the longest period of time. For more information visit https://en.wikipedia.org/wiki/Cache_replacement_policies.

##### lrucache:
  
  *description:* **`LruCache(limit = 1024)`** *it creates a empty lru cache with a specified limit*
  
  *space-complexity:* **`O(n)`** *where **n** is the no of elements in the cache*
  
  ```python
  from lrucache import LruCache
  ob = LruCache(size = 2056)
  # Now u cud insert 2056 things into the cache 
  ```
  
##### put:

  *description:* **`put(k, v = None)`** *it inserts **k, v** into the cache, existing element will be over-written*
  
  *time-complexity:* **`O(1)`**
  
  ```python
  ob.put(1001, 'apple')
  ob.put('red', 'blood')
  ```
  
##### get:

  *description:* **`get(k)`** *it returns **k, v** from the cache, if no such then returns None*
  
  *time-complexity:* **`O(1)`**
  
  ```python
  print(ob.get(1001))
  # will print
  # (1001, 'apple')
  ```

##### pop:

  *description:* **`pop(k)`** *it pops out **k, v** from the cache, if no such then returns None*
  
  *time-complexity:* **`O(1)`**
  
  ```python
  print(ob.pop(1001))
  # will print and delete
  # (1001, 'apple')
  ```
 
##### clear:

  *description:* **`clear()`** *it clears/empties the cache*
  
  *time-complexity:* **`O(1)`**
  
  ```python
  ob.clear()
  ```

##### size:

  *description:* **`size`** *it returns the max no of elements that could be added in the cache*
  
  *time-complexity:* **`O(1)`**
  
  ```python
  print(ob.size)
  # will print
  # 2056
  ```

##### faults:

  *description:* **`faults()`** *it returns the no of faults occurred until last put*
  
  *time-complexity:* **`O(1)`**
  
  ```python
  print(ob.faults())
  # will print
  # 2
  ```
  
##### resize:

  *description:* **`resize(new_size)`** *resizes the cache to new_size, if new_size is less than the old_size then discards the old elements in proper order*
  
  *time-complexity:* **`if new_size is less than old_size, then O(old_size - new_size) else O(1)`**
  
  ```python
  ob.resize(1024)
  ```

##### isEmpty:

  *description:* **`isEmpty()`** *it checks whether the cache is empty or not*
  
  *time-complexity:* **`O(1)`**
  
  ```python
  print(ob.isEmpty())
  # will print
  # False
  ```
