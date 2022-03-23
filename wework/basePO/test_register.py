from wework.basePO.index import Index


class TestRegister:
    def setup(self):
        self.index = Index()

    # def teardown(self):
    #     quit()

    def test_register(self):
        # self.index.goto_login().goto_register().register()
        self.index.goto_register().register()