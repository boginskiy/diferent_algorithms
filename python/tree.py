# Бинарное дерево


# Класс определения узла бинарного дерева
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
    

# Класс для работы со стуктурой бинарное дерево
class Tree:
    def __init__(self):
        self.root = None


    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False


    # Метод добавления вершин бинарного дерева
    def append(self, obj):

        # Если добавляемое значение меньше значения в родительском узле
        # то новая вершина добавляется в левую ветвь, иначе в правую

        # Если добавляемое значение уже существует в бинарном дереве,
        # то оно игнорируется, дубли отсутствуют

        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        
        return obj


    # Показ бинарного дерева // Алгоритм обхода в глубину // Возрастающий
    def show_tree_incr(self, node):
        if node is None:
            return
        self.show_tree_incr(node.left)
        print(node.data, end = " ")
        self.show_tree_incr(node.right)

    
    # Показ бинарного дерева // Алгоритм обхода в глубину // Убывающий
    def show_tree_decr(self, node):
        if node is None:
            return
        self.show_tree_decr(node.right)
        print(node.data, end = " ")
        self.show_tree_decr(node.left)
    
    # Показ бинарного дерева // Алгоритм обхода в ширину
    def show_wide_tree(self, node):
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end = " ")

                if x.left:
                    vn += [x.left]
                
                if x.right:
                    vn += [x.right]
                
            print()
            v = vn
            

    # Удаление узла бинарного дерева

    def __del_leaf(self, s, p):
        """Вспомогательный метод для удаления узла без потомков."""
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None
        
    def __del_one_child(self, s, p):
        """Вспомогательный метод для удаления узла с одним потомком."""
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left


    def __find_min(self, node, parent):
        """Вспомогательный метод для поиска узла с наименьшим значением."""
        if node.left:
            return self.__find_min(node.left, node)
        return node, parent


    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None
        
        # Алгоритм удаление различается в зависимости от типа узла

        # Удаление узла без потомков
        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        
        # Удаление узла с одним потомком
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        
        # Удаление узла с двумя потомками
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data

            self.__del_one_child(sr, pr)


# v = [10, 5, 7, 16, 13, 2, 20]
v = [20, 5, 24, 2, 16, 11, 18]

t = Tree()

# Добавляем вершины в бинарное дерево
for x in v:
    t.append(Node(x))

# Отображение бинарного дерева
# t.show_tree_incr(t.root)

# print()

# # Удаление узла
t.del_node(5)
# t.show_tree_incr(t.root)

# Отображение бинарного дерева
t.show_wide_tree(t.root)
