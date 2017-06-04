#!/usr/bin/env python
# -*- coding: utf-8 -*-     
from random import randrange

class Job:
    _job_list = ["Snooper Deterrent", "Guard Pet", "Contraband Sniffer", "Vermin Chaser", "Therapy Pet", "Seeing Eye Pet", "Stunt Double"]
    def __init__(self):
        self._name = self._job_list[randrange(0,len (self._job_list))]
    def __call__(self):
        return self._name

