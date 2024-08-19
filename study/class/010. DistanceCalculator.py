

class DistanceCalculator:
    def cal_euclidean(self, u, v):
        return sum((u_el - v_el)**2 for u_el, v_el in zip(u, v))**0.5

    def cal_manhattan(self, u, v):
        # manh_dist = 0
        # for u_el, v_el in zip(u, v):
        #     diff = u_el - v_el
        #     abs_diff = -diff if diff < 0 else diff
        #     manh_dist += abs_diff
        # return manh_dist

        return sum(abs(u_el - v_el) for u_el, v_el in zip(u, v))


u, v = [1, 2, 3], [10, 20, 30]

dist_cal = DistanceCalculator()
print(dist_cal.cal_euclidean(u, v))
print(dist_cal.cal_manhattan(u, v))