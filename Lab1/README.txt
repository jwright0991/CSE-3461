README - copy.py

The program takes in a local file as input and copies the file to a new file,
of the same name, created in a subdirectory called recv.

To run the program, use the command:
    
>> python3 copy.py <filename>

Including additional commandline arguments will result in an error message and
no additional action.

I've included a set of unit tests in a file called test_copy.py

Running the following command will test the program on three files that I've included in the directory with copy.py for simple testing purposes. Leaving out the path will default to the path set for my computer and the test won't pass, so be sure to include the current path for your machine.

>> python3 test_copy.py <full path to the directory that contains copy.py>

In addition to the above test, you can include additional arguments after the path name that are files to be tested. I couldn't figure out a way to run each argument as a separate test case, so one additional test case is run over all of the extra files that are given as arguments. The format is shown below.

>> python3 test_copy.py <full path to the directory that contains copy.py> <additional arguments separated by whitespace>