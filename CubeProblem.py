from search import *
from cube import *

class CubeProblem (Problem):
	"""The abstract class for a formal problem.  You should subclass this and
	implement the method successor, and possibly __init__, goal_test, and
	path_cost. Then you will create instances of your subclass and solve them
	with the various search functions."""
	
	def __init__(self, initial, goal=None):
		"""The constructor specifies the initial state, and possibly a goal
		state, if there is a unique goal.  Your subclass's constructor can add
		other arguments."""
		self.initial = initial; self.goal = Cube()
	
	def successor(self, state):
		nodes=[('U',state.U())]
		nodes.append(('D',state.D()))
		nodes.append(('L',state.L()))
		nodes.append(('R',state.R()))
		nodes.append(('U',state.U()))
		nodes.append(('B',state.B()))
		
		nodes.append(('U\'',state.Uprime()))
		nodes.append(('D\'',state.Dprime()))
		nodes.append(('L\'',state.Lprime()))
		nodes.append(('R\'',state.Rprime()))
		nodes.append(('F\'',state.Fprime()))
		nodes.append(('B\'',state.Bprime()))
		
		nodes.append(('U2',state.U2()))
		nodes.append(('D2',state.D2()))
		nodes.append(('L2',state.L2()))
		nodes.append(('R2',state.R2()))
		nodes.append(('F2',state.F2()))
		nodes.append(('B2',state.B2()))

		return nodes
	
	def goal_test(self, state):
		"""Return True if the state is a goal. The default method compares the
		state to self.goal, as specified in the constructor. Implement this
		method if checking against a single self.goal is not enough."""
		return state.isGoal()
	
	def path_cost(self, c, state1, action, state2):
		"""Return the cost of a solution path that arrives at state2 from
		state1 via action, assuming cost c to get up to state1. If the problem
		is such that the path doesn't matter, this function will only look at
		state2.  If the path does matter, it will consider c and maybe state1
		and action. The default method costs 1 for every step in the path."""
		return c + 1
	
	def value(self):
		"""For optimization problems, each state has a value.  Hill-climbing
		and related algorithms try to maximize this value."""
		abstract
	
	def h(self,n):
		heur=n.state.heuristic2()
		#print repr(n.path_cost)+" "+repr(heur)
		return heur
