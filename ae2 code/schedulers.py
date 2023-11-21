import math

from des import SchedulerDES
from event import Event, EventTypes
from process import ProcessStates

class FCFS(SchedulerDES): #First come first serve algorithm
    def scheduler_func(self, cur_event):
        ready_processes = [p for p in self.processes if p.process_state == ProcessStates.READY]

        if ready_processes:
            return min(ready_processes, key = lambda p: p.arrival_time)
        return None
    def dispatcher_func(self, cur_process):
        remaining_time = cur_process.run_for(self.quantum, self.time)
        if remaining_time == 0:
            return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=self.time)
        else:
            return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_REQ, event_time=self.time + remaining_time)


class SJF(SchedulerDES): # Shortest job first
    def scheduler_func(self, cur_event):
        ready_processes = [p for p in self.processes if p.process_state == ProcessStates.READY]
        if ready_processes:
            return min(ready_processes, key=lambda p: p.remaining_time)
        return None

    def dispatcher_func(self, cur_process):
        remaining_time = cur_process.run_for(self.quantum,self.time)
        if remaining_time == 0:
            return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=self.time)
        else:
            return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_REQ, event_time=self.time + remaining_time)


class RR(SchedulerDES): #Round Robin
    def scheduler_func(self, cur_event):
        ready_processes = [p for p in self.processes if p.process_state == ProcessStates.READY]
        if ready_processes:
            return ready_processes[0]
        return None

    def dispatcher_func(self, cur_process):
        remaining_time = cur_process.run_for(self.quantum,self.time)
        if remaining_time == 0:
            return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=self.time)
        else:
            return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_REQ, event_time=self.time + remaining_time)


class SRTF(SchedulerDES): # Shortest Remaining Time First
    def scheduler_func(self, cur_event):
        ready_processes = [p for p in self.processes if p.process_state == ProcessStates.READY]
        if ready_processes:
            return min(ready_processes, key=lambda p: p.remaining_time)
        return None

    def dispatcher_func(self, cur_process):
        remaining_time = cur_process.run_for(self.quantum,self.time)
        if remaining_time == 0:
            return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=self.time)
        else:
            return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_REQ, event_time=self.time + remaining_time)
