def main() -> None:
    set_nums = {i for i in range(5)}
    for num in set_nums:
        print(num)

    dict_nums = {i : i for i in range(5)}
    for key, value in dict_nums.items():
        print(f'key: {key}, value: {value}')


if __name__ == "__main__":
    main()