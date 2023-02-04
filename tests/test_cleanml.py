from cleanml.cleanml import make_column_names
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