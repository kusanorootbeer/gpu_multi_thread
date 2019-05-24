import os
if __name__ == "__main__":
    g = os.environ['CUDA_VISIBLE_DEVICES']
    print("This pane's CUDA_VISIBLE_DEVICES =", g)