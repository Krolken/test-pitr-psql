from test_pitr.base import Session
from test_pitr.model import TestData
import datetime
import time

while True:
    session = Session()

    item = TestData(data=f"test{datetime.datetime.utcnow()}")

    session.add(item)
    session.commit()

    session.close()
    time.sleep(0.001)
