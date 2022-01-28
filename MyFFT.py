from numpy import fft
import numpy as np

def myfft(norm):
    output = list()
    N = 64
    for n in norm:
        avg = sum(n)/len(n)
        blank = N - len(n)
        bef = blank//2
        af = blank - bef
        n = [avg]*bef + n.tolist() + [avg]*af
        n = [x-avg for x in n]
        f = fft.fft(n)
        f = abs(f)
        f = f[:N//2]
        output.append(f)
    return np.array(output)

if __name__ == "__main__":
    data = np.random.rand(300,60)
    data = myfft(data)
    
    import matplotlib.pyplot as plt
    plt.plot(data)
    plt.show()