# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T09:02:52+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, constr


class AccountHolderBalanceRequest(BaseModel):
    accountHolderCode: str = Field(
        ...,
        description='The code of the Account Holder of which to retrieve the balance.',
    )


class TransactionStatus(Enum):
    BalanceNotPaidOutTransfer = 'BalanceNotPaidOutTransfer'
    BalancePlatformSweep = 'BalancePlatformSweep'
    BalancePlatformSweepReturned = 'BalancePlatformSweepReturned'
    Chargeback = 'Chargeback'
    ChargebackCorrection = 'ChargebackCorrection'
    ChargebackCorrectionReceived = 'ChargebackCorrectionReceived'
    ChargebackReceived = 'ChargebackReceived'
    ChargebackReversed = 'ChargebackReversed'
    ChargebackReversedCorrection = 'ChargebackReversedCorrection'
    ChargebackReversedCorrectionReceived = 'ChargebackReversedCorrectionReceived'
    ChargebackReversedReceived = 'ChargebackReversedReceived'
    Converted = 'Converted'
    CreditClosed = 'CreditClosed'
    CreditFailed = 'CreditFailed'
    CreditReversed = 'CreditReversed'
    CreditReversedReceived = 'CreditReversedReceived'
    CreditSuspended = 'CreditSuspended'
    Credited = 'Credited'
    DebitFailed = 'DebitFailed'
    DebitReversedReceived = 'DebitReversedReceived'
    Debited = 'Debited'
    DebitedReversed = 'DebitedReversed'
    DepositCorrectionCredited = 'DepositCorrectionCredited'
    DepositCorrectionDebited = 'DepositCorrectionDebited'
    Fee = 'Fee'
    FundTransfer = 'FundTransfer'
    FundTransferReversed = 'FundTransferReversed'
    InvoiceDeductionCredited = 'InvoiceDeductionCredited'
    InvoiceDeductionDebited = 'InvoiceDeductionDebited'
    ManualCorrected = 'ManualCorrected'
    ManualCorrectionCredited = 'ManualCorrectionCredited'
    ManualCorrectionDebited = 'ManualCorrectionDebited'
    MerchantPayin = 'MerchantPayin'
    MerchantPayinReversed = 'MerchantPayinReversed'
    Payout = 'Payout'
    PayoutReversed = 'PayoutReversed'
    PendingCredit = 'PendingCredit'
    PendingDebit = 'PendingDebit'
    PendingFundTransfer = 'PendingFundTransfer'
    ReCredited = 'ReCredited'
    ReCreditedReceived = 'ReCreditedReceived'
    SecondChargeback = 'SecondChargeback'
    SecondChargebackCorrection = 'SecondChargebackCorrection'
    SecondChargebackCorrectionReceived = 'SecondChargebackCorrectionReceived'
    SecondChargebackReceived = 'SecondChargebackReceived'


class Amount(BaseModel):
    currency: constr(min_length=3, max_length=3) = Field(
        ...,
        description='The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes).',
    )
    value: int = Field(
        ...,
        description='The amount of the transaction, in [minor units](https://docs.adyen.com/development-resources/currency-codes).',
    )


