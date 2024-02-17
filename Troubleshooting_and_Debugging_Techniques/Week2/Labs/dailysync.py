import subprocess
import multiprocessing

src = "./data/prod/"
dest = "./data/prod_backup/"
subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__":
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    pool.apply(subprocess.call, args=(["rsync", "-arq", src, dest],))