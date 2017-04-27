function use_crawlera(splash)
    -- Put your Crawlera username and password here. This is different from your
    -- Scrappinghub account. Find your Crawlera username and password in
    -- https://app.scrapinghub.com/
    local user = splash.args.crawlera_user
    local password = ""

    local host = 'proxy.crawlera.com'
    local port = 8010
    local session_header = "X-Crawlera-Session"
    local session_id = "create"

    splash:on_request(function (request)
        -- Requests to Google domains are not allowed by Crawlera, but pages
        -- frequently include tracking code or ads served by google. Block
        -- those requests.
        --
        -- lua patterns follow a different syntax to normal regular expressions
        if string.find(request.url, 'google%.[a-z][a-z][a-z]?') or
           string.find(request.url, 'doubleclick%.net') or
           string.find(request.url, 'googleapis%.com') then
            request.abort()
            return
        end

        -- If possible, avoid using Crawlera for subresource requests that
        -- are not monitored. This will increase speed a lot. Here are some
        -- example rules that you can use to match subresources:

        -- Don't use Crawlera for domains starting with static.
        if string.find(request.url, '://static%.') ~= nil then
            return
        end

        -- Don't use Crawlera for urls ending in .png
        if string.find(request.url, '%.png$') ~= nil then
            return
        end
        request:set_header("X-Crawlera-UA", "desktop")
        request:set_header('X-Crawlera-Cookies', 'disable')
        request:set_header(session_header, session_id)
        request:set_proxy{host, port, username=user, password=password}
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
