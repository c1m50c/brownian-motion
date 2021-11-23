import matplotlib.pyplot as plt
import numpy as np


SAMPLE_POINTS: int = 10_000
START_TIME: float = 0.0
FINAL_TIME: float = 1.0


def main():
    times: np.array = np.linspace(start=START_TIME, stop=FINAL_TIME, num=SAMPLE_POINTS)
    t_step: float = times[1] - times[0]
    b_step: float = np.sqrt(t_step) * np.random.normal(size=(SAMPLE_POINTS - 1,))
    
    b0 = np.zeros(shape=(1,))
    b = np.concatenate((b0, np.cumsum(b_step)))
    
    plt.plot(times, b)
    plt.show()


if __name__ == "__main__":
    main()