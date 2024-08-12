if __name__ == '__main__':
    from utils import get_random_scores, cal_max_min
    
    def sort(data, descending=True):
        data_ = data.copy()
        data_sort = []

        n_data = len(data)
        for _ in range(n_data):
            # descending의 true, false 값을 max에 바로 대입해 식을 간결하게 만들 수 있다. 
            target_value, target_idx = cal_max_min(data_, max=descending)

            data_sort.append(target_value)
            data_.pop(target_idx)

        return data_sort
    
    data = get_random_scores()
    print(f"{data = }")
    print("Descending:", sort(data))
    print("Ascending:", sort(data, descending=False))