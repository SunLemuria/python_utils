"""
我们谈到“文本处理”时，我们通常是指处理的内容。Python 将文本文件的内容读入可以操作的字符串变量非常容易。文件对象提供了三个“读”方法：
.read()、.readline() 和 .readlines()。每种方法可以接受一个变量以限制每次读取的数据量，但它们通常不使用变量。
.read() 每次读取整个文件，它通常用于将文件内容放到一个字符串变量中。然而.read() 生成文件内容最直接的字符串表示，
但对于连续的面向行的处理，它却是不必要的，并且如果文件大于可用内存，则不可能实现这种处理。下面是read()方法示例：
"""
with open('/path/to/file', 'r') as f:
    print(f.read())

"""
调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
"""

with open('/path/to/file', 'r') as f:
    process = lambda x: x
    for line in f.readlines():
        process(line)


"""
分块读取
处理大文件是很容易想到的就是将大文件分割成若干小文件处理，处理完每个小文件后释放该部分内存。这里用了iter 和 yield：
"""


def read_in_chunks(filePath, chunk_size=1024*1024):
    """
    Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1M
    You can set your own chunk size
    """
    file_object = open(filePath)
    while True:
        chunk_data = file_object.read(chunk_size)
        if not chunk_data:
            break
        yield chunk_data


# if __name__ == "__main__":
#     filePath = './path/filename'
#     for chunk in read_in_chunks(filePath):
#         process(chunk)


"""
使用 With open()
with语句打开和关闭文件，包括抛出一个内部块异常。for line in f文件对象f视为一个迭代器，会自动的采用缓冲IO和内存管理，所以你不必担心大文件。
代码如下：
"""

# If the file is line based
with open(...) as f:
    for line in f:
        process(line)  # <do something with line>
"""
优化
面对百万行的大型数据使用with open 是没有问题的，但是这里面参数的不同也会导致不同的效率。经过测试发先参数为
"rb"时的效率是"r"的6倍。由此可知二进制读取依然是最快的模式。
"""

with open(filename, "rb") as f:
    for fLine in f:
        pass
"""
测试结果：rb方式最快，100w行全遍历2.9秒。基本能满足中大型文件处理效率需求。如果从rb(二级制读取)
读取改为r(读取模式)，慢5 - 6倍。
结论
在使用python进行大文件读取时，应该让系统来处理，使用最简单的方式，交给解释器，就管好自己的工作就行了。同时根据不同的需求可以选择不同的读取参数进一步获得更高的性能。
"""