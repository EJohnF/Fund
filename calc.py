import numpy as np
import matplotlib.pyplot as plt
from datetime import date
from dateutil.relativedelta import relativedelta

initialDonation = 20000
together = initialDonation * 2
growthEachYear = 0.1
interestRate = 0.07
initialDate = date(2018, 1, 1)
monthsToPay = 12*12


overall = 0
currentDate = initialDate
yearlyOverall = []
for i in range(25*12 + 1):
    if i % 12 == 0 and i != 0:
        initialDonation =  initialDonation * (1 + growthEachYear) if (i < monthsToPay) else 0
        together = initialDonation * 2
        yearlyOverall.append(overall)
        print('end year №', '%.0f' % (i/12), ' - ', currentDate.year - 1,
              '\t overall sum: ', '%.0f' % overall,
              '\t sum to pay: ', '%.0f' % initialDonation,
              '\t monthly fund income: ', '%.0f' % (overall * (interestRate/12.0)))
    currentDate += relativedelta(months=1)
    overall = overall * (1 + interestRate/12.0) + ( together if i < monthsToPay else 0)

