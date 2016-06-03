import gspread
import os
import traceback
import sys
from oauth2client.service_account import ServiceAccountCredentials


class SheetUtils:

    def __init__(self, sheet_id):
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(os.path.dirname(__file__),
                                                                                    'service_key.json'), scope)
        self.gc = gspread.authorize(credentials)
        sht = self.gc.open_by_key(sheet_id)
        self.worksheet = sht.get_worksheet(0)

    def __get_row(self, value):
        cell = self.worksheet.find(value)
        return cell

    def update_row(self, find, value, column):
        try:
            cell = self.__get_row(find)
            self.worksheet.update_cell(cell.row, column, value)
        except Exception:
            traceback.print_exc(file=sys.stdout)

