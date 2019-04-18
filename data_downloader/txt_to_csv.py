import argparse
import csv

txt_path = ""
csv_path = ""
max_download = 0

def extract_url():
    global txt_path
    global csv_path
    global max_download
    i = 0
    lines = open(txt_path, "r")
    csv_file = open(csv_path, "w")
    out = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    urls = []
    for line in lines:
        urls.append([line.split()[1]])
        i = i + 1
        if i > max_download: break
    out.writerows(urls)
    csv_file.close()


def main():
    global txt_path
    global csv_path
    global max_download
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', help="path to text url file", action='store', dest="txt_path", default="urls.txt")
    parser.add_argument('-c', help="path to csv url file", action='store', dest="csv_path", default="urls.csv")
    parser.add_argument('-m', help="max num of urls", action='store', dest="max", default="urls.csv")
    args = parser.parse_args()
    txt_path = args.txt_path
    csv_path = args.csv_path
    max_download = int(args.max)
    extract_url()


main()




