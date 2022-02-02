# -*- coding: utf-8 -*-
import ffmpeg
from flask import make_response, request
from flask_restful import Resource
import os
import tempfile
import urllib.request


class Convert (Resource):
    def get(self):
        """GET

        Args:
            url (str): 画像 URL
        """
        try:
            # クエリパラメーターから 画像URLを取得
            url = request.args.get("url")

            # 画像を取得
            get = urllib.request.urlretrieve(url)
            imagePath = get[0]

            with tempfile.TemporaryDirectory() as tmpdir:
                # 一時ディレクトリへ 変換後の動画を 出力
                outputPath = os.path.join(tmpdir, "out.mp4")
                con = ffmpeg.input(imagePath)
                con = ffmpeg.output(con, outputPath)
                ffmpeg.run(con)

                # 変換した動画を バイナリ配列として読み込み
                with open(outputPath, "rb") as fp:
                    bin = fp.read()

                res = make_response(bin, 200, {"Content-Type": "video/mp4"})

        except urllib.error.URLError as e:
            res = make_response(e.msg, e.code)
        
        except:
            res = make_response("Internal Server Error", 500)

        return res


    def UnimplementedMethod(self):
        """未使用 メソッド
        """
        return make_response("Method Not Allowed", 405)
    def post(self): return self.UnimplementedMethod()
    def put(self): return self.UnimplementedMethod()
    def delete(self): return self.UnimplementedMethod()
    def head(self): return self.UnimplementedMethod()
    def options(self): return self.UnimplementedMethod()
    def trace(self): return self.UnimplementedMethod()
    def patch(self): return self.UnimplementedMethod()
