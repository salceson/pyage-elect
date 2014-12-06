from pyage.core.inject import Singleton

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class NamingService(object):
	__metaclass__ = Singleton
	def __init__(self, parents_number, starting_number):
		self.counters = dict([ ('R'+str(p),starting_number+1) for p in xrange(parents_number)])

	def get_next_agent(self, parent_number):
		next_number = self.counters[parent_number]
		self.counters[parent_number] +=1
		return str(next_number)