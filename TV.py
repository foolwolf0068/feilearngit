#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:50:20 2017

@author: foolwolf0068
"""
class TV(object):
    def __init__(self):
        self.channel = 1
        self.volumeLevel=1
        self.on=False
    def turnOn(self):
        self.on=True
    def turnOff(self):
        self.off=True
    def getChannel(self):
        return self.channel
    def setChannel(self,channel):
        if self.on and 1<=self.channel<=120:
            self.channel=channel
    def getVolumeLevel(self):
        return self.volumeLevel
    def setVolume(self,volumeLevel):
        if self.on and 1<=self.volumeLevel<=7:
            self.volumeLevel=volumeLevel
    def channelUp(self):
        if self.on and self.channel<120:
            self.channel+=1
    def channelDown(self):
        if self.on and self.channel>1:
            self.channel-=1
    def volumeUp(self):
        if self.on and self.volumeLevel<7:
            self.volumeLevel+=1
    def volumeDown(self):
        if self.on and self.volumeLevel>1:
            self.volumeLevel-=1
