from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 画面にテキストを表示

def index(request):

    # 文字列をレスポンスとして返す
    # return HttpResponse('Hello! Django!!')

    # クエリパラメータに応じてインタラクティブに
    # msgというキーをGETする
    # 条件分岐でキーがない時もエラーが出ないように

    # 引数にクエリパラメータを設定

    """
    if 'msg' in request.GET:
        print(request.GET)
        msg = request.GET['msg']
        result = 'you typed: "{}" .'.format(msg)
    else:
        result = 'please send msg parameter!'
    """

    # ベタがきver.
    # result = 'your id:' + str(id) + 'your nick name:' + nickname

    # テンプレートを使って値を渡す
    params = {
        'title': 'Hello, index',
        'msg': 'サンプルで作ったページ',
        'goto': 'next'  # 2ページをindexを使って表示するためのもの
    }

    # テンプレートを使う時にはrenderを用いる
    # return render(request, 'hello/index.html')

    # パラメータを複数渡すとき
    return render(request, 'hello/index.html', params)


# nextのページを表示する
def next(request):
    params = {
        'title': 'Hello/Next',
        'msg': 'もう一つのページ',
        'goto': 'index'
    }
    return render(request, 'hello/index.html', params)