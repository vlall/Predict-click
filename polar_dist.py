import math

def polar_dist(S_1, S_2):
    if len(S_1) != len(S_2):
        return 0
    return [(1/(math.pi)) * math.acos[(sum([S_1[i][1]*S_2[i] for i in range(len(S_2))])) / ((math.sqrt(sum[i]**2)) * (math.sqrt(sum[j]**2)))
    ]]


#(sum(i*j for i,j in zip(S_1,S_2)))

        # total_sum = 0
        # for i in range(len(s1)):
        #    total_sum += s1[i]*s2[i]
