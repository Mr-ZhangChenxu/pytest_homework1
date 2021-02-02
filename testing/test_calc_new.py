# 定义测试类
import allure
import pytest

# 加载yaml测试数据
import yaml

with open('./datas/calc.yml') as f:
    datas = yaml.safe_load(f)
    add_data = datas['add']['datas']
    add_ids = datas['add']['myid']
    sub_data = datas['sub']['datas']
    sub_ids = datas['sub']['myid']
    mul_data = datas['mul']['datas']
    mul_ids = datas['mul']['myid']
    div_data = datas['div']['datas']
    div_ids = datas['div']['myid']

# 对加减乘除进行数据参数化，并返回
@pytest.fixture(params=add_data, ids=add_ids)
def get_add(request): # 加法
    data = request.param
    return data

@pytest.fixture(params=sub_data, ids=sub_ids)
def get_sub(request): # 减法
    data = request.param
    return data

@pytest.fixture(params=mul_data, ids=mul_ids)
def get_mul(request): # 乘法
    data = request.param
    return data

@pytest.fixture(params=div_data, ids=div_ids)
def get_div(request): # 除法
    data = request.param
    return data

@allure.feature('测试计算器')
class TestCalc:

    @allure.story('测试加法')
    @pytest.mark.run(order=1)
    def test_add(self, get_calc, get_add):
        # 调用add方法
        with allure.step('计算两个数的加和'):
            result = get_calc.add(get_add[0],get_add[1])
        # 判断如果结果为浮点数，保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果后，设置断言
        assert result == get_add[2]

    @allure.story('测试除法')
    @pytest.mark.run(order=4)
    def test_div(self, get_calc, get_div):
        # 调用div方法
        with allure.step('计算两个数的除商'):
            result = get_calc.div(get_div[0], get_div[1])
        # 判断如果结果为浮点数，保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果后，设置断言
        assert result == get_div[2]

    @allure.story('测试减法')
    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, get_sub):
        # 调用sub方法
        with allure.step('计算两个数的之差'):
            result = get_calc.sub(get_sub[0], get_sub[1])
        # 判断如果结果为浮点数，保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果后，设置断言
        assert result == get_sub[2]

    @allure.story('测试乘法')
    @pytest.mark.run(order=3)
    def test_mul(self, get_calc, get_mul):
        # 调用mul方法
        with allure.step('计算两个数的之积'):
            result = get_calc.mul(get_mul[0], get_mul[1])
        # 判断如果结果为浮点数，保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果后，设置断言
        assert result == get_mul[2]
