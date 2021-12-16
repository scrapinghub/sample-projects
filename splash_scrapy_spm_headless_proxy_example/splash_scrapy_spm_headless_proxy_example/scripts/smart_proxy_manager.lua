function use_crawlera(splash)
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

        -- Here, Splash will communicate with Zyte SmartProxy (formerly Crawlera) Headless Proxy.
        -- Zyte SmartProxy (formerly Crawlera) Headless Proxy should be up and running.
        request:set_proxy{"host.docker.internal", 3128}
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
