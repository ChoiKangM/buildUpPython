# 파일 입출력, 디버깅 및 예외 처리

## 파일 입출력

## 텍스트 파일 입력(읽기)
* `read()`
* `readline()`
* `readlines()`
* `open()`
    시스템 프로그래밍
    - `.` : 현재
    - `..` : 상위 폴더
* `open()`시 오류 처리

### File Encoding
* `ASCII`

## 텍스트 파일 출력(쓰기)
* `write()`
* `writelines()`
# `write()` + `join()` - `flush()`

## 바이너리 파일

## 디버깅
> 오류 처리(Debugging) : 프로그램 오동작의 원인이 되는 버그(Bug)를 제거하는 것  

### 오류의 종류
* 컴파일 오류
* Run-time 오류
* Logic 오류

## 예외처리
```python
try:
    문제가 없을 시 실행할 코드
except:
    문제 발생 시 실행할 코드
```

```python
try:
    문제가 없을 시 실행할 코드
except 예외형식:
    문제 발생 시 실행할 코드
```

```python
try:
    문제가 없을 시 실행할 코드
except 예외형식 1:
    문제 발생 시 실행할 코드
except 예외형식 2:
    문제 발생 시 실행할 코드
```

```python
try:
    문제가 없을 시 실행할 코드
except 예외형식 1:
    문제 발생 시 실행할 코드
except 예외형식 2:
    문제 발생 시 실행할 코드
else:
    except 절을 만나지 않을 시 실행할 코드
```
```python
try:
    문제가 없을 시 실행할 코드
except 예외형식 1:
    문제 발생 시 실행할 코드
except 예외형식 2:
    문제 발생 시 실행할 코드
finally:
    항상 실행되는 코드
```

## 파이썬 에러 메시지
* 구문에러(SyntaxError) : 명령의 조건 중 따옴표 오류 등, 구문 오류
    1. 따옴표나 괄호 닫기 오류
        - SyntaxError : EOL while scanning string literal
        - SyntaxError : unexpected EOF while parsing
    2. 철자나 따옴표를 빼먹은 경우
        - SyntaxError : invalid syntax
    3. 반복 블록의 들여쓰기 오류
        - SyntaxError : expected as indented block
        - SyntaxError : unindent does not match any outer indentation level
        - SyntaxError : unexpected indent
* 이름에러(NameError) : 명령의 철자 오류
    ```bash
    TraceBack (most recent call last):
        File "<pyshell#7>", line 1 ,in <module>
          PRINT("Hello")
    NameError: name "PRINT" in not defined
    ```
* 외부모듈 호출오류(Import Error) : Import로 호출 모듈 이름 오류
    ```bash
    TraceBack (most recent call last):
        File "<pyshell#10>", line 11 ,in <module>
          import turtl as t
    ImportError: No module named 'turtl'
    ```    
* 속성 오류(AttributeError): 호출 모듈의 함수, 변수를 잘못 입력
    ```bash
    TraceBack (most recent call last):
        File "<pyshell#18>", line 21 ,in <module>
          t.forward(50)
    AttributeError: 'module' object has no attribute 'forward'
    ```  
* 타입 에러 (TypeError) : 함수에 전달할 인자가 빠진 경우
    ```bash
    TypeError : ... missing... required positional argument : ....
    ```
* 값 에러 (ValueError) : 정수, 문자 간 값 변환이 불가능 오류 
    ```bash
    ValueError : invalid literal for ... ():
    ```