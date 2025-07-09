# 获取哔哩哔哩直播的真实流媒体地址，默认获取直播间提供的最高画质
# qn=150高清
# qn=250超清
# qn=400蓝光
# qn=10000原画
import requests


class BiliBili:

    def __init__(self, rid):
        """
        有些地址无法在PotPlayer播放，建议换个播放器试试
        Args:
            rid:
        """
        rid = rid
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://live.bilibili.com/',
            'Origin': 'https://live.bilibili.com'
        }
        # 先获取直播状态和真实房间号
        r_url = 'https://api.live.bilibili.com/room/v1/Room/room_init'
        param = {
            'id': rid
        }
        with requests.Session() as self.s:
            res = self.s.get(r_url, headers=self.header, params=param).json()
        if res['msg'] == '直播间不存在':
            raise Exception(f'bilibili {rid} {res["msg"]}')
        live_status = res['data']['live_status']
        if live_status != 1:
            raise Exception(f'bilibili {rid} 未开播')
        self.real_room_id = res['data']['room_id']

    def get_real_url(self, current_qn: int = 10000) -> dict:
        url = 'https://api.live.bilibili.com/xlive/web-room/v2/index/getRoomPlayInfo'
        param = {
            'room_id': self.real_room_id,
            'protocol': '0,1',
            'format': '0,1,2',
            'codec': '0,1',
            'qn': current_qn,
            'platform': 'h5',
            'ptype': 8,
        }
        res = self.s.get(url, headers=self.header, params=param).json()
        
        # 添加调试信息和错误处理
        if 'data' not in res:
            raise Exception(f'API返回错误: {res}')
        
        playurl_info = res['data'].get('playurl_info')
        if not playurl_info:
            raise Exception('无法获取播放信息，可能直播已结束或房间不存在')
        
        playurl = playurl_info.get('playurl')
        if not playurl:
            raise Exception('无法获取播放URL信息')
        
        stream_info = playurl.get('stream', [])
        if not stream_info:
            raise Exception('无法获取流信息')
        
        qn_max = 0

        # 寻找最高画质
        for data in stream_info:
            if 'format' in data and len(data['format']) > 0:
                if 'codec' in data['format'][0] and len(data['format'][0]['codec']) > 0:
                    accept_qn = data['format'][0]['codec'][0].get('accept_qn', [])
                    for qn in accept_qn:
                        qn_max = qn if qn > qn_max else qn_max
        
        if qn_max != current_qn and qn_max > 0:
            param['qn'] = qn_max
            res = self.s.get(url, headers=self.header, params=param).json()
            if 'data' in res and 'playurl_info' in res['data']:
                stream_info = res['data']['playurl_info']['playurl'].get('stream', [])

        stream_urls = {}
        # 优先获取FLV格式的流（PotPlayer兼容性更好）
        for data in stream_info:
            if 'format' not in data or len(data['format']) == 0:
                continue
                
            for format_data in data['format']:
                format_name = format_data.get('format_name', '')
                if format_name == 'flv':  # FLV格式优先
                    if 'codec' in format_data and len(format_data['codec']) > 0:
                        codec_data = format_data['codec'][0]
                        base_url = codec_data.get('base_url', '')
                        url_info = codec_data.get('url_info', [])
                        
                        for i, info in enumerate(url_info):
                            host = info.get('host', '')
                            extra = info.get('extra', '')
                            if host and base_url:
                                # 添加必要的HTTP头信息到URL
                                complete_url = f'{host}{base_url}{extra}'
                                stream_urls[f'FLV线路{i + 1}'] = complete_url
                    break
            
            if stream_urls:  # 如果找到了FLV流就退出
                break
        
        # 如果没有FLV流，再尝试获取HLS流
        if not stream_urls:
            for data in stream_info:
                if 'format' not in data or len(data['format']) == 0:
                    continue
                    
                for format_data in data['format']:
                    format_name = format_data.get('format_name', '')
                    if format_name == 'ts':  # HLS格式
                        if 'codec' in format_data and len(format_data['codec']) > 0:
                            codec_data = format_data['codec'][0]
                            base_url = codec_data.get('base_url', '')
                            url_info = codec_data.get('url_info', [])
                            
                            for i, info in enumerate(url_info):
                                host = info.get('host', '')
                                extra = info.get('extra', '')
                                if host and base_url:
                                    complete_url = f'{host}{base_url}{extra}'
                                    stream_urls[f'HLS线路{i + 1}'] = complete_url
                        break
                
                if stream_urls:  # 如果找到了流地址就退出
                    break
        
        if not stream_urls:
            raise Exception('未找到可用的直播流地址')
            
        return stream_urls


def get_real_url(rid):
    try:
        bilibili = BiliBili(rid)
        return bilibili.get_real_url()
    except Exception as e:
        print('错误详情：', str(e))
        return False


def test_url_validity(url):
    """测试URL是否有效"""
    try:
        import requests
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://live.bilibili.com/'
        }
        response = requests.head(url, headers=headers, timeout=10, allow_redirects=True)
        return response.status_code == 200
    except:
        return False


if __name__ == '__main__':
    r = input('请输入bilibili直播房间号：\n')
    result = get_real_url(r)
    if result:
        print('\n🎯 直播流地址获取成功：')
        print('=' * 60)
        for name, url in result.items():
            print(f'\n📺 {name}:')
            print(f'🔗 {url}')
            
            # 测试URL有效性
            print('🔍 测试连接...', end='', flush=True)
            if test_url_validity(url):
                print(' ✅ 连接正常')
            else:
                print(' ❌ 连接失败')
        
        print('\n' + '=' * 60)
        print('💡 使用说明:')
        print('1. 复制上面的URL地址')
        print('2. 在PotPlayer中按 Ctrl+U 打开URL')
        print('3. 如果某个线路无法播放，请尝试其他线路')
        print('4. 推荐播放器: VLC Media Player (兼容性更好)')
    else:
        print('❌ 获取直播流地址失败')