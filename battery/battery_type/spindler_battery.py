from battery.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.years_for_service = 3
    
    def needs_service(self):
        date_need_service = self.last.service_date.replace(year=self.last_service_date.year + self.nubbin_year_need_service)
        if date_need_service < self.current_date:
            return True
        else:
            return False

