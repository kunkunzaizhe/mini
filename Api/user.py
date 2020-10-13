import app,requests

class UserApi:

    def __init__(self):
        # 获取token
        self.get_token_url = app.base_url + "/token/user"
        # token 验证
        self.token_verify_url = app.base_url +"/token/verify"
        # 用户地址信息
        self.user_addr_url = app.base_url + "/address"

    def get_token_api(self):
        # 请求体
        data = {"code":app.code}
        # 返回请求对象
        return requests.post(self.get_token_url,json=data, headers=app.headers)

    def verify_token_api(self):
        # 请求参数
        data = {"token":app.headers.get("token")}
        # 返回响应对象
        return requests.post(self.token_verify_url,json=data, headers=app.headers)
