from pkgutil import get_data

from scrapy.utils.project import get_project_settings
from scrapy_splash import SplashRequest
from w3lib.http import basic_auth_header


class SplashCrawleraRequest(SplashRequest):
    crawlera_script = get_data(
        'splash_crawlera_example', 'scripts/crawlera.lua'
    ).decode('utf-8')

    def __init__(self, *cargs, **kwargs):
        settings = get_project_settings()
        assert not settings.getbool('CRAWLERA_ENABLED'), "Splash cannot be used with CRAWLERA_ENABLED. Use CRAWLERA_SPLASH_ENABLED = True instead"
        if settings.getbool('SPLASH_CRAWLERA_ENABLED'):
            args = kwargs.setdefault('args', {})
            args['lua_source'] = self.crawlera_script
            args['crawlera_user'] = settings.get('CRAWLERA_APIKEY')
            kwargs['endpoint'] = 'execute'
            kwargs['cache_args'] = ['lua_source']
            kwargs['splash_headers'] = {
                'Authorization': basic_auth_header(settings['SPLASH_APIKEY'], ''),
            }
        super(SplashCrawleraRequest, self).__init__(*cargs, **kwargs)
