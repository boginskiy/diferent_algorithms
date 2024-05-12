# Breadth-First Search << Поиск в ширину

from collections import deque


############# Create deque ###############
search_deque = deque()


def person_is_seller(seller):
    """Функция определения продавца яблок."""
    return seller == "tom"


def breadth_search(name, graph, search_deque):
    """Функция поиска в ширину продавца яблок."""
    search_deque += graph[name]

    searched = []  # Массив для отслеживания проверенных людей 

    while search_deque:
        person = search_deque.popleft()

        if not person in searched:

            if person_is_seller(person):
                print("Is {0} an apple seller!".format(person.upper()))
                return True
            else:
                search_deque += graph[person]
                searched.append(person)
    
    return False


if __name__ == '__main__':
    graph = {}
    graph["dima"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anui", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["tom", "jonny"]
    graph["anui"] = []
    graph["peggy"] = []
    graph["tom"] = []
    graph["jonny"] = []

    breadth_search("dima", graph, search_deque)

    # Is TOM an apple seller!