# Turtle graph

## This repository was built for a turtle graph project.

+ program example

```python
    import turtle as t
    # 거북이 모양으로 변경
    t.shape('turtle')
    # 가로 10 세로 20의 window 크기
    t.setup(10,20,0,0)
    # 처음 turtle 커서가 위치하는 곳 지정 
    # a, b는 x좌표 y좌표, 처음 위치는 0,0
    t.goto(a,b)
    # 특정 코드로 그린 그림 지우기
    # t.Screen().reset()

```

## excute
1. prepare run enviroment
```
vscode 
ctrl + ~ => run terminal in editor
in windows10 terminal run using windows power shell
in wsl terminal run using bash
etc...
```
2. type this instruction
```shell
$ python turtle_graph.py
```

## develope enviroment
+ windows10 
+ vscode

## if you want learn more
+ here is a link!   
[link](https://youtu.be/JHAcgz4XUK0)

## main content
`turtleBar() function`
+ function
    + Draws a bar chart for incoming inputs
+ layout 
    + axis y, axis x, graded line and legend

`turtlePie() function`
+ function
    + Draws a pie graph for incoming inputs
+ layout
    + legend

# sub content
`go_origin() function`
+ function
    + go to the origin that is (0,0)   
`line() function`
+ function
    + Draws x axis, y axis and graded line