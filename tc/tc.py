import os
import time
import sys

def parse_trace(path):
    ret = []
    with open(path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if "#" not in line and len(line) > 0:
                bw, loss, delay = list(map(float, line.split(",")))
                ret.append([bw, loss, delay])
    return ret

# need `pip install tcconfig`
def run_tc(trace, loop=True):
    os.system("tcdel eth0 --all")
    while True:
        for bw, loss, delay in trace:
           t1 = time.time()
           cmd = "tcset --change eth0 --rate {}Kbps --loss {}% --delay {}ms".format(bw, loss, delay) 
           os.system(cmd)
           print(cmd)
           time.sleep(max(0, 1 - (time.time() - t1)))
        
        os.system("tcdel eth0 --all")
        if not loop:
            break


if __name__ == "__main__":
    if len(sys.argv) == 1:
        trace = parse_trace("./trace.demo")
    else:
        trace = parse_Trace(sys.argv[1])

    run_tc(trace)
