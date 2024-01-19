# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 15:07:34 2024

@author: User
"""

class TV:
    def __init__(self):
        self.channel = 1
        self.volume = 0
        self.on = False
        
    def turnOn(self):
        self.on = True
        
    def turnOff(self):
        self.on = False
        
    def setVolume(self, volume):
        self.volume = volume
        
    def setChannel(self, channel):
        self.channel = channel
        
tv = TV()
tv.turnOn()
tv.setChannel(11)
tv.setVolume(6)

print("TV의 채널 : ", tv.channel, "\nTV의 음량 : ", tv.volume)