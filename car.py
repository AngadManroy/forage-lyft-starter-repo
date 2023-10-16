from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):
        #any new parts have to be written here
        self.engine = engine
        self.battery = battery

    #No Longer an abstract method
    def needs_service(self):
        return self.engine.needds_service() or self.battery.needs_service()
