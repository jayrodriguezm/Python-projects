import unittest
import logging
import datetime
import Logger as logger
from BookSearch import BookSearch as bs
from time import sleep

class BookSearchTests(unittest.TestCase):
    bs = None
    dt = datetime.datetime.now().time()
    logfile = logfile = "BookSearchTests-" + '-' + str(dt) + ".log"
    log = logger.custom_logger(logging.DEBUG, file_name=logfile)
    app = "/Users/jrodrigu/Documents/github/Coding/Android-App-Demo/app-debug.apk"
    platform_version = "11.0"
    device_name = "Pixel 5"

    @classmethod
    def setUp(cls):
        cls.bs = bs(cls.log)
        cls.bs.initialize(app=cls.app, platform_version=cls.platform_version, device_name=cls.device_name)
        cls.assertTrue(cls.bs.tap_continue_button(), "Failed to tap the continue button")
        cls.bs.wait_for_warning_pop_up_to_appear()
        cls.bs.tap_ok_button_pop_up()
        cls.bs.wait_for_search_box_to_appear()

    def test_init(self):
        self.assertTrue(self.bs.search_book("Last"), "Book search failed")
        self.assertTrue(self.bs.wait_for_vbooks_list_to_appear())
        self.assertTrue(self.bs.tap_book("His Last Bow"))
        self.assertTrue(self.bs.wait_for_book_information_to_appear())
        self.assertTrue(self.bs.check_book_attributes(title="His Last Bow", page_count="318 pages"))

    def test_priamo(self):
        self.assertTrue(self.bs.search_book("James Martin"), "Book search failed")
        self.assertTrue(self.bs.wait_for_vbooks_list_to_appear())
        print(self.bs.search_for_author("J. M. Bennett"))

    @classmethod
    def tearDown(cls):
        # cls.bs.quit_driver()
        pass

    if __name__ == '__main__':
        unittest.main()
