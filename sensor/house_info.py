from datetime import datetime,date
class HouseInfo:
    def __init__(self, data):
        self.data = data

    def get_data_by_area(self, field, rec_date = 0):
        field_data = []
