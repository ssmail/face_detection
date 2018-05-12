# -*- coding: utf-8 -*-
# !/usr/bin/env python
# author = Chris Hong

# Copyright 2000-2017 by Koudai Corporation.
# All rights reserved.

# This software is the confidential and proprietary information of
# Koudai Corporation ("Confidential Information"). You
# shall not disclose such Confidential Information and shall use
# it only in accordance with the terms of the license agreement
# you entered into with Koudai.

import PyBaiduYuyin as pby
import sys
import time
from ratelimit import limits

reload(sys)
sys.setdefaultencoding('utf-8')
__author__ = 'hongkefeng'


class Jarvs(object):

    def __init__(self):
        self.tts = pby.TTS(app_key='UduESRMD9LG3LbVTAd1DMVVf', secret_key='eabb65508568611ad60348afd551c918')

    @limits(calls=1, period=10)
    def say(self, text):
        self.tts.say(text)


def rate_limited(maxPerSecond):
    minInterval = 1.0 / float(maxPerSecond)

    def decorate(func):
        lastTimeCalled = [0.0]

        def rate_limited_function(*args, **kargs):
            elapsed = time.clock() - lastTimeCalled[0]
            leftToWait = minInterval - elapsed
            if leftToWait > 0:
                time.sleep(leftToWait)
            ret = func(*args, **kargs)
            lastTimeCalled[0] = time.clock()
            return ret

        return rate_limited_function

    return decorate
