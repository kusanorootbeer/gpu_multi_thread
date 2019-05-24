#!/bin/sh

if [ $3 -eq 1 ]; then
    tmux new-session -d
else
    tmux new-window
fi

for i in `seq 1 $2`
do
    if [ $1 -eq 0 ]; then
        tmux send-keys 'sh ./setgpu_run.sh 0 ' C-m
    elif [ $1 -eq 1 ]; then
        tmux send-keys 'sh ./setgpu_run.sh 1' C-m
    elif [ $1 -eq 2 ]; then
        tmux send-keys 'sh ./setgpu_run.sh 2' C-m
    elif [ $1 -eq 3 ]; then
        tmux send-keys 'sh ./setgpu_run.sh 3' C-m
    elif [ $1 -eq 4 ]; then
        tmux send-keys 'sh ./setgpu_run.sh 4' C-m
    elif [ $1 -eq 5 ]; then
        tmux send-keys 'sh ./setgpu_run.sh 5' C-m
    elif [ $1 -eq 6 ]; then
        tmux send-keys 'sh ./setgpu_run.sh 6' C-m
    else
        tmux send-keys 'sh ./setgpu_run.sh 7' C-m
    fi
    tmux new-window
    echo "      gpu No.$1 thread $i start"
    sleep 1s
done
if [ $1 -eq 0 ]; then
    tmux send-keys 'python ./check_gpu.py --gpu 0 ' C-m
elif [ $1 -eq 1 ]; then
    tmux send-keys 'python ./check_gpu.py --gpu 1 ' C-m
elif [ $1 -eq 2 ]; then
    tmux send-keys 'python ./check_gpu.py --gpu 2 ' C-m
elif [ $1 -eq 3 ]; then
    tmux send-keys 'python ./check_gpu.py --gpu 3 ' C-m
elif [ $1 -eq 4 ]; then
    tmux send-keys 'python ./check_gpu.py --gpu 4 ' C-m
elif [ $1 -eq 5 ]; then
    tmux send-keys 'python ./check_gpu.py --gpu 5 ' C-m
elif [ $1 -eq 6 ]; then
    tmux send-keys 'python ./check_gpu.py --gpu 6 ' C-m
else
    tmux send-keys 'python ./check_gpu.py --gpu 7 ' C-m
fi


