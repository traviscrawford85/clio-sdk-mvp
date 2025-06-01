from typing import Optional

from sqlalchemy import REAL, Index, Integer, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Activities(Base):
    __tablename__ = 'Activities'
    __table_args__ = (
        Index('IX_Activities_ID', 'ID'),
        Index('IX_Activities_Type', 'Type')
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Billed: Mapped[int] = mapped_column(Integer)
    Contingency_Fee: Mapped[int] = mapped_column(Integer)
    Flat_Rate: Mapped[int] = mapped_column(Integer)
    Non_Billable: Mapped[int] = mapped_column(Integer)
    No_Charge: Mapped[int] = mapped_column(Integer)
    Price: Mapped[str] = mapped_column(Text)
    Type: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Activity_Description: Mapped[Optional[int]] = mapped_column(Integer)
    Bill: Mapped[Optional[int]] = mapped_column(Integer)
    Calendar_Entry: Mapped[Optional[int]] = mapped_column(Integer)
    Communication: Mapped[Optional[int]] = mapped_column(Integer)
    Contact_Note: Mapped[Optional[int]] = mapped_column(Integer)
    Date: Mapped[Optional[str]] = mapped_column(Text)
    Document_Version: Mapped[Optional[int]] = mapped_column(Integer)
    Expense_Category: Mapped[Optional[int]] = mapped_column(Integer)
    Matter: Mapped[Optional[int]] = mapped_column(Integer)
    Matter_Note: Mapped[Optional[int]] = mapped_column(Integer)
    Note: Mapped[Optional[str]] = mapped_column(Text)
    Quantity: Mapped[Optional[str]] = mapped_column(Text)
    Quantity_In_Hours: Mapped[Optional[str]] = mapped_column(Text)
    Reference: Mapped[Optional[str]] = mapped_column(Text)
    Rounded_Quantity: Mapped[Optional[str]] = mapped_column(Text)
    Rounded_Quantity_In_Hours: Mapped[Optional[str]] = mapped_column(Text)
    Subject: Mapped[Optional[int]] = mapped_column(Integer)
    Task: Mapped[Optional[int]] = mapped_column(Integer)
    Timer: Mapped[Optional[int]] = mapped_column(Integer)
    Total: Mapped[Optional[str]] = mapped_column(Text)
    User: Mapped[Optional[int]] = mapped_column(Integer)
    Utbms_Expense: Mapped[Optional[int]] = mapped_column(Integer)
    Vendor: Mapped[Optional[int]] = mapped_column(Integer)


class ActivityDescriptions(Base):
    __tablename__ = 'ActivityDescriptions'
    __table_args__ = (
        Index('IX_ActivityDescriptions_Accessible_To_User', 'Accessible_To_User'),
        Index('IX_ActivityDescriptions_ID', 'ID')
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Accessible_To_User: Mapped[int] = mapped_column(Integer)
    Default: Mapped[int] = mapped_column(Integer)
    Visible_To_Co_Counsel: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)
    Utbms_Activity: Mapped[Optional[int]] = mapped_column(Integer)
    Utbms_Activity_Id: Mapped[Optional[int]] = mapped_column(Integer)
    Utbms_Task: Mapped[Optional[int]] = mapped_column(Integer)
    Utbms_Task_Id: Mapped[Optional[int]] = mapped_column(Integer)


class ActivityRates(Base):
    __tablename__ = 'ActivityRates'
    __table_args__ = (
        Index('IX_ActivityRates_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Flat_Rate: Mapped[int] = mapped_column(Integer)
    Rate: Mapped[str] = mapped_column(Text)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Co_Counsel_Contact_Id: Mapped[Optional[int]] = mapped_column(Integer)
    Group: Mapped[Optional[int]] = mapped_column(Integer)
    User: Mapped[Optional[int]] = mapped_column(Integer)


class Allocations(Base):
    __tablename__ = 'Allocations'
    __table_args__ = (
        Index('IX_Allocations_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Amount: Mapped[str] = mapped_column(Text)
    Has_Online_Payment: Mapped[int] = mapped_column(Integer)
    Interest: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Bill: Mapped[Optional[int]] = mapped_column(Integer)
    Contact: Mapped[Optional[int]] = mapped_column(Integer)
    Date: Mapped[Optional[str]] = mapped_column(Text)
    Description: Mapped[Optional[str]] = mapped_column(Text)
    Destination_Bank_Account: Mapped[Optional[int]] = mapped_column(Integer)
    Matter: Mapped[Optional[int]] = mapped_column(Integer)
    Parent: Mapped[Optional[int]] = mapped_column(Integer)
    Source_Bank_Account: Mapped[Optional[int]] = mapped_column(Integer)
    Voided_At: Mapped[Optional[str]] = mapped_column(Text)


class BankAccounts(Base):
    __tablename__ = 'BankAccounts'
    __table_args__ = (
        Index('IX_BankAccounts_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Balance: Mapped[str] = mapped_column(Text)
    Default_Account: Mapped[int] = mapped_column(Integer)
    Type: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Account_Number: Mapped[Optional[str]] = mapped_column(Text)
    Clio_Payment_Page_Link: Mapped[Optional[str]] = mapped_column(Text)
    Clio_Payments_Merchant_Account_Mapping: Mapped[Optional[int]] = mapped_column(Integer)
    Currency: Mapped[Optional[str]] = mapped_column(Text)
    Domicile_Branch: Mapped[Optional[str]] = mapped_column(Text)
    General_Ledger_Number: Mapped[Optional[str]] = mapped_column(Text)
    Holder: Mapped[Optional[str]] = mapped_column(Text)
    Institution: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)
    Swift: Mapped[Optional[str]] = mapped_column(Text)
    Transit_Number: Mapped[Optional[str]] = mapped_column(Text)
    User: Mapped[Optional[int]] = mapped_column(Integer)


class BankTransactions(Base):
    __tablename__ = 'BankTransactions'
    __table_args__ = (
        Index('IX_BankTransactions_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Amount: Mapped[str] = mapped_column(Text)
    Clio_Payments_Transaction: Mapped[int] = mapped_column(Integer)
    Date: Mapped[str] = mapped_column(Text)
    Funds_In: Mapped[str] = mapped_column(Text)
    Funds_Out: Mapped[str] = mapped_column(Text)
    Type: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Allocation: Mapped[Optional[int]] = mapped_column(Integer)
    Bank_Account: Mapped[Optional[int]] = mapped_column(Integer)
    Bill: Mapped[Optional[int]] = mapped_column(Integer)
    Client: Mapped[Optional[int]] = mapped_column(Integer)
    Confirmation: Mapped[Optional[str]] = mapped_column(Text)
    Currency: Mapped[Optional[str]] = mapped_column(Text)
    Description: Mapped[Optional[str]] = mapped_column(Text)
    Exchange_Rate: Mapped[Optional[str]] = mapped_column(Text)
    Matter: Mapped[Optional[int]] = mapped_column(Integer)
    Source: Mapped[Optional[str]] = mapped_column(Text)
    Transaction_Type: Mapped[Optional[str]] = mapped_column(Text)


class BankTransfers(Base):
    __tablename__ = 'BankTransfers'
    __table_args__ = (
        Index('IX_BankTransfers_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Amount: Mapped[str] = mapped_column(Text)
    Date: Mapped[str] = mapped_column(Text)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Client: Mapped[Optional[int]] = mapped_column(Integer)
    Description: Mapped[Optional[str]] = mapped_column(Text)
    Destination_Account: Mapped[Optional[int]] = mapped_column(Integer)
    Matter: Mapped[Optional[int]] = mapped_column(Integer)
    Source_Account: Mapped[Optional[int]] = mapped_column(Integer)


class BillThemes(Base):
    __tablename__ = 'BillThemes'
    __table_args__ = (
        Index('IX_BillThemes_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Account_Id: Mapped[int] = mapped_column(Integer)
    Default: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)


class Bills(Base):
    __tablename__ = 'Bills'
    __table_args__ = (
        Index('IX_Bills_Client', 'Client'),
        Index('IX_Bills_ID', 'ID')
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Balance: Mapped[str] = mapped_column(Text)
    Can_Update: Mapped[int] = mapped_column(Integer)
    Credits_Issued: Mapped[str] = mapped_column(Text)
    Due: Mapped[str] = mapped_column(Text)
    Due_At: Mapped[str] = mapped_column(Text)
    Issued_At: Mapped[str] = mapped_column(Text)
    Kind: Mapped[int] = mapped_column(Integer)
    Paid: Mapped[str] = mapped_column(Text)
    Secondary_Tax_Rate: Mapped[str] = mapped_column(Text)
    Secondary_Tax_Sum: Mapped[str] = mapped_column(Text)
    Shared: Mapped[int] = mapped_column(Integer)
    State: Mapped[int] = mapped_column(Integer)
    Sub_Total: Mapped[str] = mapped_column(Text)
    Tax_Rate: Mapped[str] = mapped_column(Text)
    Tax_Sum: Mapped[str] = mapped_column(Text)
    Total: Mapped[str] = mapped_column(Text)
    Type: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Bill_Theme: Mapped[Optional[int]] = mapped_column(Integer)
    Client: Mapped[Optional[int]] = mapped_column(Integer)
    Currency: Mapped[Optional[int]] = mapped_column(Integer)
    Destination_Account: Mapped[Optional[int]] = mapped_column(Integer)
    End_At: Mapped[Optional[str]] = mapped_column(Text)
    Group: Mapped[Optional[int]] = mapped_column(Integer)
    Memo: Mapped[Optional[str]] = mapped_column(Text)
    Number: Mapped[Optional[str]] = mapped_column(Text)
    Original_Bill: Mapped[Optional[int]] = mapped_column(Integer)
    Paid_At: Mapped[Optional[str]] = mapped_column(Text)
    Purchase_Order: Mapped[Optional[str]] = mapped_column(Text)
    Start_At: Mapped[Optional[str]] = mapped_column(Text)
    Subject: Mapped[Optional[str]] = mapped_column(Text)
    User: Mapped[Optional[int]] = mapped_column(Integer)


class CalendarEntries(Base):
    __tablename__ = 'CalendarEntries'
    __table_args__ = (
        Index('IX_CalendarEntries_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    All_Day: Mapped[int] = mapped_column(Integer)
    Court_Rule: Mapped[int] = mapped_column(Integer)
    Permission: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Calendar_Owner: Mapped[Optional[int]] = mapped_column(Integer)
    Description: Mapped[Optional[str]] = mapped_column(Text)
    End_At: Mapped[Optional[str]] = mapped_column(Text)
    Location: Mapped[Optional[str]] = mapped_column(Text)
    Matter: Mapped[Optional[int]] = mapped_column(Integer)
    Matter_Docket: Mapped[Optional[int]] = mapped_column(Integer)
    Parent_Calendar_Entry: Mapped[Optional[int]] = mapped_column(Integer)
    Parent_Calendar_Entry_Id: Mapped[Optional[int]] = mapped_column(Integer)
    Recurrence_Rule: Mapped[Optional[str]] = mapped_column(Text)
    Start_At: Mapped[Optional[str]] = mapped_column(Text)
    Summary: Mapped[Optional[str]] = mapped_column(Text)


class Calendars(Base):
    __tablename__ = 'Calendars'
    __table_args__ = (
        Index('IX_Calendars_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Color: Mapped[int] = mapped_column(Integer)
    Court_Rules_Default_Calendar: Mapped[int] = mapped_column(Integer)
    Permission: Mapped[int] = mapped_column(Integer)
    Source: Mapped[int] = mapped_column(Integer)
    Type: Mapped[int] = mapped_column(Integer)
    Visible: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Creator: Mapped[Optional[int]] = mapped_column(Integer)
    Light_Color: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)


class Communications(Base):
    __tablename__ = 'Communications'
    __table_args__ = (
        Index('IX_Communications_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Type: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Body: Mapped[Optional[str]] = mapped_column(Text)
    Date: Mapped[Optional[str]] = mapped_column(Text)
    Matter: Mapped[Optional[int]] = mapped_column(Integer)
    Received_At: Mapped[Optional[str]] = mapped_column(Text)
    Subject: Mapped[Optional[str]] = mapped_column(Text)
    User: Mapped[Optional[int]] = mapped_column(Integer)


class ContactNotes(Base):
    __tablename__ = 'ContactNotes'
    __table_args__ = (
        Index('IX_ContactNotes_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Author: Mapped[Optional[int]] = mapped_column(Integer)
    Contact: Mapped[Optional[int]] = mapped_column(Integer)
    Date: Mapped[Optional[str]] = mapped_column(Text)
    Detail: Mapped[Optional[str]] = mapped_column(Text)
    Matter: Mapped[Optional[int]] = mapped_column(Integer)
    Subject: Mapped[Optional[str]] = mapped_column(Text)


class Contacts(Base):
    __tablename__ = 'Contacts'
    __table_args__ = (
        Index('IX_Contacts_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Type: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Avatar: Mapped[Optional[int]] = mapped_column(Integer)
    Clio_Connect_Email: Mapped[Optional[str]] = mapped_column(Text)
    Company: Mapped[Optional[int]] = mapped_column(Integer)
    First_Name: Mapped[Optional[str]] = mapped_column(Text)
    Folder: Mapped[Optional[int]] = mapped_column(Integer)
    Initials: Mapped[Optional[str]] = mapped_column(Text)
    Last_Name: Mapped[Optional[str]] = mapped_column(Text)
    Middle_Name: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)
    Payment_Profile: Mapped[Optional[int]] = mapped_column(Integer)
    Prefix: Mapped[Optional[str]] = mapped_column(Text)
    Primary_Email_Address: Mapped[Optional[str]] = mapped_column(Text)
    Primary_Phone_Number: Mapped[Optional[str]] = mapped_column(Text)
    Title: Mapped[Optional[str]] = mapped_column(Text)


class ConversationMessages(Base):
    __tablename__ = 'ConversationMessages'
    __table_args__ = (
        Index('IX_ConversationMessages_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Body: Mapped[Optional[str]] = mapped_column(Text)
    Conversation: Mapped[Optional[int]] = mapped_column(Integer)
    Document: Mapped[Optional[int]] = mapped_column(Integer)
    Sender: Mapped[Optional[int]] = mapped_column(Integer)


class Conversations(Base):
    __tablename__ = 'Conversations'
    __table_args__ = (
        Index('IX_Conversations_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    First_Message: Mapped[Optional[int]] = mapped_column(Integer)
    Last_Message: Mapped[Optional[int]] = mapped_column(Integer)
    Matter: Mapped[Optional[int]] = mapped_column(Integer)
    Subject: Mapped[Optional[str]] = mapped_column(Text)


class CreditCards(Base):
    __tablename__ = 'CreditCards'
    __table_args__ = (
        Index('IX_CreditCards_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Card_Type: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Account: Mapped[Optional[int]] = mapped_column(Integer)
    Contact: Mapped[Optional[int]] = mapped_column(Integer)
    Expiry_Month: Mapped[Optional[str]] = mapped_column(Text)
    Expiry_Year: Mapped[Optional[str]] = mapped_column(Text)
    Number: Mapped[Optional[str]] = mapped_column(Text)
    User: Mapped[Optional[int]] = mapped_column(Integer)


class CreditMemos(Base):
    __tablename__ = 'CreditMemos'
    __table_args__ = (
        Index('IX_CreditMemos_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Amount: Mapped[str] = mapped_column(Text)
    Discount: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Contact: Mapped[Optional[int]] = mapped_column(Integer)
    Date: Mapped[Optional[str]] = mapped_column(Text)
    Description: Mapped[Optional[str]] = mapped_column(Text)
    User: Mapped[Optional[int]] = mapped_column(Integer)
    Voided_At: Mapped[Optional[str]] = mapped_column(Text)


class Currencies(Base):
    __tablename__ = 'Currencies'
    __table_args__ = (
        Index('IX_Currencies_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Code: Mapped[Optional[str]] = mapped_column(Text)
    Sign: Mapped[Optional[str]] = mapped_column(Text)


class CustomActions(Base):
    __tablename__ = 'CustomActions'
    __table_args__ = (
        Index('IX_CustomActions_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    UI_Reference: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Label: Mapped[Optional[str]] = mapped_column(Text)
    Target_Url: Mapped[Optional[str]] = mapped_column(Text)


class CustomFieldSets(Base):
    __tablename__ = 'CustomFieldSets'
    __table_args__ = (
        Index('IX_CustomFieldSets_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Displayed: Mapped[int] = mapped_column(Integer)
    Parent_Type: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)


class CustomFields(Base):
    __tablename__ = 'CustomFields'
    __table_args__ = (
        Index('IX_CustomFields_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Deleted: Mapped[int] = mapped_column(Integer)
    Displayed: Mapped[int] = mapped_column(Integer)
    Field_Type: Mapped[int] = mapped_column(Integer)
    Parent_Type: Mapped[int] = mapped_column(Integer)
    Required: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Display_Order: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)


class DatabaseSettings(Base):
    __tablename__ = 'DatabaseSettings'

    Name: Mapped[str] = mapped_column(Text, primary_key=True)
    StringValue: Mapped[Optional[str]] = mapped_column(Text)
    LongValue: Mapped[Optional[int]] = mapped_column(Integer)
    DoubleValue: Mapped[Optional[float]] = mapped_column(REAL)
    DateValue: Mapped[Optional[str]] = mapped_column(Text)


class DocumentAutomations(Base):
    __tablename__ = 'DocumentAutomations'
    __table_args__ = (
        Index('IX_DocumentAutomations_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    State: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Document_Template: Mapped[Optional[int]] = mapped_column(Integer)
    FileName: Mapped[Optional[str]] = mapped_column(Text)
    Matter: Mapped[Optional[int]] = mapped_column(Integer)


class DocumentCategories(Base):
    __tablename__ = 'DocumentCategories'
    __table_args__ = (
        Index('IX_DocumentCategories_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)


class DocumentTemplates(Base):
    __tablename__ = 'DocumentTemplates'
    __table_args__ = (
        Index('IX_DocumentTemplates_Document_Category', 'Document_Category'),
        Index('IX_DocumentTemplates_ID', 'ID')
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Size: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Content_Type: Mapped[Optional[str]] = mapped_column(Text)
    Document_Category: Mapped[Optional[int]] = mapped_column(Integer)
    FileName: Mapped[Optional[str]] = mapped_column(Text)
    Last_Modified_By: Mapped[Optional[int]] = mapped_column(Integer)


class Documents(Base):
    __tablename__ = 'Documents'
    __table_args__ = (
        Index('IX_Documents_ID', 'ID'),
        Index('IX_Documents_Parent', 'Parent')
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Locked: Mapped[int] = mapped_column(Integer)
    Type: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Contact: Mapped[Optional[int]] = mapped_column(Integer)
    Creator: Mapped[Optional[int]] = mapped_column(Integer)
    Deleted_At: Mapped[Optional[str]] = mapped_column(Text)
    Document_Category: Mapped[Optional[int]] = mapped_column(Integer)
    Latest_Document_Version: Mapped[Optional[int]] = mapped_column(Integer)
    Matter: Mapped[Optional[int]] = mapped_column(Integer)
    Name: Mapped[Optional[str]] = mapped_column(Text)
    Parent: Mapped[Optional[int]] = mapped_column(Integer)
    Received_At: Mapped[Optional[str]] = mapped_column(Text)


class ExpenseCategories(Base):
    __tablename__ = 'ExpenseCategories'
    __table_args__ = (
        Index('IX_ExpenseCategories_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Accessible_To_User: Mapped[int] = mapped_column(Integer)
    Entry_Type: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)
    Rate: Mapped[Optional[str]] = mapped_column(Text)
    Utbms_Code: Mapped[Optional[int]] = mapped_column(Integer)
    Xero_Expense_Code: Mapped[Optional[str]] = mapped_column(Text)


class Folders(Base):
    __tablename__ = 'Folders'
    __table_args__ = (
        Index('IX_Folders_ID', 'ID'),
        Index('IX_Folders_Parent', 'Parent')
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Locked: Mapped[int] = mapped_column(Integer)
    Root: Mapped[int] = mapped_column(Integer)
    Type: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Contact: Mapped[Optional[int]] = mapped_column(Integer)
    Creator: Mapped[Optional[int]] = mapped_column(Integer)
    Deleted_At: Mapped[Optional[str]] = mapped_column(Text)
    Document_Category: Mapped[Optional[int]] = mapped_column(Integer)
    Matter: Mapped[Optional[int]] = mapped_column(Integer)
    Name: Mapped[Optional[str]] = mapped_column(Text)
    Parent: Mapped[Optional[int]] = mapped_column(Integer)


class Groups(Base):
    __tablename__ = 'Groups'
    __table_args__ = (
        Index('IX_Groups_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Type: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)


class LegalReference(Base):
    __tablename__ = 'LegalReference'

    Topic: Mapped[str] = mapped_column(Text)
    ID: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    Jurisdiction: Mapped[Optional[str]] = mapped_column(Text)
    Source: Mapped[Optional[str]] = mapped_column(Text)
    Content: Mapped[Optional[str]] = mapped_column(Text)


class LineItems(Base):
    __tablename__ = 'LineItems'
    __table_args__ = (
        Index('IX_LineItems_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Date: Mapped[str] = mapped_column(Text)
    Group_Ordering: Mapped[int] = mapped_column(Integer)
    Kind: Mapped[int] = mapped_column(Integer)
    Price: Mapped[str] = mapped_column(Text)
    Quantity: Mapped[str] = mapped_column(Text)
    Secondary_Tax: Mapped[str] = mapped_column(Text)
    Secondary_Taxable: Mapped[int] = mapped_column(Integer)
    Sub_Total: Mapped[str] = mapped_column(Text)
    Tax: Mapped[str] = mapped_column(Text)
    Taxable: Mapped[int] = mapped_column(Integer)
    Total: Mapped[str] = mapped_column(Text)
    Type: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Activity: Mapped[Optional[int]] = mapped_column(Integer)
    Bill: Mapped[Optional[int]] = mapped_column(Integer)
    Description: Mapped[Optional[str]] = mapped_column(Text)
    Matter: Mapped[Optional[int]] = mapped_column(Integer)
    Note: Mapped[Optional[str]] = mapped_column(Text)
    User: Mapped[Optional[int]] = mapped_column(Integer)


class MatterNotes(Base):
    __tablename__ = 'MatterNotes'
    __table_args__ = (
        Index('IX_MatterNotes_ID', 'ID'),
        Index('IX_MatterNotes_Matter', 'Matter')
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Author: Mapped[Optional[int]] = mapped_column(Integer)
    Contact: Mapped[Optional[int]] = mapped_column(Integer)
    Date: Mapped[Optional[str]] = mapped_column(Text)
    Detail: Mapped[Optional[str]] = mapped_column(Text)
    Matter: Mapped[Optional[int]] = mapped_column(Integer)
    Subject: Mapped[Optional[str]] = mapped_column(Text)


class Matters(Base):
    __tablename__ = 'Matters'
    __table_args__ = (
        Index('IX_Matters_Client', 'Client'),
        Index('IX_Matters_Description', 'Description'),
        Index('IX_Matters_ID', 'ID'),
        Index('IX_Matters_Status', 'Status')
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Billable: Mapped[int] = mapped_column(Integer)
    Billing_Method: Mapped[int] = mapped_column(Integer)
    Status: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Client: Mapped[Optional[int]] = mapped_column(Integer)
    Client_Reference: Mapped[Optional[str]] = mapped_column(Text)
    Close_Date: Mapped[Optional[str]] = mapped_column(Text)
    Contingency_Fee: Mapped[Optional[int]] = mapped_column(Integer)
    Custom_Number: Mapped[Optional[str]] = mapped_column(Text)
    Description: Mapped[Optional[str]] = mapped_column(Text)
    Display_Number: Mapped[Optional[str]] = mapped_column(Text)
    Folder: Mapped[Optional[int]] = mapped_column(Integer)
    Group: Mapped[Optional[int]] = mapped_column(Integer)
    Location: Mapped[Optional[str]] = mapped_column(Text)
    Maildrop_Address: Mapped[Optional[str]] = mapped_column(Text)
    Open_Date: Mapped[Optional[str]] = mapped_column(Text)
    Originating_Attorney: Mapped[Optional[int]] = mapped_column(Integer)
    Pending_Date: Mapped[Optional[str]] = mapped_column(Text)
    Practice_Area: Mapped[Optional[int]] = mapped_column(Integer)
    Responsible_Attorney: Mapped[Optional[int]] = mapped_column(Integer)


class PracticeAreas(Base):
    __tablename__ = 'PracticeAreas'
    __table_args__ = (
        Index('IX_PracticeAreas_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Code: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)


class Relationships(Base):
    __tablename__ = 'Relationships'
    __table_args__ = (
        Index('IX_Relationships_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Contact: Mapped[Optional[int]] = mapped_column(Integer)
    Description: Mapped[Optional[str]] = mapped_column(Text)
    Matter: Mapped[Optional[int]] = mapped_column(Integer)


class Reminders(Base):
    __tablename__ = 'Reminders'
    __table_args__ = (
        Index('IX_Reminders_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Duration: Mapped[int] = mapped_column(Integer)
    State: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Next_Delivery_At: Mapped[Optional[str]] = mapped_column(Text)
    Notification_Method: Mapped[Optional[int]] = mapped_column(Integer)
    Subject: Mapped[Optional[int]] = mapped_column(Integer)


class TableSettings(Base):
    __tablename__ = 'TableSettings'
    __table_args__ = (
        Index('IX_TableSettings_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    DateLastRefreshedUtc: Mapped[str] = mapped_column(Text)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    TableName: Mapped[Optional[str]] = mapped_column(Text)
    EventToken: Mapped[Optional[str]] = mapped_column(Text)


class TaskCalendars(Base):
    __tablename__ = 'TaskCalendars'
    __table_args__ = (
        Index('IX_TaskCalendars_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Color: Mapped[int] = mapped_column(Integer)
    Visible: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)


class TaskTemplateLists(Base):
    __tablename__ = 'TaskTemplateLists'
    __table_args__ = (
        Index('IX_TaskTemplateLists_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Creator: Mapped[Optional[int]] = mapped_column(Integer)
    Description: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)
    Practice_Area: Mapped[Optional[int]] = mapped_column(Integer)


class TaskTemplates(Base):
    __tablename__ = 'TaskTemplates'
    __table_args__ = (
        Index('IX_TaskTemplates_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Priority: Mapped[int] = mapped_column(Integer)
    Private: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Description: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)
    Task_Template_List: Mapped[Optional[int]] = mapped_column(Integer)
    Template_Creator: Mapped[Optional[int]] = mapped_column(Integer)


class TaskTypes(Base):
    __tablename__ = 'TaskTypes'
    __table_args__ = (
        Index('IX_TaskTypes_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Deleted_At: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)


class Tasks(Base):
    __tablename__ = 'Tasks'
    __table_args__ = (
        Index('IX_Tasks_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Notify_Completion: Mapped[int] = mapped_column(Integer)
    Priority: Mapped[int] = mapped_column(Integer)
    Status: Mapped[int] = mapped_column(Integer)
    Statute_Of_Limitations: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Assignee: Mapped[Optional[int]] = mapped_column(Integer)
    Assigner: Mapped[Optional[int]] = mapped_column(Integer)
    Completed_At: Mapped[Optional[str]] = mapped_column(Text)
    Description: Mapped[Optional[str]] = mapped_column(Text)
    Due_At: Mapped[Optional[str]] = mapped_column(Text)
    Matter: Mapped[Optional[int]] = mapped_column(Integer)
    Name: Mapped[Optional[str]] = mapped_column(Text)
    Task_Type: Mapped[Optional[int]] = mapped_column(Integer)


class TextSnippets(Base):
    __tablename__ = 'TextSnippets'
    __table_args__ = (
        Index('IX_TextSnippets_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Whole_Word: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Phrase: Mapped[Optional[str]] = mapped_column(Text)
    Snippet: Mapped[Optional[str]] = mapped_column(Text)


class Timers(Base):
    __tablename__ = 'Timers'
    __table_args__ = (
        Index('IX_Timers_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Elapsed_Time: Mapped[Optional[str]] = mapped_column(Text)
    Start_Time: Mapped[Optional[str]] = mapped_column(Text)


class UserInvitations(Base):
    __tablename__ = 'UserInvitations'
    __table_args__ = (
        Index('IX_UserInvitations_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Account_ID: Mapped[int] = mapped_column(Integer)
    User_Type: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    EMail: Mapped[Optional[str]] = mapped_column(Text)
    Message: Mapped[Optional[str]] = mapped_column(Text)
    UID: Mapped[Optional[int]] = mapped_column(Integer)


class UserRoles(Base):
    __tablename__ = 'UserRoles'
    __table_args__ = (
        Index('IX_UserRoles_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)


class UserTypes(Base):
    __tablename__ = 'UserTypes'
    __table_args__ = (
        Index('IX_UserTypes_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)


class Users(Base):
    __tablename__ = 'Users'
    __table_args__ = (
        Index('IX_Users_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    IsWhoAmI: Mapped[int] = mapped_column(Integer)
    Account_Owner: Mapped[int] = mapped_column(Integer)
    Clio_Connect: Mapped[int] = mapped_column(Integer)
    Court_Rules_Default_Attendee: Mapped[int] = mapped_column(Integer)
    Default_Calendar_Id: Mapped[int] = mapped_column(Integer)
    Enabled: Mapped[int] = mapped_column(Integer)
    Rate: Mapped[str] = mapped_column(Text)
    Subscription_Type: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Account: Mapped[Optional[int]] = mapped_column(Integer)
    Avatar: Mapped[Optional[int]] = mapped_column(Integer)
    Default_Activity_Description: Mapped[Optional[int]] = mapped_column(Integer)
    EMail: Mapped[Optional[str]] = mapped_column(Text)
    First_Name: Mapped[Optional[str]] = mapped_column(Text)
    Initials: Mapped[Optional[str]] = mapped_column(Text)
    Job_Title: Mapped[Optional[int]] = mapped_column(Integer)
    Last_Name: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)
    Phone_Number: Mapped[Optional[str]] = mapped_column(Text)
    Time_Zone: Mapped[Optional[str]] = mapped_column(Text)


class UtbmsCodes(Base):
    __tablename__ = 'UtbmsCodes'
    __table_args__ = (
        Index('IX_UtbmsCodes_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Type: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Code: Mapped[Optional[str]] = mapped_column(Text)
    Description: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)
    Utbms_Set_Id: Mapped[Optional[int]] = mapped_column(Integer)


class UtbmsSets(Base):
    __tablename__ = 'UtbmsSets'
    __table_args__ = (
        Index('IX_UtbmsSets_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Enabled: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Name: Mapped[Optional[str]] = mapped_column(Text)


class WebHooks(Base):
    __tablename__ = 'WebHooks'
    __table_args__ = (
        Index('IX_WebHooks_ID', 'ID'),
    )

    ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    Redacted: Mapped[int] = mapped_column(Integer)
    Model: Mapped[int] = mapped_column(Integer)
    Status: Mapped[int] = mapped_column(Integer)
    ETag: Mapped[Optional[str]] = mapped_column(Text)
    Created_At: Mapped[Optional[str]] = mapped_column(Text)
    Updated_At: Mapped[Optional[str]] = mapped_column(Text)
    JSON: Mapped[Optional[str]] = mapped_column(Text)
    Expires_At: Mapped[Optional[str]] = mapped_column(Text)
    Fields: Mapped[Optional[str]] = mapped_column(Text)
    Shared_Secret: Mapped[Optional[str]] = mapped_column(Text)
    Url: Mapped[Optional[str]] = mapped_column(Text)
    User: Mapped[Optional[int]] = mapped_column(Integer)
