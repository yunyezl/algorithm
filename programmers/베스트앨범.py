def solution(genres, plays):

    answer = []
    album = {}
    playRanking = {}

    for genre in genres:
        album[genre] = {}

    for i in range(len(plays)):
        album[genres[i]][i] = plays[i]

    for genre in set(genres):
        s = list(album[genre].values())
        playRanking[genre] = sum(s)

    playRanking = sorted(playRanking.items(), key=lambda x: x[1], reverse=True)

    for i in range(len(playRanking)):
        temp = sorted(album[playRanking[i][0]].items(), key=lambda x: x[1], reverse=True)
        if len(temp) >= 2:
            for j in range(2):
                answer.append(temp[j][0])
        else:
            for j in range(len(temp)):
                answer.append(temp[j][0])

    return answer
