import openpyxl
import PySide6.QtWidgets
import sys
import DemoWindow
import numbers



def display_data(data: list):
    qt_app = PySide6.QtWidgets.QApplication(sys.argv)  # sys.argv is the list of command line arguments
    my_window = DemoWindow.Comp490DemoWindow(data)
    sys.exit(qt_app.exec())


def get_test_data() -> list[dict]:
    workbook_file = openpyxl.load_workbook("CensusMedianIncome.xlsx")
    worksheet = workbook_file.active
    final_data_list = []
    for current_row in worksheet.rows:
        state_cell = current_row[0]
        state_name = state_cell.value
        median_income2018 = current_row[1].value
        if not isinstance(median_income2018, numbers.Number):
            continue
        record = {"state_name": state_name, "median_income": median_income2018}
        final_data_list.append(record)
    return final_data_list


def get_key(value:dict):
    return value["median_income"]


def main():
    test_data = get_test_data()
    test_data.sort(key=get_key)
    display_data(test_data)


if __name__ == '__main__':
    main()
