# 定义测试类
import pytest
import yaml

from python_code.calc import Calculator

with open('./datas/calc.yml') as f:
    datas = yaml.safe_load(f)


class TestCalc:

    def setup_class(self):
        print('开始计算')
        # 实例化计算器类
        self.calc = Calculator()

    def teardown_class(self):
        print('计算结束')

    @pytest.mark.parametrize(
        'a, b, expect',
        datas['add']['datas'], ids=datas['add']['myid']
    )
    @pytest.mark.add
    def test_add(self, a, b, expect):
        # 调用add方法
        result = self.calc.add(a, b)
        # 判断如果结果为浮点数，保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果后，设置断言
        assert result == expect

    @pytest.mark.parametrize(
        'a, b, expect',
        datas['div']['datas'], ids=datas['div']['myid']
    )
    @pytest.mark.div
    def test_div(self, a, b, expect):
        # 调用div方法
        result = self.calc.div(a, b)
        # 判断如果结果为浮点数，保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果后，设置断言
        assert result == expect
