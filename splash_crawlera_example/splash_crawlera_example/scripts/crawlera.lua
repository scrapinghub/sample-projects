function use_crawlera(splash)
    -- Make sure you pass your Crawlera API key in the 'crawlera_user' arg.
    -- Have a look at the file spiders/quotes-js.py to see how to do it.
    -- Find your Crawlera credentials in https://app.scrapinghub.com/
    local user = splash.args.crawlera_user

    local host = 'proxy.crawlera.com'
    local port = 8010
    local session_header = 'X-Crawlera-Session'
    local session_id = 'create'

    splash:on_request(function (request)
        -- The commented code below can be used to speed up the crawling
        -- process. They filter requests to undesired domains and useless
        -- resources. Uncomment the ones that make sense to your use case
        -- and add your own rules.

        -- Discard requests to advertising and tracking domains.
        -- if string.find(request.url, 'doubleclick%.net') or
        --    string.find(request.url, 'analytics%.google%.com') then
        --     request.abort()
        --     return
        -- end

        -- Avoid using Crawlera for subresources fetching to increase crawling
        -- speed. The example below avoids using Crawlera for URLS starting
        -- with 'static.' and the ones ending with '.png'.
        -- if string.find(request.url, '://static%.') ~= nil or
        --    string.find(request.url, '%.png$') ~= nil then
        --     return
        -- end

        request:set_header('X-Crawlera-Cookies', 'disable')
        request:set_header(session_header, session_id)
        request:set_proxy{host, port, username=user, password=''}
    end)

    splash:on_response_headers(function (response)
        if type(response.headers[session_header]) ~= nil then
            session_id = response.headers[session_header]
        end
    end)
end

function main(splash)
    use_crawlera(splash)
    splash:go(splash.args.url)
    return splash:html()
end
