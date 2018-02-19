import Q

class lrucache:
	def __init__(self, limit = 1024):
		'''creates a lru cache with a specified limit
		'''
		self._limit = limit
		self._Q = Q.Q()
		self._hash_map = {}
		self._faults = 0
		
	def __repr__(self):
		A = []
		for i in self.getAll():
			A.append(i)
		return 'lrucache({})'.format(A)
		
	def __iter__(self):
		return self.getAll()
		
	def getKeyCount(self):
		'''returns no of keys in the cache
		'''
		return self._Q.getKeyCount()
		
	def getFaults(self):
		'''returns no of faults occurred till now
		'''
		return self._faults
		
	def getLimit(self):
		'''returns limit of the cache
		'''
		return self._limit
		
	def increaseLimit(self, by):
		'''increase the size of the cache by a positive non-zero integer
		'''
		if by > 0:
			self._limit += by
		else:
			raise ValueError('by value cannot be negetive')
			
	def doublesLimit(self):
		'''doubles the size of the cache
		'''
		self.increaseLimit(self._limit << 1)
	
	def triplesLimit(self):
		'''doubles the size of the cache
		'''
		self.increaseLimit(self._limit * 3)
	
	def isEmpty(self):
		'''check is cache is empty or not
		'''
		return self._Q.isEmpty()
		
	def isFull(self):
		'''check is cache is full or not
		'''
		return self.getKeyCount() == self.getLimit()
		
	def isHalfFull(self):
		'''check is cache is half full or not
		'''
		return self.getKeyCount() == (self.getLimit() >> 1)
		
	def __get(self, dictob, k):
		try:
			return dictob[k]
		except KeyError:
			pass
	
	def __pop(self, dictob, k):
		try:
			return dictob.pop(k)
		except KeyError:
			pass
		
	def put(self, k, v = None):
		'''put k, v into the cache
		'''
		t = self.__get(self._hash_map, k)
		if t:
			t.v = v
			return t, 1
		else:
			self._faults += 1
			if not self.isFull():
				self._hash_map[k] = t = self._Q.enQ(k, v)
			else:
				self._hash_map[k] = t = self._Q.enQ(k, v)
				k, v = self._Q.delQ()
				self._hash_map.pop(k)
			return t, 0
			
	def pop(self, k):
		'''pops out k, v from the cache, if no such k returns None
		'''
		if not self.isEmpty():
			t = self.__pop(self._hash_map, k)
			if t:
				self._Q._Q__deleteNode(t)
				return t.k, t.v
			
	def delAll(self):
		'''delete every element in the cache (empties the cache)
		'''
		if not self.isEmpty():
			for i in self.getAll():
				self.pop(i[0])
	
	def get(self, k):
		'''returns k, v from the cache, if no such k returns None
		'''
		t = self.__get(self._hash_map, k)
		if t:
			self._Q._Q__moveNodeToTail(t)
			return t.k, t.v
			
	def getAll(self):
		'''returns generator that generate all k, v pair present in the cache
		'''
		return self._Q.getAll()
			
	def printAll(self):
		'''iterate over getAll() and prints them
		'''
		self._Q.printAll()
