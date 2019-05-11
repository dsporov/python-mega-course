import datetime

ext = '.txt'

out = open(datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S-%f") + ext, 'w')
try:
  for i in range(1, 4):
    f = open('file'+str(i)+ext, 'r')
    try:
        out.write(f.read() + '\n')
    finally:
        f.close()
finally:
  out.close()


# import glob2
# from datetime import datetime
#
# filenames = glob2.glob("*.txt")
# with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
#     for filename in filenames:       
#         with open(filename, "r") as f:
#             file.write(f.read() + "\n")
