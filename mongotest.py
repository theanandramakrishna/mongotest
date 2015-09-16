#/bin/python

import time
import pymongo
import numpy
from array import array

m = pymongo.MongoClient()

doc = { 'a': 1, 'b': 'hat' }

values = array('d')

for i in xrange(0, 200):
    startTime = time.time()
    m.tests.insertTest.insert(doc, manipulate=False, w=1)
    endTime = time.time()

    executionTime = (endTime - startTime) * 1000 # In ms

    values.append(executionTime)
    print executionTime

print 'Latencies'
print '---------------------------------'
print '50th percentile: %f' % numpy.percentile(values, 50)
print '95th percentile: %f' % numpy.percentile(values, 95)
print '99th percentile: %f' % numpy.percentile(values, 99)


	
