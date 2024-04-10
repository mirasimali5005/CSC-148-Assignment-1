"""
CSC148, Winter 2024
Assignment 1

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2022 Bogdan Simion, Diane Horton, Jacqueline Smith
"""
import datetime
from math import ceil
from typing import Optional
from bill import Bill
from call import Call

# Constants for the month-to-month contract monthly fee and term deposit
MTM_MONTHLY_FEE = 50.00
TERM_MONTHLY_FEE = 20.00
TERM_DEPOSIT = 300.00

# Constants for the included minutes and SMSs in the term contracts (per month)
TERM_MINS = 100

# Cost per minute and per SMS in the month-to-month contract
MTM_MINS_COST = 0.05

# Cost per minute and per SMS in the term contract
TERM_MINS_COST = 0.1

# Cost per minute and per SMS in the prepaid contract
PREPAID_MINS_COST = 0.025


class Contract:
    """ A contract for a phone line

    This class is not to be changed or instantiated. It is an Abstract Class.

    === Public Attributes ===
    start:
         starting date for the contract
    bill:
         bill for this contract for the last month of call records loaded from
         the input dataset
    """
    start: datetime.date
    bill: Optional[Bill]

    def __init__(self, start: datetime.date) -> None:
        """ Create a new Contract with the <start> date, starts as inactive
        """
        self.start = start
        self.bill = None

    def new_month(self, month: int, year: int, bill: Bill) -> None:
        """ A new month has begun corresponding to <month> and <year>.
        This may be the first month of the contract.
        Store the <bill> argument in this contract and set the appropriate rate
        per minute and fixed cost.

        DO NOT CHANGE THIS METHOD
        """
        raise NotImplementedError

    def bill_call(self, call: Call) -> None:
        """ Add the <call> to the bill.

        Precondition:
        - a bill has already been created for the month+year when the <call>
        was made. In other words, you can safely assume that self.bill has been
        already advanced to the right month+year.
        """
        self.bill.add_billed_minutes(ceil(call.duration / 60.0))

    def cancel_contract(self) -> float:
        """ Return the amount owed in order to close the phone line associated
        with this contract.

        Precondition:
        - a bill has already been created for the month+year when this contract
        is being cancelled. In other words, you can safely assume that self.bill
        exists for the right month+year when the cancelation is requested.
        """
        self.start = None
        return self.bill.get_cost()


class TermContract(Contract):
    """ A Term contract for a phone line

        === Attributes ===
        start:
             starting date for the contract
        enddate:
            ending date for the contract
        currentdate:
            the date of the current month
        bill:
             bill for this contract for the last month of call records loaded
             the input dataset
        freeminutes:
            number of free calling minutes
        """
    start: datetime.datetime
    enddate: datetime.datetime
    currentdate: tuple[int, int]
    bill: Optional[Bill]
    termdeposit: float
    freemintues: int

    def __init__(self, start: datetime.datetime,
                 end: datetime.datetime) -> None:
        """ Create a new TermContract with the <start> date, starts as inactive
        """
        super().__init__(start)
        self.enddate = end
        self.termdeposit = TERM_DEPOSIT

    def new_month(self, month: int, year: int, bill: Bill) -> None:
        """ Advance to a new month in the contract, corresponding to <month> and
        <year>. This may be the first month of the contract.
        Store the <bill> argument in this contract and set the appropriate rate
        per minute and fixed cost.
        """
        self.bill = bill
        self.bill.set_rates("TERM", TERM_MINS_COST)
        if year == self.start.year and month == self.start.month:
            self.bill.add_fixed_cost(self.termdeposit)
        self.freemintues = TERM_MINS
        self.currentdate = (month, year)
        self.bill.free_min = 0
        self.bill.add_fixed_cost(TERM_MONTHLY_FEE)

    def bill_call(self, call: Call) -> None:
        """ Add the <call> to the bill.

        Precondition:
        - a bill has already been created for the month+year when the <call>
        was made. In other words, you can safely assume that self.bill has been
        already advanced to the right month+year.
        """
        mins = ceil(call.duration / 60.0)
        if mins > self.freemintues > 0:
            self.freemintues = 0
            self.bill.add_billed_minutes(mins - self.freemintues)
            self.bill.add_free_minutes(self.freemintues)
        elif self.freemintues >= mins:
            self.freemintues -= mins
            self.bill.add_free_minutes(mins)
        else:
            self.bill.add_billed_minutes(mins)

    def cancel_contract(self) -> float:
        """ Return the amount owed in order to close the phone line associated
        with this contract.

        Precondition:
        - a bill has already been created for the month+year when this contract
        is being cancelled. In other words, you can safely assume that self.bill
        exists for the right month+year when the cancelation is requested.
        """
        if self.currentdate > (self.enddate.month, self.enddate.year):
            self.bill.add_fixed_cost(-self.termdeposit)
        else:
            pass
        return self.bill.get_cost()


