#!/bin/bash                                                                                                                                                                                                 

sync && echo 1 | sudo tee /proc/sys/vm/drop_caches
sync && echo 2 | sudo tee /proc/sys/vm/drop_caches
sync && echo 3 | sudo tee /proc/sys/vm/drop_caches

