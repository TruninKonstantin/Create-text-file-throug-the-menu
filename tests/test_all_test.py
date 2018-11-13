from tests.test_acceptence_widget_holder_few_cliks_add import \
    UnittestWidgetHolder_Acceptence_few_click_add as acceptence_add
from tests.test_acceptence_widget_holder_few_cliks_add_few_click_del import \
    UnittestWidgetHolder_Acceptence_few_click_add_few_clicks_del as acceptence_del
from tests.test_click_widget_holder import UnittestWidgetHolder_Checking_widgetList_onClick as onClick
from tests.test_widget_holder import UnittestWidgetHolder_Checking_widgetList as listCheck
from tests.test_check_del_last_line import UnittestWidgetHolder_check_del_last_line as delLastLine

listCheck("runTest")
onClick("runTest")
delLastLine("runTest")
acceptence_add("runTest")
acceptence_del("runTest")