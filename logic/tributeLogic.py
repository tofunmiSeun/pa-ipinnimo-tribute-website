from database.tributeDB import TributeDB


class TributeLogic:

    @staticmethod
    def new_tribute(tribute_object):
        return TributeDB.add_new_tribute(tribute_object)

    @staticmethod
    def get_all_tributes():
        return TributeDB.get_all_tributes()