class BankAccountDetail(BaseModel):
    accountNumber: Optional[str] = Field(
        None,
        description='The bank account number (without separators).\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.',
    )
    accountType: Optional[str] = Field(
        None,
        description='The type of bank account.\nOnly applicable to bank accounts held in the USA.\nThe permitted values are: `checking`, `savings`.\n\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.',
    )
    bankAccountName: Optional[str] = Field(
        None, description='The name of the bank account.'
    )
    bankAccountReference: Optional[str] = Field(
        None, description='Merchant reference to the bank account.'
    )
    bankAccountUUID: Optional[str] = Field(
        None,
        description='The unique identifier (UUID) of the Bank Account.\n>If, during an account holder create or update request, this field is left blank (but other fields provided), a new Bank Account will be created with a procedurally-generated UUID.\n\n>If, during an account holder create request, a UUID is provided, the creation of the Bank Account will fail while the creation of the account holder will continue.\n\n>If, during an account holder update request, a UUID that is not correlated with an existing Bank Account is provided, the update of the account holder will fail.\n\n>If, during an account holder update request, a UUID that is correlated with an existing Bank Account is provided, the existing Bank Account will be updated.\n',
    )
    bankBicSwift: Optional[str] = Field(
        None,
        description='The bank identifier code.\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.',
    )
    bankCity: Optional[str] = Field(
        None,
        description='The city in which the bank branch is located.\n\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.',
    )
    bankCode: Optional[str] = Field(
        None,
        description='The bank code of the banking institution with which the bank account is registered.\n\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.',
    )
    bankName: Optional[str] = Field(
        None,
        description='The name of the banking institution with which the bank account is held.\n\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.',
    )
    branchCode: Optional[str] = Field(
        None,
        description='The branch code of the branch under which the bank account is registered. The value to be specified in this parameter depends on the country of the bank account:\n* United States - Routing number\n* United Kingdom - Sort code\n* Germany - Bankleitzahl\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.',
    )
    checkCode: Optional[str] = Field(
        None,
        description='The check code of the bank account.\n\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.',
    )
    countryCode: Optional[str] = Field(
        None,
        description="The two-letter country code in which the bank account is registered.\n>The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').\n\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.",
    )
    currencyCode: Optional[str] = Field(
        None,
        description="The currency in which the bank account deals.\n>The permitted currency codes are defined in ISO-4217 (e.g. 'EUR').\n",
    )
    iban: Optional[str] = Field(
        None,
        description='The international bank account number.\n>The IBAN standard is defined in ISO-13616.\n\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.',
    )
    ownerCity: Optional[str] = Field(
        None,
        description='The city of residence of the bank account owner.\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.',
    )
    ownerCountryCode: Optional[str] = Field(
        None,
        description="The country code of the country of residence of the bank account owner.\n>The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').\n\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.",
    )
    ownerDateOfBirth: Optional[str] = Field(
        None,
        description='The date of birth of the bank account owner.\nThe date should be in ISO-8601 format yyyy-mm-dd (e.g. 2000-01-31).',
    )
    ownerHouseNumberOrName: Optional[str] = Field(
        None,
        description='The house name or number of the residence of the bank account owner.\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.',
    )
    ownerName: Optional[str] = Field(
        None,
        description='The name of the bank account owner.\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.',
    )
    ownerNationality: Optional[str] = Field(
        None,
        description="The country code of the country of nationality of the bank account owner.\n>The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. 'NL').\n\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.",
    )
    ownerPostalCode: Optional[str] = Field(
        None,
        description='The postal code of the residence of the bank account owner.\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.',
    )
    ownerState: Optional[str] = Field(
        None,
        description='The state of residence of the bank account owner.\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.',
    )
    ownerStreet: Optional[str] = Field(
        None,
        description='The street name of the residence of the bank account owner.\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.',
    )
    primaryAccount: Optional[bool] = Field(
        None, description='If set to true, the bank account is a primary account.'
    )
    taxId: Optional[str] = Field(
        None,
        description='The tax ID number.\n\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.',
    )
    urlForVerification: Optional[str] = Field(
        None,
        description='The URL to be used for bank account verification.\nThis may be generated on bank account creation.\n\n>Refer to [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information) for details on field requirements.',
    )


class DetailBalance(BaseModel):
    balance: Optional[List[Amount]] = Field(
        None, description='The list of balances held by the account.'
    )
    onHoldBalance: Optional[List[Amount]] = Field(
        None, description='The list of on hold balances held by the account.'
    )
    pendingBalance: Optional[List[Amount]] = Field(
        None, description='The list of pending balances held by the account.'
    )


