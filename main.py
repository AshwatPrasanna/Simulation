import subprocess
import multiprocessing

# This is responsible for evenly dividing the range (and therefore computational time) with multiprocessing

log_2_num_threads = 3 # Number of threads being a power of 2

target = <enter target> # The range is 2^0 to 2^target (inclusive, exclusive respectively)

nums_per_thread = 2**(target - log_2_num_threads)

# The idea is to keep the number of numbers per thread the same. Therefore, 2^(target-log_2_num_threads) to 2^(target-log_2_num_threads+1) will be one thread.


list_of_thread_bounds = [] # the format is [[[...], [...]], [[...]], ...], where every element has the same number of numbers, but different numbers of elements


first_thread = []
for i in range(0, (target - log_2_num_threads)):
    first_thread.append([2**(i), 2**(i+1)])

list_of_thread_bounds.append(first_thread)

for i in range(1, 2**log_2_num_threads):
    bounds = [i*nums_per_thread, (i+1)*nums_per_thread]
    list_of_thread_bounds.append([bounds]) # in ascending order

# At this point, list_of_thread_bounds is complete. Each element in list_of_thread_bounds goes to its own thread. Later, they all have to be combined.

# File management

def run_process(queue, bounds):
    # runs synchronously
    
    results = []

    for bound in bounds:
        result = subprocess.run(["./process", str(bound[0]), str(bound[1])], capture_output=True).returncode
        results.append(result)

    queue.put(results)


def parseresults(results):
    h_k_values = []

    for k in range(2, target+1): # k is the number of digits
        if k-1 < (target - log_2_num_threads): # in the first element
            h_k_values.append(results[0][k-1])
        else:
            subset = results[2**(k-1-(target - log_2_num_threads)):2**(k-(target - log_2_num_threads))]
            elements = []
            for element in subset:
                elements.append(element[0])
            h_k_values.append(max(elements))

    print(h_k_values)

    


if __name__ == "__main__":
    processes = []
    multiprocessing.set_start_method("spawn")

    queues = [] 
    

    for index, bounds in enumerate(list_of_thread_bounds):
        queue = multiprocessing.Queue()
        queues.append(queue)
        process = multiprocessing.Process(target=run_process, name=str(index), args=(queue, bounds))
        process.start()
        processes.append(process)

    results_in_order = []

    for index, process in enumerate(processes):
        results_in_order.append(queues[index].get())
        process.join()

    parseresults(results_in_order)
