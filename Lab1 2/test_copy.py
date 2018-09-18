import sys
import os
import unittest
import filecmp
import copy

'''
path_to_dir = "/Users/JoshWright/Documents/CSE3461/"
file1 = "README.txt"
file2 = "card.jpg"
file3 = "Queue.py"
'''
if len(sys.argv) > 1:
    path_to_dir = sys.argv[1]
    if len(sys.argv) > 2:
        files = sys.argv[2:len(sys.argv)]
else:
    path_to_dir = "/Users/JoshWright/Documents/CSE3461/"

class TestCopy(unittest.TestCase):
   
    def test_main_txt(self):
        copy.main("README.txt")
        os.chdir(path_to_dir)
        self.assertEqual(True, filecmp.cmp("README.txt", "recv/README.txt"))
    def test_main_jpg(self):
        copy.main("card.jpg")
        os.chdir(path_to_dir)
        self.assertEqual(True, filecmp.cmp("card.jpg", "recv/card.jpg"))
    def test_main_py5(self):
        copy.main("Queue.py")
        os.chdir(path_to_dir)
        self.assertEqual(True, filecmp.cmp("Queue.py", "recv/Queue.py"))
    def test_main_args(self):
        for file in files:
            copy.main(file)
            os.chdir(path_to_dir)
            self.assertEqual(True, filecmp.cmp(file, "recv/"+file))
        
if __name__ =='__main__':
    if len(sys.argv)> 1:
        sys.argv=[sys.argv[0]]
        unittest.main()
    else:
        print("Error: Incorrect Number of arguments. Include a path name for the current directory")
