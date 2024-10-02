def main():
    card_rank = str(input("Enter card rank: ")).lower()   # getting card rank
    card_value = 0   # default card value
    if card_rank == 'joker':   # converting card rank to value
        card_value = 50
    elif card_rank == 'two' or card_rank == 'ace':
        card_value = 20
    elif card_rank == 'nine' or card_rank == 'ten' or \
            card_rank == 'jack' or card_rank == 'queen' or \
            card_rank == 'king':
        card_value = 10
    elif card_rank == 'four' or card_rank == 'five' or \
            card_rank == 'six' or card_rank == 'seven' or \
            card_rank == 'eight':
        card_value = 5
    elif card_rank == 'three':   # special case
        three_color = str(input('Enter the color of the card:')).lower()
        if three_color == 'black':
            card_value = 5
        elif three_color == 'red':
            card_value = 0
        else:
            print('Invalid color')
            exit()   # exit to prevent from printing anything
    else:
        print('Invalid rank')
        exit()   # exit to prevent from printing anything
    print(f'The card value is {card_value}.')   # print output


if __name__ == '__main__':
    main()
