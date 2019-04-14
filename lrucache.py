'''ADT LruCache:
		isEmpty() O(1)
		size (@property) O(1)
		faults (@property) O(1)
		clear() O(1)
		put(k, v) Exp. O(1)
		get(k) Exp. O(1)
		pop(k) Exp. O(1)
		resize(new_size) O(size - new_size) if new_size < size else O(1)
'''

class LruCache:
	class __Node:
		def __init__(self, k, v):
			self._k = k
			self._v = v
			self._next = self._prev = None
			
		def __repr__(self):
			return '{}: {}'.format(self._k, self._v)
			
	def __init__(self, size = 1024):
		self._size = size if size >= 0 else 1
		self._head = self._tail = None
		self._map = {}
		self._faults = 0
		
	def __len__(self):
		return len(self._map)
		
	def __setitem__(self, k, v):
		self.put(k, v)
		
	def __getitem__(self, k):
		return self.get(k)
		
	def __delitem__(self, k):
		self.pop(k)
		
	def __repr__(self):
		return 'LruCache({})'.format(list(self))
		
	def __iter__(self):
		return self.items()
		
	def isEmpty(self):
		''' it returns True if the cache is empty
		'''
		return self._head == None
	
	@property	
	def faults(self):
		''' it returns fault count of the cache
		'''
		return self._faults
		
	@property	
	def size(self):
		''' it returns the size (capacity) of the cache
		'''
		return self._size
		
	def clear(self):
		''' it empties the cache
		'''
		self._head = self._tail = None
		self._map.clear()
		self._faults = 0
		
	@staticmethod
	def __shrink(self, new_size):
		s = self._size
		nod = self._tail
		while s > new_size:
			nod = nod._prev
			s -= 1
		self._tail = nod
		self._tail._next = None
		
	def resize(self, new_size):
		''' resizes the cache
		'''
		assert(new_size >= 1)
		if new_size < self._size:
			self.__shrink(self, new_size)
		self._size = new_size
		self._faults = 0
		
	@staticmethod
	def __moveNodeToHead(self, nod):
		if nod != self._head:
			a = nod._prev
			b = nod._next
			if b == None:
				self._tail = a
				a._next = None
			else:
				a._next = b
				b._prev = a
			self._faults += 1
			nod._next = self._head
			self._head._prev = nod
			self._head = nod
			
	@staticmethod
	def __deleteNode(self, nod):
		if nod == self._head:
			self._head = nod._next
			if self._head:
				self._head._prev = None
			else:
				self._tail = None
		elif nod == self._tail:
			self._tail = nod._prev
			if self._tail:
				self._tail._next = None
			else:
				self._head = None
		else:
			a = nod._prev
			b = nod._next
			a._next = b
			b._prev = a
		
	def put(self, k, v):
		''' put k, v pairs in cache
		'''
		if k in self._map:
			nod = self._map[k]
			nod._v = v
			self.__moveNodeToHead(self, nod)
			return True
		self._faults += 1
		if len(self) == self._size:
			nod = self._tail
			self._map.pop(nod._k)
			self.__deleteNode(self, nod)
		nod = self.__Node(k, v)
		self._map[k] = nod
		nod._next = self._head
		if self._head == None:
			self._head = self._tail = nod
		else:
			self._head._prev = nod
			self._head = nod
		return False
		
	def get(self, k):
		''' returns val v associated with key k in cache
		'''
		nod = self._map[k]
		self.__moveNodeToHead(self, nod)
		return nod._v
		
	def pop(self, k):
		''' removes and returns val v associated with key k in cache
		'''
		nod = self._map.pop(k)
		self.__deleteNode(self, nod)
		return nod._v
		
	def items(self):
		''' returns a generator that yields all items in cache
		'''
		p = self._head
		while p != None:
			yield p
			p = p._next
