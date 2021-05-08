


def main():
    MAX_SNOW_AMT = 8
    # prompt and read input
    snowTotal = float(input('Enter the total snowfall in inches as a number: '))
    # check for snowfall limits
    if (snowTotal >= MAX_SNOW_AMT):
        print('Classes will be conducted remotely.')
    else:
        print('Classes will be conducted on campus.')

main()
