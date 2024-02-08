class Solution:
    def intToRoman(self, num: int) -> str:
        if 1000 <= num:
            return 'M' + self.intToRoman(num-1000)
        elif 900 <= num:
            return 'CM' + self.intToRoman(num-900)
        elif 500 <= num:
            return 'D' + self.intToRoman(num-500)
        elif 400 <= num:
            return 'CD' + self.intToRoman(num-400)
        elif 100 <= num:
            return 'C' + self.intToRoman(num-100)
        elif 90 <= num:
            return 'XC' + self.intToRoman(num-90)
        elif 50 <= num:
            return 'L' + self.intToRoman(num-50)
        elif 40 <= num:
            return 'XL' + self.intToRoman(num-40)
        elif 10 <= num:
            return 'X' + self.intToRoman(num-10)
        elif 9 <= num:
            return 'IX' + self.intToRoman(num-9)
        elif 5 <= num:
            return 'V' + self.intToRoman(num-5)
        elif 4 <= num:
            return 'IV' + self.intToRoman(num-4)
        elif 1 <= num:
            return 'I' + self.intToRoman(num-1)
        else:
            return ''



for i in range(1994, 1994+1):
    print(Solution().intToRoman(i))