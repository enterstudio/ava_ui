## CONTENT SECURITY POLICY (CSP) CONFIGURATION
##
## Here is where we configure exemptions from the default (strong)
## CSP policy. In an ideal world, this will be empty.
##
## Documented at: http://django-csp.readthedocs.org/en/latest/configuration.html
##
## CSP crash course at: http://django-csp.readthedocs.org/en/latest/configuration.html

CSP_STYLE_SRC = (
    ## 'self' is for all local assets, the usual default.
    "'self'",

    ## Unfortunately 'modernizr' seems to require 'unsafe-inline' styles.
    "'unsafe-inline'",

    ## CDN for a stylesheet we're pulling in.
    "http://maxcdn.bootstrapcdn.com/"
)

CSP_SCRIPT_SRC = (
    "'self'",
    ## lodash.min.js requires the use of 'unsafe-eval', which is a shame.
    "'unsafe-eval'",

    ## JQuery is being pulled from a CDN.
    "http://ajax.googleapis.com",

    ## This sha256 excemption is for the tiny little bit of javascript
    ## that the django-html5-boilerplate library is injecting at the
    ## bottom of seemingly every page. It would be nice for this to go
    ## away somehow.
    "'sha256-QElWz9ZyO3cMaja_DMF2vK4SfsTklXYMigNFQGuxka8='",
)

CSP_FONT_SRC = (
    "'self'",
    ## Bootstrap CDN
    "http://maxcdn.bootstrapcdn.com/",
)

CSP_IMG_SRC = (
    "'self'",

    ## This might not be necessary. Not having it in place was
    ## Causing a CSP violation because of an image Lastpass
    ## injects into form fields. If that's actually the only
    ## reason we're seeing those violations, than later we can
    ## remove this exemption again.
    "data:",
)