from Pages.BasePage import BasePage


class Catalog(BasePage):
    a = 123

    def wait_until_loaded(self):
        """
        Абстрактный метод для ожидания загрузки компонента.
        """
        pass
