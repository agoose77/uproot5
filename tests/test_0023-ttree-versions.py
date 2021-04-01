# BSD 3-Clause License; see https://github.com/scikit-hep/uproot4/blob/main/LICENSE

from __future__ import absolute_import

import numpy
import pytest
import skhep_testdata

import uproot

truth = {
    "n": [
        0,
        1,
        2,
        3,
        4,
        0,
        1,
        2,
        3,
        4,
        0,
        1,
        2,
        3,
        4,
        0,
        1,
        2,
        3,
        4,
        0,
        1,
        2,
        3,
        4,
        0,
        1,
        2,
        3,
        4,
    ],
    "b": [
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
    ],
    "ab": [
        [False, True, False],
        [True, False, True],
        [False, True, False],
        [True, False, True],
        [False, True, False],
        [True, False, True],
        [False, True, False],
        [True, False, True],
        [False, True, False],
        [True, False, True],
        [False, True, False],
        [True, False, True],
        [False, True, False],
        [True, False, True],
        [False, True, False],
        [True, False, True],
        [False, True, False],
        [True, False, True],
        [False, True, False],
        [True, False, True],
        [False, True, False],
        [True, False, True],
        [False, True, False],
        [True, False, True],
        [False, True, False],
        [True, False, True],
        [False, True, False],
        [True, False, True],
        [False, True, False],
        [True, False, True],
    ],
    "Ab": [
        [],
        [True],
        [True, True],
        [True, True, True],
        [True, True, True, True],
        [],
        [False],
        [False, False],
        [False, False, False],
        [False, False, False, False],
        [],
        [True],
        [True, True],
        [True, True, True],
        [True, True, True, True],
        [],
        [False],
        [False, False],
        [False, False, False],
        [False, False, False, False],
        [],
        [True],
        [True, True],
        [True, True, True],
        [True, True, True, True],
        [],
        [False],
        [False, False],
        [False, False, False],
        [False, False, False, False],
    ],
    "i1": [
        -15,
        -14,
        -13,
        -12,
        -11,
        -10,
        -9,
        -8,
        -7,
        -6,
        -5,
        -4,
        -3,
        -2,
        -1,
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
    ],
    "ai1": [
        [-14, -13, -12],
        [-13, -12, -11],
        [-12, -11, -10],
        [-11, -10, -9],
        [-10, -9, -8],
        [-9, -8, -7],
        [-8, -7, -6],
        [-7, -6, -5],
        [-6, -5, -4],
        [-5, -4, -3],
        [-4, -3, -2],
        [-3, -2, -1],
        [-2, -1, 0],
        [-1, 0, 1],
        [0, 1, 2],
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
        [4, 5, 6],
        [5, 6, 7],
        [6, 7, 8],
        [7, 8, 9],
        [8, 9, 10],
        [9, 10, 11],
        [10, 11, 12],
        [11, 12, 13],
        [12, 13, 14],
        [13, 14, 15],
        [14, 15, 16],
        [15, 16, 17],
    ],
    "Ai1": [
        [],
        [-15],
        [-15, -13],
        [-15, -13, -11],
        [-15, -13, -11, -9],
        [],
        [-10],
        [-10, -8],
        [-10, -8, -6],
        [-10, -8, -6, -4],
        [],
        [-5],
        [-5, -3],
        [-5, -3, -1],
        [-5, -3, -1, 1],
        [],
        [0],
        [0, 2],
        [0, 2, 4],
        [0, 2, 4, 6],
        [],
        [5],
        [5, 7],
        [5, 7, 9],
        [5, 7, 9, 11],
        [],
        [10],
        [10, 12],
        [10, 12, 14],
        [10, 12, 14, 16],
    ],
    "u1": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
    ],
    "au1": [
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
        [4, 5, 6],
        [5, 6, 7],
        [6, 7, 8],
        [7, 8, 9],
        [8, 9, 10],
        [9, 10, 11],
        [10, 11, 12],
        [11, 12, 13],
        [12, 13, 14],
        [13, 14, 15],
        [14, 15, 16],
        [15, 16, 17],
        [16, 17, 18],
        [17, 18, 19],
        [18, 19, 20],
        [19, 20, 21],
        [20, 21, 22],
        [21, 22, 23],
        [22, 23, 24],
        [23, 24, 25],
        [24, 25, 26],
        [25, 26, 27],
        [26, 27, 28],
        [27, 28, 29],
        [28, 29, 30],
        [29, 30, 31],
        [30, 31, 32],
    ],
    "Au1": [
        [],
        [0],
        [0, 2],
        [0, 2, 4],
        [0, 2, 4, 6],
        [],
        [5],
        [5, 7],
        [5, 7, 9],
        [5, 7, 9, 11],
        [],
        [10],
        [10, 12],
        [10, 12, 14],
        [10, 12, 14, 16],
        [],
        [15],
        [15, 17],
        [15, 17, 19],
        [15, 17, 19, 21],
        [],
        [20],
        [20, 22],
        [20, 22, 24],
        [20, 22, 24, 26],
        [],
        [25],
        [25, 27],
        [25, 27, 29],
        [25, 27, 29, 31],
    ],
    "i2": [
        -15,
        -14,
        -13,
        -12,
        -11,
        -10,
        -9,
        -8,
        -7,
        -6,
        -5,
        -4,
        -3,
        -2,
        -1,
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
    ],
    "ai2": [
        [-14, -13, -12],
        [-13, -12, -11],
        [-12, -11, -10],
        [-11, -10, -9],
        [-10, -9, -8],
        [-9, -8, -7],
        [-8, -7, -6],
        [-7, -6, -5],
        [-6, -5, -4],
        [-5, -4, -3],
        [-4, -3, -2],
        [-3, -2, -1],
        [-2, -1, 0],
        [-1, 0, 1],
        [0, 1, 2],
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
        [4, 5, 6],
        [5, 6, 7],
        [6, 7, 8],
        [7, 8, 9],
        [8, 9, 10],
        [9, 10, 11],
        [10, 11, 12],
        [11, 12, 13],
        [12, 13, 14],
        [13, 14, 15],
        [14, 15, 16],
        [15, 16, 17],
    ],
    "Ai2": [
        [],
        [-15],
        [-15, -13],
        [-15, -13, -11],
        [-15, -13, -11, -9],
        [],
        [-10],
        [-10, -8],
        [-10, -8, -6],
        [-10, -8, -6, -4],
        [],
        [-5],
        [-5, -3],
        [-5, -3, -1],
        [-5, -3, -1, 1],
        [],
        [0],
        [0, 2],
        [0, 2, 4],
        [0, 2, 4, 6],
        [],
        [5],
        [5, 7],
        [5, 7, 9],
        [5, 7, 9, 11],
        [],
        [10],
        [10, 12],
        [10, 12, 14],
        [10, 12, 14, 16],
    ],
    "u2": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
    ],
    "au2": [
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
        [4, 5, 6],
        [5, 6, 7],
        [6, 7, 8],
        [7, 8, 9],
        [8, 9, 10],
        [9, 10, 11],
        [10, 11, 12],
        [11, 12, 13],
        [12, 13, 14],
        [13, 14, 15],
        [14, 15, 16],
        [15, 16, 17],
        [16, 17, 18],
        [17, 18, 19],
        [18, 19, 20],
        [19, 20, 21],
        [20, 21, 22],
        [21, 22, 23],
        [22, 23, 24],
        [23, 24, 25],
        [24, 25, 26],
        [25, 26, 27],
        [26, 27, 28],
        [27, 28, 29],
        [28, 29, 30],
        [29, 30, 31],
        [30, 31, 32],
    ],
    "Au2": [
        [],
        [0],
        [0, 2],
        [0, 2, 4],
        [0, 2, 4, 6],
        [],
        [5],
        [5, 7],
        [5, 7, 9],
        [5, 7, 9, 11],
        [],
        [10],
        [10, 12],
        [10, 12, 14],
        [10, 12, 14, 16],
        [],
        [15],
        [15, 17],
        [15, 17, 19],
        [15, 17, 19, 21],
        [],
        [20],
        [20, 22],
        [20, 22, 24],
        [20, 22, 24, 26],
        [],
        [25],
        [25, 27],
        [25, 27, 29],
        [25, 27, 29, 31],
    ],
    "i4": [
        -15,
        -14,
        -13,
        -12,
        -11,
        -10,
        -9,
        -8,
        -7,
        -6,
        -5,
        -4,
        -3,
        -2,
        -1,
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
    ],
    "ai4": [
        [-14, -13, -12],
        [-13, -12, -11],
        [-12, -11, -10],
        [-11, -10, -9],
        [-10, -9, -8],
        [-9, -8, -7],
        [-8, -7, -6],
        [-7, -6, -5],
        [-6, -5, -4],
        [-5, -4, -3],
        [-4, -3, -2],
        [-3, -2, -1],
        [-2, -1, 0],
        [-1, 0, 1],
        [0, 1, 2],
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
        [4, 5, 6],
        [5, 6, 7],
        [6, 7, 8],
        [7, 8, 9],
        [8, 9, 10],
        [9, 10, 11],
        [10, 11, 12],
        [11, 12, 13],
        [12, 13, 14],
        [13, 14, 15],
        [14, 15, 16],
        [15, 16, 17],
    ],
    "Ai4": [
        [],
        [-15],
        [-15, -13],
        [-15, -13, -11],
        [-15, -13, -11, -9],
        [],
        [-10],
        [-10, -8],
        [-10, -8, -6],
        [-10, -8, -6, -4],
        [],
        [-5],
        [-5, -3],
        [-5, -3, -1],
        [-5, -3, -1, 1],
        [],
        [0],
        [0, 2],
        [0, 2, 4],
        [0, 2, 4, 6],
        [],
        [5],
        [5, 7],
        [5, 7, 9],
        [5, 7, 9, 11],
        [],
        [10],
        [10, 12],
        [10, 12, 14],
        [10, 12, 14, 16],
    ],
    "u4": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
    ],
    "au4": [
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
        [4, 5, 6],
        [5, 6, 7],
        [6, 7, 8],
        [7, 8, 9],
        [8, 9, 10],
        [9, 10, 11],
        [10, 11, 12],
        [11, 12, 13],
        [12, 13, 14],
        [13, 14, 15],
        [14, 15, 16],
        [15, 16, 17],
        [16, 17, 18],
        [17, 18, 19],
        [18, 19, 20],
        [19, 20, 21],
        [20, 21, 22],
        [21, 22, 23],
        [22, 23, 24],
        [23, 24, 25],
        [24, 25, 26],
        [25, 26, 27],
        [26, 27, 28],
        [27, 28, 29],
        [28, 29, 30],
        [29, 30, 31],
        [30, 31, 32],
    ],
    "Au4": [
        [],
        [0],
        [0, 2],
        [0, 2, 4],
        [0, 2, 4, 6],
        [],
        [5],
        [5, 7],
        [5, 7, 9],
        [5, 7, 9, 11],
        [],
        [10],
        [10, 12],
        [10, 12, 14],
        [10, 12, 14, 16],
        [],
        [15],
        [15, 17],
        [15, 17, 19],
        [15, 17, 19, 21],
        [],
        [20],
        [20, 22],
        [20, 22, 24],
        [20, 22, 24, 26],
        [],
        [25],
        [25, 27],
        [25, 27, 29],
        [25, 27, 29, 31],
    ],
    "i8": [
        -15,
        -14,
        -13,
        -12,
        -11,
        -10,
        -9,
        -8,
        -7,
        -6,
        -5,
        -4,
        -3,
        -2,
        -1,
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
    ],
    "ai8": [
        [-14, -13, -12],
        [-13, -12, -11],
        [-12, -11, -10],
        [-11, -10, -9],
        [-10, -9, -8],
        [-9, -8, -7],
        [-8, -7, -6],
        [-7, -6, -5],
        [-6, -5, -4],
        [-5, -4, -3],
        [-4, -3, -2],
        [-3, -2, -1],
        [-2, -1, 0],
        [-1, 0, 1],
        [0, 1, 2],
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
        [4, 5, 6],
        [5, 6, 7],
        [6, 7, 8],
        [7, 8, 9],
        [8, 9, 10],
        [9, 10, 11],
        [10, 11, 12],
        [11, 12, 13],
        [12, 13, 14],
        [13, 14, 15],
        [14, 15, 16],
        [15, 16, 17],
    ],
    "Ai8": [
        [],
        [-15],
        [-15, -13],
        [-15, -13, -11],
        [-15, -13, -11, -9],
        [],
        [-10],
        [-10, -8],
        [-10, -8, -6],
        [-10, -8, -6, -4],
        [],
        [-5],
        [-5, -3],
        [-5, -3, -1],
        [-5, -3, -1, 1],
        [],
        [0],
        [0, 2],
        [0, 2, 4],
        [0, 2, 4, 6],
        [],
        [5],
        [5, 7],
        [5, 7, 9],
        [5, 7, 9, 11],
        [],
        [10],
        [10, 12],
        [10, 12, 14],
        [10, 12, 14, 16],
    ],
    "u8": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
    ],
    "au8": [
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
        [4, 5, 6],
        [5, 6, 7],
        [6, 7, 8],
        [7, 8, 9],
        [8, 9, 10],
        [9, 10, 11],
        [10, 11, 12],
        [11, 12, 13],
        [12, 13, 14],
        [13, 14, 15],
        [14, 15, 16],
        [15, 16, 17],
        [16, 17, 18],
        [17, 18, 19],
        [18, 19, 20],
        [19, 20, 21],
        [20, 21, 22],
        [21, 22, 23],
        [22, 23, 24],
        [23, 24, 25],
        [24, 25, 26],
        [25, 26, 27],
        [26, 27, 28],
        [27, 28, 29],
        [28, 29, 30],
        [29, 30, 31],
        [30, 31, 32],
    ],
    "Au8": [
        [],
        [0],
        [0, 2],
        [0, 2, 4],
        [0, 2, 4, 6],
        [],
        [5],
        [5, 7],
        [5, 7, 9],
        [5, 7, 9, 11],
        [],
        [10],
        [10, 12],
        [10, 12, 14],
        [10, 12, 14, 16],
        [],
        [15],
        [15, 17],
        [15, 17, 19],
        [15, 17, 19, 21],
        [],
        [20],
        [20, 22],
        [20, 22, 24],
        [20, 22, 24, 26],
        [],
        [25],
        [25, 27],
        [25, 27, 29],
        [25, 27, 29, 31],
    ],
    "f4": [
        -14.899999618530273,
        -13.899999618530273,
        -12.899999618530273,
        -11.899999618530273,
        -10.899999618530273,
        -9.899999618530273,
        -8.899999618530273,
        -7.900000095367432,
        -6.900000095367432,
        -5.900000095367432,
        -4.900000095367432,
        -3.9000000953674316,
        -2.9000000953674316,
        -1.899999976158142,
        -0.8999999761581421,
        0.10000000149011612,
        1.100000023841858,
        2.0999999046325684,
        3.0999999046325684,
        4.099999904632568,
        5.099999904632568,
        6.099999904632568,
        7.099999904632568,
        8.100000381469727,
        9.100000381469727,
        10.100000381469727,
        11.100000381469727,
        12.100000381469727,
        13.100000381469727,
        14.100000381469727,
    ],
    "af4": [
        [-13.899999618530273, -12.899999618530273, -11.899999618530273],
        [-12.899999618530273, -11.899999618530273, -10.899999618530273],
        [-11.899999618530273, -10.899999618530273, -9.899999618530273],
        [-10.899999618530273, -9.899999618530273, -8.899999618530273],
        [-9.899999618530273, -8.899999618530273, -7.900000095367432],
        [-8.899999618530273, -7.900000095367432, -6.900000095367432],
        [-7.900000095367432, -6.900000095367432, -5.900000095367432],
        [-6.900000095367432, -5.900000095367432, -4.900000095367432],
        [-5.900000095367432, -4.900000095367432, -3.9000000953674316],
        [-4.900000095367432, -3.9000000953674316, -2.9000000953674316],
        [-3.9000000953674316, -2.9000000953674316, -1.899999976158142],
        [-2.9000000953674316, -1.899999976158142, -0.8999999761581421],
        [-1.899999976158142, -0.8999999761581421, 0.10000000149011612],
        [-0.8999999761581421, 0.10000000149011612, 1.100000023841858],
        [0.10000000149011612, 1.100000023841858, 2.0999999046325684],
        [1.100000023841858, 2.0999999046325684, 3.0999999046325684],
        [2.0999999046325684, 3.0999999046325684, 4.099999904632568],
        [3.0999999046325684, 4.099999904632568, 5.099999904632568],
        [4.099999904632568, 5.099999904632568, 6.099999904632568],
        [5.099999904632568, 6.099999904632568, 7.099999904632568],
        [6.099999904632568, 7.099999904632568, 8.100000381469727],
        [7.099999904632568, 8.100000381469727, 9.100000381469727],
        [8.100000381469727, 9.100000381469727, 10.100000381469727],
        [9.100000381469727, 10.100000381469727, 11.100000381469727],
        [10.100000381469727, 11.100000381469727, 12.100000381469727],
        [11.100000381469727, 12.100000381469727, 13.100000381469727],
        [12.100000381469727, 13.100000381469727, 14.100000381469727],
        [13.100000381469727, 14.100000381469727, 15.100000381469727],
        [14.100000381469727, 15.100000381469727, 16.100000381469727],
        [15.100000381469727, 16.100000381469727, 17.100000381469727],
    ],
    "Af4": [
        [],
        [-15.0],
        [-15.0, -13.899999618530273],
        [-15.0, -13.899999618530273, -12.800000190734863],
        [-15.0, -13.899999618530273, -12.800000190734863, -11.699999809265137],
        [],
        [-10.0],
        [-10.0, -8.899999618530273],
        [-10.0, -8.899999618530273, -7.800000190734863],
        [-10.0, -8.899999618530273, -7.800000190734863, -6.699999809265137],
        [],
        [-5.0],
        [-5.0, -3.9000000953674316],
        [-5.0, -3.9000000953674316, -2.799999952316284],
        [-5.0, -3.9000000953674316, -2.799999952316284, -1.7000000476837158],
        [],
        [0.0],
        [0.0, 1.100000023841858],
        [0.0, 1.100000023841858, 2.200000047683716],
        [0.0, 1.100000023841858, 2.200000047683716, 3.299999952316284],
        [],
        [5.0],
        [5.0, 6.099999904632568],
        [5.0, 6.099999904632568, 7.199999809265137],
        [5.0, 6.099999904632568, 7.199999809265137, 8.300000190734863],
        [],
        [10.0],
        [10.0, 11.100000381469727],
        [10.0, 11.100000381469727, 12.199999809265137],
        [10.0, 11.100000381469727, 12.199999809265137, 13.300000190734863],
    ],
    "f8": [
        -14.9,
        -13.9,
        -12.9,
        -11.9,
        -10.9,
        -9.9,
        -8.9,
        -7.9,
        -6.9,
        -5.9,
        -4.9,
        -3.9000000000000004,
        -2.9000000000000004,
        -1.9000000000000004,
        -0.9000000000000004,
        0.09999999999999964,
        1.0999999999999996,
        2.0999999999999996,
        3.0999999999999996,
        4.1,
        5.1,
        6.1,
        7.1,
        8.1,
        9.1,
        10.1,
        11.1,
        12.1,
        13.1,
        14.1,
    ],
    "af8": [
        [-13.9, -12.9, -11.9],
        [-12.9, -11.9, -10.9],
        [-11.9, -10.9, -9.9],
        [-10.9, -9.9, -8.9],
        [-9.9, -8.9, -7.9],
        [-8.9, -7.9, -6.9],
        [-7.9, -6.9, -5.9],
        [-6.9, -5.9, -4.9],
        [-5.9, -4.9, -3.9000000000000004],
        [-4.9, -3.9000000000000004, -2.9000000000000004],
        [-3.9000000000000004, -2.9000000000000004, -1.9000000000000004],
        [-2.9000000000000004, -1.9000000000000004, -0.9000000000000004],
        [-1.9000000000000004, -0.9000000000000004, 0.09999999999999964],
        [-0.9000000000000004, 0.09999999999999964, 1.0999999999999996],
        [0.09999999999999964, 1.0999999999999996, 2.0999999999999996],
        [1.0999999999999996, 2.0999999999999996, 3.0999999999999996],
        [2.0999999999999996, 3.0999999999999996, 4.1],
        [3.0999999999999996, 4.1, 5.1],
        [4.1, 5.1, 6.1],
        [5.1, 6.1, 7.1],
        [6.1, 7.1, 8.1],
        [7.1, 8.1, 9.1],
        [8.1, 9.1, 10.1],
        [9.1, 10.1, 11.1],
        [10.1, 11.1, 12.1],
        [11.1, 12.1, 13.1],
        [12.1, 13.1, 14.1],
        [13.1, 14.1, 15.1],
        [14.1, 15.1, 16.1],
        [15.1, 16.1, 17.1],
    ],
    "Af8": [
        [],
        [-15.0],
        [-15.0, -13.9],
        [-15.0, -13.9, -12.8],
        [-15.0, -13.9, -12.8, -11.7],
        [],
        [-10.0],
        [-10.0, -8.9],
        [-10.0, -8.9, -7.8],
        [-10.0, -8.9, -7.8, -6.7],
        [],
        [-5.0],
        [-5.0, -3.9],
        [-5.0, -3.9, -2.8],
        [-5.0, -3.9, -2.8, -1.7],
        [],
        [0.0],
        [0.0, 1.1],
        [0.0, 1.1, 2.2],
        [0.0, 1.1, 2.2, 3.3],
        [],
        [5.0],
        [5.0, 6.1],
        [5.0, 6.1, 7.2],
        [5.0, 6.1, 7.2, 8.3],
        [],
        [10.0],
        [10.0, 11.1],
        [10.0, 11.1, 12.2],
        [10.0, 11.1, 12.2, 13.3],
    ],
    "str": [
        "hey-0",
        "hey-1",
        "hey-2",
        "hey-3",
        "hey-4",
        "hey-5",
        "hey-6",
        "hey-7",
        "hey-8",
        "hey-9",
        "hey-10",
        "hey-11",
        "hey-12",
        "hey-13",
        "hey-14",
        "hey-15",
        "hey-16",
        "hey-17",
        "hey-18",
        "hey-19",
        "hey-20",
        "hey-21",
        "hey-22",
        "hey-23",
        "hey-24",
        "hey-25",
        "hey-26",
        "hey-27",
        "hey-28",
        "hey-29",
    ],
}


