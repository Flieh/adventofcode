#import parse

if __name__ == "__main__":
    f = open('sampledata.txt', 'r')
    f = open('data.txt', 'r')
    data = f.read().split('\n')
    data.pop()
    print(data)
