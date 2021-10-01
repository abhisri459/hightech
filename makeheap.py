class MakeHeap:
	def __init__(self):
		self._swaps = []
		self._data = []

	def ReadData(self):
		n = int(input())
		self._data = [int(s) for s in input().split()]
		assert n == len(self._data)

	def WriteResponse(self):
		print(len(self._swaps))
		for swap in self._swaps:
		  print(swap[0], swap[1])

	def GenerateSwaps(self):
		for i in range(int((len(self._data)-2)/2), -1, -1):
			j = i
			while True:
				l = 2*j+1
				r = 2*j+2
				if l>len(self._data)-1: break
				if r>len(self._data)-1:
					if self._data[j]>self._data[l]:
						self._swaps.append([j,l])
						self._data[j], self._data[l] = self._data[l], self._data[j]
					break
				if self._data[j]<=min(self._data[l],self._data[r]): break
				k = l if self._data[l]<self._data[r] else r
				self._swaps.append([j,k])
				self._data[j], self._data[k] = self._data[k], self._data[j]
				j = k

	def Solve(self):
		self.ReadData()
		self.GenerateSwaps()
		self.WriteResponse()

if __name__ == '__main__':
	heap_builder = MakeHeap()
	heap_builder.Solve()