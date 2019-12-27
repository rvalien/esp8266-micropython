# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
# uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import time, network
# import webrepl
# webrepl.start()
gc.collect()

CONFIG = {
    # WIFI Configuration
    "SSID": 'V',
    "WIFI_PASSWORD": '9067505115',
}

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print(CONFIG.get('SSID'))
    print(CONFIG.get('WIFI_PASSWORD'))
    print('connecting to network...')
    wlan.connect(CONFIG.get('SSID'), CONFIG.get('WIFI_PASSWORD'))
    while not wlan.isconnected():
        time.sleep(1)

print('\nDevice IP: \nhttp://' + str(wlan.ifconfig()[0]))
print(CONFIG.get('CLIENT_ID'))

