#46 CONTENEDOR DE AGUA
"""
 * Dado un array de números enteros positivos, donde cada uno representa unidades de bloques apilados, debemos calcular cuantas unidades de agua quedarán atrapadas entre ellos.
 *
 * - Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].
 *
 *          ⏹
 *          ⏹
 *   ⏹💧💧 ⏹
 *   ⏹💧⏹⏹💧 ⏹
 *   ⏹💧⏹⏹💧 ⏹
 *   ⏹💧⏹⏹⏹⏹
 *
    [4, 0, 3, 6, 1, 2, 3]

 *          ⏹
 *          ⏹
 *   ⏹💧💧 ⏹
 *   ⏹💧⏹⏹💧 💧 ⏹
 *   ⏹💧⏹⏹💧 ⏹⏹
 *   ⏹💧⏹⏹⏹⏹⏹
    

 *   Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades de agua. Suponemos que existe un suelo impermeable en la parte inferior que retiene el agua.
"""

from typing import List, Tuple

def count_water_lr(blocks: List[int]) -> Tuple[int, int]:
    """from left to right, count the available spaces for water storage"""
    count = 0
    wall_index = 0

    for i in range(1, len(blocks)):
        if blocks[i] >= blocks[wall_index]:
            count += sum(blocks[wall_index] - blocks[j] for j in range(wall_index, i))
            wall_index = i
    return count, wall_index

def get_total_water(blocks: List[int]) -> int:
    """function to determinate the quantity of water we can storage in the blocks"""
    result, last_processed_wall = count_water_lr(blocks)
    if last_processed_wall + 2 < len(blocks):
        result += count_water_lr(blocks[:last_processed_wall - 1:-1])[0]
    return result

def test_case(blocks: List[int], expected: int):
    check_valid_test_case(blocks)
    returned = get_total_water(blocks)
    if returned != expected:
        raise Exception(
            f"Case with blocks {blocks}, returns {returned} but it should be {expected}"
        )

def check_valid_test_case(blocks: List[int]):
    if any(b < 0 for b in blocks):
        raise Exception(
            f"Case with block {blocks} is not valid, it should contain only positive values"
        )

def main():
    """
           #
           #
        #..#
        #.##.#
        #.##.#
        #.####
    """
    test_case([4, 0, 3, 6, 1, 3], 7)

    """
          #
          #
          #..#
        #.##.#
        #.##.#
        ####.#
    """
    test_case([3, 1, 6, 3, 0, 4], 7)

    """
        #...#
        ##..#
        ###.#
    """
    test_case([3, 2, 1, 0, 3], 6)

    """
            #...#...#
          #.#...#.#.#
          #.#.#.#.#.#
        #.#.#.#.#.#.#.#
        #.#.#.#.#.#.#.#
    """
    test_case([2, 0, 4, 0, 5, 0, 3, 0, 5, 0, 4, 0, 5, 0, 2], 31)

    """
        #.........#
        ##.......##
        ###.....###
        ####...####
        #####.#####
    """
    test_case([5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5], 25)

    """
        
              #...#
         #...###.##.#
        ###.#######.##
    """
    test_case([1, 2, 1, 0, 1, 2, 3, 2, 1, 2, 3, 0, 2, 1], 10)

    """
              #.#
          #...#.#
        #.#.#.#.#
        #########
    """
    test_case([2, 1, 3, 1, 2, 1, 4, 1, 4], 9)

    """
              #..#
         #....#..#
         ##.#.#.##
        #####.#####
    """
    test_case([1, 3, 2, 1, 2, 0, 4, 1, 2, 4, 1], 12)

    """
                    #
            #.....#.# 
        #...#..#..#.#.# 
        #.#.#.###.###.#.#.#
        #.###.###########.#
    """
    test_case([3, 0, 2, 1, 4, 0, 2, 3, 2, 1, 4, 2, 5, 1, 3, 1, 2, 0, 2], 25)

    """
          #
          ####
         ######
        #########
    """
    test_case([1, 2, 4, 3, 3, 3, 2, 1, 1], 0)

    """
              #...#
            #.#...#.#
          #.#.#...#.#.#
        #.#.#.#.#.#.#.#.#
    """
    test_case([1, 0, 2, 0, 3, 0, 4, 0, 1, 0, 4, 0, 3, 0, 2, 0, 1], 23)

    """
        #.........#
        #.#.....#.#
        #.#.#.#.#.#
        #.#.#.#.#.#
        #.###.###.#
    """
    test_case([5, 0, 4, 1, 3, 0, 3, 1, 4, 0, 5], 29)

    """
            #.#
            #.#
          #.###.#
        #.#.###.#.#
        #.#######.#
    """
    test_case([2, 0, 3, 1, 5, 3, 5, 1, 3, 0, 2], 10)

    """
        #####.#####
        ###########
        ###########
        ###########
        ###########
    """
    test_case([5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5], 1)

    """
        #....#....#
        #....#....#
        #...###...#
        #..#####..#
        ###########
    """
    test_case([5, 1, 1, 2, 3, 5, 3, 2, 1, 1, 5], 26)

    # Casos extremos, para comprobar complejidad O(n)
    test_case([i for i in range(1, 1000001)], 0)
    test_case([i % 2 for i in range(1000001)], 499999)
    test_case([1 - i % 2 for i in range(1000001)], 500000)
    test_case([i % 100000 for i in range(1000000)], 44999550000)
    test_case([99999 - i % 100000 for i in range(1000000)], 44999550000)
    test_case([1000000000 * (i % 2) for i in range(1000001)], 499999000000000)
    test_case([1000000000 * (1 - i % 2) for i in range(1000001)], 500000000000000)

    # Casos extra
    test_case([], 0)
    test_case([1, 0], 0)
    test_case([0, 1], 0)
    test_case([1, 0, 1], 1)
    test_case([0, 1, 0], 0)

    print("All cases passed!")

if __name__ == '__main__':
    main()

