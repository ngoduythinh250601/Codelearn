def tennisSet(score1, score2):
    if score1 < score2:
        score1, score2 = score2, score1
    return (score1 == 6 and score2 < 5) or (score1 == 7 and 5 <= score2 < 7)
