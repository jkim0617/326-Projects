# Todo
# DONE extract source and destination file name from the command line
# DONE open source file in read mode and destination file in write mode
# DONE create a pipe
# DONE use the fork system call to create a child process
# DONE In the parent process, read from the source file and write to the write end of the pipe
# DONE In the child process, read from the read end of the pipe and write to the destination file
# DONE close file descriptors (r and w)

import os
import sys

print("*-----------------------------*")

if __name__ == "__main__":
  if (len(sys.argv) != 3): # case of incorrect # of arguments
    print("Invalid # of arguments. Please follow format: \"./fileCopy input.txt copy.txt \"")
    exit()
  inputFile = open(sys.argv[1],"r") #set first argument as input file in read only mode
  copyFile = open(sys.argv[2],"w") #set second argument as output file in write only mode

r,w = os.pipe() # craete the pipe with r being the read end and w being the write end

pid = os.fork() # create the fork

if(pid < 0): # validate fork creation
  print("Fork Failed")
  inputFile.close()
  copyFile.close()
  os.close(r)
  os.close(w)
  exit()

# print("pid:", pid)

if pid > 0: # parent process, read from the source file and write to the write end of the pipe
  os.close(r)

  print("Entered Parent Process")
  os.write(w, inputFile.read().encode()) # read to read end of pipe

  os.close(w)
  inputFile.close()

else: # child process, read from the read end of the pipe and write to the destination file
  os.close(w)

  print("Entered Child Process")
  rOpen = os.fdopen(r)
  copyFile.write(rOpen.read()) # write to write end of pipe

  os.close(r)
  copyFile.close()
  print("File successfully copied")