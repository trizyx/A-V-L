from __future__ import print_function

from sheets import spreadsheet_service
from sheets import drive_service

def read_range():
    range_name = 'Sheet1!A1:H10'  # retrieve data from existing sheet
    spreadsheet_id = '1_rK5CFa3JFto4JFwmxnS1KfKh9JAwNa1UDkduE2Wv1c'
    result = spreadsheet_service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    rows = result.get('values', [])
    print('{0} rows retrieved.'.format(len(rows)))
    print('{0} rows retrieved.'.format(rows))
    return rows

def write_range(value):
    values = [['vadim132006@mail.ru', 'aboba']]
    spreadsheet_id = '1_rK5CFa3JFto4JFwmxnS1KfKh9JAwNa1UDkduE2Wv1c'  # get the ID of the existing sheet
    range_name = 'Sheet1!A2:H2'  # the range to update in the existing sheet  # new row of data
    value_input_option = 'USER_ENTERED'
    values[0].append(value)
    print(values)
    body = {
        'values': values

    }
    result = spreadsheet_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption=value_input_option, body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))

if __name__ == '__main__':

    write_range('vadimaboba')

    read_range()