from Base import Base
from time import sleep


class BookSearch(Base):
    _book_search_id = "com.codepath.android.booksearch:id/search_src_text"
    _book_search_box_id = "com.codepath.android.booksearch:id/action_bar_container"
    _book_title_id = "com.codepath.android.booksearch:id/tvTitle"
    _book_page_cover_id = "com.codepath.android.booksearch:id/ivBookCover"
    _book_page_title_id = "com.codepath.android.booksearch:id/tvTitle"
    _book_page_author_id = "com.codepath.android.booksearch:id/tvAuthor"
    _book_page_publisher_id = "com.codepath.android.booksearch:id/tvPublisher"
    _book_page_page_count_id = "com.codepath.android.booksearch:id/tvPageCount"
    _cancel_button_id = "com.android.permissioncontroller:id/cancel_button"
    _continue_button_id = "com.android.permissioncontroller:id/button_group"
    _ok_button_pop_up_id = "android:id/button1"
    _search_button_id = "com.codepath.android.booksearch:id/action_search"
    _switch_widget_id = "android:id/switch_widget"
    _warning_pop_up_id = "android:id/content"

    def check_book_attributes(self, cover=None, title=None, author=None, publisher=None, page_count=None):
        result_1 = True
        result_2 = True
        result_3 = True
        result_4 = True
        result_5 = True
        if cover:
            result_1 = (cover == self.get_element_attribute_by_id(self._book_page_cover_id, "text"))
        if title:
            result_2 = (title == self.get_element_attribute_by_id(self._book_page_title_id, "text"))
        if author:
            result_3 = (author == self.get_element_attribute_by_id(self._book_page_author_id, "text"))
        if publisher:
            result_2 = (publisher == self.get_element_attribute_by_id(self._book_page_publisher_id_id, "text"))
        if page_count:
            result_2 = (page_count == self.get_element_attribute_by_id(self._book_page_page_count_id, "text"))
        return result_1 and result_2 and result_3 and result_4 and result_5

    def is_book_present(self, book_title):
        book_list = self.return_list_of_elements_by_id(self._book_title_id)
        if book_list:
            for book in book_list:
                title = self.get_element_attribute(book, "text")
                if title and (book_title in title):
                    self._logger.info(f'The book {book_title} found in the list')
                    return True
            self._logger.info(f'The book {book_title} not found in the list')
        else:
            self._logger.error("No book list found")
        return False

    def search_book(self, book):
        result_1 = self.tap_search_button()
        result_2 = self.type_by_id(self._book_search_id, book)
        try:
            self._driver.press_keycode(66)
        except Exception as e:
            self._logger.error(f'An error has been reported by Appium when pressing the search button')
            return False
        else:
            self._logger.info(f'Query to search book {book} executed successfully')
            return result_1 and result_2

    def tap_book(self, book_title):
        book_list = self.return_list_of_elements_by_id(self._book_title_id)
        if book_list:
            for book in book_list:
                title = self.get_element_attribute(book, "text")
                if title and (book_title in title):
                    self._logger.info(f'The book {book_title} found in the list, attenpting to tap the registry')
                    return self.tap_element(book)
            self._logger.error(f'The book {book_title} not found in the list')
        else:
            self._logger.error("No book list found")
        return False

    def search_for_author(self, author):
        book_list = self.return_list_of_elements_by_id(self._book_title_id)
        if book_list:
            for book in book_list:
                self.tap_element(book)
                self.wait_for_book_information_to_appear()
                if self.get_element_attribute_by_id(self._book_page_author_id, "text") == author:
                    return self.get_element_attribute_by_id(self._book_page_title_id, "text")
                else:
                    self.go_back()
            return None
        else:
            None

    def tap_cancel_button(self):
        return self.tap_button(self._cancel_button_id)

    def tap_ok_button_pop_up(self):
        return self.tap_button(self._ok_button_pop_up_id)

    def tap_continue_button(self):
        return self.tap_button(self._continue_button_id)

    def tap_search_button(self):
        return self.tap_button(self._search_button_id)

    def tap_switch_widget(self):
        return self.tap_button(self._switch_widget_id)

    def wait_for_book_information_to_appear(self):
        return self.wait_for_element_to_appear_by_id(self._book_page_page_count_id)

    def wait_for_search_box_to_appear(self):
        return self.wait_for_element_to_appear_by_id(self._book_search_box_id)

    def wait_for_vbooks_list_to_appear(self):
        return self.wait_for_element_to_appear_by_id(self._book_title_id)

    def wait_for_warning_pop_up_to_appear(self):
        return self.wait_for_element_to_appear_by_id(self._warning_pop_up_id)