class FieldName(Enum):
    accountCode = 'accountCode'
    accountHolderCode = 'accountHolderCode'
    accountHolderDetails = 'accountHolderDetails'
    accountNumber = 'accountNumber'
    accountStateType = 'accountStateType'
    accountStatus = 'accountStatus'
    accountType = 'accountType'
    address = 'address'
    balanceAccount = 'balanceAccount'
    balanceAccountActive = 'balanceAccountActive'
    balanceAccountCode = 'balanceAccountCode'
    balanceAccountId = 'balanceAccountId'
    bankAccount = 'bankAccount'
    bankAccountCode = 'bankAccountCode'
    bankAccountName = 'bankAccountName'
    bankAccountUUID = 'bankAccountUUID'
    bankBicSwift = 'bankBicSwift'
    bankCity = 'bankCity'
    bankCode = 'bankCode'
    bankName = 'bankName'
    bankStatement = 'bankStatement'
    branchCode = 'branchCode'
    businessContact = 'businessContact'
    cardToken = 'cardToken'
    checkCode = 'checkCode'
    city = 'city'
    companyRegistration = 'companyRegistration'
    constitutionalDocument = 'constitutionalDocument'
    controller = 'controller'
    country = 'country'
    countryCode = 'countryCode'
    currency = 'currency'
    currencyCode = 'currencyCode'
    dateOfBirth = 'dateOfBirth'
    description = 'description'
    destinationAccountCode = 'destinationAccountCode'
    document = 'document'
    documentContent = 'documentContent'
    documentExpirationDate = 'documentExpirationDate'
    documentIssuerCountry = 'documentIssuerCountry'
    documentIssuerState = 'documentIssuerState'
    documentName = 'documentName'
    documentNumber = 'documentNumber'
    documentType = 'documentType'
    doingBusinessAs = 'doingBusinessAs'
    drivingLicence = 'drivingLicence'
    drivingLicenceBack = 'drivingLicenceBack'
    drivingLicenceFront = 'drivingLicenceFront'
    drivingLicense = 'drivingLicense'
    email = 'email'
    firstName = 'firstName'
    formType = 'formType'
    fullPhoneNumber = 'fullPhoneNumber'
    gender = 'gender'
    hopWebserviceUser = 'hopWebserviceUser'
    houseNumberOrName = 'houseNumberOrName'
    iban = 'iban'
    idCard = 'idCard'
    idCardBack = 'idCardBack'
    idCardFront = 'idCardFront'
    idNumber = 'idNumber'
    identityDocument = 'identityDocument'
    individualDetails = 'individualDetails'
    infix = 'infix'
    jobTitle = 'jobTitle'
    lastName = 'lastName'
    lastReviewDate = 'lastReviewDate'
    legalArrangement = 'legalArrangement'
    legalArrangementCode = 'legalArrangementCode'
    legalArrangementEntity = 'legalArrangementEntity'
    legalArrangementEntityCode = 'legalArrangementEntityCode'
    legalArrangementLegalForm = 'legalArrangementLegalForm'
    legalArrangementMember = 'legalArrangementMember'
    legalArrangementMembers = 'legalArrangementMembers'
    legalArrangementName = 'legalArrangementName'
    legalArrangementReference = 'legalArrangementReference'
    legalArrangementRegistrationNumber = 'legalArrangementRegistrationNumber'
    legalArrangementTaxNumber = 'legalArrangementTaxNumber'
    legalArrangementType = 'legalArrangementType'
    legalBusinessName = 'legalBusinessName'
    legalEntity = 'legalEntity'
    legalEntityType = 'legalEntityType'
    logo = 'logo'
    merchantAccount = 'merchantAccount'
    merchantCategoryCode = 'merchantCategoryCode'
    merchantHouseNumber = 'merchantHouseNumber'
    merchantReference = 'merchantReference'
    microDeposit = 'microDeposit'
    name = 'name'
    nationality = 'nationality'
    originalReference = 'originalReference'
    ownerCity = 'ownerCity'
    ownerCountryCode = 'ownerCountryCode'
    ownerDateOfBirth = 'ownerDateOfBirth'
    ownerHouseNumberOrName = 'ownerHouseNumberOrName'
    ownerName = 'ownerName'
    ownerPostalCode = 'ownerPostalCode'
    ownerState = 'ownerState'
    ownerStreet = 'ownerStreet'
    passport = 'passport'
    passportNumber = 'passportNumber'
    payoutMethodCode = 'payoutMethodCode'
    payoutSchedule = 'payoutSchedule'
    pciSelfAssessment = 'pciSelfAssessment'
    personalData = 'personalData'
    phoneCountryCode = 'phoneCountryCode'
    phoneNumber = 'phoneNumber'
    postalCode = 'postalCode'
    primaryCurrency = 'primaryCurrency'
    reason = 'reason'
    registrationNumber = 'registrationNumber'
    returnUrl = 'returnUrl'
    schedule = 'schedule'
    shareholder = 'shareholder'
    shareholderCode = 'shareholderCode'
    shareholderCodeAndSignatoryCode = 'shareholderCodeAndSignatoryCode'
    shareholderCodeOrSignatoryCode = 'shareholderCodeOrSignatoryCode'
    shareholderType = 'shareholderType'
    shareholderTypes = 'shareholderTypes'
    shopperInteraction = 'shopperInteraction'
    signatory = 'signatory'
    signatoryCode = 'signatoryCode'
    socialSecurityNumber = 'socialSecurityNumber'
    sourceAccountCode = 'sourceAccountCode'
    splitAccount = 'splitAccount'
    splitConfigurationUUID = 'splitConfigurationUUID'
    splitCurrency = 'splitCurrency'
    splitValue = 'splitValue'
    splits = 'splits'
    stateOrProvince = 'stateOrProvince'
    status = 'status'
    stockExchange = 'stockExchange'
    stockNumber = 'stockNumber'
    stockTicker = 'stockTicker'
    store = 'store'
    storeDetail = 'storeDetail'
    storeName = 'storeName'
    storeReference = 'storeReference'
    street = 'street'
    taxId = 'taxId'
    tier = 'tier'
    tierNumber = 'tierNumber'
    transferCode = 'transferCode'
    ultimateParentCompany = 'ultimateParentCompany'
    ultimateParentCompanyAddressDetails = 'ultimateParentCompanyAddressDetails'
    ultimateParentCompanyAddressDetailsCountry = (
        'ultimateParentCompanyAddressDetailsCountry'
    )
    ultimateParentCompanyBusinessDetails = 'ultimateParentCompanyBusinessDetails'
    ultimateParentCompanyBusinessDetailsLegalBusinessName = (
        'ultimateParentCompanyBusinessDetailsLegalBusinessName'
    )
    ultimateParentCompanyBusinessDetailsRegistrationNumber = (
        'ultimateParentCompanyBusinessDetailsRegistrationNumber'
    )
    ultimateParentCompanyCode = 'ultimateParentCompanyCode'
    ultimateParentCompanyStockExchange = 'ultimateParentCompanyStockExchange'
    ultimateParentCompanyStockNumber = 'ultimateParentCompanyStockNumber'
    ultimateParentCompanyStockNumberOrStockTicker = (
        'ultimateParentCompanyStockNumberOrStockTicker'
    )
    ultimateParentCompanyStockTicker = 'ultimateParentCompanyStockTicker'
    unknown = 'unknown'
    value = 'value'
    verificationType = 'verificationType'
    virtualAccount = 'virtualAccount'
    visaNumber = 'visaNumber'
    webAddress = 'webAddress'
    year = 'year'


