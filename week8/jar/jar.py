
class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        imoji = "🍪"
        return f"{self.size*imoji}"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        self.size = self.size + n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        self.size = self.size - n


    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self,capacity):
         if not capacity > 0:
            raise ValueError
         self._capacity = capacity

         
    @property
    def size(self):
       return self._size

    @size.setter
    def size(self,size):
        if size > self.capacity:
            raise ValueError
        self._size = size



def main():
    jar = Jar()
    jar.deposit(1)
    print(jar.size)
    print(str(jar))
    jar.deposit(11)
    print(str(jar))
    print(jar.size)
    jar.withdraw(5)
    print(jar.size)
    print(str(jar))

if __name__ == "__main__":
    main()
