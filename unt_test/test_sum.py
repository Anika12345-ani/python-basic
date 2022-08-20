import unittest
class unitTest(unittest. Testcase):
    #test case 1
    def test_sum_tc1(self):
        assert sum([1, 1]) == 2, "should be 2"

    def test_sum_tc2(self):
        assert sum([1, 1, 1]) == 3, "should be 3"

 if __name__ == "main":
     test_sum_tc1()
     test_sum_tc2()