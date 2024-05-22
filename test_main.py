import unittest
from unittest.mock import patch, MagicMock
import mysql.connector
import tkinter
from main import prodtoTable, removeProd, viewProds, bill, newCust

class TestShopManagementSystem(unittest.TestCase):

    @patch('mysql.connector.connect')
    def test_prodtoTable(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        prodName = MagicMock(return_value='Product1')
        prodPrice = MagicMock(return_value='10')
        date = MagicMock(return_value='2023-05-01')
        prodtoTable()
        mock_cursor.execute.assert_called_with("INSERT INTO products(date,prodName,prodPrice) VALUES(%s,%s,%s)", ('2023-05-01', 'Product1', '10'))

    @patch('mysql.connector.connect')
    def test_removeProd(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        prodName = MagicMock(return_value='Product1')
        removeProd()
        mock_cursor.execute.assert_called_with("DELETE from products where LOWER(prodName) = 'product1'")

    @patch('mysql.connector.connect')
    def test_viewProds(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('2023-05-01', 'Product1', '10'), ('2023-05-02', 'Product2', '20')]
        viewProds()
        mock_cursor.execute.assert_called_with('SELECT * FROM products')

    @patch('mysql.connector.connect')
    def test_bill(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('2023-05-01', 'Product1', '10'), ('2023-05-02', 'Product2', '20'), ('2023-05-03', 'Product3', '30')]
        custName = MagicMock(return_value='John')
        date = MagicMock(return_value='2023-05-01')
        name1 = MagicMock(return_value='2')
        name2 = MagicMock(return_value='3')
        name3 = MagicMock(return_value='0')
        bill()
        mock_cursor.execute.assert_called_with('SELECT * FROM products')

    @patch('mysql.connector.connect')
    def test_newCust(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('2023-05-01', 'Product1', '10'), ('2023-05-02', 'Product2', '20'), ('2023-05-03', 'Product3', '30')]
        custName = MagicMock(return_value='John')
        date = MagicMock(return_value='2023-05-01')
        name1 = MagicMock(return_value='2')
        name2 = MagicMock(return_value='3')
        name3 = MagicMock(return_value='0')
        newCust()
        mock_cursor.execute.assert_called_with('SELECT * FROM products')

if __name__ == '__main__':
    unittest.main()
