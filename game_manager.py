from enum import Enum
import numpy as np

from grid import OccupierType
from probe import ProbeInputType, ProbeDirection, ProbeState


class GameState(Enum):
    NONE = 0
    MOVING = 0
    PROBE = 0
    GUESS = 0


class GameManager:
    def __init__(self, grid, snake, probe_info):
        self.grid = grid
        self.snake = snake
        self.rng = np.random.default_rng()
        self.prey_location = -1
        self.spawn_prey()
        self.adj_mat = self.create_grid_adj_mat(grid.size, grid.size)
        self.distances = self.calc_distances(self.adj_mat)
        self.lives = 3
        # self.probe_vector = [.3333, .3333, .3333]
        # self.probe_vector = [1, 0, 0]
        self.probe_info = probe_info

        # self.grid = Grid(10, 50)
        # self.snake = Snake(self.grid)

        self.snake.add_on_collision_listener(self.on_collision)
        self.snake.add_on_collected_food_listener(self.on_collected_food)

    def on_move(self, direction):
        if self.probe_info.state is not ProbeState.NONE: return
        self.snake.move(direction)

    def on_probe_start(self):
        # TODO: make ui visible
        # TODO: freeze snake movement, disable guessing
        # vector = self.probe_info.get_probe_vector()
        # print("PROBING WITH VECTOR: ", vector)
        self.snake.on_probe()
        iad = self.snake.get_probe_idxs_and_directions()
        idxs = iad[0]
        dirs = iad[1]
        self.probe_info.set_probe_idxs(idxs)
        self.probe_info.set_probe_directions(dirs)
        # TODO: set_disabled
        # q = self.query(vector)
        # dis = q[0]
        # vec = q[1]
        # print(q)
        # self.probe_info.set_measured_distance(dis)
        # self.probe_info.set_probe_vector_output(vec)

    def on_query(self):
        vector = self.probe_info.get_probe_vector()
        print("PROBING WITH VECTOR: ", vector)
        q = self.query(vector)
        dis = q[0]
        vec = q[1]
        print(q)
        self.probe_info.set_measured_distance(dis)
        self.probe_info.set_probe_vector_output(vec)
        # TODO: make bottom ui visible

    def on_collision(self):
        # TODO:
        self.on_death()

    def on_death(self):
        print("YOU DEAD!!!")
        # TODO: [Take player back to "beginning of turn state" so they can continue playing]
        # TODO: reset probe grid occupier

    def on_fail(self):
        print("YOU MADE AN INCORRECT GUESS!!!")
        self.lives -= 1  # increment the number of lives downward. (i.e. decrement lives)
        if self.lives < 1:
            # TODO: [UI tells you you're dead. Game over]
            self.on_death()
        # TODO: [Take player back to "beginning of turn state" so they can continue playing]
        # TODO: reset probe grid occupier

    def on_success(self):
        print("YOU GUESSED CORRECTLY!!!")
        # TODO:
        # TODO: [prey location is revealed to player]
        self.grid.set_occupier(self.prey_location, OccupierType.PREY)
        # TODO: [player is asked to move snake to prey location]

    def on_collected_food(self):
        # TODO:
        print("COLLECTED FOOD!!!")
        self.snake.grow(1)
        self.on_reset_prey()

    def on_reset_prey(self):
        self.spawn_prey()

    def on_strike(self):
        if self.grid.selected_node is None:
            print("NO SQUARE SELECTED!!!")
            # TODO
            return
        guess = self.grid.selected_node.idx
        print("GUESSING: ", guess)
        print("PREY: ", self.prey_location)

        if guess == self.prey_location:
            self.on_success()
        else:
            self.on_fail()
        # TODO: [Take player back to "beginning of turn state" so they can continue playing]

    def spawn_prey(self):
        # TODO: don't spawn on top of snake
        self.prey_location = self.rng.integers(0, self.grid.size * self.grid.size)
        print("PREY LOCATED AT: ", self.prey_location)

    def create_grid_adj_mat(self, rows, columns):
        # Returns the adjacency matrix of a grid with rows number of rows and columns number of columns

        N = rows * columns

        graph = np.zeros((N, N))
        for j in range(rows - 1):
            for i in range(columns - 1):
                graph[j * columns + i, j * columns + i + 1] = 1
                graph[j * columns + i + 1, j * columns + i] = 1
                graph[j * columns + i, (j + 1) * columns + i] = 1
                graph[(j + 1) * columns + i, j * columns + i] = 1

        for j in range(rows - 1):
            graph[j * columns + columns - 1, (j + 1) * columns + columns - 1] = 1
            graph[(j + 1) * columns + columns - 1, j * columns + columns - 1] = 1

        for i in range(columns - 1):
            graph[(rows - 1) * columns + i, (rows - 1) * columns + i + 1] = 1
            graph[(rows - 1) * columns + i + 1, (rows - 1) * columns + i] = 1

        return graph

    def calc_distances(self, graph):
        # Returns array with each entry being the shortest distance between
        # two vertices.
        # The input is the adjacency matrix of the graph
        # Uses the Floyd-Warshall algorithm
        N = graph.shape[0]
        dist = np.full((N, N), np.inf)
        print(dist)
        dist[graph == 1] = 1
        print(dist)
        dist[range(N), range(N)] = 0
        print(dist)
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if dist[i, j] > dist[i, k] + dist[k, j]:
                        dist[i, j] = dist[i, k] + dist[k, j]
        return dist

    # def probeable_vertices(self, graph, snake_body):
    #     # Returns a list of vertices that the user is allowed to probe.
    #     # Where snake_body is a list of vertices, the first being the snake's
    #     # tail and the last being the snake's head.
    #     # And where graph is the adjacency matrix of the graph
    #
    #     assert len(snake_body) > 1, 'The snake\'s body must be two or more vertices.'
    #
    #     vect = graph[snake_body[-1]]  # 1 for vertices adjacent to head, 0 otherwise
    #     vect[snake_body[-2]] = 0  # Remove the space just behind the snake's head
    #
    #     # Return indices of vertices that are adjacent to the head, but not just
    #     # behind the head.
    #     return np.where(vect)[0]

    def query(self):
        # Given a probe state and the prey's location, this function returns
        # the measured distance resulting from the probe as well as the new
        # probe state that remains after measurement.

        # probed_vertices = self.probeable_vertices(graph, snake_body)  # vertices to be probed
        probed_vertices = self.snake.get_probe_idxs()

        distances = self.distances[probed_vertices, self.prey_location]
        # distances from probed vertices to the prey

        probabilities = np.abs(probe_vector) ** 2  # probs. of the different outcomes
        probabilities = probabilities / np.sum(probabilities)  # enforce summing up to 1

        measured_distance = self.rng.choice(distances, p=probabilities)

        # Get resulting state after measurement
        new_probe_vector = np.copy(probe_vector)
        new_probe_vector[distances != measured_distance] = 0

        # Normalize
        norm = np.sum(np.abs(new_probe_vector) ** 2) ** 0.5
        new_probe_vector = new_probe_vector / norm
        # new_norm = np.sum(np.abs(new_probe_vector) ** 2)
        # fp_error_allowance = 0.0000000001
        # assert 1 - new_norm < fp_error_allowance, f'Norm is {new_norm}, but it should be 1.'

        return measured_distance, new_probe_vector

    # def probe_measurement(self):
    #     probabilities = np.abs(self.probe_info.probe_vector_output) ** 2  # probabilities of different outcomes
    #     # Randomly choose a direction according to Born rule probabilities.
    #     return self.rng.choice(self.probe_info.probe_directions, p=probabilities)

    # def probe_unitary(self, unitary_mat, probe_vector):
    #     # Simply multiplies the probe state by the given unitary matrix
    #
    #     n = unitary_mat.shape(1)
    #     assert n == len(probe_vector), 'Probe vector dimension doesn\'t match.'
    #     assert n == unitary_mat.shape(0), 'Given matrix not square'
    #     assert unitary_mat.conj().T @ unitary_mat == np.eye(n), 'Given matrix not unitary'
    #
    #     return unitary_mat @ probe_vector


