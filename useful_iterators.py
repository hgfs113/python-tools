import random


class NumberIterator:
    def __init__(self, N, name):
        self.N = N
        self.name = name

    def __iter__(self):
        return self.generate(range(self.N))

    def generate(self, reader):
        for row in reader:
            yield row, self.name

            
if __name__ == "__main__":
    it1 = NumberIterator(10, "n1")
    it2 = NumberIterator(15, "n2")

    r1 = iter(it1)
    r2 = iter(it2)
    readers = [r1, r2]

    while True:
        reader_idx = random.randint(0, len(readers) - 1)
        reader = readers[reader_idx]
        try:
            batch = next(reader)
        except StopIteration:
            print(f"StopIteration at: {reader_idx=}")
            readers.pop(reader_idx)
            if len(readers) == 0:
                break
            continue
        print(batch)

