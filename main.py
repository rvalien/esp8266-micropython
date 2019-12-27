import dht
import json
from time import sleep
from machine import Pin
from micropyserver import MicroPyServer


def show_index_page(request):
    html_file = open("index.html")
    html = html_file.read()
    html_file.close()
    server.send(html, content_type="Content-Type: text/html")


def do_on(request):
    """ on request handler """
    led.value(1)
    server.send("ON")


def do_off(request):
    """ off request handler """
    led.value(0)
    server.send("OFF")


def show_data(request):
    """ request handler """
    d.measure()
    data = {"temperature": d.temperature(), "humidity": d.humidity()}
    json_str = json.dumps(data)
    server.send(json_str, content_type="Content-Type: application/json")


def counter(request):
    result = {'count': 0}
    while True:

        # The value function returns the current level of the pin,
        # either 1 for a high logic level or 0 for a low logic level.
        # Notice how the button is at a high level (value returns 1) when
        # it's not pressed. This is because the pull-up resistor keeps the pin at
        # a high level when it's not connected to ground through the button.
        # When the button is pressed then the input pin connects to ground
        # and reads a low level (value returns 0).
        if not button.value():
            # Remember that the internal led turn on
            # when the pin is LOW
            led.value(0)
        else:
            led.value(1)
            result['count'] += 1
        data = json.dumps(result)
        server.send(data, content_type="Content-Type: application/json")
        print(result)
        sleep(3)


button = Pin(12, Pin.IN, Pin.PULL_UP)
led = Pin(13, Pin.OUT)
d = dht.DHT22(Pin(14))

""" init server """
server = MicroPyServer()
server.add_route("/", show_index_page)
server.add_route("/data", show_data)
server.add_route("/on", do_on)
server.add_route("/off", do_off)
server.add_route("/c", counter)
""" start server """
server.start()
