# last version draft

`algorithm introduce`
+ 첫번째 숫자인 1을 맨윗 행 중간열에 배치한다.
+ 두번째 수부터는 오른쪽 대각선 위로 이동하며 숫자를 배치한다. 행렬의 범위를 넘어가면 반대쪽 끝으로 돌아온다.
+ 만약 숫자를 놓아야하는 자리에 이미 다른 숫자가 배치되어 있다면 현재 위치에서 행을 하나 내린 같은 열의 위치에 숫자를 놓는다. 다음 숫자는 다시 2번을 수행한다.

`case`
1. 좌우 반전 x 2개
2. 90회전 x 4개
총 8개

`reference`   
그림 참조
