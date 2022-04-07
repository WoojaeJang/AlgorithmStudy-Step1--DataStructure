# 1주차 - 🧱 스택과 큐

## [✍ 강의 정리]

### PART 01 스택

#### 스택이란? 
- 영어로 Stack '쌓다' 라는 의미
- 프로그래밍에서 목록 혹은 리스트에서 접근이 한쪽에서만 가능한 구조
- LIFO(Last-In, First-Out)가 기본원리
- 대표적인 내장함수
	- push
	- peek
	- pop
<br/>

#### 스택의 구조
BOOKS
[ BOOK 1, BOOK 2, BOOK 3]

- push : 가장 마지막에 추가
push BOOK 4 -> BOOKS [ BOOK 1, BOOK 2, BOOK 3, BOOK 4 ]

- peek : 가장 마지막 데이터 확인
peek BOOKS -> BOOK 4

- pop : 제일 마지막 데이터 추출
pop BOOKS -> BOOKS [ BOOK 1, BOOK 2, BOOK 3]
<br/>

#### PYTHON 스택의 구현 방법
- 직접 구현
- 이미 구현된 클래스 import
- List를 스택으로 구현

- 스택에서 '이미 구현된 클래스 import', 'List를 스택으로 구현' 안씀
<br/>

#### PYTHON 스택 직접 구현 및 활용
```python
class Stack(list) :
	push = list.append
	
	def peek(self) :
		return self[-1]
			self[len(self)-1]

# Pop은 list의 내장함수로 이미 존재한다.

s = Stack()
s.push(1)
s.push(5)
s.push(10)

print("my stack is : ", s)			my stack is :  [1, 5, 10]
print("popped value is : ", s.pop())	popped value is :  10
print("my stack is : ", s)			my stack is :  [1, 5]
print("peeked value is : ", s.peek())	peeked value is :  5
print("my stack is : ", s)			my stack is :  [1, 5]
```
<br/>

#### PYTHON List를 스택으로 활용
```python
s = []
s.append(1)
s.append(5)
s.append(10)
print("my stack is : ", s)			my stack is :  [1, 5, 10]
print("poped value is : ", s.pop())	poped value is :  10
print("my stack is : ", s)			my stack is :  [1, 5]
print("peeked value is : ", s[-1])		print("peeked value is : ", s[-1])
print("my stack is : ", s)			print("my stack is : ", s)
```
<br/>

#### 스택의 활용
- 웹페이지에서 이전페이지 다음페이지 기능
- 깊이 우선 탐색(DFS)
<br/>


### PART 02 큐

#### 큐란?
- 영어로 Queue '일이 처리되기를 기다리는 리스트' 라는 의미
- 프로그래밍에서 목록 혹은 리스트에서 접근이 양쪽에서 가능한 구조
- FIFO(First-In, First-Out)가 기본원리
- 대표적인 내장함수
	- put
	- peek
	- get
<br/>

#### 큐의 구조
BOX 리스트
[ BOX 1, BOX 2, BOX 3]

- put : 가장 마지막에 추가
put BOX 4 -> BOX 리스트 [ BOX 1, BOX 2, BOX 3, BOX 4 ]

- peek : 가장 먼저 들어간 데이터 확인
peek BOX 리스트 -> BOX 1

- pop : 제일 마지막 데이터 추출
get BOX 리스트 -> BOX 리스트 [ BOX 2, BOX 3, BOX 4 ]
<br/>
		
#### PYTHON 큐의 구현방법
- 직접 구현
- 이미 구현된 클래스 import
- List를 큐로 구현
<br/>

#### PYTHON 큐 직접 구현 및 활용
```python
class Queue(list) :
    put = list.append
    
    def peek(self) :
        return self[0]
    
    def get(self):
        return self.pop(0)

q = Queue()
q.put(1)
q.put(5)
q.put(10)

print("my queue is : ", q)			my queue is :  [1, 5, 10]
print("removed value is : ", q.get())	removed value is :  1
print("my queue is : ", q)			my queue is :  [5, 10]
print("peeked value is : ", q.peek())	peeked value is :  5
print("my queue is : ", q)			my queue is :  [5, 10]
```
<br/>

#### PYTHON 구현된 클래스 import
* 강의 오류인듯 하다... 안됨....
```python
from queue import Queue

q = Queue()
q.put(1)
q.put(5)
q.put(10)

print("my queue is : ", q)
print("removed value is : ", q.get())
print("my queue is : ", q)
print("peeked value is : ", q.peek())
print("my queue is : ", q)
```
<br/>

#### PYTHON List를 큐로 활용
```python
q = []
q.append(1)
q.append(5)
q.append(10)

print("my queue is : ", q)			my queue is :  [1, 5, 10]
print("removed value is : ", q.pop(0))	removed value is :  1
print("my queue is : ", q)			my queue is :  [5, 10]
print("peeked value is : ", q[0])		peeked value is :  5
print("my queue is : ", q)			my queue is :  [5, 10]
```
<br/>

#### 큐의 활용
- 프린터 인쇄 대기열
- 너비 우선 탐색(BFS)
<br/><br/>


## [🥇 문제풀이]

### W01_1_주식가격
||
|---|
|[문제 원본 보기](https://programmers.co.kr/learn/courses/30/lessons/42584)|
|[풀이 보기](./../code/practice/w01_prc_1_주식가격.py)| 
  

<br/>

### W01_2_기능개발
||
|---|
|[문제 원본 보기](https://programmers.co.kr/learn/courses/30/lessons/42586)|  
|[풀이 보기]("./../code/practice/w01_prc_2_기능개발.py")|

<br/>

### W01_3_다리를 지나는 트럭
||
|---|
|[문제 원본 보기](https://programmers.co.kr/learn/courses/30/lessons/42583)|
|[풀이](./../code/practice/w01_prc_3_다리를지나는트럭.py)|

<hr>
