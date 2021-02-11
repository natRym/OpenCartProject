from src.framework.BaseTest import BaseTest
from src.pages.MainPage import MainPage


class TestSearchOrder(BaseTest):

    def test_search_order(self):
        self.logger.log_step(1, 'Main Page is opened')
        main_page = MainPage()

        self.logger.log_step(2, "Top bar is found")
        main_page.top_bar()

        self.logger.log_step(3, "Logo is found")
        main_page.logo()

        self.logger.log_step(4, "Search field is found")
        main_page.search_field()

        #
        #
        # self.logger.log_step(2, 'Customise results')
        # results_page = SearchResultPage()
        # results_page.select_language(language=lang)
        # results_page.select_condition(condition=condition)
        # results_page.select_sort_results(sort_value_name=sort_name)
        #
        # self.logger.log_step(3, 'Check Results')
        # results = results_page.get_order_names_in_list()
        # assert False not in [order_name in order for order in
        #                      results], "List has not relevant results! - %s" % [order for order in results if
        #                                                                         order_name not in order]
