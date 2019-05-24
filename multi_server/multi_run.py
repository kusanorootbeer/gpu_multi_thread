
import argparse
import os
import csv

server=0
gpulist=1
thread=2
program_dir=3
pyprogram=4
program_opt=5

def decomment(csvfile):
    for row in csvfile:
        raw = row.split('#')[0].strip()
        if raw: yield raw

if __name__=="__main__":
    server_run_list = []
    with open('./multi_server/run_list.csv', 'r') as f:
        reader = csv.reader(decomment(f),skipinitialspace=True)
        for row in reader:
            server_run_list.append(row)

    for i, runs in enumerate(server_run_list):
        # import pdb;pdb.set_trace()
        cmd = 'scp Nthread.sh check_gpu.py setgpu_run.sh start.py {}:/home/kusano/{}'.format(runs[server], runs[program_dir]) 
        os.system(cmd)

        cmd = 'ssh {} "cd {}; python start.py --gpulist {} --thread {} --pyprogram {} {}"'.format(runs[server], runs[program_dir], runs[gpulist], runs[thread], runs[pyprogram], runs[program_opt])
        os.system(cmd)
        
