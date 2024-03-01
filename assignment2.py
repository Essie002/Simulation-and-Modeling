import math
import random

queue_limit = 100
busy = 1
idle = 0

# Function to initialize simulation parameters
def initialize():
    global clock, server_status, num_in_q, time_last_event, time_next_event, num_custs_delayed, total_of_delays, area_num_in_q, area_server_status
    clock = 0 # Initializing simulation clock
    server_status = idle 
    num_in_q = 0 # Initializing number of customers in the queue
    time_last_event = 0.0 
    num_custs_delayed = 0 
    total_of_delays = 0.0 
    area_num_in_q = 0.0 
    area_server_status = 0.0 
    time_next_event = [0] * 3 # Initializing time of next event for 2 events
    time_next_event[1] = clock + expon(mean_interarrival) # Initializing time of next arrival
    time_next_event[2] = 1.0e+30 # Initializing time of next departure to occur at an almost infinitely distant time in the future

# advance the simulation clock to the next event
def timing():
    global clock, time_next_event, next_event_type
    min_time_next_event = 1.0e+29  # Initializing minimum time for next event
    next_event_type = 0
    for i in range(1, num_events + 1): # Looping through all event types
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i] # Updating minimum time for next event
            next_event_type = i
    if next_event_type == 0: # If no event is found
        print("\nEvent list empty at time", clock)
        exit(1)
    clock = min_time_next_event

# arrival of customers
def arrive():
    global clock, server_status, num_in_q, total_of_delays, num_custs_delayed
    time_next_event[1] = clock + expon(mean_interarrival) # Setting next arrival event time
    if server_status == busy:
        num_in_q += 1
        if num_in_q > queue_limit:
            print("\nOverflow of the array time_arrival at", clock)
            exit(2)
        time_arrival[num_in_q] = clock # Storing arrival time of customer
    else: # idle
        delay = 0.0 # Initializing delay
        total_of_delays += delay #Accumulating delays
        num_custs_delayed += 1 # Incremening no. of custo being delayed
        server_status = busy
        time_next_event[2] = clock + expon(mean_service) # Setting next departure event time

# departure of customers
def depart():
    global clock, server_status, num_in_q, total_of_delays, num_custs_delayed
    if num_in_q == 0:
        server_status = idle
        time_next_event[2] = 1.0e+30 # Setting next departure event time
    else: # custo in queue
        num_in_q -= 1 
        delay = clock - time_arrival[1] # Calculating delay of departed customer
        total_of_delays += delay
        num_custs_delayed += 1
        time_next_event[2] = clock + expon(mean_service) # Setting next departure event time
        for i in range(1, num_in_q + 1):
            time_arrival[i] = time_arrival[i + 1] # Updating arrival times in queue

def report():
    global total_of_delays, num_custs_delayed, clock, area_num_in_q, area_server_status
    with open("mm1.out", "w") as outfile:
        outfile.write("Single server queuing system\n\n")
        outfile.write("Mean interarrival time%11.3f minutes\n\n" % mean_interarrival)
        outfile.write("Mean service time%16.3f minutes\n\n" % mean_service)
        outfile.write("Number of customers%14d\n\n" % num_delays_required)
        outfile.write("Average delay in queue%11.3f minutes\n\n" % (total_of_delays / num_custs_delayed))
        outfile.write("Averge number in queue%10.3f\n\n" % (area_num_in_q / clock))
        outfile.write("Server utilization%15.3f\n\n" % (area_server_status / clock))
        outfile.write("Time simulation ended%12.3f minutes" % clock)

def update_time_avg_stats():
    global clock, area_num_in_q, area_server_status, time_last_event
    time_since_last_event = clock - time_last_event
    time_last_event = clock
    area_num_in_q += num_in_q * time_since_last_event
    area_server_status += server_status * time_since_last_event

# generate exponential random variables
def expon(mean):
    return -mean * math.log(random.random())

# Reading input from file
with open("mm1.in", "r") as infile:
    mean_interarrival, mean_service, num_delays_required = map(float, infile.readline().split())

num_events = 2 # Total number of event types
time_arrival = [0] * (queue_limit + 1) # Initializing array to store arrival times of customers

initialize()

# Running the simulation until required number of customers are served
while num_custs_delayed < num_delays_required:
    timing() 
    update_time_avg_stats()
    if next_event_type == 1: # If next event is arrival
        arrive() 
    elif next_event_type == 2: # If next event is departure
        depart()

report() # Generate sim report


