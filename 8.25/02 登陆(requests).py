import requests
url = 'https://user.qzone.qq.com/1104781249'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    # 时效性
    # 'cookie': 'eas_sid=m175G9t8W0M0U0F0K967o9W5S6; pgv_pvi=6796872704; pgv_pvid=989602496; _qpsvr_localtk=0.1981450504338882; pgv_si=s7463355392; pgv_info=ssid=s1901979724; ptui_loginuin=1104781249; uin=o1104781249; skey=@YNqL36vyD; RK=K6TE2teTTz; ptcz=451cc449e0c684f4aa051e8bb131d4c87ae6db46353e406fa7404182ec02d7e4; p_uin=o1104781249; pt4_token=6--HXc48VlDU71Z7XD37hyEFIJzI1b*Z5BwLGWLphLA_; p_skey=33dDEddBt4U*xRG4ls4VZtFfpfqboViawpXpUmrFsCk_; Loading=Yes; qz_screen=1600x900; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; 1104781249_todaycount=0; 1104781249_totalcount=55664; QZ_FE_WEBP_SUPPORT=1; qzmusicplayer=qzone_player_1104781249_1598318208940; cpu_performance_v8=0'
}
response = requests.get(url,headers = headers)
with open('QQ空间.html','w',encoding='utf-8') as file:
    file.write(response.text)