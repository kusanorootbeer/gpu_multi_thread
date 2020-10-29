#!/bin/sh

if [ $3 -eq 1 ]; then
    tmux new-session -d
else
    tmux new-window
fi

for i in `seq 1 $2`
do
    tmux send-keys "sh ./setgpu_run.sh $1" C-m
    tmux new-window
    echo "      gpu No.$1 thread $i start"
    sleep 1s
done

tmux send-keys "python ./check_gpu.py --gpu 0" C-m
