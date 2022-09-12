'''
部门的接口业务流程
部门的增，删除，更新，详情，以及断言
'''
import jsonpath

from http_接口.http_直播实战.http_实战_直播_第二节_mine.apis.department.department import Department


class TestDepartment():
    def setup_class(self):
        self.create_json_data = {
                "name": "0703研发中心917",
                "name_en": "0703RDGZ",
                "parentid": 1,
                "order": 1,
                "id": 917
            }
        self.update_json_data = {
            "id": 917,
            "name": "yangbing研发中心",
            "name_en": "yangbingRDGZ",
            "parentid": 1,
            "order": 1
        }
        self.id='917'
        self.department=Department()

    def test_depart_flow(self):
        '''创建部门，更新部门，删除部门'''
        create_res=self.department.create_department(self.create_json_data)
        _list = self.department.department_detil()
        assert create_res.json().get("id") in jsonpath.jsonpath(_list.json(), "$..id")

        # self.department.update_department(self.update_json_data)
        # _list = self.department.department_detil()
        # assert self.update_json_data.get("name") in jsonpath.jsonpath(_list.json(), "$..name")
        #
        # self.department.del_depaerment(self.id)
        # _list = self.department.department_detil()
        # assert self.id not in jsonpath.jsonpath(_list.json(), "$..id")
