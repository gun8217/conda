if __name__ == '__main__':
    from utils import get_random_scores, cal_max_min
    
    data = get_random_scores()
    print(f"{data = }")

    target_value, target_idx = cal_max_min(data)
    print(f"{target_value = }, {target_idx = }")
    target_value, target_idx = cal_max_min(data, max=False)    
    print(f"{target_value = }, {target_idx = }")