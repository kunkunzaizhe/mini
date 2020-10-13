import app, requests


class OrderApi:
    def __init__(self):
        # 订单列表
        self.order_list_url = app.base_url + "/order/by_user"
        # 创建订单
        self.create_order_url = app.base_url + "/order"
        # 查看订单
        self.query_order_url = app.base_url + "/order/{}"

    def order_list_api(self, page=1):
        data = {"page": page}
        return requests.get(self.order_list_url, params=data, headers=app.headers)

    def create_order_api(self, product_id, count):
        data = {"products": [{"product_id": product_id, "count": count}]}
        return requests.post(self.create_order_url, json=data, headers=app.headers)

    def query_order_api(self, order_id):
        return requests.get(self.query_order_url.format(order_id), headers=app.headers)
