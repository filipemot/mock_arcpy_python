
# Criando Mock do Arcpy para Testes Unitários   

**Instalação**  

- pip install mock

**Código Base**

    import arcpy  
      
      
    def search_results(feature_class ):
      fields = ['Campo1']  
        results = []  
        cursor = arcpy.da.SearchCursor(feature_class, fields)  
        for row in cursor:  
            results.append(row[0])  
        return results  
      
      
    if __name__ == '__main__':  
        print(search_results("D:/Estudos/Python/mock_arcpy_python/ArcProProject/MockTestArcpy/MockTestArcpy.gdb/TabelaTeste" ))

**Código Testes**

No código base, temos o uso "arcpy.da.SearchCursor" função contida no módulo do arcpy. Sendo assim é necessário fazer um mock dessa chamada e definimos o return_value dessa função. Assim conseguimos executar o teste desse método.


    import unittest  
    from unittest.mock import patch  
      
    import main  
      
      
    class TestMain(unittest.TestCase):  
        @patch('main.arcpy.da.SearchCursor')  
        def test_get_results(self, spy_search_cursor):  
            spy_search_cursor.return_value = [['Teste1'], ['Teste2']]  
            return_values = main.search_results("feature_class")  
            self.assertEqual(len(return_values), 2)  
            self.assertEqual(return_values[0], 'Teste1')  
            self.assertEqual(return_values[1], 'Teste2')

