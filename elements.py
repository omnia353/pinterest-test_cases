elements = {
    "login": {
        "login_btn": {"method": "xpath",
                      "value": '//*[@id="__PWS_ROOT__"]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/button'},
        "e-mail_ip": {'method': 'xpath',
                      'value': '//*[@id="email"]'},
        "pass_ip": {'method': 'xpath',
                    'value': '//*[@id="password"]'},
        "confirm_login_btn": {'method': 'xpath',
                              'value': '//*[@id="__PWS_ROOT__"]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div/div/div/div[3]/form/div[5]/button'},
        "title": {'method': 'xpath',
                  'value': '//*[@id="__PWS_ROOT__"]/div[1]/div/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]'}
    },
    "home": {
        "header": {"method": "xpath",
                   "value": '//*[@id="__PWS_ROOT__"]/div[1]/div[3]/div/div/div/div[1]/div/div[2]/div[1]'},
        "search-bar": {'method': 'xpath',
                       'value': '//*[@id="searchBoxContainer"]/div/div/div[2]/input'},
        "search-bar2": {'method': 'xpath',
                        'value': '//*[@id="searchBoxContainer"]/div/div/div[1]/input'},
        "ip-confirm": {'method': 'xpath',
                       'value': '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/form/span[3]/input'},
        "picture1": {'method': 'xpath',
                     'value': '//*[@id="__PWS_ROOT__"]/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[1]/a/div/div[1]/div/div/div/div/div/img'},
        "following-btn": {'method': 'xpath',
                          'value': '//*[@id="HeaderContent"]/header/div/div/div[2]/div/div/div/div[3]/div/a/div/span'},
        "picture2": {'method': 'tag_name',
                     'value': 'img'}
    }
}
