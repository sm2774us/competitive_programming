#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# EPI ( Elements Of Programming Interviews - Adnan Aziz ) : x to the power of y ( x^y )
#
# Description:
#
# Write a program that takes a double x and an integer y and returns x^y.
# You can ignore overflow and underflow.
#
# Hint: Exploit mathematical properties of exponentiation.
#
# **************************************************************************
# Source: https://github.com/adnanaziz/EPIJudge/blob/master/epi_judge_python/power_x_y.py (EPI - x to the power of y)
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
import unittest


class Solution(object):
    def power(self, x: float, y: int) -> float:
        result, power = 1.0, y
        if y < 0:
            power, x = -power, 1.0 / x
        while power:
            if power & 1:
                result *= x
            x, power = x * x, power >> 1
        return result


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_power(self) -> None:
        sol = Solution()
        for x, y, solution in (
            [1.4434757236195281, 12, 81.830237516844],
            [-1.0006612108596369, -2217, -0.23098094677379155],
            [1.0002834272148748, 9522, 14.85611487317237],
            [12.742204083907403, -32, 4.287204382781865e-36],
            [-1.0000900945810876, 11333, -2.7759579506143144],
            [1.0009527767684638, 2713, 13.245432102894338],
            [-33.39859347898841, -15, -1.3934049046693264e-23],
            [-0.9995431471379314, 16560, 0.0005171321645226984],
            [1.0008047242601628, -19097, 2.130712791834006e-07],
            [26.009670142825087, -38, 1.678324406851151e-54],
            [-1.0004147889224355, 267, -1.1170884251055078],
            [0.9993534485152967, 5181, 0.035053962717426244],
        ):
            self.assertEqual(solution, sol.power(x, y))


# main
if __name__ == "__main__":
    unittest.main()
