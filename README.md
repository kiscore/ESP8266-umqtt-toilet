# ESP8266-umqtt-toilet
利用ESP8266，使用micropython控制GPIO，通过传感器获取电平数据，通过EMQT传送数据。

传感器类型：
人体红外传感器 HC-SR501
继电器  高电平触发

publish-main.py Program: 
  1)监听pin4针脚，如果读取到了高电平数据，则把pin5设置为高电平，pin5去触发继电器，
  让继电器耦合。
  2）监听到pin4为高电平的同时，publish一条数据给EMQT,让订阅该主题的其他端收到这个消息。
subcribe-main.py Program:
  订阅主题toilet，改变某个pin的电平
  主题规则：woman_on 打开女厕所有人示意灯，woman_off关闭女厕所有人示意灯。
