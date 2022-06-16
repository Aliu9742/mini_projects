import argparse

def get_args():
    parser = argparse.ArgumentParser(
        description="take in integers (-9999 to 9999) and return their name in string")
    parser.add_argument(
        "-n", type=int, help="input integer")
    return parser.parse_args()


def count(num: int) -> str:
    "given a number as int (eg. 12) return its name in string (twelve)"

    num_name = ['zero', 'one', 'two', 'three', 'four', 'five',
                'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']

    prefixes = {2: 'twen',
                3: 'thir',
                5: 'fif'}

    suffixes = {1: 'ty',
                2: ' hundred',
                3: ' thousand'}
    sign = ""
    if num < 0:
        sign = "negative"
        num = abs(num)

    if num <= 12:
        # 0-12
        return "{} {}".format(sign, num_name[num]).strip()

    elif num <= 19:
        # 13-19
        ones_place_digit = int(str(num)[1])
        if ones_place_digit in prefixes.keys():
            # takes care of thirteen and fifteen
            prefix = prefixes[ones_place_digit]
        else:
            prefix = num_name[ones_place_digit]
        return "{} {}teen".format(sign, prefix).strip()

    elif num <= 9999:
        #20 and above
        # if num is 183 digits is [3, 8, 1]
        #3*10^0 + 8*10^1 + 1*10^2
        # storing the number backwards ensures the index of digits list corresponds to powers of 10
        digits = [int(d) for d in str(num)[::-1]]
        digits_name = [''] * len(digits)

        for index, d in enumerate(digits):
            if index in suffixes.keys():
                if d == 0:
                    digits_name[index] = 'and'

                elif d in prefixes.keys():
                    digits_name[index] = '{}{}'.format(
                        prefixes[d], suffixes[index])
                else:
                    digits_name[index] = '{}{}'.format(
                        num_name[d], suffixes[index])
            else:
                if d == 0:
                    digits_name[index] = ''
                else:
                    digits_name[index] = num_name[d]

        digits_name.reverse()
        return ("{} ".format(sign) + ' '.join(digits_name)).strip()
    else:
        return "I don't know how to count that"


if __name__ == "__main__":
    args = get_args()
    print(count(args.n))
