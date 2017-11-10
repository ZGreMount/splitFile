#split a file to severl smaller files based on different people

#import pdb

def saveFile(fileName, context):
    #print(fileName, context)
    file = open(fileName, 'w')

    for i in context:
        file.write(i)
    
    file.close()

def splitFile(fileName):
    file = open(fileName)

    count = 1
    adult = []
    kid = []

    for eachline in file:
        if eachline[:6] != '//////':
            #print(eachline)
            (name, none, words) = eachline.partition(':')
            if name == 'baoqingtian':
                adult.append(words)
            else:
                kid.append(words)
        else:
            adultFile = 'adult' + str(count)
            kidFile = 'kid' + str(count)
            saveFile(adultFile, adult)
            saveFile(kidFile, kid)

            adult = []
            kid = []
            count += 1

    adultFile = 'adult' + str(count)
    kidFile = 'kid' + str(count)
    saveFile(adultFile, adult)
    saveFile(kidFile, kid)

    file.close()


if __name__ == '__main__':
    _DEBUG = False
    if _DEBUG == True:
        import pdb
        pdb.set_trace()

    splitFile('/home/zhaohuizhen/Python/share/test.txt')
