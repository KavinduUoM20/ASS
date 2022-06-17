import OUTPUTS

def main():

    ToolKit=[
        OUTPUTS.waterTap("Water Tap 001"),
        OUTPUTS.shutters("Shutter 001"),
        OUTPUTS.lightBulb("Light Bulb 001"),
        OUTPUTS.fireAlarm("Fire Alarm 001"),
        OUTPUTS.TempController("Temp Controller 001")
    ]

    print("\nSimulating My Home Automation System...\n")

    switcher= {
        ToolKit[0]: print(ToolKit[0].getTapID()+" is ["+ ToolKit[0].getTapStatus() +"] as Moisture Sensor Value is "+ str(ToolKit[0].getMoistureValue())),
        ToolKit[1]: print(ToolKit[1].getShutterID()+" is ["+ToolKit[1].getShutterStatus()+"] as Timer Value is "+ str(ToolKit[1].getShutTime())),
        ToolKit[2]: print(ToolKit[2].getBulbID()+" is ["+ToolKit[2].getBulbStatus()+"] as Timer Value and Motion Sensor are "+ str(ToolKit[2].time)+ " and "+ToolKit[2].getMotionStatus()),
        ToolKit[3]: print(ToolKit[3].getAlarmID() + " is [" + ToolKit[3].getAlarmStatus() + "] as Temperature and Smoke Sensor are " + str(ToolKit[3].getTempStatus()) + " and " + ToolKit[3].getSmokeStatus()),
        ToolKit[4]: print(ToolKit[4].getTempControllerID()+ " - ["+ToolKit[4].getControllerStatus()+"] as Temperature Level is "+ str(ToolKit[4].getTemp()))
    }
    def switch(vals):
        return switcher.get(vals,default)()


if __name__=="__main__":
    main()