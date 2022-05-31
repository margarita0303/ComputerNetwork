from time import sleep
import json
max_distance = 16

class Rip:
    def __init__(self):
        self.is_changed = False
        self.dists = dict()
        self.next_hop = dict()
        self.current_step = 1

    def deep_add_edge(self, src, dest, dist):
        if src not in self.dists:
            self.dists[src] = dict()
            self.next_hop[src] = dict()
        self.dists[src][dest] = dist
        self.next_hop[src][dest] = dest
        
    def add_edge(self, src, dest):
        self.deep_add_edge(src, dest, 1)
        self.deep_add_edge(dest, src, 1)
        self.deep_add_edge(src, src, 0)
        self.deep_add_edge(dest, dest, 0)

    def get_distance(self, a, b):
        return self.dists[a][b] if a in self.dists and b in self.dists[a] else max_distance

    def start(self):
        while True:
            print('STEP SIMULATION NUMBER', self.current_step)
            self.is_changed = False
            for (v, vals) in self.dists.items():
                for (u, d) in vals.items():
                    if d != 1: 
                        continue
                    for k in self.dists.keys():
                        try_to_update = False
                        vertex_from = u
                        vertex_to = k
                        vertex_using = v
                        if self.get_distance(vertex_using, vertex_to) + 1 < self.get_distance(vertex_from, vertex_to):
                            self.dists[vertex_from][vertex_to] = self.dists[vertex_using][vertex_to] + 1
                            self.next_hop[vertex_from][vertex_to] = vertex_using
                            try_to_update = True
                        else:
                            try_to_update = False
                        self.is_changed |= try_to_update
            for (v, vals) in self.dists.items():
                print('Step simulation number', self.current_step, 'of router', v)
                print('[Source IP]         [Destination IP]    [Next Hop]          [Metric]')
                for (u, d) in vals.items():
                    if d != 0:
                        print(f'{v:<20}{u:<20}{self.next_hop[v][u]:<20}{d:<20}')
                print()
            print('\n') 
            self.current_step += 1
            sleep(1)
            if not self.is_changed:
                break

if __name__ == "__main__":
    with open('config.json') as json_d:
        data = json.load(json_d)
        rip = Rip()
        for element in data:
            rip.add_edge(element['src'], element['dest'])
        rip.start() 
