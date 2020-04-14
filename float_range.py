class FloatRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    # 正向迭代
    def __iter__(self):
        t = self.start
        while round(t, 2) <= round(self.end, 2):
            yield t
            t += self.step  # 反向迭代

    def __reversed__(self):
        t = self.end
        while round(t, 2) >= round(self.start, 2):
            yield t
            t -= self.step


if __name__ == "__main__":
    for x in FloatRange(3.0, 4.0, 0.2):
        print(x)
    for x in reversed(FloatRange(3.0, 4.0, 0.2)):
        print(x)
