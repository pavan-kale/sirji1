def job_schedule(jobs):
  jobs.sort(key = lambda x:x[1], reverse = True)
  max_deadline = max(jobs, key = lambda x:x[2])[2]
  slot = [False] * max_deadline
  profit = 0
  n = len(jobs)

  for i in range(n):
    deadline = jobs[i][2] - 1
    
    while deadline>=0 and slot[deadline]:
      deadline = deadline - 1
      
    if deadline>=0:
      slot[deadline] = True
      profit += jobs[i][1]
    
  return profit

jobs = [(1, 50, 2), (2, 10, 1), (3, 20, 2), (4, 30, 1), (5, 40, 3)]
print(job_schedule(jobs))

# Certainly! Let’s break down the loop within the job_schedule function step by step:

# Initialization:
# The loop iterates over the range of indices from 0 to n-1 (where n is the total number of jobs).
# For each iteration, it performs the following steps:
# Deadline Adjustment:
# deadline = jobs[i][2] - 1 calculates the adjusted deadline for the i-th job.
# jobs[i][2] retrieves the deadline of the i-th job (since the deadline is stored at index 2 in each job tuple).
# Subtracting 1 ensures that the deadline is inclusive (i.e., the job can be scheduled up to and including the specified deadline).
# Slot Availability Check:
# The while loop checks whether there is an available slot before the adjusted deadline:
# while deadline >= 0 and slot[deadline]:
# If deadline is greater than or equal to zero (i.e., a valid time slot), and the slot at that deadline is already occupied (slot[deadline] is True), the loop continues.
# If the slot is already taken, the code decrements deadline by 1 to check the previous time slot.
# This process repeats until an available slot is found or until deadline becomes negative.
# Job Scheduling:
# If an available slot is found (i.e., deadline >= 0), the following steps occur:
# slot[deadline] = True marks the slot as occupied (indicating that the job is scheduled at that time).
# profit += jobs[i][1] adds the profit of the i-th job to the total profit.
# The job is successfully scheduled within its adjusted deadline.
# Return Total Profit:
# After processing all jobs, the function returns the accumulated profit.
# In summary, this loop ensures that each job is scheduled within its specified deadline (inclusive) while maximizing the total profit. It iterates through the sorted jobs, checks for available slots, and updates the profit accordingly. The algorithm prioritizes higher-profit jobs and schedules them optimally within the given deadlines.