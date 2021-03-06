import cProfile
import io
import logging
import pstats
import os

import pydarn

"""
This is a simple testing script for the Dmap read and write
methods. Warning: need a file to read in.
"""
logging.getLogger('pydarn').setLevel(logging.INFO)
fitacf_file = "../testfiles/20180220.0001.00.rkn.3.0.fitacf"
dmap = pydarn.DmapRead(fitacf_file)
pr = cProfile.Profile()
pr.enable()
d = dmap.read_records()
pr.disable()
s = io.StringIO()
sortby = 'cumtime'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print("Performance for Dmap Read")
print("File: ", fitacf_file)
print("Size: {} MB".format(os.path.getsize(fitacf_file)/1000000))
print(s.getvalue())

dmap = pydarn.DmapRead("../testfiles/20180220.0001.00.rkn.3.0.fitacf")
dmap_data = dmap.read_records()
dmap_write = pydarn.DmapWrite(dmap_data)
pr = cProfile.Profile()
pr.enable()
d = dmap_write.write_dmap("test_dmap_performance.dmap")
pr.disable()
s = io.StringIO()
sortby = 'cumtime'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print("Performance for Dmap Write")
print(s.getvalue())

os.remove("test_dmap_performance.dmap")
