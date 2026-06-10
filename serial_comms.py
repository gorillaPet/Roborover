# import serial
# import time


# robo_on = True
# while robo_on:
#     message = input("Type: ")
#     s.write((message + '\n').encode())  # \n lets Arduino use readStringUntil('\n')

#     if s.in_waiting:
#         response = s.readline().decode().strip()
#         print("Arduino says:", response)

#     if message == "q":
#         robo_on = False

# s.close()




# send wheel bits (1&2) and pedal bits (9&10):








