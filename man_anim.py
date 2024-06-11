import subprocess
import time

c1 = '''A
  | 0 |
  \\---/
    |
    |
  /---\\
  |   |
B'''

c2 = '''C
 \\  0  /
  \\---/
    |
    |
  /---\\
  |   |
D'''

c3 = '''E
 \\  -  /
  \\---/
    |
    |
  /---\\
  |   |
F'''

c4 = '''G
 \\  0  /
  \\---/
    |
    |
  /---\\-
  |   
H'''


animation = [c1, c2, c3, c1, c4]

for frame_num in range(1, 5000):
  subprocess.run("clear")
  frame_1 = frame_num % len(animation)
  frame_2 = (round(frame_num / 2)) % len(animation)
  #print(animation[frame_1])
  #print(animation[frame_2])
  #print(animation[frame_1] + animation[frame_2])
  print(animation[frame_1], animation[frame_2])
  time.sleep(0.5)
