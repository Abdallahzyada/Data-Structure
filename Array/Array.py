class Array:
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0

    def __len__(self):
        return self.__nItems

    def get(self, n):
        if 0 <= n < self.__nItems:
            return self.__a[n]

    def set(self, n, value):
        if 0 <= n < self.__nItems:
            return self.__a[n] == value

    def insert(self, item):
        self.__a[self.__nItems] = item
        self.__nItems += 1

    def find(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                return j
            return -1

    def search(self, item):
        return self.get(self.find(item))

    def delete(self, item):
        for i in range(self.__nItems):
            if self.__a[i] == item:
                self.__nItems -= 1
                for j in range(i, self.__nItems):
                    self.__a[j] = self.__a[j + 1]
                return True
        return False

    def traverse(self, function=print):
        for i in range(self.__nItems):
            function(self.__a[i])

    def getMaxNum(self):
        st = []
        for i in range(self.__nItems):
            st.append(str(self.__a[i]))
        return max(st)

    def deleteMaxNum(self):
        return self.delete(int(self.getMaxNum()))
