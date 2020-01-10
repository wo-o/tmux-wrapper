class Dialogue :

    @staticmethod
    def get_target() :
        target = None
        while not target :
            target = input(f'Type target : ')
        return target

    @staticmethod
    def get_range(start) :

        end = -1
        while start > end :
            end = int(input(f'Select range. Type greater than or equal to {start} :'))
        return end