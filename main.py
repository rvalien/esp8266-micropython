from micropyserver import MicroPyServer
import esp
import json
import time
import dht
from machine import Pin


def show_message(request):
    """
     request handler
    """
    html = """<!DOCTYPE html>
    <html>
    <head> <title>ESP8266 Pins</title> </head>
    <body> <h1>ESP8266 Pins</h1>
    </body>
    </html>
    """
    
    server.send(html, content_type='text/html charset=utf-8')


def do_on(request):
    ''' on request handler '''
    pin.value(1)
    server.send("ON") ]

def do_off(request):
    ''' off request handler '''
    pin.value(0)
    server.send("OFF")


def show_data(request):
    """ request handler """
    d = dht.DHT22(machine.Pin(14))
    d.measure()
    data = {"temperature": d.temperature(), "humidity": d.humidity()}
    json_str = json.dumps(data)
    server.send(json_str, content_type="Content-Type: application/json")



pin = machine.Pin(13, machine.Pin.OUT)
server = MicroPyServer()
''' add request handler '''
server.add_route("/", show_message)
server.add_route("/data", show_data)
server.add_route("/on", do_on)
server.add_route("/off", do_off)
''' start server '''
server.start()

