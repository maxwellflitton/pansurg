<<<<<<< Updated upstream
=======
import os
import pickle
from datetime import datetime

>>>>>>> Stashed changes
from .data_update import DataUpdate


class Papers(list):
    """
    This class is responsible for downloading and containing the papers.
    """
    def __init__(self) -> None:
        """
        The constructor for the Papers class.
        """
        super().__init__([])
<<<<<<< Updated upstream
        self._get_data()
=======
        Time_now = datetime.now()
        timestamp_now = datetime.timestamp(Time_now)

        

        if self.cache_exists is True and force_refresh is False:
            """
            Add timestamp functionality if timestamp more than 7 days
            (604800 seconds) force_refresh
            """
            if timestamp_now < timestamp + 604800:
                self.load()

            else:
                break
                
                
        else:
            first_load_time = datetime.now()
            timestamp = datetime.timestamp(first_load_time)
            self._get_data()

            self._save()
>>>>>>> Stashed changes


    def _get_data(self) -> None:
        """
        Updates self with data from source.

        :return: None
        """
        print("Getting data from source...")
        data_getter = DataUpdate()
        data_getter.get_data()

        for paper in data_getter.data:
            self.append(paper)
        print("data collected")
