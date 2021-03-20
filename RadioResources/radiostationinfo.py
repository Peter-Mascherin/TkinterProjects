import json

#possible root background shades
# #3D3939 (original)
# #181818 (spotify)
# #1E1E1E (vs code)
# #202020 (youtube search bar area)
# #1A1A1A (instagram)

#1BCF5B - (original status text colour)
# base station text colour (spotify) - #1ED760

urls = '''{
    "stations":[
        {
            "radiourl": "https://ice23.securenetsystems.net/CIDC",
            "radioname":    "Z103.5",
            "stationimage": "RadioResources/z103.5.png"
        },
        {
            "radiourl": "https://rogers-hls.leanstream.co/rogers/tor981.stream/icy?environment=tunein&args=tunein_01",
            "radioname":    "98.1 CHFI",
            "stationimage": "RadioResources/98.1chfi.png"
        },
        {
            "radiourl": "http://newcap.leanstream.co/CHBMFM-MP3?args=tunein_01",
            "radioname":    "Boom 97.3",
            "stationimage": "RadioResources/boom97.3.png"
        },
        {
            "radiourl": "https://rogers-hls.leanstream.co/rogers/tor925.stream/icy?environment=tunein&args=tunein_01",
            "radioname":    "KiSS 92.5",
            "stationimage": "RadioResources/kiss92.5.png"
        },
        {
            "radiourl": "http://192.111.140.6:9683/stream",
            "radioname":    "EDE - EDM Club",
            "stationimage": "RadioResources/ede.png"
        },
        {
            "radiourl": "https://corus.leanstream.co/CFNYFM-MP3?args=tunein",
            "radioname":    "102.1 The Edge",
            "stationimage": "RadioResources/theedge.png"
        },
        {
            "radiourl": "http://pulseedm.cdnstream1.com:8124/1373_128",
            "radioname":    "Pulse EDM",
            "stationimage": "RadioResources/pulseedm.png"
        },
        {
            "radiourl": "http://strm112.1.fm/atr_mobile_mp3",
            "radioname":    "1FM Trance Radio",
            "stationimage": "RadioResources/tranceamsterdam.png"
        }
       

    ]
}'''

suggesiontext = '''{
    "textblob": "Your currently on the suggestions page, from here you can suggest radio stations. Note: To enable suggestions you must switch 'Allow less secure apps' to On in the Google Account Control page"
}'''
