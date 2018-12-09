
def main():

    sample = '' 
    status = ''

    outfile = open('out.txt', 'w')

    with open('report.log') as report:
        for line in report.readlines():
            if 'Scanning' in line:
                sample = line.split(' ')[1]
                continue

            if 'Trojan.Mauvasie' in line:
                outfile.write(sample)


if __name__ == '__main__':

    main()

