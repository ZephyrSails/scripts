import numpy as np
import matplotlib.pyplot as plt
import sys
import random

# python3 server_explod_rate.py 32 10 3 300

if __name__ == "__main__":
    bucket_count = int(sys.argv[1])
    bucket_size = int(sys.argv[2])
    retry = int(sys.argv[3])
    throws = int(sys.argv[4])

    cumulated_chance = 0
    boom_rates = []

    in_process_chance = 1 / bucket_count
    not_in_process_chance = (bucket_count - 1) / bucket_count
    print(in_process_chance, not_in_process_chance)

    # for concurrent_request_count in range(bucket_count, 10000):
    #     if concurrent_request_count < bucket_size:
    #         boom_rates.append(0)
    #         continue
    #     cumulated_chance += in_process_chance ** concurrent_request_count * not_in_process_chance ** (concurrent_request_count - bucket_count) * 16
    #     boom_rates.append(cumulated_chance)
    # plt.plot(boom_rates)
    # plt.show()


    # for concurrent_request_count in range(10):
    #     if concurrent_request_count < bucket_size:
    #         boom_rates.append(0)
    #         continue
    #
    #     safe_rate = 0
    #     for ball_in_bucket in range(bucket_size):
    #         print(ball_in_bucket, concurrent_request_count - ball_in_bucket)
    #         safe_rate += in_process_chance ** ball_in_bucket * not_in_process_chance ** (concurrent_request_count - ball_in_bucket)
    #         print(safe_rate)
    #     boom_rates.append(1 - safe_rate * bucket_count)
    #     print("***")
    # plt.plot(boom_rates)
    # plt.show()

    I = 2000

    results = []
    for throw in range(throws):
        if (throw % 10 == 1):
            print(throw, results[-1])
        res = 0

        for i in range(I):
            chances = [0] * bucket_count
            # add_zero = False
            failed = False
            for t in range(throw):
                throw_failed = True
                for _ in range(retry):
                    b = int(random.random() * bucket_count)
                    if (chances[b] == bucket_size):
                        continue
                    else:
                        chances[b] += 1
                        throw_failed = False
                        break
                if throw_failed:
                    failed = True
                    break
            res += int(failed)
        results.append(res / float(I))
    print(results)

    fig, ax = plt.subplots()
    ax.plot(results)

    bucket_count = int(sys.argv[1])
    bucket_size = int(sys.argv[2])
    retry = int(sys.argv[3])
    throws = int(sys.argv[4])

    ax.set(
        xlabel="concurrent requests",
        ylabel="failure rate",
        title="{} process, each process throughput {}, retry: {}, from {} samples".format(
            bucket_count, bucket_size, retry, I
        ),
    )
    # ax.plot(results)
    plt.show()