class FieldType(BaseModel):
    field: Optional[str] = Field(None, description='The full name of the property.')
    fieldName: Optional[FieldName] = Field(None, description='The type of the field.')
    shareholderCode: Optional[str] = Field(
        None,
        description='The code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.',
    )


class PayoutSpeed(Enum):
    INSTANT = 'INSTANT'
    SAME_DAY = 'SAME_DAY'
    STANDARD = 'STANDARD'


class PayoutAccountHolderRequest(BaseModel):
    accountCode: str = Field(
        ..., description='The code of the account from which the payout is to be made.'
    )
    accountHolderCode: str = Field(
        ...,
        description='The code of the Account Holder who owns the account from which the payout is to be made.\nThe Account Holder is the party to which the payout will be made.',
    )
    amount: Optional[Amount] = Field(
        None,
        description='An object containing the currency and value of the payout.\nIf the account has multiple currencies, specify the currency to be used.\nIf the `bankAccountUUID` is provided in the request, the currency supported by the bank is used.\nIf the `payoutMethodCode` is provided in the request, the specified payout method is selected.',
    )
    bankAccountUUID: Optional[str] = Field(
        None,
        description='The unique ID of the Bank Account held by the Account Holder to which the payout is to be made.\nIf left blank, a bank account is automatically selected.',
    )
    description: Optional[constr(max_length=200)] = Field(
        None,
        description='A description of the payout. Maximum 200 characters.\nAllowed: **abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/?:().,\'+ ";**',
    )
    merchantReference: Optional[str] = Field(
        None,
        description='A value that can be supplied at the discretion of the executing user in order to link multiple transactions to one another.',
    )
    payoutMethodCode: Optional[str] = Field(
        None,
        description='The unique ID of the payout method held by the Account Holder to which the payout is to be made.\nIf left blank, a payout instrument is automatically selected.',
    )
    payoutSpeed: Optional[PayoutSpeed] = Field(
        'STANDARD',
        description='Speed with which payouts for this account are processed. Permitted values: `STANDARD`, `SAME_DAY`.',
    )


