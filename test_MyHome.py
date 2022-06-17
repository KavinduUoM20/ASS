import unittest
import INPUTS
import OUTPUTS

class MyHomeTestOutputs(unittest.TestCase):

    #Reset Methods
    def test_resetSmokeSensor(self):
        SS1 = INPUTS.SmokeSensor()
        SS1.resetSmoke()
        self.assertEqual(SS1.getSmoke(), 0)

    def test_resetTempSensor(self):
        TS1 = INPUTS.TempSensor()
        TS1.resetTemp()
        self.assertEqual(TS1.getTemp(), 0)

    def test_resetTimer(self):
        TM1 = INPUTS.Timer()
        TM1.resetTime()
        self.assertEqual(TM1.getTime(), "00:00")

    def test_resetMoistureSensor(self):
        MIS1= INPUTS.MoistureSensor()
        MIS1.resetMoistureLevel()
        self.assertEqual(MIS1.getMoistureLevel(),0)

    def test_resetMotionSensor(self):
        MS1 = INPUTS.MotionSensor()
        MS1.resetMotion()
        self.assertEqual(MS1.getMotion(), 0)

    #Status Methods
    def test_WaterTapStatus(self):
        self.assertTrue(OUTPUTS.waterTap("WT1").getTapStatus() in ["OPEN","CLOSE"])

    def test_MotionSensor(self):
        self.assertTrue(INPUTS.MotionSensor().status in [1,0])

    def test_BulbStatus(self):
        self.assertTrue(OUTPUTS.lightBulb("BL2").getBulbStatus() in ["ON", "OFF"])

    def test_FireAlarmStatus(self):
        self.assertTrue(OUTPUTS.fireAlarm("FA2").getAlarmStatus() in ["OFF","ON"])

    def test_ShutterStatus(self):
        self.assertTrue(OUTPUTS.shutters("SH1").getShutterStatus() in ["CLOSE", "OPEN"])

    def test_TempContollerStatus(self):
        self.assertTrue(OUTPUTS.TempController("TC1").getControllerStatus() in ["AC Switched ON","Heater Switched ON","No Controller is ON"])


if __name__ == "__main__":
    unittest.main()

