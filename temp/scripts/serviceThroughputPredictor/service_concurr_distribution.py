import random
import sys

import matplotlib.pyplot as plt
import numpy as np


# python3 service_concurr_distribution.py 500 900 1 20

if __name__ == "__main__":
    request_count = int(sys.argv[1])  # 500
    time_window_sec = int(sys.argv[2])  # 900
    average_process_sec = int(sys.argv[3])  # 1 sec
    n_bins = int(sys.argv[4])  # 32

    sample_times = 2000
    samples = []

    for s in range(sample_times):
        if s % 10 == 0:
            print(s)
        request_list = []
        for i in range(request_count):
            s_t = random.random() * time_window_sec
            e_t = s_t + average_process_sec
            request_list.append((s_t, e_t))

        request_list = sorted(request_list, key=lambda pair: pair[0])

        max_concur = 0

        for i in range(len(request_list)):
            s_t, e_t = request_list[i]
            concur = 0
            j = i - 1
            while j > 0 and request_list[j][1] > s_t:
                j -= 1
                concur += 1
            j = i + 1
            while j < len(request_list) and request_list[j][0] < e_t:
                j += 1
                concur += 1
            max_concur = max(max_concur, concur)
        samples.append(max_concur)

    fig, ax = plt.subplots()
    ax.hist(samples, bins=n_bins)
    ax.set(
        xlabel="maximum concurrent requests",
        ylabel="happend times",
        title="{} requests in {} sec, average request time {} sec, from {} samples".format(
            request_count, time_window_sec, average_process_sec, sample_times
        ),
    )
    # ax.plot(results)
    plt.show()
