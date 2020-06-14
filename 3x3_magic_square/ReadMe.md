# 결과 자동저장

```shell
# debug mode
$ echo y | python 3x3.py >> 3x3_test.txt
# not debug
$ echo n | python 3x3.py >> 3x3_test.txt
```

# 결과
`time ranking`
1. version 4
2. version 1
3. version 2

`code length`
1. version 4
2. version 1, version 2

# 사용 알고리즘
+ version1, 2
    - backtracking
        + 안되는 경우의 수를 각각의 for loop에서 cut하여 다음단계로 진행안되게 만듦
    - problem : code길이, 시간

+ version 3 (정답 확인용)
    - mathematical approach
        + 마방진의 수학적원리에 근거 대칭성, 홀수와 짝수의 관계 활용

+ version 4 (last version, 제출용)
    - mathematical approach
         + 마방진의 수학적원리에 근거 대칭성, 홀수와 짝수의 관계 활용

# log
>   modify date: 2020-05-30 pm12:42   
>   editor: seongminyoo
