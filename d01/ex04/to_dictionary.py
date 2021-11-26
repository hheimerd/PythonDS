

def to_dictionary(tuples: list):
    dictionary = {}
    for tuple in tuples:
        num = str(tuple[1])
        if num in dictionary:
            dictionary[num].append(tuple[0])
        else:
            dictionary[num] = [tuple[0]]

    return dictionary


def main():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]

    countries_dict = to_dictionary(list_of_tuples)
    for num, countries in countries_dict.items():
        for country in countries:
            print("'{}' : '{}".format(num, country))

    # for country in list_of_tuples:
    #     print("'{}' : '{}".format(country[1], country[0]))


if __name__ == '__main__':
    main()
