

# solidpython-tutorial


## Description

SolidPython tutorial for generating OpenSCAD code from Python code.

By generating an STL file from OpenSCAD, you can output it with a 3D printer.

Finally in this repository we get the contribution graph from GitHub,
Convert it to a 3D object (STL) and output it with a 3D printer.

[Generated Github contribution calendar 3D object](python/sp04_github_contribution.stl)

Python コードから OpenSCAD のコードを生成する SolidPython のチュートリアル。

OpenSCAD から STL ファイルを生成することで、3Dプリンタで出力することができる。

最終的にこのリポジトリでは、Github から コントリビューショングラフを取得し、
それを 3Dオブジェクト(STL)に変換し、3Dプリンタでの出力を行います。


## Setup
```shell
brew install --cask openscad
pipenv install
```

## Included utilities

### [openscad_utils.py](./python/openscad_utils.py)
Utility for executing commands to generate STL files using OpenSCAD applications.

OpenSCAD アプリケーションを使って、STL ファイルを生成するコマンドを実行するためのユーティリティ。

### [github_utils.py](./python/github_utils.py)

Get the Github user page, parse the HTML (SVG) of the contribution graph content,
A utility that retrieves contribution graph data.

You don't need an access token because you're just looking at an HTML page.


Github のユーザーページを取得し、コントリビューショングラフの内容のHTML(SVG)をパースし、
コントリビューショングラフのデータを取得するユーティリティ。

HTML ページを見るだけなのでアクセストークンは必要ありません。

