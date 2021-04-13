import serial
import time

#serport='/dev/ttyACM0'
serport='/dev/ttyUSB0'
ser_tmout=10
try:
    ser=serial.Serial(serport, 9600,timeout=ser_tmout)
except:
    print("Error opening "+serport)
    quit()

print("opened Port: "+ser.name + "  " + "Timeout: " + str(ser_tmout))
ser.write(b'\nWaiting for Input:\n')
time.sleep(1)
count=0
print(":")
answer=''
while True:
  ch=ser.read()

  if len(ch) == 0:
      print("Timed out...\nLast (uncomplete) Line: " + answer)
      ser.write(b'\nTimed out... closing Connection\n')
      break
  try:
      dch=ch.decode()
  except:
      ch=b'*'
  answer += ch.decode()
  if ch == b'\r'or ch == b'\n':
      print ("Got Line: " + answer)
      answer=''
print("Bye")


#    try:
#        ser_bytes = ser.readline()
#        answer = ser_bytes[0:len(ser_bytes)-1].decode("utf-8")
#        print (answer)
#    except:
#        time.sleep(1)
#        print(":")
#        continue
#    print(decoded_bytes)


#    ser.write(b'+\n')
#    ser.flush()
#    print(".")
#    time.sleep(3)
    
#    while not ser.available() :
#        print(".")
#    if Serial.available :    
#    answer=ser.readline()
#    if str(answer) =="Q" :
#        print("!")
#        ser.close()
#        quit()
#    print (answer.decode())

ser.close()

