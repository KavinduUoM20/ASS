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
        values = ["OPEN","CLOSE"]
        WT1 = OUTPUTS.shutters("WT1")
        self.assertEqual(WT1.getStatus(), any(values))

    def test_MotionSensor(self):
        values = [True,False]
        MS1 = INPUTS.MotionSensor()
        self.assertEqual(MS1.getMotion(), any(values))

    def test_BulbStatus(self):
        values = ["OFF","ON"]
        LB1 = OUTPUTS.lightBulb("LB1")
        self.assertEqual(LB1.getStatus(),any(values))

    def test_FireAlarmStatus(self):
        values = ["OFF","ON"]
        FA1 = OUTPUTS.fireAlarm("FA1")
        self.assertEqual(FA1.getStatus(),any(values))

    def test_ShutterStatus(self):
        values = ["CLOSE", "OPEN"]
        SH1 = OUTPUTS.shutters("SH1")
        self.assertEqual(SH1.getStatus(), any(values))

    def test_TempContollerStatus(self):
        values = ["CLOSE", "OPEN"]
        TC1 = OUTPUTS.TempController("TC1")
        self.assertEqual(TC1.getStatus(), any(values))


if __name__ == "__main__":
    unittest.main()

