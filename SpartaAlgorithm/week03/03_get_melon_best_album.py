genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    
    index_dict = {}
    total_dict = {}

    for k,v in zip(genre_array,play_array):
        if k in index_dict.keys():
            index_dict[k].append([play_array.index(v),v])
            total_dict[k] += v
        else:
            index_dict[k] = [[play_array.index(v),v]]
            total_dict[k] = v

    result = []
    sorted_genre = sorted(total_dict.items(),key = lambda x : x[1],reverse = True)
    
    for k,_ in sorted_genre:
        index_array = sorted(index_dict[k],key = lambda x : x[1],reverse= True)
        for i in index_array:
            if index_array.index(i) > 2:
                break
            result.append(i[0])
    
    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ",   get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))