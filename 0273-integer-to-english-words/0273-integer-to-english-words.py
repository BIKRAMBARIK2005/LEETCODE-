class Solution(object):

    below_20 = [
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
        "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
        "Fourteen", "Fifteen", "Sixteen", "Seventeen",
        "Eighteen", "Nineteen"
    ]

    tens = [
        "", "", "Twenty", "Thirty", "Forty", "Fifty",
        "Sixty", "Seventy", "Eighty", "Ninety"
    ]

    def helper(self, num):

        if num == 0:
            return ""

        elif num < 20:
            return self.below_20[num] + " "

        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)

        else:
            return (self.below_20[num // 100] +
                    " Hundred " +
                    self.helper(num % 100))

    def numberToWords(self, num):

        if num == 0:
            return "Zero"

        billion = num // 1000000000
        million = (num // 1000000) % 1000
        thousand = (num // 1000) % 1000
        rest = num % 1000

        ans = ""

        if billion:
            ans += self.helper(billion) + "Billion "

        if million:
            ans += self.helper(million) + "Million "

        if thousand:
            ans += self.helper(thousand) + "Thousand "

        if rest:
            ans += self.helper(rest)

        return ans.strip()