# Python 语法笔记

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
