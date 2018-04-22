import numpy as np
import matplotlib.pyplot as plt

def visualize_grid(Xs,ubound=255.0,padding=1):
    (N,H,W,C)=Xs.shape
    grid_size=int(np.ceil(np.sqrt(N)))
    grid_height=H*grid_size+padding*(grid_size-1)
    grid_width=W*grid_size+padding*(grid_size-1)
    grid=np.zeros((grid_height,grid_width,C))
    next_idx=0
    y0,y1=0,H
    for y in range(grid_size):
        x0,x1=0,W
        for x in range(grid_size):
            if next_idx<N:
                img=Xs[next_idx]
                low,high=np.min(img),np.max(img)
                grid[y0:y1,x0:x1]=ubound*(img-low)/(high-low)
                next_idx+=1
            x0+=W+padding
            x1+=W+padding
        y0+=H+padding
        y1+=H+padding
    return grid

def show_net_weights(net):
    W1=net.params['W1']
    W1=W1.reshape(32,32,3,-1).transpose(3,0,1,2)
    plt.imshow(visualize_grid(W1,padding=3).astype('uint8'))
    plt.axis('off')
    plt.show()