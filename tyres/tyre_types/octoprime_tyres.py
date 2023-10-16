from tyres.tyre import Tyre

class Octoprime_Tyres(Tyre):
    def __init__(self, wear):
        self.wear = wear
        self.service_needed = 3

    def needs_service(self):
        for wear_produced in self.wear:
            sum_wear += wear_produced
        if sum_wear >= self.service_needed:
            return True
        return False