import pytest


# @pytest.fixture()
# def login():
#     print('登录操作')
#     #yield 激活fixture等teardown
#     yield
#     print('注销')

# # 测试用例1、3需要登录
# # 传入fixture方法
# def test_case1(login):
#     print('测试用例1')
#
# @pytest.mark.usefixtures('login')
# def test_case2():
#     print('测试用例1')
#
# def test_case3(login):
#     print('测试用例1')
#
# def test_case4():
#     print('测试用例1')




class TestDemo:

    def test_a(self, connectDB):
        print('测试用例a')

    def test_b(self, connectDB):
        print('测试用例b')

class TestDemo1:

    def test_c(self, connectDB):
        print('测试用例c')

    def test_d(self, connectDB):
        print('测试用例d')