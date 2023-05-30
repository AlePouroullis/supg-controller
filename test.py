from mapElitesSUPG import load_genomes
import time

if __name__ == "__main__":
   print("Starting")
   start_time = time.time()
   genomes = load_genomes(200)
   for key, val in genomes[0].nodes.items():
      print(key, val)

   print("--- %s seconds ---" % (time.time() - start_time))

