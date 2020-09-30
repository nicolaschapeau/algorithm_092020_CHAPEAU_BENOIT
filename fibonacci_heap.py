import math

class Heap(object):
    """
    Une heap est une structure de données sous forme d'arbre.
    https://en.wikipedia.org/wiki/Heap_(data_structure)
    """

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        pass

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        pass

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def decrease_key(self, current_value: int, new_value :int) -> None:
        """
        Modify une valeur dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: object) -> None:
        """
        Fusionne deux arbres

        """
        pass

class Tree(object):
    def __init__(self):
        self.children = []
        self.size = 0

    def add_value(self, tree):
        self.children.append(tree)
        self.size += 1

    def __repr__(self):
        return repr(self.children)

class FibonacciHeap(Heap):
    """
    Une fibonnaci heap est un arbre permettant de stocker et trier des donnés efficacement
    https://en.wikipedia.org/wiki/Fibonacci_heap
    L'implémentation est décrite en anglais : https://en.wikipedia.org/wiki/Fibonacci_heap#Implementation_of_operations
    et en français : https://fr.wikipedia.org/wiki/Tas_de_Fibonacci#Implémentation_des_opérations
    """

    def __init__(self):
        self.trees = []
        self.least = None
        self.count = 0

    def __repr__(self):
        return repr(self.trees)

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        new_tree = Tree()
        new_tree.add_value(value)
        self.trees.append(new_tree)
        self.count = self.count + 1
        #
        # print(f'Value {value} added. ')
        pass

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        pass

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def decrease_key(self, current_value: int, new_value :int) -> None:
        """
        Modifie une valeur dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: Heap) -> None:
        """
        Fusionne deux arbres
        """
        trees_sizes = [tree.size for tree in self.trees]
        min_size = min(set(z for z in trees_sizes if trees_sizes.count(z) > 1))
        first_tree = None
        last_tree = None

        for tree in self.trees:
            if (tree.size == min_size):
                first_tree = tree
                break

        for tree in self.trees[::-1]:
            if (tree.size == min_size):
                last_tree = tree
                break

        if first_tree.children[0] < last_tree.children[0]:
            first_tree.add_value(last_tree)
            self.trees.remove(last_tree)
        elif first_tree.children[0] > last_tree.children[0]:
            last_tree.add_value(first_tree)
            self.trees.remove(first_tree)
        pass


fheap = FibonacciHeap()
data = [1, 3, 12, 31, 5, 8, 11, 4, 0, 7]



for value in data:
    fheap.insert(value)

print('0  :', fheap.trees)
fheap.merge(fheap)
print('1  :', fheap.trees)
fheap.merge(fheap)
print('2  :', fheap.trees)
fheap.merge(fheap)
print('3  :', fheap.trees)
fheap.merge(fheap)
print('4  :', fheap.trees)
fheap.merge(fheap)
print('5  :', fheap.trees)
fheap.merge(fheap)
print('6  :', fheap.trees)
fheap.merge(fheap)
print('7  :', fheap.trees)
fheap.merge(fheap)
print('8  :', fheap.trees)
# print(fheap.trees)
# fheap.merge(fheap)
# print(fheap.trees)



# print(f'Nbr of trees : {fheap.count}')

# print(fheap.find_min())
