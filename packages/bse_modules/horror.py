class HorrorBase():
    def __init__(self, ps, mv):
        self.ps = ps
        self.mv = mv

    def Move(self, mv_path):
        for i in self.mv:
            self.ps = mv_path[i]
            if self.ps == mv_path[-1]:
                return



    

