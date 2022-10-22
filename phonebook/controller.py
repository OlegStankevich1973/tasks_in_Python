

import view
import model

def run():
        menu = view.show_menu()
        if menu == 1:
            data = view.get_info()
            res = view.show_export()
            if res ==1:
                res_record = model.txt_data_record(data)
            if res ==2:
                res_record = model.csv_data_record(data)
            
                       
        if menu == 2:
            res = view.show_import()
            if res == 1:
                option_reading_txt = model.txt_data_reading()
            if res == 2:
                option_reading_csv = model.csv_data_reading()

        
       


