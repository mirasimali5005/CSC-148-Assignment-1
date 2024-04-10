# CSC-148-Assignment-1
A1 Documentation
The Contract class serves as the foundation for various customer contract types, having common functionalities and properties essential for managing contracts. The TermContract subclass is tailored for fixed-term agreements, mainly for handling deposits and o=ering potential free minutes. The MTMContract subclass supports month-to-month agreements, providing flexibility with standard monthly charges and additional call fees. Lastly, the PrepaidContract subclass caters to users preferring to pay upfront, monitoring and managing credit balances with a focus on prepayment. Each subclass inherit the base Contract functionalities to fit their specific contract type requirements.
TermContract:
The TermContract class is a part of the Contract class. The TermContract class handles contracts that last for a set amount of time and includes details such as how much money to put down at the start and how many free minutes the customer gets. This class takes care of the money put down at the start, gives out the free minutes, and looks after the monthly fees. The class details the monthly evolution of contracts, including how call durations are deducted from free minutes and the calculation of final charges upon contract termination. This is important for dealing with the initial deposit if the contract is canceled.
These are the methods for the TermContract class:
1. The initializer
2. The new_month method
3. The bill_call method
4. The cancel_contract method
These are the attributes for the TermContract class:
1. Start:startingdateforthecontract
2. Enddate:endingdateforthecontract
  
3. Currentdate:thedateofthelatestmonththatisadded 4. Bill:thebillforthiscontractforthelastmonth
5. Freeminutes:numberoffreecallingminutes
These are the attribute types of the TermContract class: 1. Start:datetime.datetime
2. Enddate:datetime.datetime
3. Currentdate:tuple[int,int]
4. Bill:Optional[Bill] 5. Freeminutes:int 6. Termdeposit:float
These are the representation invariants for the TermContract class: 1. Termdeposit>=0
2. Start>currentdate>enddate
3. Freeminutes>0
Methods for TermContract class:
1) The Initializer:
The initializer creates a new term contract with the <start> date. The initializer inherits start from using super() from the parent class and also initializes self.enddate as end and self.termdeposit as TERM_DEPOSIT
2) The new_month method:
Overview:
The method updates the contract status for the new month, indicated by <month> and <year>. The method records the <bill> for this period, setting the rates for calls and the standard monthly fee. The method requires inputs for the month and year, both as integers, and accepts a bill object. The method does not return anything but changes the self.bills data. With the arrival of the new month, the method assigns the values to <current_month> and <current_year>. The term_deposit will be added to the bill, if this is the first month of the term_contract
    
Implementation:
The new_month method in the TermContract class updates the billing information when a new month begins, designated by <month> and <year>. This method may mark the start of the contract. The method processes the <bill> parameter, setting the rates for calls at TERM_MINUTES and the standard monthly charge, TERM_MONTHLY_FEE. This method accepts integers for both the month and year, along with a Bill object. The method does not provide a return value but instead updates the self.bills attribute. When a new month commences, <current_month> and <current_year> are recorded as the specified month and year. If this period signifies the inaugural month of the TermContract, the TERM_DEPOSIT is then included in the bill.
3) The bill_call method:
Overview:
The bill_call method charges for a particular call. The method requires a Call object as input and adds the charge for this call to the existing bill. Before using this method, there should already be a bill set up for the same month and year as the call. This ensures that the billing information is up to date when the call charges are added.
Implementation:
This method calculates the duration of a call and determines whether the duration of the call falls under free minutes or should be billed. The call's duration is converted from seconds to the nearest whole minute if needed. If the duration is less than or equal to the available free minutes, the method subtracts from the free minutes and logs the call as such. Should the duration exceed the free minutes, the method sets the remaining free minutes to zero, charges for the additional minutes, and updates the bill to reflect these changes.
    
4) The cancel_contract method:
Overview:
The cancel_contract method calculates the total amount a client must pay to end their contract. The method gives back a number with decimals (a float) that tells the total amount due, including any last costs tied to how the contract was used. If a client stops the contract after the set date, they will get back the full deposit they put in at the start. This method expects that there's already a bill for the month and year when the contract is getting cancelled. This means the bill for the right time should be ready before someone asks to end the contract.
Implementation:
When terminating a phone contract, this method computes the total amount due. Verifying whether the contract is ending after its designated end date and, if so, an initial deposit was made, it deducts this deposit from the owed amount. The method then sums all charges on the bill, including any calls exceeding the allotted free minutes, and provides the total amount due.
   
MTMContract:
The MTMContract, a subclass of the Contract class, handles month-to-month phone contracts. This class focuses on the monthly billing cycle and its related charges. The class helps keep track of monthly bills, which includes a fixed monthly fee plus additional charges based on call usage. The class also describes how to move contracts from one month to the next and figures out the total amount due if the contract is cancelled. Additionally, the class inherits the bill_call and cancel_contract methods from classes’ parent class.
These are the methods for MTMContract class: 1. Theinitializer
2. Thenew_monthmethod
These are the attributes for MTMContract class:
1. Start:thestartingdateforthecontract
2. Bill:thebillforthiscontractforthelastmonth
These are the attribute types for MTMContract class: 1. Start:datetime.datetime
2. Bill:Optional[bill]
Methods for MTMContract:
1) The initializer:
The initializer method creates a new MTMContract with a specified <start>
and inherits the start attribute from the parent Contract class.
   
