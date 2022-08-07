from dataclasses import dataclass, field


@dataclass
class UserInfo:
    name: str
    gender: str
    age: str = '0'
    nickname: str = ''
    email: str = ''
    #sub_info: str = ''
    _sub_info: str = field(init=False, repr=False)


def main() -> None:
    user_info = UserInfo(
        name='Tax',
        gender='Male',
        age='23'
    )
    
    print(user_info)



if __name__ == "__main__":
    main()