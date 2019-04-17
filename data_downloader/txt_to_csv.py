import argparse
import csv

txt_path = ""
csv_path = ""

def extract_url():
    global txt_path
    global csv_path
    lines = open(txt_path, "r")
    csv_file = open(csv_path, "w")
    out = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    urls = []
    for line in lines:
        urls.append([line.split()[1]])
    print(urls)
    out.writerows(urls)
    csv_file.close()


def main():
    global txt_path
    global csv_path
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', help="path to text url file", action='store', dest="txt_path", default="urls.txt")
    parser.add_argument('-c', help="path to csv url file", action='store', dest="csv_path", default="urls.csv")
    args = parser.parse_args()
    txt_path = args.txt_path
    csv_path = args.csv_path
    extract_url()


main()




