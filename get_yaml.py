import yaml
import sys
def get_value(term):
    f = open('system.yml')
    dataMap = yaml.load(f)
    f.close()
    return dataMap[term]
def main():
    term = sys.argv[1]
    print get_value(term)

if __name__ == '__main__':
    main()
