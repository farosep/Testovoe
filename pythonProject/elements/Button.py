from elements.BaseElement import BaseElement


class Button(BaseElement):
    @property
    def _element(self):
        return self._find_element()

    @property
    def _clickable_element(self):
        return self._find_clickable_element()

    def click(self, with_scroll=True):
        """Клик по элементу с заданным локатором."""
        if with_scroll:
            self.scroll_to_element()
        self._clickable_element.click()
