class Hash:
    MAX = 20

    def __init__(self):
        self.arr = [[] for i in range(Hash.MAX)]

    @staticmethod
    def get_hash(key) -> int:
        sum = 0
        for ch in key:
            sum += ord(ch)
        return sum % Hash.MAX

    # BY USING __setitem__,__getitem__ WE CAN PERFORM OPERATIONS BY USING [] ONLY (LIKE DICT)
    def __setitem__(self, key, val):
        hash_value = Hash.get_hash(key)
        for idx, ele in enumerate(self.arr[hash_value]):
            if len(ele) == 2 and ele[0] == key:
                self.arr[hash_value][idx][1] = val  # UPDATION
                break
        else:
            self.arr[hash_value].append([key, val])

    def __getitem__(self, key):
        hash_value = Hash.get_hash(key)
        for ele in self.arr[hash_value]:
            if ele[0] == key:
                return ele[1]

        return None

    def __delitem__(self, key) -> bool:
        hash_value = Hash.get_hash(key)
        for idx ,ele in enumerate(self.arr[hash_value]):
            if len(ele)==2 and ele[0]==key:
                self.arr[hash_value].pop(idx)
        else:
            return False

    def show(self):
        print(self.arr)
        # print(self.arr[0][0][0])


if __name__ == '__main__':
    my_hash = Hash()
    my_hash['sabari'] = 21
    my_hash['nithi'] = 11
    my_hash['chithra'] = 43

    my_hash.show()
    print(my_hash['chithra'], my_hash['nithi'], my_hash.__getitem__('nithi')
          , my_hash.__delitem__('raj'))
    del my_hash['sabari']

    # UPDATION
    print('before update chithra:', my_hash['chithra'])
    my_hash['chithra'] = 45
    print('after update:', my_hash['chithra'])

    # MAKING & HANDLING COLLISION
    my_hash['thini'] = 43
    print(my_hash['nithi'], "--> we can see here nithi value isn't overwritten")
    my_hash.show()
    
    
    
