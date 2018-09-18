import sys
import os
'''
@Author Josh Wright
Lab 1
Copies a file in the current directory to a subdirectory called 'recv'.
'''
def main(arg1):
    '''
    Constants
    '''
    SUBDIR = "recv"
    BYTELEN = 1000
    
    '''Try to open the file or print an error message and exit if the file doesn't
    exist'''
    try:
        fileIn = open(arg1,"rb")
    except FileNotFoundError:
        print("Error: File Does Not Exist!")
        return
    
    '''Check to make sure the recv directory exists and creates the directory if
    it doesnt' exist, then change into the directory and open a file for writing
    in the directory'''
    if not os.path.isdir(SUBDIR):
        os.mkdir(SUBDIR)
    os.chdir(SUBDIR)
    fileOut = open(arg1,"wb")
    '''Read up to 1000 bytes of the file'''
    line = fileIn.read(BYTELEN)
    '''Until reading a line from the file returns an empty string, keep reading 1000 bytes at a time'''
    while line:
        fileOut.write(line)
        line = fileIn.read(BYTELEN)
        
    '''close both files when the loop is done'''
    fileIn.close()
    fileOut.close()
if __name__ == '__main__':
    '''Check to make sure that only two commandline arguments were passed in.'''
    if(len(sys.argv) == 2):
        main(sys.argv[1])
    else:
       print("Error: incorrect number of arguments")
