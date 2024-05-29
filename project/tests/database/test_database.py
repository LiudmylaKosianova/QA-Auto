import pytest
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

 

    