class RefundFundsTransferRequest(BaseModel):
    amount: Amount = Field(..., description='The amount to be transferred.')
    merchantReference: Optional[str] = Field(
        None,
        description='A value that can be supplied at the discretion of the executing user in order to link multiple transactions to one another.',
    )
    originalReference: str = Field(
        ..., description='A PSP reference of the original fund transfer.'
    )


class RefundNotPaidOutTransfersRequest(BaseModel):
    accountCode: str = Field(
        ..., description='The code of the account from which to perform the refund(s).'
    )
    accountHolderCode: str = Field(
        ...,
        description='The code of the Account Holder which owns the account from which to perform the refund(s).',
    )


class ServiceError(BaseModel):
    errorCode: Optional[str] = Field(
        None, description='The error code mapped to the error message.'
    )
    errorType: Optional[str] = Field(None, description='The category of the error.')
    message: Optional[str] = Field(
        None, description='A short explanation of the issue.'
    )
    pspReference: Optional[str] = Field(
        None, description='The PSP reference of the payment.'
    )
    status: Optional[int] = Field(None, description='The HTTP response status.')


class SetupBeneficiaryRequest(BaseModel):
    destinationAccountCode: str = Field(
        ..., description='The destination account code.'
    )
    merchantReference: Optional[str] = Field(
        None,
        description='A value that can be supplied at the discretion of the executing user.',
    )
    sourceAccountCode: str = Field(..., description='The benefactor account.')


class Type(Enum):
    BalanceAccount = 'BalanceAccount'
    Commission = 'Commission'
    Default = 'Default'
    MarketPlace = 'MarketPlace'
    PaymentFee = 'PaymentFee'
    Remainder = 'Remainder'
    Surcharge = 'Surcharge'
    Tip = 'Tip'
    VAT = 'VAT'
    Verification = 'Verification'


class SplitAmount(BaseModel):
    currency: Optional[constr(min_length=3, max_length=3)] = Field(
        None,
        description='The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes).\n\nIf this value is not provided, the currency in which the payment is made will be used.',
    )
    value: int = Field(
        ...,
        description='The amount in [minor units](https://docs.adyen.com/development-resources/currency-codes).',
    )


