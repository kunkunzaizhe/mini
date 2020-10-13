from Api.apiFactory import ApiFactory
import app, utils, pytest


@pytest.mark.run(order=0)
class TestUserApi:

    def test_get_token(self):
        # 响应对象
        res = ApiFactory.get_user_api().get_token_api()
        # 断言状态吗
        # assert res.status_code == 200
        utils.common_assert_code(res)
        # 断言token存在
        assert len(res.json().get("token")) > 0
        # 保存token到 app配置文件
        app.headers["token"] = res.json().get("token")
        print("app.headers:{}".format(app.headers))

    def test_verif_token(self):
        # 响应对象
        res = ApiFactory.get_user_api().verify_token_api()
        # 断言状态吗
        assert res.status_code == 200
        # 断言有效
        assert res.json().get("isValid") is True
