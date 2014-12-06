
class Votes(object):
    def __init__(self, votes, candidate):
        #super(Votes, self).__init__()
        self.votes = [list(h) for h in votes]
        self.fitness = None
        self.candidate = candidate

    def __str__(self):
        return "{0}\nfitness: {1}\n HASH: {2}".format(self.votes, self.fitness, self.__hash__())
        
