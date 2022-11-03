import data_provider as dp
import csv_creater as cs
import txt_creater as tx
import show_menu as sh

#cs.create_table()

if sh.show_menu() == 1:
    print(cs.read_csv_text())
elif sh.show_menu() == 2:
    data = dp.data_collection()
    cs.create_csv(data)
elif sh.show_menu() == 3:
    tx.create_txt()
else:
    print('Перезапустите программу, такого пункта в меню нет')




