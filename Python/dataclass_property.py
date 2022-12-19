from dataclasses import dataclass


@dataclass
class UserInfo:
    name: str
    gender: str
    age: str = '0'
    nickname: str = ''
    email: str = ''

    @property
    def basic_info(self):
        return f'{self.name} / {self.gender} / {self.age}'


def main() -> None:
    user_info = UserInfo(
        name='Tax',
        gender='Male',
        age='23'
    )
    
    print(f'Basic info : {user_info.basic_info}')



if __name__ == "__main__":
    main()