def main() -> None:
    var1 = 10
    var2 = 20

    var1, var2 = var2, var1

    print(f'var1 : {var1}')
    print(f'var2 : {var2}')


if __name__ == "__main__":
    main()