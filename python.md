# Python 语法笔记

## 基础语法

### 循环

- for 循环
  ```python
  for i in range(5):
      print(i)
  ```
  - `range(start, stop[, step])`：生成从 start 到 stop 的整数序列，步长为 step，默认从 0 开始，步长为 1，不包含 stop。

## 常用容器

### list

- 创建：`list()` 或 `[]`
- 读取元素：
  - `list[i]`
  - `list[start:end:step]`，从 0 开始，不包含 end
  - 比如
    ```python
    list = [1, 2, 3, 4, 5]
    print(list[1])  # 2
    print(list[1:3])  # [2, 3]
    print(list[1:4:2])  # [2, 4]
    print(list[::2])  # [1, 3, 5]
    print(list[::-1])  # [5, 4, 3, 2, 1]
    ```
- 添加元素：
  - `append(x)`：右侧添加元素
  - `insert(i, x)`：在指定位置添加元素
  - `extend(iterable)`：右侧添加多个元素
- 查找元素：
  - `index(x[, start[, end]])`：返回第一个匹配元素的索引
  - `count(x)`：返回元素出现的次数
- 删除元素：
  - `remove(x)`：删除指定元素
  - `pop([i])`：删除指定位置的元素
  - `pop()`：删除右侧最后一个元素
- 修改元素：
  - `list[i] = x`
- 获取大小：
  - `len(list)`
- 切片：
  - `list[start:end:step]`

## 队列与栈

### deque

- 创建：`deque([iterable[, maxlen]])`
- 添加元素：
  - `append(x)`：右侧添加元素
  - `appendleft(x)`：左侧添加元素
- 删除元素：
  - `pop()`：右侧删除元素
  - `popleft()`：左侧删除元素
- peek：
  - `peek()`：返回右侧第一个元素
  - `peekleft()`：返回左侧第一个元素
- 获取大小：
  - `len(deque)`

### queue

- 创建：`queue.Queue(maxsize)`
- 添加元素：
  - `put(item[, block[, timeout]])`：添加元素
  - `put_nowait(item)`：等同于`put(item, False)`
- 删除元素：
  - `get([block[, timeout]])`：删除元素
  - `get_nowait()`：等同于`get(False)`
- peek：
  - `queue.Queue`没有peek方法，但可以通过`queue.Queue.queue[0]`获取第一个元素

### stack

- 创建：`list()`
- 添加元素：
  - `append(x)`：右侧添加元素
- 删除元素：
  - `pop()`：右侧删除元素
- peek：
  - `stack[-1]`：返回右侧第一个元素