class MTMContract(Contract):
    """ A Month-to-Month contract for a phone line

        === Attributes ===
        start:
             starting date for the contract.
        bill:
             bill for this contract for the last month of call records loaded
             the input dataset.
        """
    start: datetime.datetime
    bill: Optional[Bill]

    def __init__(self, start: datetime.datetime) -> None:
        """ Create a new MTMContract with the <start> date, starts as inactive
        """
        super().__init__(start)

    def new_month(self, month: int, year: int, bill: Bill) -> None:
        """ Advance to a new month in the contract, corresponding to <month> and
        <year>. This may be the first month of the contract.
        Store the <bill> argument in this contract and set the appropriate rate
        per minute and fixed cost.
        """
        self.bill = bill
        self.bill.set_rates("MTM", MTM_MINS_COST)
        self.bill.add_fixed_cost(MTM_MONTHLY_FEE)


class PrepaidContract(Contract):
    """
    A pre-paid contract for a phoneline

    There are several conditions for this contract:
    - The contract is initialized with bill credits
    - Every month, if credit amount falls below 10,
      the contract will automatically add 25 credits
    - If contract contains negative credits, then
      cancelling the contract will bill the customer
      for these remaining credits

    === Attributes ===
    start:
         Starting date for the contract.
    bill:
         Bill for this contract for the last month of call records loaded from
         the input dataset.
    balance:
        The amount of credits that this contract has left.
    """

    start: datetime.datetime
    balance: float
    bill: Optional[Bill]

    def __init__(self, start: datetime.datetime, balance: float) -> None:
        """ Create a new PrepaidContract with the <start> date, starts as inact
        """
        super().__init__(start)
        self.balance = -balance

    def new_month(self, month: int, year: int, bill: Bill) -> None:
        """ Advance to a new month in the contract, corresponding to <month> and
        <year>. This may be the first month of the contract.
        Store the <bill> argument in this contract and set the appropriate rate
        per minute and fixed cost.
        """
        self.bill = bill
        if self.balance > -10:
            self.balance = self.balance - 25
        self.bill.add_fixed_cost(self.balance)
        self.bill.set_rates("PREPAID", PREPAID_MINS_COST)

    def bill_call(self, call: Call) -> None:
        """ Add the <call> to the bill.

        Precondition:
        - a bill has already been created for the month+year when the <call>
        was made. In other words, you can safely assume that self.bill has been
        already advanced to the right month+year.
        """
        temp = call.duration / 60.0
        self.bill.add_billed_minutes(ceil(temp))
        self.balance += ceil(temp) * PREPAID_MINS_COST

    def cancel_contract(self) -> float:
        """ Return the amount owed in order to close the phone line associated
        with this contract.

        Precondition:
        - a bill has already been created for the month+year when this contract
        is being cancelled. In other words, you can safely assume that self.bill
        exists for the right month+year when the cancelation is requested.
        """
        return self.balance if self.balance >= 0 else 0.0


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'allowed-import-modules': [
            'python_ta', 'typing', 'datetime', 'bill', 'call', 'math'
        ],
        'disable': ['R0902', 'R0913'],
        'generated-members': 'pygame.*'
    })
