from birthday import Birthday


def main():

    # initialize table
    hash_table = []
    for _ in range(12):
        hash_table.append([])

    # populate table
    birthdays = open('./bdaylist.txt')

    for i, date in enumerate(birthdays.readlines()):
        splitted = date.split('/')
        birthday = Birthday(splitted[0], splitted[1], splitted[2])

        hash_table[hash(birthday)].append((birthday, i))

    for k, l in enumerate(hash_table):
        print('Hash location ', k, 'has', len(l), 'in it.')


if __name__ == '__main__':
    main()
