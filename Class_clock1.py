class Clock:
    def __init__(self,time):
        self.time=time
    def times(self):
        self.time="6.30"
        print(self.time)
clock=Clock("5.30")
clock.times()
