import numpy as np
from itertools import permutations
from math import hypot

network_counter = 0

while True:
    try:
        N = int(input())

        if N == 0:
            break
        elif N < 0:
            print("Invalid data detected! Check your input!")
        else:
            network_counter += 1

            dist_covered = np.zeros((N, N))
            coords_list = []

            for i in range(N):
                coords_list.append(list(map(int, input().split())))
            for i in range(N):
                for j in range(i + 1, N):
                    dist_covered[i, j] = dist_covered[j, i] = hypot(
                        coords_list[i][0] - coords_list[j][0],
                        coords_list[i][1] - coords_list[j][1]
                    )

            result = dist_covered.sum() + 16*N
            result_way = None

            for current_way in permutations(range(N)):
                print(current_way)
                total_dist_covered = 0
                for i in range(1, N):
                    total_dist_covered += dist_covered[current_way[i-1],
                                                       current_way[i]] + 16
                if total_dist_covered < result:
                    result = total_dist_covered
                    result_way = current_way

            print("*"*79)
            print("Network #{0}".format(network_counter))
            if N == 1:
                print("The network consists only of 1 route\n"
                      "No cable required to maintain this")

            else:
                for i in range(1, N):
                    print("Cable requirement to connect {0} to {1} is {2:.2f} feet."
                        .format(
                            coords_list[result_way[i-1]], coords_list[result_way[i]],
                            dist_covered[result_way[i-1], result_way[i]]+16
                        )
                    )
                print("Number of feet cable required is {0:.2f}".format(result))

    except ValueError:
        print("Invalid data detected! Check your input!")
