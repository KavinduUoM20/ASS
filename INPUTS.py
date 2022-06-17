from datetime import datetime
import random

class Timer():

    def __init__(self):
        self.timenow = self.setTime()

    def getTime(self):
        return self.timenow

    def setTime(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        return current_time

    def resetTime(self):
        self.timenow = "00:00"

class TempSensor():

    def __init__(self):
        self.status = self.setTemp()

    def getTemp(self):
        return self.status

    def setTemp(self):
        return random.choice(range(0, 400))

    def resetTemp(self):
        self.status = 0

class SmokeSensor():

    def __init__(self):
        self.status = self.setSmoke()

    def getSmoke(self):
        return self.status

    def setSmoke(self):
        return random.choice(range(0, 2))

    def resetSmoke(self):
        self.status = 0

class MotionSensor():

    def __init__(self):
        self.status = self.setMotion()

    def getMotion(self):
        return self.status

    def setMotion(self):
        self.status = random.choice(range(0,2))

    def resetMotion(self):
        self.status=0

class MoistureSensor():

    def __init__(self):
        self.level = random.choice(range(0, 100))

    def getMoistureLevel(self):
        return self.level

    def resetMoistureLevel(self):
        self.level=0