from datetime import datetime
import SI1145.SI1145 as SI1145
import time


sensor = SI1145.SI1145()


def main():
    with open("logs.txt", "a") as myfile:
        vis = sensor.readVisible()
        IR = sensor.readIR()
        UV = sensor.readUV()
        uvIndex = UV / 100.0
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        myfile.write(dt_string + " Vis: " + str(vis) + " IR: " + str(IR) + " UV Index: " + str(uvIndex) + "\n")


while True:
    main()
    time.sleep(5)
