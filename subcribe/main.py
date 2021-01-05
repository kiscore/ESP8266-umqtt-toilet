from simple import MQTTClient
import machine
import time

'''
Program: 
  订阅主题toilet，改变某个pin的电平
  主题规则：woman_on 打开女厕所有人示意灯，woman_off关闭女厕所有人示意灯。
CreateTime: 2020-12-16
'''

man_led = machine.Pin(4, machine.Pin.OUT)
woman_led = machine.Pin(5, machine.Pin.OUT)


def sub_cb(topic, msg):
    print(topic, msg)
    if str(msg) == "b'man_on'":
        man_led.on()
    if str(msg) == "b'man_off'":
        man_led.off()
    if str(msg) == "b'woman_on'":
        woman_led.on()
    if str(msg) == "b'woman_off'":
        woman_led.off()


def main(server="0.0.0.0"):
    try:
        c = MQTTClient("yitian-it", server)
        c.set_callback(sub_cb)
        time.sleep(4)
        c.connect()
        c.subscribe(b"toilet")
        while True:
            c.check_msg()
            time.sleep(1.5)
    except Excepthion as e:
        print(e)
        c.disconnect()
        machine.reset()


if __name__ == "__main__":
    main()
