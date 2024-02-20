class ATM:
    banknotes = [20, 50, 100, 200, 500]

    def __init__(self):
        self.got = [0] * len(self.banknotes)

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.got[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * len(self.banknotes)
        for i in range(len(self.banknotes) - 1, -1, -1):
            if self.banknotes[i] <= amount and self.got[i] > 0:
                count = min(amount // self.banknotes[i], self.got[i])
                amount -= self.banknotes[i] * count
                ans[i] = count
                if amount == 0:
                    break
        else:
            return [-1]

        for i in range(len(self.banknotes)):
            self.got[i] -= ans[i]
        return ans
