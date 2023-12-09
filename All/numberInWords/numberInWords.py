digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
x = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]


def conv(num, s):
    ans = digits[num // 100] + " hundred " if num // 100 > 0 else ""
    num %= 100
    if num < 10:
        ans += digits[num]
    elif num < 20:
        ans += teens[num % 10]
    else:
        ans += x[num // 10] + ("-" + digits[num % 10] if num % 10 > 0 else "")
    return ans + s if len(ans) > 0 else ans


def numberInWords(n):
    ans = (
        conv(n // 1000000, " million ")
        + conv((n % 1000000) // 1000, " thousand ")
        + conv(n % 1000, "")
    )
    ans = " ".join(ans.split())
    return ans.capitalize()