class Transaction(BaseModel):
    amount: Optional[Amount] = Field(None, description='The amount of the transaction.')
    bankAccountDetail: Optional[BankAccountDetail] = Field(
        None, description='The details of the bank account to where a payout was made.'
    )
    captureMerchantReference: Optional[str] = Field(
        None, description='The merchant reference of a related capture.'
    )
    capturePspReference: Optional[str] = Field(
        None, description='The psp reference of a related capture.'
    )
    creationDate: Optional[datetime] = Field(
        None, description='The date on which the transaction was performed.'
    )
    description: Optional[str] = Field(
        None, description='A description of the transaction.'
    )
    destinationAccountCode: Optional[str] = Field(
        None,
        description='The code of the account to which funds were credited during an outgoing fund transfer.',
    )
    disputePspReference: Optional[str] = Field(
        None, description='The psp reference of the related dispute.'
    )
    disputeReasonCode: Optional[str] = Field(
        None, description='The reason code of a dispute.'
    )
    merchantReference: Optional[str] = Field(
        None, description='The merchant reference of a transaction.'
    )
    paymentPspReference: Optional[str] = Field(
        None, description='The psp reference of the related authorisation or transfer.'
    )
    payoutPspReference: Optional[str] = Field(
        None, description='The psp reference of the related payout.'
    )
    pspReference: Optional[str] = Field(
        None, description='The psp reference of a transaction.'
    )
    sourceAccountCode: Optional[str] = Field(
        None,
        description='The code of the account from which funds were debited during an incoming fund transfer.',
    )
    transactionStatus: Optional[TransactionStatus] = Field(
        None,
        description='The status of the transaction.\n>Permitted values: `PendingCredit`, `CreditFailed`, `CreditClosed`, `CreditSuspended`, `Credited`, `Converted`, `PendingDebit`, `DebitFailed`, `Debited`, `DebitReversedReceived`, `DebitedReversed`, `ChargebackReceived`, `Chargeback`, `ChargebackReversedReceived`, `ChargebackReversed`, `Payout`, `PayoutReversed`, `FundTransfer`, `PendingFundTransfer`, `ManualCorrected`.',
    )
    transferCode: Optional[str] = Field(
        None, description='The transfer code of the transaction.'
    )


class TransactionListForAccount(BaseModel):
    accountCode: str = Field(
        ..., description='The account for which to retrieve the transactions.'
    )
    page: int = Field(
        ...,
        description='The page of transactions to retrieve.\nEach page lists fifty (50) transactions.  The most recent transactions are included on page 1.',
    )


class TransferFundsRequest(BaseModel):
    amount: Amount = Field(..., description='The amount to be transferred.')
    destinationAccountCode: str = Field(
        ...,
        description='The code of the account to which the funds are to be credited.\n>The state of the Account Holder of this account must be Active.',
    )
    merchantReference: Optional[str] = Field(
        None,
        description='A value that can be supplied at the discretion of the executing user in order to link multiple transactions to one another.',
    )
    sourceAccountCode: str = Field(
        ...,
        description='The code of the account from which the funds are to be debited.\n>The state of the Account Holder of this account must be Active and allow payouts.',
    )
    transferCode: str = Field(
        ...,
        description='The code related to the type of transfer being performed.\n>The permitted codes differ for each platform account and are defined in their service level agreement.',
    )


class AccountDetailBalance(BaseModel):
    accountCode: Optional[str] = Field(
        None, description='The code of the account that holds the balance.'
    )
    detailBalance: Optional[DetailBalance] = Field(
        None, description='Details of the balance held by the account.'
    )


class AccountHolderTransactionListRequest(BaseModel):
    accountHolderCode: str = Field(
        ...,
        description='The code of the account holder that owns the account(s) of which retrieve the transaction list.',
    )
    transactionListsPerAccount: Optional[List[TransactionListForAccount]] = Field(
        None,
        description='A list of accounts to include in the transaction list. If left blank, the last fifty (50) transactions for all accounts of the account holder will be included.',
    )
    transactionStatuses: Optional[List[TransactionStatus]] = Field(
        None,
        description='A list of statuses to include in the transaction list. If left blank, all transactions will be included.\n>Permitted values:\n>* `PendingCredit` - a pending balance credit.\n>* `CreditFailed` - a pending credit failure; the balance will not be credited.\n>* `Credited` - a credited balance.\n>* `PendingDebit` - a pending balance debit (e.g., a refund).\n>* `CreditClosed` - a pending credit closed; the balance will not be credited.\n>* `CreditSuspended` - a pending credit closed; the balance will not be credited.\n>* `DebitFailed` - a pending debit failure; the balance will not be debited.\n>* `Debited` - a debited balance (e.g., a refund).\n>* `DebitReversedReceived` - a pending refund reversal.\n>* `DebitedReversed` - a reversed refund.\n>* `ChargebackReceived` - a received chargeback request.\n>* `Chargeback` - a processed chargeback.\n>* `ChargebackReversedReceived` - a pending chargeback reversal.\n>* `ChargebackReversed` - a reversed chargeback.\n>* `Converted` - converted.\n>* `ManualCorrected` - manual booking/adjustment by Adyen.\n>* `Payout` - a payout.\n>* `PayoutReversed` - a reversed payout.\n>* `PendingFundTransfer` - a pending transfer of funds from one account to another.\n>* `FundTransfer` - a transfer of funds from one account to another.',
    )


