# @file      time_utils.py
# @author    Ignacio Vizzo     [ivizzo@uni-bonn.de]
#
# Copyright (c) 2019 Ignacio Vizzo, all rights reserved

import time


def timeit(f):

    def wrap(*args, **kargs):
        time1 = time.time()
        ret = f(*args, **kargs)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__,
                                                    (time2 - time1) * 1000.0))

        return ret

    return wrap
