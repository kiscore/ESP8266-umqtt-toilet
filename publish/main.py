from simple import MQTTClient
import machine
import time

'''
Program: 
  1)监听pin4针脚，如果读取到了高电平数据，则把pin5设置为高电平，pin5去触发继电器，
  让继电器耦合。
  2）监听到pin4为高电平的同时，publish一条数据给EMQT,让订阅该主题的其他端收到这个消息。

'''
man_send = False
woman_send = False


def publish_msg(topic, msg):
    if topic and msg:
        try:
            c = MQTTClient("umqtt_client", "139.196.218.120")
            c.connect()
            c.publish(topic, msg)
            c.disconnect()
        except Exception as e:
            print(e)
            time.sleep(3)
            machine.idle()


if __name__ == "__main__":
    time.sleep(5)
    # man_monitor_pin = machine.Pin(5, machine.Pin.IN)
    # man_notify_pin = machine.Pin(3, machine.Pin.OUT)
    woman_monitor_pin = machine.Pin(4, machine.Pin.IN)
    woman_notify_pin = machine.Pin(5, machine.Pin.OUT)
    while 1:
        # 男厕所感应器
        # if man_monitor_pin() == 1:
        #     man_notify_pin.on()
        #     topic = b"toilet"
        #     msg = b"man_on"
        #     if man_send is False:
        #         publish_msg(topic, msg)
        #         man_send = True
        #     print("man---->1")
        # if man_monitor_pin() == 0:
        #     man_notify_pin.off()
        #     topic = b"toilet"
        #     msg = b"man_off"
        #     if man_send:
        #         publish_msg(topic, msg)
        #         man_send = False
        #     print("man---->0")
        # 女厕所感应器
        if woman_monitor_pin() == 1:
            woman_notify_pin.on()
            topic = b"toilet"
            msg = b"woman_on"
            if woman_send is False:
                publish_msg(topic, msg)
                woman_send = True
            print("woman---->1")
        if woman_monitor_pin() == 0:
            woman_notify_pin.off()
            topic = b"toilet"
            msg = b"woman_off"
            if woman_send:
                publish_msg(topic, msg)
                woman_send = False
            print("woman---->0")
        time.sleep(1)
