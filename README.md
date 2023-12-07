# Advent of Code 2023
> Advent of Code is an annual set of Christmas-themed computer programming challenges that follow an Advent calendar.
> The programming puzzles cover a variety of skill sets and skill levels and can be solved using any programming language.

For challenge descriptions and inputs, check out: https://adventofcode.com/

## Challenges
 Day | Name | CPython | PyPy | CUDA JIT | Stars |
 :-:| :-: | :-: | :-: | :-: | :-: |
 01 | [Trebuchet?!](day_01) | 45 ms | 41 ms | - | ⭐️⭐️ |
 02 | [Cube Conundrum](day_02) | 26 ms | 32 ms | - | ⭐️⭐️ |
 03 | [Gear Ratios](day_03) | 31 ms | 41 ms | - | ⭐️⭐️ |
 04 | [Scratchcards](day_04) | 28 ms | 30 ms | - | ⭐️⭐️ |
 05 | [If You Give A Seed A Fertilizer](day_05) | ~ 2 h | 16 min | 4.4 s | ⭐️⭐️ |
 06 | [Wait For It](day_06) | 4490 ms | 81 ms | 615 ms | ⭐️⭐️ |
 07 | [Camel Cards](day_07) | 29 ms | 48 ms | - | ⭐️⭐️ |

To measure the process time with both CPython and PyPy, run the following:
``` shell
python measure_time.py <iterations> <source_script> <source_script_input>
```

> [!NOTE]  
> The specified runtimes above are for the second task of each day.
> For very short runtimes (< 50 ms) with few loop iterations and numerical computations, PyPy shows no significant advantages over CPython, and in some cases is even slower (probably due to the warm-up time).
> The CUDA JIT compiler of the numba library which translates python functions into PTX code does not work together with PyPy out of the box.