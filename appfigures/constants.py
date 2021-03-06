from archive import ARCHIVE_BASE_URI, ALL_REPORTS, LATEST_REPORTS
from data import DATA_BASE_URI, APPLE_STORE_ID, CATEGORIES_COLLECTION, \
                 COUNTRIES_COLLECTION, CURRENCIES_COLLECTION, LANGUAGES_COLLECTION
from events import EVENTS_BASE_URI, ALL_PRODUCTS
from external_accounts import EXTERNAL_ACCOUNTS_BASE_URI, ANDROID_MARKET, \
                              GOOGLE_CHECKOUT, ITUNES_CONNECT
from iads import IADS_BASE_URI
from ranks import RANKS_BASE_URI, TIMEZONE_EST, TIMEZONE_USER, TIMEZONE_UTC
from reviews import REVIEWS_BASE_URI, MAJOR_COUNTRIES, MINOR_COUNTRIES
from sales import SALES_BASE_URI
from users import USERS_BASE_URI, EXTERNAL_ACCOUNTS_COLLECTION, PRODUCTS_COLLECTION


PODIO_API_URL_1_1 = "https://api.appfigures.com/v1.1"

REPORT_TYPE_HOURLY = "hourly"
REPORT_TYPE_DAILY = "daily"
REPORT_TYPE_WEEKLY = "weekly"
REPORT_TYPE_MONTHLY = "monthly"
REPORT_TYPE_FINANCIAL = "financial"
REPORT_TYPE_PAYMENT = "payment"
REPORT_TYPE_ALL = "all"

REPORT_BY_PRODUCT = "products"
REPORT_BY_DATE = "dates"
REPORT_BY_COUNTRY = "countries"
REPORT_BY_PRODUCT_AND_DATE = "products+dates"
REPORT_BY_DATE_AND_PRODUCT = "dates+products"
REPORT_BY_PRODUCT_AND_COUNTRY = "products+countries"
REPORT_BY_COUNTRY_AND_PRODUCT = "countries+products"
