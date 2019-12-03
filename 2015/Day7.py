class cell:
	def __init__(self, name, chart, t = None, val = None, source1 = None, source2 = None):
		self.name = name
		self.chart = chart
		self.type = t
		self.val = val
		self.source1 = source1
		self.source2 = source2
	def getval(self):
		if self.val is not None:
			if isinstance(self.val, int):
				return self.val
			if self.val.isdigit():
				return int(self.val)
			return self.chart[self.val].getval()
		if self.type == "AND":
			if self.source1.isdigit():
				a = int(self.source1)
			else:
				a = self.chart[self.source1].getval()
			if self.source2.isdigit():
				b = int(self.source1)
			else:
				b = self.chart[self.source2].getval()
			self.val = a & b
			return self.val
		if self.type == "NOT":
			if self.source1.isdigit():
				self.val = ~ int(self.source1)
				return self.val
			else:
				self.val = ~ self.chart[self.source1].getval()
				return self.val
		if self.type == "LSHIFT":
			if self.source1.isdigit():
				a = int(self.source1)
			else:
				a = self.chart[self.source1].getval()
			if self.source2.isdigit():
				b = int(self.source2)
			else:
				b = self.chart[self.source2].getval()
			self.val = a << b
			return self.val
		if self.type == "RSHIFT":
			if self.source1.isdigit():
				a = int(self.source1)
			else:
				a = self.chart[self.source1].getval()
			if self.source2.isdigit():
				b = int(self.source2)
			else:
				b = self.chart[self.source2].getval()
			self.val = a>>b
			return self.val
		if self.type == "OR":
			if self.source1.isdigit():
				a = int(self.source1)
			else:
				a = self.chart[self.source1].getval()
			if self.source2.isdigit():
				b = int(self.source2)
			else:
				b = self.chart[self.source2].getval()
			self.val = a | b
			return self.val
a = None
chart = {}
with open("Day7") as f:
	for line in f:
		hold = line.split()
		if len(hold) == 3:
			ncell = cell(hold[2], chart, val = hold[0])
		elif len(hold) == 4:
			ncell = cell(hold[3], chart, t = "NOT", source1 = hold[1])
		else:
			ncell = cell(hold[4], chart, t = hold[1], source1 = hold[0], source2 = hold[2])
		chart[ncell.name] = ncell
		if ncell.name == "a":
			a = ncell
print a.getval()