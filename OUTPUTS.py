import INPUTS

class waterTap():

    def __init__(self, id):
        self.tapID = id
        self.moistVal = INPUTS.MoistureSensor().getMoistureLevel()
        self.status = self.setStatus()

    def getTapID(self):
        return self.tapID

    def getTapStatus(self):
        return self.status

    def getMoistureValue(self):
        return self.moistVal

    def setStatus(self):
        if self.moistVal >  41:
            return "CLOSE"
        else:
            return "OPEN"

    def reset(self):
        INPUTS.MoistureSensor.resetMoistureLevel()

class lightBulb():

    def __init__(self,id):
        self.bulbID = id
        self.time = INPUTS.Timer().getTime()
        self.motionStatus = INPUTS.MotionSensor().getMotion()
        self.bulbStatus= self.setStatus()

    def getBulbID(self):
        return self.bulbID

    def getMotionStatus(self):
        if self.motionStatus==1:
            return "ON"
        else:
            return "OFF"

    def getBulbStatus(self):
        return self.bulbStatus

    def getStatus(self):
        if self.bulbStatus=="ON" or self.bulbStatus=="DIM":
            return True
        else:
            return False

    def setStatus(self):
        if int(self.time[:2]) in [18,19,20,21,22,23,0,1,2,3,4,5,6] and self.motionStatus==1:
            return "ON"
        if int(self.time[:2]) in [18,19,20,21,22,23,0,1,2,3,4,5,6] :
            return "DIM"
        else:
            return "OFF"

    def reset(self):
        self.bulbStatus = self.MotionSensor().resetMotion()

class fireAlarm():

    def __init__(self,id):
        self.fireAlarmID = id
        self.smokeStatus = INPUTS.SmokeSensor().getSmoke()
        self.tempStatus = INPUTS.TempSensor().getTemp()
        self.alarmStatus= self.setAlarmStatus()

    def getAlarmID(self):
        return self.fireAlarmID

    def getAlarmStatus(self):
        return self.alarmStatus

    def getSmokeStatus(self):
        return "ON" if self.smokeStatus==1 else "OFF"

    def getTempStatus(self):
        return self.tempStatus

    def setAlarmStatus(self):
        if self.tempStatus>100 and self.smokeStatus==1:
            return "ON"
        else:
            return "OFF"

    def reset(self):
        pass

class shutters():

    def __init__(self,id):
        self.shutterID = id
        self.shutTime = INPUTS.Timer().getTime()
        self.shutterStatus = self.setStatus()

    def getShutterID(self):
        return self.shutterID

    def getShutTime(self):
        return self.shutTime

    def getShutterStatus(self):
        return self.shutterStatus

    def setStatus(self):
        thours = self.shutTime[:2]
        if int(thours) in [18,19,20,21,22,23,0,1,2,3,4,5,6]:
            return "CLOSE"
        else:
            return "OPEN"


    def reset(self):
        self.shutterStatus=INPUTS.Timer().setTime()

class TempController():

    def __init__(self,id):
        self.ContID=id
        self.temp = INPUTS.TempSensor().getTemp()
        self.contStatus = self.setStatus()

    def getTempControllerID(self):
        return self.ContID

    def getTemp(self):
        return self.temp

    def getControllerStatus(self):
        return self.contStatus

    def setStatus(self):
        if self.temp<100 and self.temp>30:
            return "AC Switched ON"
        if self.temp<20 and self.temp>0:
            return "Heater Switched ON"
        else:
            return "No Controller is ON"

    def reset(self):
        self.temp=INPUTS.TempSensor().resetTemp()