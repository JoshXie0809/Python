class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age =age
    
    def study(self, course_name):
        print('%s is learning %s' %(self.name, course_name))
        
    def watch_movie(self):
        if self.age < 18:
            print('%s is watchimg cartoon.' % self.name)
        else:
            print('%s is watching porn. ' % self.name)   

class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')




class Clock(object):
    def __init__(self, hour, minute, second):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._minute += 1
            self._second -= 60
            if self._minute == 60:
                self._hour += 1
                self._minute -= 60
                if self._hour == 24:
                    self._hour = 0
    
    def show(self):
        
        return '%02d:%02d:%02d' % (self._hour, self._minute,self._second)


class Move(object):

    def __init__(self, x, y):
        self.__aax = x
        self.__aay = y

    def move_to(self, new_x, new_y):
        self.__aax =  new_x
        self.__aay =  new_y
    
    def move_by(self, dx, dy):
        self.__aax +=  dx
        self.__aay +=  dy

    def nowPlace(self):
        print("You are located at x: %2f  y : %2f" % (self.__aax, self.__aay))
