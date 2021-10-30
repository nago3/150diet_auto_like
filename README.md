# 150diet_auto_like

instagramのいいねプログラムを作成する

## 環境構築

1. git clone —
2. 環境の確認
  - pyenv —version
  - pip —version
  - pipenv —version
  ※ ないものはインストールする
3. pipenvに入っている内容をインストールする
  - pipenv install
  ※ 新規に追加する場合は
4. Pipenv を起動する
  - pipenv shell
  ※ 終了は `exit` を入力する
5. pipenv のパッケージを更新する場合
  - pipenv update

※ `requirements.txt` を使うパターンもあるが、今回は Pipenv を利用する
※ Pipfile と Pipfile.lock はバージョン管理すること

## 作業環境

`pipenv shell` コマンドで仮想環境を構築し、その中で作業をする

