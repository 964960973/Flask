import execjs


def music_url(id):
  ids = id
  # data = '{"ids":"[1473782328]","level":"standard","encodeType":"aac","csrf_token":""}'
  data = '{"ids":"'+str([ids])+'","level":"standard","encodeType":"aac","csrf_token":""}'
  with open(r"../网易云音乐/网易云.js", encoding="utf-8") as f:
    ctx = execjs.compile(f.read())
  info = ctx.call('d', data, '010001','00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7','0CoJUm6Qyw8W8jud')
  return info['encText'], info['encSecKey']
music_url('aa')