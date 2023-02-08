from cleanml import make_column_names, remove_spl_chars_in_columns
import pandas as pd

def test_make_column_names():
    data_to_read = {'Name':['cheeka','cherry'],
                'Age of Children':[14,10],
                'Name of School (Mention full name)':['InOrbit','InOrbit'],
                }
    data = pd.DataFrame(data_to_read)
    expected = ['name','age_of_children','school_name']
    data_new = make_column_names(data, column_dict={'Name of School (Mention full name)':'school_name'})
    actual = data_new.columns.to_list()
    assert expected == actual, "Column names conversion is incorrect!"

def test_remove_spl_chars_in_columns():
    data_to_read = {'child_name_(mention_full_name??)':['cheeka','cherry'],
                'age_%':[14,10],
                'name_of_School_(mention_full_name_&*!)':['InOrbit','InOrbit'],
                }
    data_new = pd.DataFrame(data_to_read)
    expected = ['child_name_mention_full_name', 'age','name_of_School_mention_full_name']
    data_new = remove_spl_chars_in_columns(data_new, spl_chars_excepted=['_'])
    actual = data_new.columns.to_list()
    assert expected == actual, "Column names conversion is incorrect!"