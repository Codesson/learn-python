"""
Chapter 12: 예외 처리 (Error Handling)
========================================
try-except를 사용한 오류 처리를 배웁니다.
"""

# ============================================================
# JavaScript vs Python 비교 - 예외 처리
# ============================================================
#
#  JavaScript                         Python
#  ─────────────────────────────────  ─────────────────────────────
#  try {                              try:
#    ...                                  ...
#  } catch (error) {                  except Exception as e:
#    ...                                  ...
#  } finally {                        finally:
#    ...                                  ...
#  }                                  (+ else: 블록이 추가로 있음!)
#
#  throw new Error("msg")            raise Exception("msg")
#  new TypeError("msg")               raise TypeError("msg")
#  error.message                      str(e)
#  error instanceof TypeError         isinstance(e, TypeError)
#
#  class MyError extends Error {}     class MyError(Exception): ...
#
#  핵심 차이:
#  1) catch → except (키워드가 다름!)
#  2) throw → raise
#  3) Python에는 else 블록이 있음 (에러가 안 나면 실행)
#  4) 에러 타입별로 except를 분리하여 잡을 수 있음 (JS는 catch 하나)
#  5) Python은 에러 타입을 지정하여 특정 에러만 잡을 수 있음
#

# ============================================================
# 1. 에러의 종류 (주석 해제하면 에러 발생)
# ============================================================
print("=== 주요 에러 종류 ===")

# SyntaxError: 문법 오류 (실행 전에 발생)
# print("hello"

# NameError: 정의되지 않은 변수
# print(undefined_variable)

# TypeError: 타입 불일치
# result = "3" + 5

# ValueError: 값이 적절하지 않음
# int("hello")

# IndexError: 인덱스 범위 초과
# lst = [1, 2, 3]; print(lst[10])

# KeyError: 딕셔너리에 없는 키
# d = {"a": 1}; print(d["b"])

# ZeroDivisionError: 0으로 나누기
# result = 10 / 0

# FileNotFoundError: 파일을 찾을 수 없음
# open("없는파일.txt")

print("(에러 종류는 주석으로 확인하세요)")
print()


# ============================================================
# 2. 기본 try-except
# ============================================================
print("=== 기본 try-except ===")

# 에러 없이 안전하게 처리
try:
    result = 10 / 0
except ZeroDivisionError:
    print("에러: 0으로 나눌 수 없습니다!")

print("프로그램이 계속 실행됩니다!")

print()


# ============================================================
# 3. 여러 에러 처리
# ============================================================
print("=== 여러 에러 처리 ===")


def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("에러: 0으로 나눌 수 없습니다!")
    except TypeError:
        print("에러: 숫자만 입력할 수 있습니다!")
    return None


print(safe_divide(10, 3))        # 3.333...
print(safe_divide(10, 0))        # None (ZeroDivisionError)
print(safe_divide("10", 3))      # None (TypeError)

print()


# ============================================================
# 4. 에러 메시지 가져오기
# ============================================================
print("=== 에러 메시지 ===")

try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError as e:
    print(f"에러 종류: {type(e).__name__}")
    print(f"에러 메시지: {e}")

print()


# ============================================================
# 5. except Exception (범용 예외 처리)
# ============================================================
print("=== 범용 예외 처리 ===")

try:
    result = int("abc")
except Exception as e:
    print(f"에러 발생: {type(e).__name__}: {e}")

print()


# ============================================================
# 6. else 와 finally
# ============================================================
print("=== else & finally ===")

# else: 에러가 없을 때 실행  ← JS에 없는 기능!
# finally: 에러 유무와 상관없이 항상 실행 (JS와 동일)

def read_number(text):
    try:
        number = int(text)
    except ValueError:
        print(f"  '{text}'은(는) 숫자가 아닙니다!")
    else:
        print(f"  성공! 숫자: {number}")
    finally:
        print(f"  처리 완료 (입력값: '{text}')")


print("--- 성공 케이스 ---")
read_number("42")

print("--- 실패 케이스 ---")
read_number("hello")

print()


# ============================================================
# 7. raise - 에러 직접 발생시키기
# ============================================================
print("=== raise ===")


def set_age(age):
    """나이를 설정하는 함수 (유효성 검사 포함)"""
    # JS: throw new TypeError("...")  →  Python: raise TypeError("...")
    if not isinstance(age, int):
        raise TypeError("나이는 정수여야 합니다!")
    if age < 0:
        raise ValueError("나이는 0 이상이어야 합니다!")
    if age > 150:
        raise ValueError("나이가 너무 큽니다!")
    return age


# 정상 케이스
try:
    result = set_age(25)
    print(f"나이 설정: {result}")
except (TypeError, ValueError) as e:
    print(f"에러: {e}")

# 에러 케이스
try:
    result = set_age(-5)
except ValueError as e:
    print(f"에러: {e}")

try:
    result = set_age("스물다섯")
except TypeError as e:
    print(f"에러: {e}")

print()


# ============================================================
# 8. 사용자 정의 예외
# ============================================================
print("=== 사용자 정의 예외 ===")


class InsufficientBalanceError(Exception):
    """잔액 부족 에러"""
    # JS: class InsufficientBalanceError extends Error { ... }
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"잔액 부족! 현재 잔액: {balance}원, 출금 요청: {amount}원"
        )


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(self.balance, amount)
        self.balance -= amount
        return self.balance


account = BankAccount(10000)

try:
    account.withdraw(3000)
    print(f"출금 성공! 잔액: {account.balance}원")
    account.withdraw(50000)  # 잔액 부족!
except InsufficientBalanceError as e:
    print(f"에러: {e}")
    print(f"  부족 금액: {e.amount - e.balance}원")

print()


# ============================================================
# 9. 실전 예제: 안전한 입력 처리
# ============================================================
print("=== 실전 예제: 안전한 입력 ===")


def get_integer(prompt, min_val=None, max_val=None):
    """안전하게 정수를 입력받는 함수"""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"  {min_val} 이상의 값을 입력하세요.")
                continue
            if max_val is not None and value > max_val:
                print(f"  {max_val} 이하의 값을 입력하세요.")
                continue
            return value
        except ValueError:
            print("  올바른 정수를 입력하세요.")


# 주석 해제하여 직접 테스트해 보세요!
# age = get_integer("나이를 입력하세요: ", min_val=0, max_val=150)
# print(f"입력된 나이: {age}")


# ============================================================
# 10. 실전 예제: 파일 안전하게 읽기
# ============================================================
print("=== 실전 예제: 파일 안전 읽기 ===")


def safe_read_file(filepath):
    """파일을 안전하게 읽는 함수"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {filepath}")
    except PermissionError:
        print(f"파일 읽기 권한이 없습니다: {filepath}")
    except Exception as e:
        print(f"예상치 못한 에러: {e}")
    return None


content = safe_read_file("없는파일.txt")
print(f"결과: {content}")


# ============================================================
# 연습 문제
# ============================================================
"""
[연습 1] 사용자에게 두 숫자를 입력받아 나누기를 수행하세요.
         - 숫자가 아닌 입력에 대해 에러 처리
         - 0으로 나누는 경우 에러 처리
         - 성공할 때까지 반복

[연습 2] 리스트의 특정 인덱스에 접근하는 안전한 함수를 작성하세요.
         에러 시 기본값을 반환하도록 하세요.

[연습 3] NegativeNumberError라는 사용자 정의 예외를 만들고,
         음수가 입력되면 이 에러를 발생시키는 제곱근 함수를 작성하세요.
"""
