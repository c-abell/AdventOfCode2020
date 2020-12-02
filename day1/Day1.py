class TwoSum:
    def __init__(self):
        pass

    def add(self, number1, number2):
        return number1 + number2

    def readinput(self):
        nums = []
        input = open("input.txt", "r")
        for line in input:
            nums.append(line[:-1])
        input.close()
        return nums

    def splitnums(self, numbers):
        bignums = []
        littlenums = []
        for number in numbers:
            if int(number) > 999:
                bignums.append(int(number))
            else:
                littlenums.append(int(number))
        bignums.sort()
        littlenums.sort()
        return bignums, littlenums

    def addnums(self, bignums, littlenums):
        for littlenum in littlenums:
            for bignum in bignums:
                if self.add(littlenum, bignum) == 2020:
                    return bignum, littlenum

    def multnums(self, number1, number2):
        return number1 * number2

    def findthreesum(self, littlenums):
        x = 0
        y = 1
        z = 2
        nums = []
        while x < len(littlenums):
            while y < len(littlenums):
                while z < len(littlenums):
                    if littlenums[x] + littlenums[y] + littlenums[z] == 2020:
                        nums.append(littlenums[x])
                        nums.append(littlenums[y])
                        nums.append(littlenums[z])
                        return nums
                    else:
                        z+=1
                y+=1
                z = 0
            x+=1
            y = 0
            z = 0

    def multthreenums(self, numbers):
        return numbers[0] * numbers[1] * numbers[2]


instance = TwoSum()
nums = instance.readinput()
bignums, littlenums = instance.splitnums(nums)
num1, num2 = instance.addnums(bignums, littlenums)
answer1 = instance.multnums(num1, num2)
threenums = instance.findthreesum(littlenums)
answer2 = instance.multthreenums(threenums)
