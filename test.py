if __name__ == "__main__": 
   import sys 
   import multiprocessing
   # print num cores
   print(multiprocessing.cpu_count())
    # print arguments from commmand line 
   print(sys.argv)