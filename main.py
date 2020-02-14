import csv


def main():
    path = 'BasiYarasiListes.csv'

    fileCSV = open('BasiYarasiListes-formatted.csv', 'w', newline='\n')
    writer = csv.writer(fileCSV)
    with open(path, encoding="utf8", errors='ignore') as f:
        for row in csv.reader(f, delimiter='@'):
            writer.writerow(row)

if __name__ == "__main__":
    main()

