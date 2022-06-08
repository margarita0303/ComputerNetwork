class Line:
    def __init__(self, destination, distance, first):
        self.destination = destination
        self.distance = distance
        self.first = first

    def print(self):
        print(self.destination, self.distance, self.first)

class Table:
    def __init__(self, name):
        self.name = name
        self.strings = []
        self.vertexes = set()

    def get_name(self):
        return self.name

    def add(self, destination, distance, first):
        new_line = Line(destination, distance, first)
        self.vertexes.add(destination)
        self.strings.append(new_line)
        self.strings.sort(key= lambda i: i.destination)
        
    def delete(self, destination):
        contains = False
        string = None
        for s in self.strings:
            if s.destination == destination:
                contains = True
                string = s
                break
        if contains == True:
            self.strings.remove(string)
    
    def change(self, destination, length, first):
        ind = None
        for i in range(len(self.strings)):
            if self.strings[i].destination == destination:
                ind = i
                break
        if ind != None:
            self.strings[ind].distance = length
            self.strings[ind].first = first

    def print(self):
        self.strings.sort(key= lambda i: i.destination)
        for i in range(len(self.strings)):
            self.strings[i].print()

    def get_dist(self, dest):
        for s in self.strings:
            if s.destination == dest:
                return s.distance
        return 0

class DistanceVectorRouting:
    def __init__(self, file_name):
        class Vertex:
            def __init__(self, name):
                self.name = name
                self.table = Table(name)
                self.neigbours = []
                self.table.add(self.name, 0.0, self.name)
                self.neigbours.append(self.name)

            def append_line(self, destination, dist):
                self.neigbours.append(destination)
                self.table.add(destination, dist, destination)
                self.neigbours.sort()

            def update(self, tables):
                is_updated = False
                tables.sort(key= lambda i: i.name)
                for table in tables:
                    table.strings.sort(key= lambda i: i.destination)
                    if table.name in self.neigbours:
                        for line in table.strings:
                            new_dist = 0
                            to_add = 0
                            for s in self.table.strings:
                                if s.destination == table.name:
                                    to_add = s.distance
                            new_dist = line.distance + to_add
                            if line.destination in self.table.vertexes:
                                if new_dist < self.table.get_dist(line.destination):
                                    self.table.change(line.destination, new_dist, table.name)
                                    is_updated = True
                            else:
                                self.table.add(line.destination, new_dist, table.name)
                                is_updated = True
                return is_updated

            def get_table(self):
                return self.table

            def print(self):
                print("Name", self.name)
                self.table.print()

        self.vertexes = []
        self.file_name = file_name
        f = open(file_name, 'r')
        lines = f.read().strip().split("\n")
        vertexes_set = set()
        for line in lines:
            values = line.split()
            vertexes_set.add(values[0])
            vertexes_set.add(values[1])
        for vertex_name in vertexes_set:
            new_vertex = Vertex(vertex_name)
            self.vertexes.append(new_vertex)
        for line in lines:
            values = line.split()
            for vertex in self.vertexes:
                if vertex.name == values[0]:
                    vertex.append_line(values[1], float(values[2]))
                if vertex.name == values[1]:
                    vertex.append_line(values[0], float(values[2]))

    def run(self):
        step = 1
        while True:
            stop = False
            print("\nStep", step)
            step += 1
            self.vertexes.sort(key= lambda i: i.name)
            for vertex in self.vertexes:
                vertex.print()
            for vertex in self.vertexes:
                tables = []
                for vertex2 in self.vertexes:
                    tables.append(vertex2.get_table())
                tables.sort(key= lambda i: i.name)
                if vertex.update(tables) == False:
                    stop = True
            if stop == True:
                break

if __name__ == '__main__':
    task = DistanceVectorRouting("graph1.txt")
    task.run()
