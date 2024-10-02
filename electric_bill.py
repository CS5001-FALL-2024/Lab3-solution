# get user input
def get_input_kwh_rate():
    return float(input("What is your base rate?"))


def get_input_kwh():
    return float(input("What is your usage?"))


# calculate bill
def calculate_bill(usage: float, rate: float) -> float:
    # if type(usage) != float or type(rate) != float or type(usage) != int or type(rate) != int:

    if rate < 0:
        print("Negative number(s) detected")
        exit(0)
    if 0 <= usage <= 1000.0:
        return usage * rate
    elif 1000.0 < usage:
        return 1000 * rate + (usage - 1000.0) * 1.25 * rate
    else:
        print("Negative number(s) detected")
        exit(0)



def main():
    rate = get_input_kwh_rate()
    usage = get_input_kwh()
    bill = calculate_bill(usage, rate)
    print(f'The total amount due is ${bill}')


if __name__ == "__main__":
    main()