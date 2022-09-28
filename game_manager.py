from enum import Enum
import numpy as np
import time
from scipy import linalg
import qiskit
import itertools

from grid import OccupierType, Grid


class GameState(Enum):
    NONE = 0
    MOVING = 0
    PROBE = 0
    GUESS = 0


class GameManager:
    def __init__(self, grid, snake):
        self.grid = grid
        self.snake = snake
        self.last_output = None
        self.rng = np.random.default_rng()
        self.prey_location = -1
        self.spawn_prey()
        self.adj_mat = self.create_grid_adj_mat(grid.size, grid.size)
        self.distances = self.calc_distances(self.adj_mat)
        self.lives = 3

        # self.grid = Grid(10, 50)
        # self.snake = Snake(self.grid)

        self.snake.add_on_collision_listener(self.on_collision)

    def on_move(self, direction):
        self.snake.move(direction)

    def on_probe(self, vector):
        # TODO:
        print(self.probe_measurement(vector))

    def on_collision(self):
        # TODO:
        self.on_death()

    def on_death(self):
        # TODO: [Take player back to "beginning of turn state" so they can continue playing]
        pass

    def on_fail(self):
        # TODO: [Take player back to "beginning of turn state" so they can continue playing]
        pass

    def on_success(self):
        # TODO:
        # TODO: [prey location is revealed to player]
        prey_revealed = True
        # TODO: [player is asked to move snake to prey location]
        pass

    def on_strike(self):
        guess = self.grid.selected_node

        if guess == self.prey_location:
            self.on_success()
        else:
            self.lives -= 1  # increment the number of lives downward. (i.e. decrement lives)
            if self.lives < 1:
                # TODO: [UI tells you you're dead. Game over]
                self.on_death()
            else:
                self.on_fail()
        # TODO: [Take player back to "beginning of turn state" so they can continue playing]

    # def button_up(rows, columns, prey_revealed, prey_location):  # and similar functions for down, left, right
    #
    #     head = snake_body[-1]
    #     new_head = head - columns  # index of square one above the head. Replace for other directions.
    #
    #     # Detect collision with edge
    #     if new_head not in range(rows * columns):
    #         # Do nothing. I.e. ignore when player tells snake to move off grid.
    #         return
    #
    #     # Detect collision with self
    #     if new_head in snake_body[1:]:
    #         # [UI tells you you're dead. Game over]
    #
    #         return
    #
    #     # Move snake
    #     snake_body.append(new_head)
    #     # Grow snake only when the prey location is revealed and prey is reached
    #     if not (prey_revealed and new_head == prey_location):
    #         snake_body.pop(0)
    #
    #     return

    def spawn_prey(self):
        # TODO: don't spawn on top of snake
        prey_location = self.rng.integers(0, self.grid.size)

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

    def query(self, probe_vector):
        # Given a probe state and the prey's location, this function returns
        # the measured distance resulting from the probe as well as the new
        # probe state that remains after measurement.

        # probed_vertices = self.probeable_vertices(graph, snake_body)  # vertices to be probed
        probed_vertices = self.snake.get_probe_idxs()

        # TODO: is this broken?????
        distances = self.distances[probed_vertices, np.full(len(probed_vertices, self.prey_location))]
        # distances from probed vertices to the prey

        probabilities = np.abs(probe_vector) ** 2  # probs. of the different outcomes
        probabilities = probabilities / np.sum(probabilities)  # enforce summing up to 1

        measured_distance = self.rng.choice(distances, probabilities)

        # Get resulting state after measurement
        new_probe_vector = np.copy(probe_vector)
        new_probe_vector[distances != measured_distance] = 0

        # Normalize
        norm = np.sum(np.abs(new_probe_vector) ** 2) ** 0.5
        new_probe_vector = new_probe_vector / norm
        new_norm = np.sum(np.abs(new_probe_vector) ** 2)
        assert new_norm == 1, f'Norm is {new_norm}, but it should be 1.'

        return measured_distance, new_probe_vector

    def probe_measurement(self, probe_vector):
        # Returns the index of a vertex that results from measuring the
        # given probe state.

        # probed_vertices = self.probeable_vertices(graph, snake_body)  # vertices that were probed
        probed_vertices = self.snake.get_probe_idxs()

        probabilities = np.abs(probe_vector) ** 2  # probabilities of different outcomes

        # Randomly choose a vertex according to Born rule probabilities.
        measured_vertex = self.rng.choice(probed_vertices, p=probabilities)

        return measured_vertex

    def probe_unitary(self, unitary_mat, probe_vector):
        # Simply multiplies the probe state by the given unitary matrix

        n = unitary_mat.shape(1)
        assert n == len(probe_vector), 'Probe vector dimension doesn\'t match.'
        assert n == unitary_mat.shape(0), 'Given matrix not square'
        assert unitary_mat.conj().T @ unitary_mat == np.eye(n), 'Given matrix not unitary'

        return unitary_mat @ probe_vector


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

    def spawn(self):
        # self.body[0] = 55
        self.add_to_head(55)
        # self.body[1] = 65
        self.add_to_tail(65)

    def grow(self, amount):
        self.target_length += amount

    def get_head_coords(self):
        return self.grid.get_coords(self.body[0])

    def get_probe_coords(self):
        return self.grid.get_coords(self.grid.up(self.body[0])), \
               self.grid.get_coords(self.grid.right(self.body[0])), \
               self.grid.get_coords(self.grid.down(self.body[0])), \
               self.grid.get_coords(self.grid.left(self.body[0]))

    def get_probe_idxs(self):
        idxs = [self.grid.up(self.body[0]), self.grid.right(self.body[0]), self.grid.down(self.body[0]),
                self.grid.left(self.body[0])]
        idxs.remove(self.body[1])
        return idxs

    def move(self, direction):
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
        if new_head in self.body:
            self.on_collision()
            return
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
        self.grid.set_occupier(idx, OccupierType.NONE)

    def on_collision(self):
        for listener in self.on_collision_listeners:
            listener()

    def add_on_collision_listener(self, listener):
        self.on_collision_listeners.append(listener)

    # def update_snake_position(self):
    #     for i in self.body:
    #         self.grid.nodes[i].occupier = OccupierType.SNAKE
