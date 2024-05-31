import pytest
from sqlite3 import OperationalError
from modules.common.database import Database

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_users():
    db = Database()
    info = db.get_all_users()
    print(info)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    info = db.get_user_address_by_name("Sergii")
    
    assert info[0][0] == "Maydan Nezalezhnosti 1"
    assert info[0][1] == "Kyiv"
    assert info[0][2] == "3127"
    assert info[0][3] == "Ukraine"

@pytest.mark.database
def test_product_qt_update():
    db = Database()
    db.update_product_qt_by_id(1,25)
    info = db.select_product_qt_by_id(1)
    assert info[0][0] == 25

@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qt_by_id(4)

    assert water_qnt[0][0] == 30 

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, "test", "test", 999)
    db.delete_product_by_id(99)
    info = db.select_product_attr_by_id(99)
    assert len(info) == 0

@pytest.mark.database
def test_details_order():
    db = Database()
    order_info = db.get_detailed_order()
    print(order_info)
    assert len(order_info) == 1
    assert order_info[0][1] == "Sergii"
    assert order_info[0][2] == "солодка вода"

@pytest.mark.database_plus
def test_get_user_address_with_nonexistent_name():
    db = Database()
    # info1 = db.get_user_address_by_name(True)
    # assert len(info1) == 0
    info = db.get_user_address_by_name("Nonexistent_name")
    assert len(info) == 0
    info1 = db.get_user_address_by_name("")
    assert len(info1) == 0
    info2 = db.get_user_address_by_name("  ")
    assert len(info2) == 0

@pytest.mark.database_plus
def test_select_quantity_nonexistent_id():
    db = Database()
    info = db.select_product_qt_by_id(1984)
    assert len(info) == 0

@pytest.mark.database_plus
def test_update_quantity_nonexistent_id():
    db = Database()
    db.update_product_qt_by_id(999, 21)
    info = db.select_product_qt_by_id(999)
    assert len(info) == 0
    info2 = db.select_product_attr_by_id(999)
    assert len(info2) == 0

@pytest.mark.database_plus
def test_update_quantity_with_string1():
    db = Database()

    # db.update_product_qt_by_id(1, False)
    # """ It updated quatity to be 0 (converted my boolean False = 0)"""
    # db.update_product_qt_by_id(1, "971")
    # """ It updated quatity to be 971 (converted my string into integer, although I did not ask for it!)"""
    # db.update_product_qt_by_id(1, "seven")
    # """ It caused OperationalError: no such column 'seven' """
    # db.update_product_qt_by_id(1, "") # causes OperationalError
    # db.update_product_qt_by_id(1, " ") # causes OperationalError

    """An attempt to update quantity column with a string
       raises an exception"""

    with pytest.raises(OperationalError):
        db.update_product_qt_by_id(1, "nine")

    with pytest.raises(OperationalError):
        db.update_product_qt_by_id(1, "")

    with pytest.raises(OperationalError):
        db.update_product_qt_by_id(1, "  ")

@pytest.mark.database_plus
def test_update_quantity_with_string2():
    """An attempt to update quantity column with a string "quantity"
       is completely ignored"""
    db = Database()
    db.update_product_qt_by_id(1, 21) 
    before = db.select_product_qt_by_id(1)
    before_update_qt = before[0][0]
    assert before_update_qt == 21

    db.update_product_qt_by_id(1, "quantity") # when string is the same as the column name the update is ignored

    after = db.select_product_qt_by_id(1)
    after_update_qt = after[0][0]

    assert after_update_qt == before_update_qt

# @pytest.mark.database_plus
# def test_update_quantity_with_string_datatype():
#     db = Database()
#     before = db.select_product_qt_by_id(1)
#     before_update_qt = before[0][0]

#     db.update_product_qt_by_id(1,"five")

#     after = db.select_product_qt_by_id(1)
#     after_update_qt = after[0][0]
#     assert after_update_qt == before_update_qt


    
