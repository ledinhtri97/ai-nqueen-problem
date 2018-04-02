import math

#______________________________________________________________________________
# goodguy and badguys Problem

class State():
	def __init__(self, badguyLeft, goodguyLeft, ship, badguyRight, goodguyRight):
		self.badguyLeft = badguyLeft
		self.goodguyLeft = goodguyLeft
		self.ship = ship
		self.badguyRight = badguyRight
		self.goodguyRight = goodguyRight
		self.parent = None

	def is_goal(self):
		if ((self.badguyLeft == 0) & (self.goodguyLeft == 0)):
			return True
		else:
			return False

	def is_valid(self):
		if ((self.goodguyLeft >= 0 & self.goodguyRight >= 0 )\
                   & (self.badguyLeft >= 0 & self.badguyRight >= 0) \
                   & ((self.goodguyLeft == 0) | (self.goodguyLeft >= self.badguyLeft)) \
                   & ((self.goodguyRight == 0) | (self.goodguyRight >= self.badguyRight))):
			return True
		else:
			return False

	def __eq__(self, other):
		return ((self.badguyLeft == other.badguyLeft) & (self.goodguyLeft == other.goodguyLeft) \
                   & (self.ship == other.ship) & (self.badguyRight == other.badguyRight) \
                   & (self.goodguyRight == other.goodguyRight))

	def __hash__(self):
		return hash((self.badguyLeft, self.goodguyLeft, self.ship, self.badguyRight, self.goodguyRight))

def successors(cur_state):
	children = [];
	if cur_state.ship == 'left':
		new_state = State(cur_state.badguyLeft, cur_state.goodguyLeft - 2, 'right',
                                  cur_state.badguyRight, cur_state.goodguyRight + 2)
		## Two goodguy cross left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.badguyLeft - 2, cur_state.goodguyLeft, 'right',
                                  cur_state.badguyRight + 2, cur_state.goodguyRight)
		## Two badguys cross left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.badguyLeft - 1, cur_state.goodguyLeft - 1, 'right',
                                  cur_state.badguyRight + 1, cur_state.goodguyRight + 1)
		## One goodguy and one badguy cross left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.badguyLeft, cur_state.goodguyLeft - 1, 'right',
                                  cur_state.badguyRight, cur_state.goodguyRight + 1)
		## One goodguy crosses left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.badguyLeft - 1, cur_state.goodguyLeft, 'right',
                                  cur_state.badguyRight + 1, cur_state.goodguyRight)
		## One badguy crosses left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
	else:
		new_state = State(cur_state.badguyLeft, cur_state.goodguyLeft + 2, 'left',
                                  cur_state.badguyRight, cur_state.goodguyRight - 2)
		## Two goodguy cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.badguyLeft + 2, cur_state.goodguyLeft, 'left',
                                  cur_state.badguyRight - 2, cur_state.goodguyRight)
		## Two badguy cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.badguyLeft + 1, cur_state.goodguyLeft + 1, 'left',
                                  cur_state.badguyRight - 1, cur_state.goodguyRight - 1)
		## One goodguy and one badguy cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.badguyLeft, cur_state.goodguyLeft + 1, 'left',
                                  cur_state.badguyRight, cur_state.goodguyRight - 1)
		## One goodguy crosses right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.badguyLeft + 1, cur_state.goodguyLeft, 'left',
                                  cur_state.badguyRight - 1, cur_state.goodguyRight)
		## One badguy crosses right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
	return children

def breadth_first_search():
	initial_state = State(3,3,'left',0,0)
	if initial_state.is_goal():
		return initial_state
	frontier = list()
	explored = set()
	frontier.append(initial_state)
	while frontier:
		state = frontier.pop(0)
		if state.is_goal():
			return state
		explored.add(state)
		children = successors(state)
		for child in children:
			if (child not in explored) or (child not in frontier):
				frontier.append(child)
	return None

def print_solution(solution):
		path = []
		path.append(solution)
		parent = solution.parent
		while parent:
			path.append(parent)
			parent = parent.parent

		for t in range(len(path)):
			state = path[len(path) - t - 1]
			print( "(" + str(state.badguyLeft) + "," + str(state.goodguyLeft) \
                              + "," + state.ship + "," + str(state.badguyRight) + "," + \
                              str(state.goodguyRight) + ")")

def main():
	solution = breadth_first_search()
	print( "goodguy and badguys solution:")
	print( "(badguyLeft,goodguyLeft,ship,badguyRight,goodguyRight)")
	print_solution(solution)

# if called from the command line, call main()
if __name__ == "__main__":
    main()