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
        self.count = 0
        self.min = None

    def __repr__(self):
        return repr(self.trees)

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        new_tree = Tree()
        new_tree.add_value(value)
        self.trees.append(new_tree)
        if self.min is None or self.min > value:
            self.min = value
        self.count += 1
        pass

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """

        self.min = int(min(tree.children[0] for tree in self.trees)) if len(self.trees) else None

        return self.min

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        min_value = self.find_min()

        for index, tree in enumerate(self.trees):
            if tree.children[0] == min_value:
                tree.children.remove(tree.children[0])
                for subtree in tree.children:
                    self.trees.insert(index, subtree)
                    self.count += 1
                self.trees.remove(tree)
                self.count -= 1

        return min_value

    def merge(self, fibonnaci_heap=None) -> None: 
        """
        Fusionne deux arbres
        """

        if fibonnaci_heap:
            if fibonnaci_heap.min < self.min:
                self.min = fibonnaci_heap.min
            for subtree in fibonnaci_heap.trees:
                self.trees.append(subtree)
                self.count += 1
        else:
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
                self.count -= 1
            elif first_tree.children[0] > last_tree.children[0]:
                last_tree.add_value(first_tree)
                self.trees.remove(first_tree)
                self.count -= 1

    def consolidate(self) -> None:
        """
        Fusionne l'arbre au maximum
        """
        vertically = None

        while vertically != 0:
            trees_sizes = [tree.size for tree in self.trees]
            min_array = [z for z in trees_sizes if trees_sizes.count(z) > 1]
            min_size = min(set(min_array)) if set(min_array) else 0
            vertically = math.frexp(min_array.count(min_size))[1] - 1 if min_size else 0
            horizontally = math.floor(min_array.count(min_size) / 2)

            for h in range(horizontally):
                self.merge()



# def test_heap(heap, heap2):
#     heap.insert(5)
#     heap.insert(1)
#     heap.insert(10)
#     heap.insert(0)

#     heap2.insert(2)
#     heap2.insert(10)
#     heap2.insert(15)
#     heap2.insert(12)

#     heap2.consolidate()

#     heap.merge(heap2)

#     heap.consolidate()

#     heap.delete_min()
#     heap.delete_min()
#     heap.delete_min()

#     heap.insert(3)
#     heap.insert(7)
#     heap.insert(4)
#     heap.insert(8)

#     heap.consolidate()

#     print(heap.trees)

# heap = FibonacciHeap()
# heap2 = FibonacciHeap()
# test_heap(heap, heap2)
