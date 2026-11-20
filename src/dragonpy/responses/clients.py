from typing import TypedDict

from dragonpy.responses.authorization import SecurityDetails


class VerifyTotpResponse(TypedDict):
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
    loginToken: str | None
    loginTokenExpiry: str
    token: str
    tokenExpiry: str
    refreshToken: str
    refreshTokenExpiry: str
    dateEmailVerifyUntil: str | None
    securityDetails: SecurityDetails | None
    clientId: int
    clientCode: str
    planTypeId: int
    planType: str
    isVerified: bool
    accountTypeId: int | None
    company: str
    id: int
    dateEntry: str
