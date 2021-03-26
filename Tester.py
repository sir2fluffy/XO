# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 11:41:21 2021

@author: charl
"""

# setting up cw timetable
#

cw_slots = [[11, True],[41, True],[48, False],[83, False],[89, False],[96, True],[131, True],[137, True],[144, True],[155, True],[179, True],[209, True]]

import time_table 

cw_table = time_table.table


for slot in cw_slots:
    mode_dict = {True:'Clan',False:'Levi'}
    mode = mode_dict[slot[1]]
    cw_table.add_event(4,0,slot[0],0,mode)

