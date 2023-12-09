import time
import tracemalloc

class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def branch_and_bound(jobs):
    n = len(jobs)
    jobs.sort(key=lambda x: x.profit, reverse=True)

    def is_feasible(sequence):
        selected_jobs = sequence[:]

        for job in sequence:
            if job.deadline < len(selected_jobs):
                return False
            selected_jobs.insert(job.deadline, job)

        return all(selected_jobs[i].deadline >= i + 1 for i in range(len(selected_jobs)))

    def bound(sequence, current_profit):
        return current_profit + sum([job.profit for job in sequence])

    def backtrack(sequence, current_profit):
        nonlocal best_sequence, best_profit

        if not is_feasible(sequence):
            return

        if current_profit > best_profit:
            best_sequence = sequence[:]
            best_profit = current_profit

        for job in jobs:
            if job not in sequence:
                new_sequence = sequence + [job]
                new_profit = bound(new_sequence, current_profit)

                if new_profit > best_profit:
                    backtrack(new_sequence, current_profit + job.profit)

    best_sequence = []
    best_profit = 0

    backtrack([], 0)

    return best_sequence

start_time = time.time()
tracemalloc.start()

# Example usage
if __name__ == "__main__":
    jobs = [Job(i, i + 1, (i + 1) * 10) for i in range(1, 30)]
    
    optimal_sequence = branch_and_bound(jobs)

    if optimal_sequence:
        print("Optimal Job Sequence:", [job.id for job in optimal_sequence])
        print("Total Profit:", sum([job.profit for job in optimal_sequence]))
    else:
        print("No feasible solution found.")

print("Process finished --- %s seconds ---" % (time.time() - start_time))

snapshot = tracemalloc.take_snapshot()
tracemalloc.stop()
top_stats = snapshot.statistics('lineno')

# Print the top memory usage statistics
for stat in top_stats:
    print(stat)