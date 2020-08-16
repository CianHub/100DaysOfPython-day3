from datetime import datetime
import time
import threading


class Stopwatch():
    start_time = None
    stop_time = None

    def start_stopwatch(self):
        self.start_time = datetime.now()
        print('Stopwatch started at: ' + str(self.start_time.time()))

    def stop_stopwatch(self):
        if self.start_time is not None:
            self.stop_time = datetime.now()
            print('Stopwatch stopped at: ' + str(self.stop_time.time()))

            self.time_recorded()

    def time_recorded(self):
        if self.stop_time is not None and self.start_time is not None:
            print('Time recorded: ' +
                  str((self.stop_time - self.start_time).total_seconds()) + ' seconds')
