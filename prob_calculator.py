import random
import copy

random.seed(95)
class Hat():
    def __init__(self,**kwargs):
        self.contents = list()
        self.arguments = dict()
        for ball,number in kwargs.items():
            self.arguments[ball] = number
        for key in self.arguments.keys():
            x = self.arguments[key]
            for y in range(x):
                self.contents.append(key)


    def draw(self,n_of_balls):
        all_removed = list()
        if n_of_balls > len(self.contents):
            return self.contents
        
        for x in range(n_of_balls):
            all_removed.append(self.contents.pop(random.randrange((len(self.contents)))))
        return all_removed

def experiment(**kwargs):

    num_balls_drawn = kwargs['num_balls_drawn']
    num_experiments = kwargs['num_experiments']
    count = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(kwargs['hat'])
        expected_balls = copy.deepcopy(kwargs['expected_balls'])
        drawn_balls = hat_copy.draw(num_balls_drawn)

        for color in drawn_balls:
            if(color in expected_balls):
                expected_balls[color]-=1

        if(all(x <= 0 for x in expected_balls.values())):
            count +=1
        
    return count/num_experiments