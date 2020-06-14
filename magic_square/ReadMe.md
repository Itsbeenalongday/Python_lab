# 기말과제 홀수 마방진
+ contents
    - 프로젝트에 대한 설명
    - 코드에 대한 설명테스트 
    - 실행 결과

## 3 x 3 마방진
+ requirement
```
3x3 마방진 - magic_3x3.py (가로/세로/대각선의 합이 같음, 입력숫자는 한번씩만 사용)
입력숫자를 input 명령으로 사용자가 자유롭게 입력할 수 있도록 한다. 
1 1 2 2 3 3 4 4 5 
출력은 각각의 답을 한줄로 stdout 으로 다음 예와 같이 출력하고
2 1 3 2 1 4 2 3 5
stderr에 다음과 예와 같이 출력한다. 
총 1 개의 답이 있습니다. 계산시간은 총 3.45 초 입니다. 
```
+ introduce project
1. 입력으로 9개의 숫자를 받는다.
2. 입력받은 것은 문자열이므로 `str.split()`함수를 사용하여 문자로 parsing한 결과를 리스트로 만든다.
3. `map()`함수를 사용하여 리스트의 문자들을 int형으로 변환한다.
4. `count()`함수
    + `permutaions()`함수에 들어가서 리스트 원소들로 이루어진 순열을 만든다.
    + 해당 순열이 마방진 조건을 만족하면 답이므로 답의 갯수를 +1 시킨다.
5. 최종적 답의 수와 걸린 시간을 출력한다.

+ result

![result image](https://git.ajou.ac.kr/seongminyoo/python_lab/-/raw/master/magic_square/results/3x3%20%EA%B2%B0%EA%B3%BC.jpeg)

## n x n 마방진
