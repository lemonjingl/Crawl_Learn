import requests

url='https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
         ,'Acs - Token':'1672992340848_1673043972109 _DO3 + OHd5ccCOBOxkFrk9AP5zmTpy4pNPt / GqaCgfDgPkp3I50Uks4hS6dsPB5 + kwNxUNWaj0uPreeH7qrSGBemC78d3rrOvb + z3g3QhQQ / 0fynS2 / 6hqfZuHKGRWFB4Mu + qzs5 / buUVvjPZqFK9QXnt4LZ5X2qNaz5U2qhwMKBRMdfMrIosxH3pyQZhp6 + 4zpLYFF2bMfNSg / sccGrIGey7bE + FhWcDqqgHSNDxm6 + EiI9VpWA9GOf + j6caTqkfaQPUN60Ntcl6y0aw533glJ9 / Ib2O7eucWSQVGJOPBs2M / 5.优质采 + gnhwXcYKS / hb5KZDVXJN8TLtCCWN3bCf0y0a / mKg ==',
'Cookie': 'BAIDUID=47BE7EE0A9F427E0B5979669D4436B02:FG=1; BIDUPSID=47BE7EE0A9F427E0B5979669D4436B02; PSTM=1665543468; ZFY=LRIv29VFzeddN5w:Bm19pQTJ:ACf2RVMD9JblIcZK:AncM:C; __bid_n=1844b95814ce61fa054207; FEID=v10-a26467ede6bc86ef914c615644d756eaa08cd1d4; BDUSS=2FUb2dvaUxwQjRGaXpNTkFNaXpUWkZaTU0tU3loaEJJMUJSMktJLVFPd1FuY0ZqSVFBQUFBJCQAAAAAAAAAAAEAAAC47d~2wbrBusDuzsTA7s7EwboAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAQmmMQEJpjU; BDUSS_BFESS=2FUb2dvaUxwQjRGaXpNTkFNaXpUWkZaTU0tU3loaEJJMUJSMktJLVFPd1FuY0ZqSVFBQUFBJCQAAAAAAAAAAAEAAAC47d~2wbrBusDuzsTA7s7EwboAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAQmmMQEJpjU; BAIDUID_BFESS=47BE7EE0A9F427E0B5979669D4436B02:FG=1; __xaf_fpstarttimer__=1672149513474; __xaf_thstime__=1672149513574; FPTOKEN=JpWhjq+ynFKQhmw1GFVQLNR9LOFsyxs/iQy5iB9ZHhrhF0s/rLF28AnCvL011ut9MxHDUjC4gtxPwiP1Kc7yco1YkVCgC9JaH++5oHum2oU9zPHWuuDqxA1BTBgGEy45A6WALqPIGHOBihlHy8+ak0OrJkC9dGsFz0Z7uwLEb3at3t62+4AUENQBALJysPgaq9x210klZ8ozMLSmfzy0yfXfpLSALqwR37pgQaD/v0n7zCWJZiJhRCJVjYJasoeqSjgFUQTMJS/p6KOwsKhwS+qiHRKBcK2V1FXf6/JIT6XOY34oTGOqMEX3H2vXmguDJ9eJcHip09HsHpdxjqMMoqKhV9KpaWpWHTVtFBhrp+lZAiH4mAs2Id4VoJm4Ps7DawlNm7EXlzULEA3hrZVbE0mlfjkvv+Ia1MfHY42Xgaxc+T2iCiACv7PfNYqXj65U|CDAbvJ5XvK6ZBuzPKrsYPaMywPqnQPW0Fqh0RBA7dxg=|10|6b97789d55eba9b22ee61bd574b87150; __xaf_fptokentimer__=1672149513687; H_PS_PSSID=37783_36558_37972_37647_37550_38023_37907_38012_36920_37989_37797_37928_37900_26350_37957_37881; BA_HECTOR=0h008k2la484810l80ah0lmj1hrh5vp1l; delPer=0; PSINO=7; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1673043907; ab_sr=1.0.1_MDA0YzNkNDE0YjM3ZTc1ZWQyNWRkMWZhMzExMDAyMDMyZmM2MjcyNTQ5M2U1OWUyN2U0YTQ1NzljZDA5ODI4OTYyMzNmM2U1NTY1MGRkMWRjMWYwMGVjMzZiNjVhNzFmZDk0NjVkNzA3OThlNTNjOWI1ZjAxZDQyYTExNGQ4YzczZmY1NmRjMWRjYzBlNjA2M2JmZjJjMzEzY2Q1MDhiYTEzYWJhOTRlNzg5NWM2MWQ5MzhlOWM1ODQ5N2E5ZDNm; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1673043971'
         }
query={'from': 'en',
'to': 'zh',
'query': 'apple',
'simple_means_flag': '3',
'sign': '704513.926512',
'token': 'ce379503c4e8482f8884181a40389f42'}

response=requests.post(url=url,data=query,headers=headers)
print(response.json())