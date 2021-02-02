import pytest
from python_code.calc import Calculator

# 使用fixture方法对计算器进行实例化
@pytest.fixture(scope='module')
def get_calc():
    print('开始计算') # 实现执行用例前打印：开始计算
    calc = Calculator()
    yield calc
    print('结束计算') # 实现执行用例后打印：结束计算