class GlobalDirection(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class RelativeDirection(Enum):
    FORWARD = 0
    RIGHT = 1
    LEFT = 2


class Snake:
    def __init__(self, grid):
        self.target_length = 2
        self.body = []
        self.grid = grid
        self.spawn()
        # self.game_manager = game_manager
        self.on_collision_listeners = []
        self.on_collected_food_listeners = []

    def spawn(self):
        # self.body[0] = 55
        self.add_to_head(55)
        # self.body[1] = 65
        self.add_to_tail(65)

    def grow(self, amount):
        self.target_length += amount

    def get_probe_idxs(self):
        # TODO: account for edges????
        idxs = [self.grid.up(self.body[0]), self.grid.right(self.body[0]), self.grid.down(self.body[0]),
                self.grid.left(self.body[0])]
        idxs.remove(self.body[1])
        # TODO: does this work?
        unavailable = idxs.count(-1)
        for i in range(unavailable):
            idxs.remove(-1)
        return idxs

    def get_probe_idxs_and_directions(self):
        # TODO: account for edges????
        idxs = self.get_probe_idxs()
        probe_directions = []
        for i in idxs:
            probe_directions.append(self.get_relative_direction(i))
        return idxs, probe_directions

    def get_relative_direction(self, idx):
        head = self.body[0]
        d = self.get_direction()
        if idx > head:
            if idx == head + 1:  # right
                if d == GlobalDirection.UP:
                    return ProbeDirection.RIGHT
                elif d == GlobalDirection.RIGHT:
                    return ProbeDirection.FORWARD
                elif d == GlobalDirection.DOWN:
                    return ProbeDirection.LEFT
            else:  # down
                if d == GlobalDirection.RIGHT:
                    return ProbeDirection.RIGHT
                elif d == GlobalDirection.DOWN:
                    return ProbeDirection.FORWARD
                elif d == GlobalDirection.LEFT:
                    return ProbeDirection.LEFT
        elif self.body[0] == self.body[1] - 1:  # left
            if d == GlobalDirection.UP:
                return ProbeDirection.LEFT
            elif d == GlobalDirection.DOWN:
                return ProbeDirection.RIGHT
            elif d == GlobalDirection.LEFT:
                return ProbeDirection.FORWARD
        else:  # up
            if d == GlobalDirection.UP:
                return ProbeDirection.FORWARD
            elif d == GlobalDirection.RIGHT:
                return ProbeDirection.LEFT
            elif d == GlobalDirection.LEFT:
                return ProbeDirection.RIGHT

    def get_direction(self):
        if self.body[0] > self.body[1]:
            if self.body[0] == self.body[1] + 1:
                print("right")
                return GlobalDirection.RIGHT
            else:
                print("down")
                return GlobalDirection.DOWN
        elif self.body[0] == self.body[1] - 1:
            print("left")
            return GlobalDirection.LEFT
        else:
            print("up")
            return GlobalDirection.UP

    def move(self, direction):
        # TODO: reset probe grid occupier

        new_head = -1
        if direction == GlobalDirection.UP:
            new_head = self.grid.up(self.body[0])
        elif direction == GlobalDirection.RIGHT:
            new_head = self.grid.right(self.body[0])
        elif direction == GlobalDirection.DOWN:
            new_head = self.grid.down(self.body[0])
        elif direction == GlobalDirection.LEFT:
            new_head = self.grid.left(self.body[0])

        if new_head == -1:
            return
        elif new_head == self.body[1]: # don't allow movement backward
            new_head = -1
            return
        elif new_head in self.body[2:]: #don't count movement back as collision
            self.on_collision()
            return
        elif self.grid.nodes[new_head].occupier == OccupierType.PREY:
            self.on_collected_food()
        self.add_to_head(new_head)
        while len(self.body) > self.target_length:
            self.remove_from_tail()

    def add_to_head(self, idx):
        self.body.insert(0, idx)
        type = OccupierType.SNAKE_HEAD_V
        if len(self.body) > 1:
            if self.body[1] == self.grid.left(idx) or self.body[1] == self.grid.right(idx):
                type = OccupierType.SNAKE_HEAD_H
            self.grid.set_occupier(self.body[1], OccupierType.SNAKE)

        self.grid.set_occupier(idx, type)

    def add_to_tail(self, idx):
        self.body.append(idx)
        # self.grid.nodes[idx].occupier = OccupierType.SNAKE
        self.grid.set_occupier(idx, OccupierType.SNAKE)

    def remove_from_tail(self):
        idx = self.body.pop()
        # self.grid.nodes[idx].occupier = OccupierType.NONE
        if self.grid.nodes[idx].occupier == OccupierType.SNAKE:
            # if prey is on snake body, it shouldn't disappear when snake off
            self.grid.set_occupier(idx, OccupierType.NONE)

    def on_collision(self):
        for listener in self.on_collision_listeners:
            listener()

    def add_on_collision_listener(self, listener):
        self.on_collision_listeners.append(listener)

    def on_probe(self):
        for i in self.get_probe_idxs():
            self.grid.set_occupier(i, OccupierType.PROBE)

    def add_on_collected_food_listener(self, listener):
        self.on_collected_food_listeners.append(listener)

    def on_collected_food(self):
        for listener in self.on_collected_food_listeners:
            listener()
