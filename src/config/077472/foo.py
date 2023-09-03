from configobj import ConfigObj as co
import requests
from mastodon import Mastodon as M

c = co('session.conf')
m = M(access_token=c['mastodon']['access_token'],
      api_base_url=c['mastodon']['instance'])