@pytest.mark.parametrize(
    "version",
    [
        "5.23.02",  # 2009-02-26, TTree version 16, TBranch version 11
        "5.24.00",  # 2009-06-30, TTree version 16, TBranch version 11
        "5.25.02",  # 2009-10-01, TTree version 17, TBranch version 12
        "5.26.00",  # 2009-12-14, TTree version 18, TBranch version 12
        "5.27.02",  # 2010-04-27, TTree version 18, TBranch version 12
        "5.28.00",  # 2010-12-15, TTree version 18, TBranch version 12
        "5.29.02",  # 2011-04-21, TTree version 18, TBranch version 12
        "5.30.00",  # 2011-06-28, TTree version 19, TBranch version 12
        "6.08.04",  # 2017-01-13, TTree version 19, TBranch version 12
        "6.10.05",  # 2017-07-28, TTree version 19, TBranch version 12   is this 6.10.04?
        "6.14.00",  # 2018-06-13, TTree version 20, TBranch version 13
        "6.16.00",  # 2019-01-23, TTree version 20, TBranch version 13
        "6.18.00",  # 2019-06-25, TTree version 20, TBranch version 13
        "6.20.04",  # 2020-04-01, TTree version 20, TBranch version 13
    ],
)
def test(version):
    with uproot.open(
        skhep_testdata.data_path("uproot-sample-{0}-uncompressed.root".format(version))
    )["sample"] as sample:
        arrays = sample.arrays(sample.keys(), library="np")

        assert set(arrays.keys()) == set(truth.keys())
        for key in truth.keys():
            if isinstance(
                sample[key].interpretation, uproot.interpretation.jagged.AsJagged
            ):
                assert [row.tolist() for row in arrays[key]] == truth[key]
            else:
                assert arrays[key].tolist() == truth[key]

        assert sample.file._streamers is None
