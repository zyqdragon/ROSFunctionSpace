import numpy as np
from time import sleep
from multiprocessing import shared_memory
# Attach to the existing shared memory block
existing_shm = shared_memory.SharedMemory(name='testspace')
# Note that a.shape is (6,) and a.dtype is np.int64 in this example
while True:
   c = np.ndarray((2,3), dtype=np.int64, buffer=existing_shm.buf)
   print("-------c=",c)
   sleep(1)
existing_shm.close()
existing_shm.unlink()
