# -*- coding: utf-8 -*-
"""
Created on Feb 28 12:11:28 2015
Dynadeck Assignment
@author: Claire Vannelli

"""

# main function; create all other functions outside of this 
def main():
    txt_File = 'dynadeck.txt'
    term_time = What_time(txt_File,'CONTROL_TERMINATION')
    time_step = Timesteps(txt_File, 'DATABASE_NODOUT')
    total_steps = (float(What_time)/float(Timesteps))
    print('Termination time is {}'.format(term_time))
    print('Time step is {}'.format(time_step))
    print('Total number of time steps is {}'.format(total_steps))
    
# this function will extract the model termination time from file dynadeck.txt
# first number on line after *CONTROL_TERMINATION 
def What_time(txt_File, HEADER):
    open(txt_File)
    finished = False 
    while finished = False:
        for line in txt_File.input():
            process(line)
            val = line.split(',')[0]
        elif HEADER
        finished = True
        return val
    
# this function will extract the time step when results are saved in file dynadeck.txt
# first number on the line after *DATABASE_NODOUT
def Timesteps(txt_File, HEADER):
    open(txt_File)
    finished = False 
    while finished = False:
        for line in txt_File.input():
            process(line)
            val = line.split(',')[0]
        elif HEADER
        finished = True
        return val

if __name__ == "__main__": main()