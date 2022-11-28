class World:
	happiness = None
	selfedu = list()

	@classmethod
	def thanks(cls):
		hours = 0
		while cls.happiness is None:
			if hours == 10000:
				cls.happiness = 'Victory'
			cls.learn(hours)
			hours += 1

	@classmethod
	def learn(cls, count):
		cls.selfedu.append(f'Занятие {count} в копилку!')

	def show(self):
		return self.selfedu

w = World()
w.thanks()
for i in range(10000):
	w.learn(i)
print(w.show())