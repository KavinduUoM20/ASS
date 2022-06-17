import OUTPUTS


def main():
    w1 = OUTPUTS.waterTap("w2")
    print(w1.getTapStatus())
    print(w1.moistVal)
    print(w1.getMoistureValue())


if __name__=="__main__":
    main()