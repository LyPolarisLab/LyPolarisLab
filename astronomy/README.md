# Black Hole Simulator

Schwarzschild radius calculator using real astronomical data (NASA).

## Versions

**v1** (`black_hole_v1.py`) — Calculates and plots Schwarzschild radii for 9 known black holes on a log scale (Matplotlib). Compares stellar black holes (Cygnus X-1, V404 Cygni) with supermassive ones (Sagittarius A*, TON 618, Phoenix A).

**v2** (`black_hole_v2.py`) — Interactive simulator with structured data dictionaries:
- 3 categories of black holes: stellar, intermediate, supermassive
- 7 astronomical objects (planets and stars) with detailed properties
- Menu: simulate an object, explore known black holes, compare two, create a custom one
- Automatic mass-based classification

## Formula

Schwarzschild radius: `r = 2GM/c²`

## Dependencies

```
matplotlib
```
