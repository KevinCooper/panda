def do_run_on_file(fname):
    arr = []
    num = 0
    with open(fname) as f:
        for line in f.readlines():
            if "Time taken for before_block_exec (nanoseconds): " in line:
                arr.append(int(line.split(": ")[1]))
                num += 1
    return max(arr), min(arr), sum(arr) * 1.0 / num, num

f_list = ["Python_runner", "C_runner"]

for q in f_list:
    max_num, min_num, average, num_counted = do_run_on_file(q)
    print(f"{q}: average: {average} min: {min_num} max: {max_num} sample size of {num_counted}")