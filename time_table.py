# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 11:41:39 2021

@author: charl
"""
def to_sec(day, hour, minute, seconds=0):
    seconds = seconds + (minute*60) + (hour*60*60) + (day * 60 *60 *24)
    return seconds

def to_hms(query_seconds):
    "returns the hours minutes and seconds"
    hours = int(query_seconds/(60*60))    
    query_seconds = query_seconds - (hours*60*60)   
    minutes = int(query_seconds/(60))    
    seconds = query_seconds - (minutes*60)
    return int(hours),int(minutes),int(seconds)


class table:
    events = []


    
    def add_event(duration, day, hour, minute,description): # think monday is day = 0
        "duration is in hours (decimal so duration = 4.5 is 4 hours 30 minutes)"
        start_time = to_sec(day, hour, minute)
        end_time = start_time + to_sec(0,duration,0)
        table.events.append((start_time,end_time,description))
        
        
    def next_event(query_day, query_hour, query_minute,raw_output = False):
        query_time = to_sec(query_day, query_hour, query_minute)
        
        
        for week in (0,1):
            query_time = query_time - (week* to_sec(7,0,0))
            for event in table.events:
                event_start_time = event[0]
                event_end_time = event[1]
                details = event[2]
                print(event_start_time)
                if query_time < event_end_time:
                    if query_time > event_start_time:
                        #details to return, time till in seconds, and the event descirption
                        time_till = event_end_time - query_time
                        
                        if raw_output == True:
                            time_till = to_hms(time_till)
                        event_active = True
                        return time_till,event_active, details
                    
                    
                    
                    elif query_time < event_start_time:
                        time_till = event_start_time - query_time
                        if raw_output == True:
                            time_till = to_hms(time_till)
                        event_active = False
                        return time_till,event_active, details
              
