class dll_node:
	def __init__(self, k, v):
		'''a dll node
		<-[k, v]-> <-[k, v]->
		'''
		self.k = k
		self.v = v
		self._next = self._prev = None
		
class Q:
	def __init__(self):
		'''create a empty queue
		'''
		self._head = self._tail = None
		self._key_count = 0
		
	def getKeyCount(self):
		'''returns no of keys in the queue
		'''
		return self._key_count
		
	def isEmpty(self):
		'''checks if the queue is empty or not
		'''
		return self._head == None
		
	def __getNode(self, k, v):
		return dll_node(k, v)
	
	def enQ(self, k, v = None):
		'''enqueues k, v into the queue, also returns the newly created node
		'''
		nod = self.__getNode(k, v)
		self._key_count += 1
		if self.isEmpty():
			self._head = self._tail = nod
		else:
			nod._prev = self._tail
			self._tail._next = nod
			self._tail = nod
		return nod
			
	def delQ(self):
		'''delqueues k, v from the queue, also returns k, v as tuple
		'''
		if not self.isEmpty():
			self._key_count -= 1
			p = self._head
			self._head = p._next
			if self._head:
				self._head._prev = None
			return p.k, p.v
			
	def __moveNodeToTail(self, node):
		if node != self._tail:
			if node == self._head:
				self._head = node._next
				self._head._prev = None
			else:
				p = node._prev
				q = node._next
				p._next = q
				q._prev = p
			node._prev = self._tail
			self._tail._next = node
			self._tail = node
			self._tail._next = None
			
	def __deleteNode(self, node):
		if node == self._head:
			self._head = node._next
			if self._head:
				self._head._prev = None
			node._next = None
		elif node == self._tail:
			self._tail = node._prev
			if self._tail:
				self._tail._next = None
			node._prev = None
		else:
			p = node._prev
			q = node._next
			p._next = q
			q._prev = p
			node._next = node._prev = None
		self._key_count -= 1
			
	def getAll(self):
		'''returns a generator that yields every k, v pair present in the queue
		'''
		if not self.isEmpty():
			p = self._head
			while p:
				z = p.k, p.v
				p = p._next
				yield z
				
	def printAll(self):
		'''uses getAll() and prints it on the console
		'''
		if not self.isEmpty():
			for i in self.getAll():
				print(i)
			
