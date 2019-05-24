import os
import subprocess as sp
import argparse
import requests
from time import sleep

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpu", required=True)
    args = parser.parse_args()

    import pdb;pdb.set_trace()
    gpu = args.gpu
    cmd = 'nvidia-smi --id={} --query-gpu=memory.used --format=csv,noheader,nounits'.format(gpu)
    empty_f = 0
    while True:
        sleep(500)
        memory = sp.check_output(cmd, shell=True)
        # import pdb;pdb.set_trace()
        memory = int(memory)
        if memory <= 100:
            empty_f += 1
        else:
            empty_f = 0

        if empty_f >= 2:
            break
    server = os.uname()[1].split('.')[0]
    line("Empty memoly alert \n \n Server: {} \n Gpu: {} ".format(server, gpu), 0)



def line(Me, num):
    if num == 0:
        line_notify_token = 'hogefugahogefuga'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    message = '\n' + Me
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)

if __name__ == '__main__':
    main()