class AccountTransactionList(BaseModel):
    accountCode: Optional[str] = Field(None, description='The code of the account.')
    hasNextPage: Optional[bool] = Field(
        None,
        description='Indicates whether there is a next page of transactions available.',
    )
    transactions: Optional[List[Transaction]] = Field(
        None, description='The list of transactions.'
    )


class ErrorFieldType(BaseModel):
    errorCode: Optional[int] = Field(None, description='The validation error code.')
    errorDescription: Optional[str] = Field(
        None, description='A description of the validation error.'
    )
    fieldType: Optional[FieldType] = Field(None, description='The type of error field.')


class PayoutAccountHolderResponse(BaseModel):
    bankAccountUUID: Optional[str] = Field(
        None,
        description='The unique ID of the Bank Account to which the payout was made.',
    )
    invalidFields: Optional[List[ErrorFieldType]] = Field(
        None,
        description='Contains field validation errors that would prevent requests from being processed.',
    )
    merchantReference: Optional[str] = Field(
        None,
        description='The value supplied by the executing user when initiating the transfer; may be used to link multiple transactions.',
    )
    payoutSpeed: Optional[PayoutSpeed] = Field(
        'STANDARD',
        description='Speed with which payouts for this account are processed. Permitted values: `STANDARD`, `SAME_DAY`.',
    )
    pspReference: Optional[str] = Field(
        None,
        description='The reference of a request. Can be used to uniquely identify the request.',
    )
    resultCode: Optional[str] = Field(None, description='The result code.')


class RefundFundsTransferResponse(BaseModel):
    invalidFields: Optional[List[ErrorFieldType]] = Field(
        None,
        description='Contains field validation errors that would prevent requests from being processed.',
    )
    merchantReference: Optional[str] = Field(
        None,
        description='The value supplied by the executing user when initiating the transfer refund; may be used to link multiple transactions.',
    )
    message: Optional[str] = Field(None, description='The message of the response.')
    originalReference: Optional[str] = Field(
        None, description='A PSP reference of the original fund transfer.'
    )
    pspReference: Optional[str] = Field(
        None,
        description='The reference of a request. Can be used to uniquely identify the request.',
    )
    resultCode: Optional[str] = Field(None, description='The result code.')


class RefundNotPaidOutTransfersResponse(BaseModel):
    invalidFields: Optional[List[ErrorFieldType]] = Field(
        None,
        description='Contains field validation errors that would prevent requests from being processed.',
    )
    pspReference: Optional[str] = Field(
        None,
        description='The reference of a request. Can be used to uniquely identify the request.',
    )
    resultCode: Optional[str] = Field(None, description='The result code.')


class SetupBeneficiaryResponse(BaseModel):
    invalidFields: Optional[List[ErrorFieldType]] = Field(
        None,
        description='Contains field validation errors that would prevent requests from being processed.',
    )
    pspReference: Optional[str] = Field(
        None,
        description='The reference of a request. Can be used to uniquely identify the request.',
    )
    resultCode: Optional[str] = Field(None, description='The result code.')


