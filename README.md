# Vacuum Cleaner Problem (Artificial Intelligence)

This repository contains a Python implementation of the **Vacuum Cleaner Problem**, a simple example used in Artificial Intelligence to demonstrate how an intelligent agent interacts with an environment.

## Problem Description

The Vacuum Cleaner agent operates in an environment with two rooms: **Room A** and **Room B**.
Each room can be either **Clean** or **Dirty**.

The agent performs the following actions:

* **Clean** the room if it is dirty.
* **Move** to the next room if the current room is clean.

The goal of the agent is to **clean all rooms in the environment**.

## Algorithm

1. Start in **Room A**.
2. Check the state of the current room.
3. If the room is **Dirty**, clean it.
4. Move to the next room.
5. Repeat the process until **both rooms are clean**.

## Requirements

* Python 3.x

## How to Run

Run the program using Python:

```
python vacuum_cleaner_problem.py
```

## Sample Input

```
Enter status of Room A (Clean/Dirty): Dirty
Enter status of Room B (Clean/Dirty): Dirty
```

## Sample Output

```
Initial State: {'A': 'Dirty', 'B': 'Dirty'}

Room A is Dirty. Cleaning...
Room B is Dirty. Cleaning...

Both rooms are clean. Task completed.

Final State: {'A': 'Clean', 'B': 'Clean'}
```

## Author

Jagadeshwar Surneni
