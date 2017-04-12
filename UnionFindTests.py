from UnionFind import *
import unittest
import random

class TestUnionFindMethods(unittest.TestCase):

    def test_create_init_values(self):
        uf = UnionFind(200)
        for i in range(200):
            self.assertEqual(uf.find(i), i)

    def test_union(self):
        uf = UnionFind(9)
        uf.union(3, 4)
        for i in range(9):
            if 3 <= i <= 4:
                self.assertEqual(uf.find(i), uf.find(3))
            else:
                self.assertEqual(uf.find(i), i)

    def test_union_chain(self):
        items = [i for i in range(200)]
        uf = UnionFind(200)
        random.shuffle(items)
        last_item = None
        for item in items:
            if last_item is not None:
                uf.union(item, last_item)
            last_item = item
        final_name = uf.find(0)
        for item in items:
            self.assertEqual(final_name, uf.find(item))       

class TestUTUnionFindMethods(unittest.TestCase):
    def get_simple_items(self):
        return ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    def test_create_init_values_string(self):
        items = self.get_simple_items()
        uf = UTUnionFind(items)
        for item in items:
            self.assertEqual(uf.find(item), item)

    def test_union(self):
        items = self.get_simple_items()
        uf = UTUnionFind(items)
        item1 = items[3]
        item2 = items[4]
        uf.union(item1, item2)
        for item in items:
            if item in [item1, item2]:
                self.assertEqual(uf.find(item), uf.find(item2))
            else:
                self.assertEqual(uf.find(item), item)

    def test_union_chain(self):
        items = self.get_simple_items()
        uf = UTUnionFind(items)
        random.shuffle(items)
        last_item = None
        for item in items:
            if last_item is not None:
                uf.union(item, last_item)
            last_item = item
        final_name = uf.find(items[0])
        for item in items:
            self.assertEqual(final_name, uf.find(item))

    

if __name__ == '__main__':
    unittest.main()


            
    



    
