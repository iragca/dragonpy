from typing import TypedDict


class SecurityDetails(TypedDict):
    is2FAEnabled: bool
    isAuthApp: bool
    isEmailAuth: bool
    isSMSAuth: bool
    isSMSLocal: bool
    emailAddress: str
    mobileNo: str


class LoginResponse(TypedDict):
    username: str
    isPasswordExpired: bool
    isMobilePin: bool
    isEmailVerified: bool
    is2FAEnabled: bool
    isAuthApp: bool
    isEmailAuth: bool
    isSMSAuth: bool
    isSuspended: bool
    isClosed: bool
    isDisabled: bool
    dateDisabled: str | None
    disabledByCmsAccountUserId: int | None
    isTestAccount: bool
    testAccountDefaultOTP: str | None
    dontAskMeAgain: bool
    loginAttempts: int
    pinAttempts: int
    referredBy: str
    isRegFromMobile: bool
    loginToken: str
    loginTokenExpiry: str
    token: str
    tokenExpiry: str | None
    refreshToken: str
    refreshTokenExpiry: str | None
    dateEmailVerifyUntil: str | None
    securityDetails: SecurityDetails
    clientId: int
    clientCode: str
    planTypeId: int
    planType: str
    isVerified: bool
    accountTypeId: int | None
    company: str
    id: int
    dateEntry: str
