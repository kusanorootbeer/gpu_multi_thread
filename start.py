import argparse
import os
from time import sleep
from check_gpu import line
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpulist", help="List of using gpu No., as an example [0,1,2,3]", required=True)
    parser.add_argument("--pyprogram", help="Path of running program, as an example ./hoge/run.py", required=True)
    parser.add_argument("--thread", type=int, help="Number of thread of running program, as an example 4", required=True)
    parser.add_argument("--unpack_session", action="store_false", default=True)
    args = parser.parse_args()

    server = os.uname()[1].split('.')[0]
    line("Program start alert  Server: {}".format(server), 0)

    gpulist = eval(args.gpulist)
    thread = args.thread
    unpack_session = args.unpack_session
    os.environ['RUN_PROGRAM'] = args.pyprogram
    first_loop = True
    for g in gpulist:
        # print("gpu No.{} build start".format(g))
        if first_loop:
            os.system("hostname")
            cmd = "sh ./Nthread.sh {} {} 1".format(g, thread)
            if unpack_session:
                first_loop = False
        else:
            cmd = "sh ./Nthread.sh {} {} 0".format(g, thread)
        os.system(cmd)
