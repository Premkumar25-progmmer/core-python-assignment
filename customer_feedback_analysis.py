def positive_feedback(ratings):
    # if no ratings are given
    if len(ratings) == 0:
        return "No ratings available."

    # count ratings which are 4 or 5
    positive = 0
    for r in ratings:
        if r >= 4:
            positive += 1

    percent = (positive / len(ratings)) * 100
    return round(percent, 2)

ratings = [5, 4, 3, 5, 2, 4, 1, 5]

percentage = positive_feedback(ratings)
print("Positive Feedback:", str(percentage) + "%")
