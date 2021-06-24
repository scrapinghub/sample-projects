function use_crawlera(splash)
    -- Make sure you pass your Smart Proxy Manager API key in the 'crawlera_user' arg.
    -- Have a look at the file spiders/quotes-js.py to see how to do it.
    -- Find your Smart Proxy Manager credentials in https://app.zyte.com/
    local user = splash.args.crawlera_user
    local password = ''

    local host = 'proxy.zyte.com'
    local port = 8011
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

        -- Avoid using Smart Proxy Manager for subresources fetching to increase crawling
        -- speed. The example below avoids using Smart Proxy Manager for URLS starting
        -- with 'static.' and the ones ending with '.png'.
        -- if string.find(request.url, '://static%.') ~= nil or
        --    string.find(request.url, '%.png$') ~= nil then
        --     return
        -- end
        request:set_proxy(host, port, user, password)
        request:set_header('X-Crawlera-Profile', 'desktop')
        request:set_header('X-Crawlera-Cookies', 'disable')
        request:set_header(session_header, session_id)
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
    splash:wait(1)
    return splash:html()
end
