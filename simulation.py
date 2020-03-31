import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

from matplotlib.animation import FuncAnimation


class society():
    def __init__(self, XY, states):
        self.XY, self.states = XY, states
        self.directions = ["left", "right", "up", "down", "stop"]
        self.fig, self.ax = plt.subplots()

    def setup(self):
        self.sect = self.ax.scatter(self.XY[:, 0], self.XY[:, 1], c=self.states,
                                    cmap="jet", edgecolor="k")
        return self.sect,

    def update(self, i):
        self.step(i)
        self.sect.set_offsets(self.XY)
        # self.sect.set_array()
        return self.sect,

    def step(self, i):
        if(i % 100 == 0):
            self.dxy = np.zeros((self.XY.shape[0], 2))
            for i in range(self.XY.shape[0]):
                directon = random.choice(self.directions)
                if(directon == "left"):
                    self.dxy[i, 0] -= 10
                if(directon == "right"):
                    self.dxy[i, 0] += 10
                if(directon == "up"):
                    self.dxy[i, 1] += 10
                if(directon == "down"):
                    self.dxy[i, 1] -= 10
        for i in range(self.XY.shape[0]):
            temp = self.XY[i]+0.01*self.dxy[i]
            if(temp[0] > 100 or temp[0] < 0):
                self.dxy[i] *= -1
            if(temp[1] > 100 or temp[1] < 0):
                self.dxy[i] *= -1

        self.XY += 0.01*self.dxy


if __name__ == '__main__':
    # a = AnimatedScatter()
    Xs, Ys, states = [], [], []
    for i in range(100):
        Xs.append(random.random()*100)
        Ys.append(random.random()*100)
        states.append("blue")
    S = society(np.random.random((100, 2))*100, states)
    ani = FuncAnimation(S.fig, S.update, interval=30,
                        init_func=S.setup, blit=True)
    plt.show()
