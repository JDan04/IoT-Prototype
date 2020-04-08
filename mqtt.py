from flask_mqtt import Mqtt

topic = ""
payload = ""

mqtt = Mqtt()

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('test')
    pass

@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    if level == MQTT_LOG_INFO:
        print('Info: {}'.format(buf))
    if level == MQTT_LOG_NOTICE:
        print('Notice: {}'.format(buf))
    if level == MQTT_LOG_WARNING:
        print('Warning: {}'.format(buf))
    if level == MQTT_LOG_ERR:
        print('Error: {}'.format(buf))
    if level == MQTT_LOG_DEBUG:
        print('Debug: {}'.format(buf))

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    global topic
    global payload

    topic = message.topic
    payload = message.payload.decode()
