#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 10:09:40 2017

@author: foolwolf0068
"""

from TV import TV
def main():
    tv1=TV()
    tv1.turnOn()
    tv1.setChannel(20)
    tv1.setVolume(3)
    
    tv2=TV()
    tv2.turnOn()
    tv2.channelUp()
    tv2.channelUp()
    tv2.channelUp()
    tv2.volumeUp()
    
    print("tv1's channel is",tv1.getChannel(),"and volume level is",tv1.getVolumeLevel())
    print("tv2's channel is",tv2.getChannel(),"and volume level is",tv2.getVolumeLevel())
main()