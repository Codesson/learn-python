"""
Chapter 13: 클래스 & 객체지향 프로그래밍 (OOP)
================================================
class, 상속, 캡슐화 등 OOP의 기본을 배웁니다.
"""

# ============================================================
# JavaScript vs Python 비교 - 클래스
# ============================================================
#
#  JavaScript                           Python
#  ─────────────────────────────────    ─────────────────────────────
#  class Dog {                          class Dog:
#    constructor(name) {                    def __init__(self, name):
#      this.name = name                        self.name = name
#    }                                  
#    bark() {                               def bark(self):
#      console.log("멍!")                       print("멍!")
#    }                                  
#  }                                    
#
#  class Cat extends Animal {}          class Cat(Animal):
#  super()                              super().__init__()
#  new Dog("바둑이")                    Dog("바둑이")     (new 키워드 없음!)
#  dog instanceof Dog                   isinstance(dog, Dog)
#  this.name                            self.name
#
#  get name() { return this._name }     @property  def name(self):
#  set name(v) { this._name = v }       @name.setter  def name(self, v):
#  static method() {}                   @staticmethod  def method():
#  #privateField                        __private_field  (__ 접두사)
#
#  핵심 차이:
#  1) this → self (self는 첫 번째 매개변수로 명시적 전달!)
#  2) constructor → __init__
#  3) new 키워드 불필요
#  4) extends → 괄호 안에 부모 클래스
#  5) 메서드의 첫 인자에 항상 self를 넣어야 함 (가장 큰 차이!)
#

# ============================================================
# 1. 클래스 기초
# ============================================================
print("=== 클래스 기초 ===")


class Dog:
    """강아지를 표현하는 클래스"""

    # __init__: 초기화 메서드 (생성자)  ← JS의 constructor()
    def __init__(self, name, breed, age):
        self.name = name      # JS의 this.name = name
        self.breed = breed    # self = JS의 this (명시적 전달!)
        self.age = age

    # 메서드 (행동) - self를 반드시 첫 인자로!
    def bark(self):           # JS: bark() { ... } (self 불필요)
        print(f"{self.name}: 멍멍!")

    def info(self):
        print(f"이름: {self.name}, 견종: {self.breed}, 나이: {self.age}살")


# 인스턴스 생성 (new 키워드 없음!)
# JS: const dog1 = new Dog("바둑이", "진돗개", 3)
dog1 = Dog("바둑이", "진돗개", 3)
dog2 = Dog("초코", "푸들", 2)

dog1.bark()
dog2.bark()
dog1.info()
dog2.info()

# 속성 접근/수정
print(f"\n{dog1.name}의 나이: {dog1.age}")
dog1.age = 4
print(f"생일 후 나이: {dog1.age}")

print()


# ============================================================
# 2. 클래스 변수 vs 인스턴스 변수
# ============================================================
print("=== 클래스 변수 vs 인스턴스 변수 ===")


class Student:
    # 클래스 변수: 모든 인스턴스가 공유
    school = "파이썬 학교"
    student_count = 0

    def __init__(self, name, grade):
        # 인스턴스 변수: 각 인스턴스 고유
        self.name = name
        self.grade = grade
        Student.student_count += 1

    def introduce(self):
        print(f"[{self.school}] {self.name} ({self.grade}학년)")


s1 = Student("홍길동", 1)
s2 = Student("이영희", 2)
s3 = Student("김철수", 3)

s1.introduce()
s2.introduce()
print(f"총 학생 수: {Student.student_count}")

print()


# ============================================================
# 3. 특수 메서드 (매직 메서드 / 던더 메서드)
# ============================================================
print("=== 특수 메서드 ===")


