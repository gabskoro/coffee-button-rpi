import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
  input_state = GPIO.input(18)
  if input_state == False:
    headers = {'Auth': '123'}
	requests.post('http://gabrijelskoro.com/api/click', headers = headers)
    time.sleep(0.2)
