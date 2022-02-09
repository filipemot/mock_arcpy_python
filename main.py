import arcpy  # type: ignore


def search_results(feature_class):
    fields = ['Campo1']
    results = []
    cursor = arcpy.da.SearchCursor(feature_class, fields)
    for row in cursor:
        results.append(row[0])
    return results


if __name__ == '__main__':
    print(search_results(
        "D:/Estudos/Python/mock_arcpy_python/ArcProProject/MockTestArcpy/MockTestArcpy.gdb/TabelaTeste2"))