class Split(BaseModel):
    account: Optional[str] = Field(
        None,
        description='Unique identifier of the account where the split amount should be sent. This is required if `type` is **MarketPlace** or **BalanceAccount**.\n\n',
    )
    amount: SplitAmount = Field(..., description='The amount of this split.')
    description: Optional[str] = Field(None, description='A description of this split.')
    reference: Optional[str] = Field(
        None,
        description='Your reference for the split, which you can use to link the split to other operations such as captures and refunds.\n\nThis is required if `type` is **MarketPlace** or **BalanceAccount**. For the other types, we also recommend sending a reference so you can reconcile the split and the associated payment in the transaction overview and in the reports. If the reference is not provided, the split is reported as part of the aggregated [TransferBalance record type](https://docs.adyen.com/reporting/marketpay-payments-accounting-report) in Adyen for Platforms.',
    )
    type: Type = Field(
        ...,
        description='The type of split.\nPossible values: **Default**, **PaymentFee**, **VAT**, **Commission**, **MarketPlace**, **BalanceAccount**, **Remainder**, **Surcharge**, **Tip**.',
    )


class TransferFundsResponse(BaseModel):
    invalidFields: Optional[List[ErrorFieldType]] = Field(
        None,
        description='Contains field validation errors that would prevent requests from being processed.',
    )
    merchantReference: Optional[str] = Field(
        None,
        description='The value supplied by the executing user when initiating the transfer; may be used to link multiple transactions.',
    )
    pspReference: Optional[str] = Field(
        None,
        description='The reference of a request. Can be used to uniquely identify the request.',
    )
    resultCode: Optional[str] = Field(None, description='The result code.')


class AccountHolderBalanceResponse(BaseModel):
    balancePerAccount: Optional[List[AccountDetailBalance]] = Field(
        None, description='A list of each account and their balances.'
    )
    invalidFields: Optional[List[ErrorFieldType]] = Field(
        None,
        description='Contains field validation errors that would prevent requests from being processed.',
    )
    pspReference: Optional[str] = Field(
        None,
        description='The reference of a request. Can be used to uniquely identify the request.',
    )
    resultCode: Optional[str] = Field(None, description='The result code.')
    totalBalance: Optional[DetailBalance] = Field(
        None, description='The total balance of the account holder.'
    )


class AccountHolderTransactionListResponse(BaseModel):
    accountTransactionLists: Optional[List[AccountTransactionList]] = Field(
        None, description='A list of the transactions.'
    )
    invalidFields: Optional[List[ErrorFieldType]] = Field(
        None,
        description='Contains field validation errors that would prevent requests from being processed.',
    )
    pspReference: Optional[str] = Field(
        None,
        description='The reference of a request. Can be used to uniquely identify the request.',
    )
    resultCode: Optional[str] = Field(None, description='The result code.')


class DebitAccountHolderRequest(BaseModel):
    accountHolderCode: str = Field(..., description='The code of the account holder.')
    amount: Amount = Field(
        ...,
        description="The amount to be debited from the account holder's bank account.",
    )
    bankAccountUUID: str = Field(
        ...,
        description="The Adyen-generated unique alphanumeric identifier (UUID) of the account holder's bank account.",
    )
    description: Optional[constr(max_length=35)] = Field(
        None,
        description='A description of the direct debit. Maximum length: 35 characters.\n\nAllowed characters: **a-z**, **A-Z**, **0-9**, and special characters **/?:().,\'+ ";**.',
    )
    merchantAccount: str = Field(..., description='Your merchant account.')
    splits: List[Split] = Field(
        ...,
        description='Contains instructions on how to split the funds between the accounts in your platform. The request must have at least one split item.',
    )


class DebitAccountHolderResponse(BaseModel):
    accountHolderCode: Optional[str] = Field(
        None, description='The code of the account holder.'
    )
    bankAccountUUID: Optional[str] = Field(
        None,
        description="The Adyen-generated unique alphanumeric identifier (UUID) of the account holder's bank account.",
    )
    invalidFields: Optional[List[ErrorFieldType]] = Field(
        None,
        description='Contains field validation errors that would prevent requests from being processed.',
    )
    merchantReferences: Optional[List[str]] = Field(
        None,
        description='List of the `reference` values from the `split` array in the request.',
    )
    pspReference: Optional[str] = Field(
        None,
        description='The reference of a request. Can be used to uniquely identify the request.',
    )
    resultCode: Optional[str] = Field(None, description='The result code.')
