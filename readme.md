# How to use and the view, as an example
    python start.py --gpulist [0,1] --pyprogram ./run.py --thread 4

gpu No.0 thread 1 start  
gpu No.0 thread 2 start  
gpu No.0 thread 3 start  
gpu No.0 thread 4 start  
gpu No.1 thread 1 start  
gpu No.1 thread 2 start  
gpu No.1 thread 3 start  
gpu No.1 thread 4 start  

## build session 
tmux sessionごとにgpu番号は統一してる  

--pack_sessionをつければtmuxのsessionは一つにまとめてくれる

# How to use multi server 
    python multi_server/multi_run.py

ambassador.cs.scitec.kobe-u.ac.jp  
　　gpu No.0 thread 1 start  
　　gpu No.0 thread 2 start  
　　gpu No.1 thread 1 start  
　　gpu No.1 thread 2 start  

sydney.cs.scitec.kobe-u.ac.jp  
　　gpu No.0 thread 1 start  
　　gpu No.0 thread 2 start  
　　gpu No.1 thread 1 start  
　　gpu No.1 thread 2 start  

これを使えば手元のpcから一度に複数のserverでrunできる．  
multi server multi thread run!

# 注意 
run_list.csvの通りのserver, gpulist, threadで python programを回してくれる．  
回す前にはmulti_run.pyの25行目を，自分のuser nameに書き換える必要あり.  

check_gpu.pyのline アクセストークンは，自分のを使ってほしい




