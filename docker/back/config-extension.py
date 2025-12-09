INSTALLED_APPS += [
    "mozilla_django_oidc",
    "taiga_contrib_oidc_auth",
]

AUTHENTICATION_BACKENDS = list(AUTHENTICATION_BACKENDS) + [
    "taiga_contrib_oidc_auth.oidc.TaigaOIDCAuthenticationBackend",
]

# Add the OIDC urls
ROOT_URLCONF = "settings.urls"

# OIDC Settings
OIDC_CALLBACK_CLASS = "taiga_contrib_oidc_auth.views.TaigaOIDCAuthenticationCallbackView"
OIDC_RP_SCOPES = "openid profile email"
OIDC_RP_SIGN_ALGO = "RS256"
# These two are private! Don't commit them to VCS. Getting the values from
# environment variables is a good way.
import os
OIDC_RP_CLIENT_ID = os.getenv("OIDC_RP_CLIENT_ID")
OIDC_RP_CLIENT_SECRET = os.getenv("OIDC_RP_CLIENT_SECRET")
OIDC_BASE_URL = os.getenv("OIDC_BASE_URL")
OIDC_OP_JWKS_ENDPOINT = OIDC_BASE_URL + "/protocol/openid-connect/certs"
OIDC_OP_AUTHORIZATION_ENDPOINT = OIDC_BASE_URL + "/protocol/openid-connect/auth"
OIDC_OP_TOKEN_ENDPOINT = OIDC_BASE_URL + "/protocol/openid-connect/token"
OIDC_OP_USER_ENDPOINT = OIDC_BASE_URL + "/protocol/openid-connect/userinfo"
