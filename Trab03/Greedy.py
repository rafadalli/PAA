import time
import tracemalloc

class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_sequencing_with_deadlines(jobs):
    n = len(jobs)
    jobs.sort(key=lambda x: x.profit, reverse=True)

    result = [-1] * (max(job.deadline for job in jobs) + 1)
    total_profit = 0

    for job in jobs:
        available_slot = job.deadline

        while available_slot > 0 and result[available_slot] != -1:
            available_slot -= 1

        if available_slot != 0:
            result[available_slot] = job.id
            total_profit += job.profit

    return result[1:], total_profit

start_time = time.time()
tracemalloc.start()

# Example usage
if __name__ == "__main__":
    jobs = [Job(i, i + 1, (i + 1) * 10) for i in range(1, 30)]

    optimal_sequence, total_profit = job_sequencing_with_deadlines(jobs)

    print("Optimal Job Sequence:", optimal_sequence)
    print("Total Profit:", total_profit)

print("Process finished --- %s seconds ---" % (time.time() - start_time))

snapshot = tracemalloc.take_snapshot()
tracemalloc.stop()
top_stats = snapshot.statistics('lineno')

# Print the top memory usage statistics
for stat in top_stats:
    print(stat)