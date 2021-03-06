#encoding=utf-8


POST_TXT = """
            <xml>
                <ToUserName><![CDATA[toUser]]></ToUserName>
                <FromUserName><![CDATA[fromUser]]></FromUserName>
                <CreateTime>1348831860</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[this is a test]]></Content>
                <MsgId>1234567890123456</MsgId>
            </xml>
            """

RESPONSE_TXT = '''
            <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[%s]]></MsgType>
                <Content><![CDATA[%s]]></Content>
                <FuncFlag>%d</FuncFlag>
            </xml>
            '''

#need to init
RESPONSE_TXT_PIC = """
            <xml>
                <ToUserName><![CDATA[toUser]]></ToUserName>
                <FromUserName><![CDATA[fromUser]]></FromUserName>
                <CreateTime>12345678</CreateTime>
                <MsgType><![CDATA[news]]></MsgType>
                <ArticleCount>2</ArticleCount>
                <Articles>
                <item>
                <Title><![CDATA[title1]]></Title>
                <Description><![CDATA[description1]]></Description>
                <PicUrl><![CDATA[picurl]]></PicUrl>
                <Url><![CDATA[url]]></Url>
                </item>
                <item>
                <Title><![CDATA[title]]></Title>
                <Description><![CDATA[description]]></Description>
                <PicUrl><![CDATA[picurl]]></PicUrl>
                <Url><![CDATA[url]]></Url>
                </item>
                </Articles>
                <FuncFlag>0</FuncFlag>
            </xml>
            """

KEYWORDS_DIC = {
    'help': ('help', 'h', '?', u'？', u'帮助',),
    'btc': ('btc', 'b', u'比特币', u'汇率', u'价格',),
    'ltc': ('ltc', 'l', u'利特币',),
    'mtgox': ('mtgox', 'mt', 'gox'),
    'btce': ('btce', 'btc-e',),
    'btcchina': ('btcc', 'btcchina', u'比特币中国'),
    'fxbtc': ('fx', 'fxbtc',),
    '42btc': ('42btc',),
    'todo': ('todo',),
}

RESPONSE_SUBSCRIBE = u"欢迎关注比特币助手！比特币助手让您可以随时随地查询比特币、利特币实时价格，\
并且不定期推送比特币、利特币最新资讯。\
\r\n输入h或help查看帮助。"

RESPONSE_UNSUPPORTED_TYPE = u"不支持的消息类型，目前仅支持文本格式消息。\
\r\n输入h或help查看帮助。"

# compatible display style with both android and ios
RESPONSE_HELP = u"""【btc】比特币实时行情汇总
【ltc】利特币实时行情汇总
【mt】MtGox比特币实时行情
【btce】BTC-E比特币实时行情
【btcc】BTCChina比特币实时行情
【fx】FXBTC比特币实时行情
【todo】正在开发的命令

任何建议意见请直接留言"""

RESPONSE_TODO = u"""正在开发的命令：
【】以美元/人民币价格显示
【】最近n分钟/小时/天价格
【】24小时价格走势图
【】N天价格走势图

任何建议意见请直接留言"""
