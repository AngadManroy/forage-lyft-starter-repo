from tyres.tyre import Tyre

class Carrigan_Tyres(Tyre):
    def __init__(self, wear):
        self.wear = wear
        self.service_need = 0.9

    def needs_service(self):
        for wear_produced in self.wear:
            if wear_produced >= self.service_need:
                return True
        return False