2) The new_month method:
Overview:
When the MTMContract enters a new month, marked by <month> and <year>, this method updates the contract's billing details. The method saves the <bill> information, establishing the rates for calls and a set monthly cost. Accepting the month and year as numbers, and the bill as a bill object, the method modifies the self.bills without returning any data, setting the current_month and current_year to the specified month and year.
Implementation:
In the implementation of the new_month method within the MTMContract, the method updates the billing details to account for a new month, referencing the specified month and year. This method also incorporates the fixed monthly fee into the billing summary. Additionally, this method accepts a billing object to adjust with the latest charges. It ensures the billing in the contract reflects the updated charges for the new month, although it does not return any specific value.
3) The bill_call method:
Overview:
The bill_call method is inherited from the parent class when the contract is first set up. This method is used to calculate charges for a call and update the bill accordingly. The method does not return a value, only changes the bill in the contract to show the new charges for calls made.
Implementation:
In the MTMContract, the bill_call method is not specifically used; the method is directly inherited from the parent class. This means the method is available for use in MTMContract without needing to be redefined.
      
4) The cancel_contract:
Overview:
The cancel_contract method, like the bill_call method, is inherited from the parent class upon the initialization of the contract. This method is utilized to finalize the account when the contract is terminated. The method calculates any remaining charges and refunds any deposits, if applicable. The method does not return a value but updates the contract's billing information to reflect the closure.
Implementation:
Implementation: For the MTMContract, the cancel_contract method is not uniquely implemented within the class; it is inherited from the parent class. Consequently, this method is accessible within MTMContract and functions according to the behavior defined in the parent class without modification.
   
PrePaid contract:
The PrepaidContract class, a subclass of the Contract class, manages phone services paid for in advance by customers. Instead of monthly billing after use, this class deducts charges from the prepaid credits. The class monitors the balance and adds more credits automatically when the balance is low. The class also takes care of charging for calls and applies monthly charges. When the contract ends, the class handles refunds for any unused credits or charges for additional usage.
These are the methods for PrePaid class: 1. Theinitializer
2. Thenew_monthmethod
3. Thebill_callmethod
4. Thecancel_contractmethod
These are the attributes for PrePaid class:
1. Start:thestartingdateforthecontract
2. Bill:thebillforthiscontractforthelastmonth
3. Balance:theamountofcreditsthatthiscontracthasleft
These are the attribute types for PrePaid class: 1. Start:datetime.datetime
2. Bill:Optional[Bill]
3. Balance:float
Methods for PrePaid:
1) The initializer method:
The initializer method for the PrepaidContract class sets up a new contract beginning from a specific start date. This method receives the starting attributes from its parent class, Contract, and sets up the initial credit balance for the account.
   
2) The new_month method:
Overview:
The new_month method is designed to progress the state of a contract into a subsequent month while updating associated billing details. The method requires three pieces of information: the month, year, and a Bill object that will represent the financial activity for that month. The method does not produce a return value but is important to maintain accurate and current billing records as time advances.
Implementation:
When the new_month function is used, the method brings the contract's billing up to the present month, reducing the balance by any set monthly costs. If the balance goes too low, the method adds more money to it. This keeps the account in good standing for the new month.
3) The bill_call method:
Overview:
The bill_call method is designed to calculate the billing for individual phone calls. The method accepts a call object as input and updates the bill with the call cost. This method presumes that a bill corresponding to the month and year of the call already exists; hence, operating on the assumption that self.bill is correct for the current month and year.
Implementation:
For prepaid contracts, the bill_call method starts by converting the call duration from seconds to the nearest whole minute. The method then computes the call's cost using the contract's per-minute rate and deducts this amount from the prepaid balance. The cost is also added to the bill. This ensures the billing accurately reflects the duration and cost of the calls, while the prepaid balance is adjusted to represent the call charges.
      
4) The cancel_contract method:
Overview:
The interface for the cancel_contract method in the PrepaidContract class is designed to assess the final balance at the end of a contract. This method does not need any input parameters because the method operates based on the existing balance within the contract. The goal is to figure out if money should be returned to the client or if there's a remaining balance that the client needs to pay. The outcome is provided as a number with decimal places (float), reflecting either the refund due to the client or the additional amount the client owes when the contract is finished. This method ensures that the financial aspect of the contract is concluded correctly.
Implementation:
Upon the termination of the contract, the method examines if there are leftover credits in the account. If there is a positive balance, the method arranges for the return of these unused credits. If the balance is negative, showing that the service was used more than what was prepaid for, the method works out the total amount that should be paid back. This ensures the final bill reflects the accurate use of the service.
   
