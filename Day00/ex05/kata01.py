def kata01():
    languages = {
            'Python': 'Guido van Rossum',
            'Ruby': 'Yukihiro Matsumoto',
            'PHP': 'Rasmus Lerdorf',
            }
    for x, y in languages.items():
        print(x, "was created by", y)


kata01()
