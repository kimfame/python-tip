PRICES = {
    'apple': 1_400,
    'banana': 1_200,
    'car': 100_000_000_000,
    'mouse': 500,
    'TV': 23_000,
}

def show_prices():
    print(type(PRICES['apple']))

    for key, value in PRICES.items():
        print(f'{key}: {value}')


def main():
    show_prices()


if __name__ == "__main__":
    main()