class Vector:
    """2D 벡터 클래스"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """print()로 출력할 때"""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        """개발자용 표현"""
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):
        """+ 연산자"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """- 연산자"""
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        """== 비교"""
        return self.x == other.x and self.y == other.y

    def __len__(self):
        """len() 호출 시 벡터의 크기(정수)"""
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def magnitude(self):
        """벡터의 크기"""
        return (self.x ** 2 + self.y ** 2) ** 0.5


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 == v2: {v1 == v2}")
print(f"|v1| = {v1.magnitude():.2f}")

print()


# ============================================================
# 4. 상속 (Inheritance)
# ============================================================
print("=== 상속 ===")


class Animal:
    """동물 기본 클래스"""

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name}: {self.sound}!")

    def __str__(self):
        return f"{self.name} (동물)"


class Cat(Animal):     # JS: class Cat extends Animal { }
    """고양이 클래스 (Animal 상속)"""

    def __init__(self, name, color):
        super().__init__(name, "야옹")    # JS: super(name, "야옹")
        self.color = color

    def purr(self):
        print(f"{self.name}가 골골거립니다...")

    def __str__(self):
        return f"{self.name} ({self.color} 고양이)"


class Parrot(Animal):
    """앵무새 클래스"""

    def __init__(self, name, can_talk=True):
        super().__init__(name, "꽥꽥")
        self.can_talk = can_talk

    def speak(self):
        """메서드 오버라이딩"""
        if self.can_talk:
            print(f"{self.name}: 안녕하세요! (말하는 앵무새)")
        else:
            super().speak()     # 부모 메서드 호출


cat = Cat("나비", "검은색")
parrot = Parrot("폴리")

cat.speak()
cat.purr()
print(cat)

parrot.speak()

# isinstance(): 인스턴스 확인
print(f"\ncat은 Cat? {isinstance(cat, Cat)}")
print(f"cat은 Animal? {isinstance(cat, Animal)}")
print(f"parrot은 Cat? {isinstance(parrot, Cat)}")

print()


# ============================================================
# 5. 캡슐화 (Encapsulation)
# ============================================================
print("=== 캡슐화 ===")


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance     # __ 접두사: private
        # JS: #balance (# 접두사)  →  Python: __balance (__ 접두사)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"입금 {amount:,}원 → 잔액: {self.__balance:,}원")
        else:
            print("입금액은 양수여야 합니다.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("잔액 부족!")
        elif amount <= 0:
            print("출금액은 양수여야 합니다.")
        else:
            self.__balance -= amount
            print(f"출금 {amount:,}원 → 잔액: {self.__balance:,}원")

    def get_balance(self):
        """잔액 조회 (getter)"""
        return self.__balance


account = BankAccount("홍길동", 100000)
account.deposit(50000)
account.withdraw(30000)
print(f"현재 잔액: {account.get_balance():,}원")

# account.__balance  # AttributeError! (직접 접근 불가)

print()


# ============================================================
# 6. @property 데코레이터
# ============================================================
print("=== @property ===")


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property                    # JS: get radius() { return this._radius }
    def radius(self):
        """반지름 getter"""
        return self._radius

    @radius.setter               # JS: set radius(value) { this._radius = value }
    def radius(self, value):
        """반지름 setter (유효성 검사)"""
        if value <= 0:
            raise ValueError("반지름은 양수여야 합니다!")
        self._radius = value

    @property
    def area(self):
        """넓이 (읽기 전용)"""
        import math
        return math.pi * self._radius ** 2

    @property
    def circumference(self):
        """둘레 (읽기 전용)"""
        import math
        return 2 * math.pi * self._radius


c = Circle(5)
print(f"반지름: {c.radius}")
print(f"넓이: {c.area:.2f}")
print(f"둘레: {c.circumference:.2f}")

c.radius = 10  # setter 호출
print(f"변경 후 넓이: {c.area:.2f}")

try:
    c.radius = -1   # 유효성 검사 에러
except ValueError as e:
    print(f"에러: {e}")

print()


# ============================================================
# 7. @classmethod와 @staticmethod
# ============================================================
print("=== classmethod & staticmethod ===")


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

    @classmethod
    def from_string(cls, date_string):
        """문자열에서 Date 객체 생성 (대체 생성자)"""
        year, month, day = map(int, date_string.split("-"))
        return cls(year, month, day)

    @staticmethod
    def is_valid_date(year, month, day):
        """유효한 날짜인지 확인 (인스턴스와 무관)"""
        return 1 <= month <= 12 and 1 <= day <= 31


# classmethod 사용
d = Date.from_string("2025-12-25")
print(f"날짜: {d}")

# staticmethod 사용
print(f"유효한 날짜? {Date.is_valid_date(2025, 12, 25)}")
print(f"유효한 날짜? {Date.is_valid_date(2025, 13, 1)}")

print()


# ============================================================
# 8. 실전 예제: 간단한 할 일 관리
# ============================================================
print("=== 실전 예제: Todo 관리 ===")


class Todo:
    def __init__(self, title, priority="보통"):
        self.title = title
        self.priority = priority
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        status = "V" if self.completed else " "
        return f"[{status}] [{self.priority}] {self.title}"


class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, title, priority="보통"):
        self.todos.append(Todo(title, priority))

    def complete(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index].complete()

    def show(self):
        if not self.todos:
            print("할 일이 없습니다!")
            return
        for i, todo in enumerate(self.todos):
            print(f"  {i}. {todo}")

    @property
    def pending_count(self):
        return sum(1 for t in self.todos if not t.completed)


my_list = TodoList()
my_list.add("파이썬 공부하기", "높음")
my_list.add("운동하기", "보통")
my_list.add("책 읽기", "낮음")

print("--- 할 일 목록 ---")
my_list.show()

my_list.complete(0)
print("\n--- 업데이트 후 ---")
my_list.show()
print(f"남은 할 일: {my_list.pending_count}개")


# ============================================================
# 연습 문제
# ============================================================
"""
[연습 1] Rectangle 클래스를 만드세요.
         - width, height 속성
         - area() (넓이), perimeter() (둘레) 메서드
         - __str__ 메서드

[연습 2] Animal 클래스를 상속받아 Dog, Cat, Bird 클래스를 만들고,
         각각 다른 speak() 메서드를 구현하세요.

[연습 3] 쇼핑 카트 시스템을 만드세요.
         - Product 클래스 (이름, 가격)
         - Cart 클래스 (상품 추가, 삭제, 총액 계산)
"""
